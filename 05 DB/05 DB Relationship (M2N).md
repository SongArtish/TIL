# DB Relationship (M : N)

2020.09.23



---

[TOC]

---



## 1. 중개모델

> 각각의 모델과 1:N관계를 맺어 서로 다른 모델을 중개해주는 역할을 한다.



### 1.1 중개모델 만들기

**1.1.1 중개모델 작성**

- 먼저 `models.py`에 중개모델을 다음과 같이 작성한다.

```python
# hospitals/models.py

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
```

- 이후 DB 초기화를 해준다. DB를 초기화 할 때는 `migrations/000X`번 파일과 `db.sqlite3`를 삭제한다.
- migrate을 다시 진행한다.

**1.1.2 객체 만들기**

- 이후 shell_plus에서 객체를 생성한 후, reservation을 만든다.

```shell
In [4]: reservation1 = Reservation.objects.create(doctor=doctor1, patient=patient1)      

In [6]: reservation2 = Reservation.objects.create(doctor=doctor2, patient=patient1)      
```

**1.1.3 역참조**

- **`<모델>.<중개모델>_set.all()`**
- 서로 다른 의사와 예약이 2번 잡힌 patient1의 reservation을 조회해보면 다음과 같다.

```shell
In [7]: patient1.reservation_set.all()
Out[7]: <QuerySet [<Reservation: 1번 의사의 1번 환자>, <Reservation: 2번 의사의 1번 환자>]>
```

**1.1.4 `ManyToManyField` 활용**

- `ManyToManyField`는 2개의 모델 중 어느 쪽에 있어도 상관 없다.

```python
# hospitals/models.py

class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    ...
```

- shell에서 다음과 같이 출력할 수 있다.

```shell
In [9]: patient1.doctors.all()
Out[9]: <QuerySet [<Doctor: 1번 의사 john>, <Doctor: 2번 의사 eric>]>
```

**1.1.5 `related_name`를 활용한 양쪽 역참조**

- `related_name`을 이용하면 Doctor에서도 역참조를 할 수 있다.

```python
# hospitals/models.py

    doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')

```

```shell
In [3]: doctor1 = Doctor.objects.get(pk=1)

In [4]: doctor1.patients.all()
Out[4]: <QuerySet [<Patient: 1번 환자 Song>]>
```



### 1.2 중개모델 없이 : `ManyToManyField`

> `M : N 관계`를 간단하게 사용할 경우, Django에서는 `ManyToManyField`와 `related_name`을 사용해서 중개모델이 없는 것처럼 사용할 수도 있다.

```python
# hospitals/models.py

class Doctor(models.Model):
    name = models.TextField()
	# ...

class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name='patients')
	# ...
```



## 2. ManyToManyField

> `ManyToManyField(to, **options)`는 M:N 관계를 나타내기 위해 사용하는 필드로, 하나의 필수 위치 인자(M:N 관계로 설정할 모델 클래스)가 필요하다.

**Arguments**

모두 optional 하며 관계가 작동하는 방식을 제어한다.

**`related_name`**

- ForeignKey의 related_name과 동일

**`through`**

- 중개 테이블을 직접 작성하려는 경우 지정
- 일반적으로 추가 데이터를 M:N 관계와 연결하려는 경우에 사용

**`symmetrical`** (대칭적)

- ManyToManyField가 동일한 모델(self)을 가리키는 정의에서만 사용
- 자기(self)를 참조를 하는 경우 비대칭적으로 모델을 생성하기 위해서는 `symmetrical=False`라는 옵션을 사용한다.
- 예시

```python
# 친구신청
friends = models.ManyToManyField(self, symmetrical=True)
```

```python
# 팔로잉/팔로워
followings = models.ManyToManyField(self, symmetrical=False, related_name='followers')
```



## 3. <실습> Like 만들기

**Model 생성**

- 역참조 시 기존의 모델의 역참조와 충돌하므로 `related_name`도 입력한다.

```python
# articles/models.py

# 좋아요 모델
like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_users')
```

**url 생성**

```python
# articles/urls.py

path('<int:article_pk>/like/', views.like, name='like'),
```

**view 함수 생성**

```python
# articles/views.py

@require_POST
def like(request, article_pk):
    # 인증된 사용자만 가능
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        # user가 article에 좋아요를 눌렸는지 안 눌렸는지
        if request.user in article.like_users.all():
            # 좋아요 취소
            article.like_users.remove(request.user)
        else:
            # 좋아요
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')
```

- 전체에서 1개를 찾는 경우 `.exists()`가 더 빠르게 동작한다.
- 좋아요가 하나도 존재하지 않는 경우 `.get()`은 오류를 발생한다. `.filter()`의 경우 QuerySet을 반환하기 떄문에 filter를 사용한다.

```python
# articles/views.py

#...
if article.like_users.filter(pk=request.user.pk).exists():
    # if request.user in article.like_users.all():
    # 좋아요 취소
    article.like_users.remove(request.user)
```

**템플릿에 추가**

```html
<!-- index.html -->

...
  {% for article in articles %}
    ...
    <form action={% url 'articles:like' article.pk %} method = 'POST'>
      {% csrf_token %}
      {% if request.user in article.like_users.all %}
        <input type="submit" value="좋아요 취소">
      {% else %}
        <input type="submit" value="좋아요">
      {% endif %}
    </form>
    <br>
```

**fontawesome과 bootstrap 이용해서 하트 UI 넣기**

...

- fontawesome에 가입이 안 되는 경우, 간단한 구현을 위해서 `window 키` + `.`에서 이모티콘을 활용해서 입력해도 된다.

```django
<!-- index.html -->
{% if request.user in article.like_users.all %}
{% comment %} <input type="submit" value="❤"> {% endcomment %}
	<button class="btn btn-ling" style="color: crimson,">❤</button>
{% else %}
	<button class="btn btn-ling" style="color: crimson,">🤍</button>
{% endif %}
```

**좋아요 인원 수 출력**

```django
<!-- index.html -->

{{ article.like_users.all|length}} 명이 이 글을 좋아합니다.
```



## 4. <실습> 프로필 페이지 만들기

**url 생성**

```python
# accounts/urls.py

path('<username>', views.profile, name='profile'),
```

**view 함수 생성**

```python
# accounts/views.py

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

def profile(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username = username)
    context = {
        'person' : person,
    }
    return render(request, 'accounts/profile.html', context)
```

**템플릿 생성**

```html
<!-- accounts/profile.html -->

{% extends 'base.html' %}

{% block content %}
<h1 class="text-center">{{ person.username }}의 프로필</h1>
<hr>
<!-- 팔로우/언팔로우 버튼 -->

<hr>
<!-- 게시글 -->
<h2>{{ person.username}}이 작성한 게시글</h2>
{% for article in person.article_set.all %}
  <div>{{ article.title }}</div>
{% endfor %}
<hr>
<!-- 댓글 -->
<h2>{{ person.username}}이 작성한 댓글</h2>
{% for comment in person.comment_set.all %}
  <div>{{ comment.content }}</div>
{% endfor %}
<hr>
<!-- 좋아요 한 글 -->
<h2>{{ person.username}}이 좋아요한 글</h2>
{% for article in person.like_users.all %}
  <div>{{ article.title }}</div>
{% endfor %}
{% endblock  %}
```

**게시글 작성자의 프로필로 가는 링크 만들기**

```html
<!-- index.html -->

<p><b>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{article.user.username }}</a></b></p>
```

**내 프로필로 가는 링크 만들기**

```html
<!-- base.html -->

<h3><a href="{% url 'articles:index' %}">Hello, {{ user.username }}</a></h3>
{% if request.user.is_authenticated %}
	<a href="{% url 'accounts:profile' user.username %}">Profile</a>
	...
```



## 5. <실습> Follow 만들기

**model 생성**

- 아래와 같이 자기참조를 하게 되면, `id`, `from_<model>_id`, `to_<model>_id` 이 3가지 중개 테이블의 필드가 생성되게 된다.

```python
# accounts/models.py

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

- `ManyToManyField`는 기존 모델에 필드가 추가되는 것이 아닌, 새로운 중개 테이블이 생성된다.

**url 생성**

```python
# accounts/urls.py

    path('<int:user_pk>/follow', views.follow, name='follow'),
```

**view 함수 생성**

```python
# accounts/views.py

@require_POST
def follow(request, user_pk):
    # 상대편
    person = get_object_or_404(get_user_model(),pk=user_pk)
    # 나
    user = request.user

    # 나 자신은 팔로우할 수 없다.
    if user != person:
    # if user in person.followers.all():
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
        else:
            person.followers.add(user)
    return redirect('accounts:profile', person.username)
```

**템플릿에 버튼 생성**

- Bootstrap `Jumbotron`을 넣어준다.

```html
<!-- accounts/profile.html -->

<!-- 팔로우/팔로잉 수 -->
<div class="jumbotron">
  <h1 class="display-4">{{ person.username }}</h1>
  <p class="lead">
    팔로워 수 : {{ person.followers.all|length }} / 팔로잉 수 : {{ person.followings.all | length }}
  </p>
  {% if request.user != person %}
    <!-- 팔로우/언팔로우 버튼 -->
    <form action="{% url 'accounts:follow' person.pk%}" method="POST">
      {% csrf_token %}
      {% if request.user in person.followers.all %}
        <button class="btn btn-primary">Unfollow</button>
      {% else %}
        <button class="btn btn-primary">Follow</button>
      {% endif %}
    </form>
  {% endif %}
</div>
<hr>
```



## <심화> 템플릿 분할 :star:

> [Django Template Tag](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/)에서 `{% include %}` 태그를 참고한다.

- 템플릿을 분할하여 include 태그를 사용한다.
- 템플릿 유지/보수에 매우 유용한다.

```django
<!-- accounts/profile.html -->

{% include 'accounts/_follow.html' %}
```



## <심화> Query 최적화

### Query 변수화

> `{% with%}`태그를 이훃해서 query를 변수화하여 중복되는 query 사용을 최적화 할 수 있다.

```django
<!-- accounts/_follow.html -->

<div class="jumbotron">
  {% with followers=person.followers.all followings=person.followings.all%}
    ...
  {% endwith %}
</div>
```

### Similar, Duplicate된 Query 제거하기

> ```
> ......?
> ```
>
> 자세한 내용은 [DB Access Optimization](https://docs.djangoproject.com/en/3.1/topics/db/optimization/) 문서를 참고한다.



***Copyright* © Song_Artish**