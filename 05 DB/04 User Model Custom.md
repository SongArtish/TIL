# User Model Custom

2020.09.23

> 여기서는 `1: N Relationship Field` 중 하나인 User에 대해서 학습한다.

---

[TOC]

---



## 1. User 모델 개념

> 유저 지정 모델을 참조하는 `AUTH_USER_MODEL` 설정 값을 변경해 기본 유저 모델을 재정의(override) 할 수 있다. ( [Customizing authentication in Django](https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#custom-users-and-the-built-in-auth-forms))
>
> - **단, 프로젝트의 첫 migrate를 실행하기 전에 완료해야 한다.**

### `AUTH_USER_MODEL`

> User를 나타내는데 사용하는 모델로, 기본 값은 `auth.User`이다.

- User를 나타내는 모델은 Django에서 다음과 같은 순서로 정의되어 있다.

```python
from models.Model
from AbstractBaseUser
from AbstractUser
import User
```

### `AbstractBaseUser`

- password와 last_login만 기본적으로 제공하기 때문에 자유도가 높지만 다른 필요한 필드는 모두 작성해야 한다.

### `AbstractUser`

- 관리자 권한과 함께 완전한 기능을 갖춘 유저 모델을 구현하는 기본 클래스



## 2. User 모델 커스텀

### 2.1 User 모델 만들기

**클래스 생성**

- 기본 `models.Model`이 아닌 Django에서 제공하는 `AbstractUser`를 import 해서 상속받는 모델을 생성한다.

- migrate를 하기 전에 아래와 같이 `pass`를 입력한 클래스라도 생성하도록 한다!

```python
# accounts/models.py

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

**settings.py 설정**

- settings.py 제일 밑에 등록할 User 모델을 입력한다.

```python
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```

**admin 등록**

- admin페이지에서 AUTH_USER_MODEL을 변경한다.

```python
# accounts/admin.py

from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```



### Built-in Auth Forms

1. **일반 Form 형태**

   - `AbstractBaseUser`의 모든 subclass와 호환된다.
   - 종류 : `AuthenticationForm, SetPasswordForm, PasswordChangeForm, AdminPasswordChangeForm`

2. **Model Form 형태**

   - User와 연결되어 있어서 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야 한다.
   - 종류 : `UserCreationForm, UserChangeForm`

   

### 2.2 UserCreationFrom 커스텀

- 활성화된 user가 auth.User에서 account.User에서 변경되었기 때문에 account.User를 사용하는 모델폼을 다시 작성해야 한다.
- 기존의 `UseCreationForm`을 상속하고, Meta도 기존 `UserCreationForm`의 `Meta`를 상속받는다.
- ㄱ리고 meta의 model만 활성화된 user mode(`get_user_model`)로 변경해주면 된다.

```python
# accounts/forms.py

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)
```

- 마지막의 tuple의 항목은 사용자가 원하는 방식으로 가감할 수 있다.
- 회원가입 form을 변경해준다.

```python
# accounts/views.py

from .forms import CustomUserCreationForm

def signup(request):
    # ...
    form = CustomUserCreationForm(request.POST)
    ...
```



### User 모델 참조 :gem:

1. **settings.AUTH_USER_MODEL** : 유저 모델에 대한 외래 키 또는 M : N 관계를 정의할 때 사용한다.
   - models.py에서 유저 모델을 참조할 때 사용
   - 반환값 : 문자열

2. **get_user_model()**
   - models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용
   - 반환값 : User Object



### 2.3 유저 모델 참조하기

**`ForeignKey` 작성하기**

- Article 모델에서 User 모델을 참조받는다.

```python
# articles/models.py

from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ...

```

- 이후 `makemigrations`를 하면 <u>다음과 같은 화면</u>이 터미널에 표시된다.

---

**<참고> migrate 시의 오류 해결방법**

- 이것은 기존 데이터에 대해서 default 값이 존재하지 않기 때문에 발생한다.

```bash
$ python manage.py makemigrations
You are trying to add a non-nullable field 'user' to article without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option:
```

- 여기서 1번 옵션을 선택하기 위해 **1**을 입력한다.

```bash
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>>
```

- 이후 default 값으로 적당하게 **1**을 입력한다.
- 다음과 같이 생성 시 default 값을 입력해줘도 된다.

```python
# articles/modesl.py

class Article(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
```

---



## 3. User : Article



### 3.1 form에서 User 항목 숨기기

- 게시글 작성 Form에서 사용자 지정 항목이 표시되므로 이것을 제거해준다.

```python
# articles/forms.py

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        # 1안 : 표시할 항목 선택하기
        fields = ['title', 'content',]
        # 2안 : 제외할 항목 선택하기
        exclude = ['user',]
```



### 3.2 작성자 정보 저장하기

- 그리고 form에서 article을 저장하기 전, user에 대한 정보를 저장하는 코드를 작성한다.

```python
# articles/views.py

def create(request):
    # ...
    	if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            ...
```



### 3.3 게시글 작성자 표시하기

`article.user.username`

- user에서 `__str__`을 기본적으로 `user.username`으로 지정하고 있다.

```django
<!-- articles/index.html -->

{% for article in articles %}
    <p><b>작성자 : {{ article.user.username }}</b></p>
	...
```



### 3.4 게시글 수정자 확인하기

- 게시글을 수정하는 요청이 들어온 경우, 작성자(article.user)와 현재 수정자(request.user)가 같은지 비교한다.

```python
# articles/views.py

def update(request, pk):
    # ...
        # 수정저와 게시글 작성자가 같은지 확인하기!
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    # 다르다면 index 페이지로 돌려보내기
    else:
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
```

- 위와 같은 방법으로 삭제 요청을 받는 경우에논 작성자와 요청자를 비교한다.

```python
# articles/views.py

def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', pk)
```



### 3.5 사용자의 글이 아니면 수정/삭제 버튼 보이지 않기

- 템플릿에서 요청자와 작성자가 같은지 확인한는 if문을 만들어 그 안에 수정/삭제 버튼을 넣어준다.

```django
<!-- articles/detail.html -->

...
{% if request.user == article.user %}
	<a href="{% url 'articles:update' article.pk %}">UPDATE</a><br>
	<form action="{% url 'articles:delete' article.pk %}" method="POST">
    	{% csrf_token %}
    	<input type="submit" value="DELETE">
	</form>
{% endif %}
...
```



## 4. User : Comment



### 4.1 댓글에서 User모델 참조하기

- 게시글에서와 같은 방식으로 댓글에서도 User 테이블을 참조하도록 코드를 작성한다.
- 모델이기 때문에 참조할 테이블 이름을 **`settings.AUTH_USER_MODEL`**로 참조하도록 한다 ! :star:

```python
# articles/models.py

class Comment(models.Model):
    # ...
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	...
```

- model이 변경 되었기 때문에 migrate을 진행한다.



### 4.2 form에서 User 항목 숨기기

- 댓글 작성란에서 user를 선택할 수 있는 창을 보여주지 않도록 한다.

```python
# articles/forms.py

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ['article', 'user',]
```



### 4.3 작성 시 user 값 저장하기

- commnet를 작성할 때, comment의 user 값을 불러와서 저장해준다.

```python
# articles/views.py
def comments_create(request, pk):
	# ...
    if comment_form.is_valid():
            comment = comment_form.save(commit = False)
            comment.article = article
            # comment의 user 값을 저장해준다.
            comment.user = request.user
            comment.save()
```

- 작성하려는 사람이 로그인이 되었는지도 확인해준다.

```python
def comments_create(request, pk):
	if request.user.is_authenticated:
        ...
```



### 4.4 댓글 작성자 표시하기

- 템플릿에서 `comment.user.username`을 추가하여 댓글 작성자를 표시한다.

```django
<!-- articles/detail.html -->
...
{% for comment in comments %}
    <li>
      {{comment.user.username}} : {{ comment.content }}
    ...
```



### 4.5 로그인 유저에게만 댓글 작성창 나타내기

- 템플릿에서 로그인 유저인지를 확인하는 if문을 작성하고 해당 if문 안에 댓글 작성 코드를 넣는다.
- else문을 사용해서 댓글을 작성하지 않은 경우에는 로그인을 하라는 메시지를 표시하며 로그인 페이지로 넘겨주는 `<a>` 태그를 작성한다.

```django
<!-- articles/detail.html -->

...
<h4>댓글 작성</h4>
{% if request.user.is_authenticated %}
    <form action="{% url 'articles:comments_create' article.pk %}" method = 'POST'>
        {% csrf_token %}
        {{ comment_form }}
        <input type="submit">
    </form>
{% else %}
	<a href="{% url 'accounts:login' %}">[댓글을 작성하려면 로그인하세요.]</a>
{% endif %}
...
```



### 4.6 댓글 작성자 외 삭제버튼 가리기

- if문을 사용한다.

```html
<!-- articles/detail.html -->

...
{% if request.user == commnet.user %}
	<form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" class="d-inline">
    	{% csrf_token %}
    	<input type="submit" value="DELETE">
	</form>
{% endif %}
...
```



### 4.7 작성자 외 댓글 삭제 logic 변경

- `comments_delete` 함수에서 로그인 여부 및 현재 요청자가 댓글 작성자와 동일한지를 확인한 후 댓글이 삭제되도록 함수의 logic을 개편한다.

```python
# articles.views.py

@require_POST
def comments_delete(request, article_pk, comment_pk):
    # 1. 로그인 여부 확인
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        # 댓글 작성자인지 확인
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)
```



*Copyright* © Song_Artish