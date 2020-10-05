# Django CRUD

>대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인 
Create(생성), Read(읽기), Update(갱신), Delete(삭제)를 묶어서 일컫는 말



---

[TOC]

---



## Create

데이터를 작성하는 3가지 방법

**첫번째 방법**

- `article = Article()` : 모델 클래스로부터 인스턴스 생성
- `article.title` : 인스턴스로 클래스 변수에 접근해 해당 인스턴스 변수 변경
- `article.save()` : 인스턴스로 메서드 호출하여 DB에 실제로 저장

**두번째 방법**

- 클래스로 인스턴스 생성시, keyword 인자를 함께 작성

```shell
article = Article(title='second', content='django!')
article.save()
```

**세번째 방법**

- create() 메서드를 사용하면 쿼리셋 객체를 생성하고 save하는 로직이 한 번의 스텝으로 가능하게 된다.

```shell
 Article.objects.create(title='third', content='django!!')
```

​	

## Read

`all()`

- `QuerySet`을 return
- 리스트는 아니지만, 리스트와 거의 비슷하게 동작(조작할 수 있음)

---

`get()`

> pk 값 등 unique한 값을 조회할 때 사용한다.

- 객체가 없으면 `DoesNotExist` , 객체가 여러개면 `MultipleObjectReturned` 에러가 발생
- 위와 같은 특징을 가지고 있기 때문에 unique 혹은 Not Null 특징을 가지고 있으면 사용할 수 있다.

```shell
Article.object.get(pk=3)
Article.object.get(content='django!')
```
- `id` 혹은 `pk`로도 조회할 수 있다.

---

`filter()`

- 지정된 조회 매개 변수와 일치하는 객체를 포함하는 QuerySet을 리턴한다.

```shell
# 예시
>>> Article.objects.filter(content='django!')
<QuerySet [<Article: first>, <Article: fourth>]>
```



## Update

- 생성된 인스턴스 객체를 불러와 인스턴스 변수에 접근해 새로운 값으로 변경하고 저장한다.

```shell
article = Article.object.get(pk=3)
article.title = 'byebye'
article.save()
```



## Delete

- 생성된 인스턴스 객체를 불러온 후, `.delete()` 메서드를 호출하여 인스턴스를 삭제한다.

```shell
article.delete()
```



## Admin

- 이러한 DB의 CRUD를 admin페이지를 활용하면 쉽게 조작할 수 있다.

**관리자 생성**

```bash
$ python manage.py createsuperuser
```

**admin 페이지 등록**

```python
# admin.py
from .models import <모델명>

admin.site.register(<모델명>)
```



# Django CRUD 페이지 작성 요령



## 사전 준비

1. **URL 분리**

프로젝트 폴더 `urls.py`

```python
# crud/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

앱 폴더 `urls.py` - 앱 이름을 만들어준다.

```python
# articles/urls.py

from django.urls import path

app_name = 'articles'
urlpatterns = [
  
]
```



2. **base 템플릿 설정**

`base.html`

```html
<!-- templates/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="<https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css>"
    integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
<body>
  <div class="container">
    {% block content %}
    {% endblock %}
  </div>
  <script src="<https://code.jquery.com/jquery-3.5.1.slim.min.js>"
    integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous">
  </script>
  <script src="<https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js>"
    integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous">
  </script>
  <script src="<https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js>"
    integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous">
  </script>
</body>
</html>
```

`settings.py`

- `BASE_DIR` 이후는 base 템플릿이 위치할 폴더를 입력한다.

```python
# crud/settings.py

'DIRS': [BASE_DIR / 'templates'],
```



3. **메인 페이지 설정**

앱 폴더 `urls.py`, `views.py`, `index.html`

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
]


# articles/views.py

def index(request):
    return render(request, 'articles/index.html')
```

```django
<!-- templates/articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">Articles</h1>
{% endblock %}
```



## READ

`index.html` 수정

```python
# articles/views.py

from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
```

- DB에 접근하여 데이터를 불러온다.

```django
<!--templates/articles/index.html-->

{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">Articles</h1>
  <hr>
  {% for article in articles %}
    <p>글 번호: {{ article.pk }}</p>
    <p>글 제목: {{ article.title }}</p>
    <p>글 내용: {{ article.content }}</p>
    <hr>
  {% endfor %}
{% endblock %}
```



## CREATE

`new.html` - 실제 작성페이지 만들기

```python
# articles/urls.py

path('new/', views.new, name='new'),
```

```python
# articles/views.py

def new(request):
    return render(request, 'articles/new.html')
```

```django
<!-- templates/articles/new.html -->

{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">NEW</h1>
  <form action="{% url 'article:create '%}" method="POST">
    <label for="title">Title: </label>
    <input type="text" name="title"><br>
    <label for="content">Content: </label>
    <textarea name="content" cols="30" rows="5"></textarea><br>
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```

```django
<!-- templates/articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">Articles</h1>
  <a href="{% url 'articles:new' %}">[new]</a>
  <hr>
{% endblock  %}
```



`create.html` - 작성한 요청을 넘겨주는 페이지 만들기

```python
# article/urls.py

path('create/', views.create, name='create'),
```

```python
# article/views.py

from django.shortcuts import render, redirect
from .models import Article

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:detail', article.pk)
```

- 생성 요청을 받은 후, `create` 함수를 통해 해당 DB를 생성한 후, 메인페이지로 redirect한다.



**게시글 순서 변경**

```python
# articles/views.py

def index(request):
    # 1. articles = Article.objects.all()[::-1]	 # 파이썬이 변경
    # 2. articles = Artile.objects.order_by('-pk')  # DB에서 변경
```

- `order_by` 는 단일 쿼리에서는 사용할 수 없고 QuerySet 에서만 사용 가능하다.



**Http Method POST**

> `GET` 요청을 할 경우, 데이터가 URL에 노출되며 이러한 경우를 방지하기 위해서 CRUD의 C/U/D에서는 `POST` 방식을 사용한다. CRUD의 R의 경우, `GET`방식을 사용한다.



**CSRF Token**

> 사이트 간 요청 위조(Cross-Site-Request-Fogery)를 방지한다. 

- `POST`를 요청하는 `<form>` 태그 밑에 `{% csrf_token %}`을 입력한다.



## DETAIL

**urls 설정**

- variable routing → 주소를 통해 요청이 들어올 때 특정 값을 변수화 시킬 수 있다.
- 우리는 pk 값을 변수화 시켜 사용할 것. pk는 detail 함수의 pk라는 이름의 인자로 넘어가게 된다!
- `index.html` 의 `<a href="/articles/{{ article.pk }}/">[글 보러가기]</a>`  부분에서 `{{ article.pk }}` 가 실제 특정 숫자(pk값)일 것이고 요청이 보내질 때 숫자로 넘어 간다.
- 그럼 path에서 해당하는 숫자는 pk라는 변수에 저장될 것이다.

```python
# articles/urls.py

path('<int:pk>/', views.detail, name='detail'),
```

**views 설정**

```python
# articles/views.py

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```

**templates 설정**

- `detail.html` 파일 생성 후, `index.html` 페이지에 `detail.html` 페이지로 이동할 수 있는 링크를 생성한다.

```django
<!-- templates/articles/detail.html -->

{% extends 'base.html' %}

{% block content %}
  <h2 class='text-center'>DETAIL</h2>
  <h3>{{ article.pk }} 번째 글</h3>
  <hr>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>작성 시각: {{ article.created_at|date:"SHORT_DATE_FORMAT" }}</p>
  <p>수정 시각: {{ article.updated_at|date:"M j, Y" }}</p>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock  %}
```

```django
<!-- templates/articles/index.html -->

{% extends 'base.html' %}

{% block content %}
<h1 class="text-center">Articles</h1>
<a href="{% url 'articles:new' %}">[new]</a>
<hr>
{% for article in articles %}
  <p>글 번호: {{ article.pk }}</p>
  <p>글 제목: {{ article.title }}</p>
  <p>글 내용: {{ article.content }}</p>
  **<a href="{% url 'articles:detail' article.pk %}">[detail]</a>**
  <hr>
{% endfor %}
{% endblock  %}
```



**`humanize` (참고)**

> A set of Django template filters useful for adding a “human touch” to data.
>
> https://docs.djangoproject.com/en/3.1/ref/contrib/humanize/#module-django.contrib.humanize

```django
{% extends 'base.html' %}
{% load humanize %}

{% block content %}
  <h2 class='text-center'>DETAIL</h2>
  <h3>{{ article.pk }} 번째 글</h3>
  <hr>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>작성 시각: {{ article.created_at|naturalday }}</p>
  <p>수정 시각: {{ article.updated_at|naturaltime }}</p>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock  %}
```



## DELETE

`urls.py`

```python
# articles/urls.py

path('<int:pk>/delete/', views.delete, name='delete'),
```

`views.py`

```python
# articles/views.py

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)
```

- 이러한 구문을 통해 요청이 `POST`일 경우에만, 해당 DB를 삭제하게 한다.

```django
<!-- articles/detail.html -->

{% extends 'base.html' %}

{% block content %}
  ...
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <button class="btn btn-danger">DELETE</button>
  </form><br>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```



## Update

`urls.py`

```python
# articles/urls.py

path('<int:pk>/edit/', views.delete, name='edit'),
path('<int:pk>/update/', views.update, name='update'),
```

`views.py`

```python
# articles/views.py

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
```

`edit.html`

```django
<!-- articles/edit.html -->

{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">EDIT</h1>
  <form **action="{% url 'articles:update' article.pk %}"** method="POST">
    {% csrf_token %}
    <label for="title">Title: </label>
    <input type="text" name="title" value="{{ article.title }}"><br>
    <label for="content">Content: </label>
    <textarea name="content" cols="30" rows="5">{{ article.content }}</textarea><br>
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```



***Copyright* © Song_Artish**