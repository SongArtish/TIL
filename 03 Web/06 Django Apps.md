# Apps

> 여러 개의 앱 관리하기

***

[TOC]

***



## 시작하기

### 생성

> 프로젝트와 앱을 생성한다.

```bash
$ django-admin startproject <프로젝트 이름>
$ python manage.py startapp <앱 이름>
```

### 설정

> 앱을 등록하고 언어와 시간을 설정한다.

- 위치 : `setting.py > INSTALLED_APPS`



## 1. 여러 개의 앱

### `urls.py`

- 위치 : `<프로젝트 폴더> / url.py`

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<앱 폴더>/', include('<앱 폴더>.urls')),
    # <url>/<앱 폴더>/ 이하로 연결하는 역할
]
```



### `urls.py`

- 위치 : `<앱 폴더> / urls.py`

> 앱 폴더 내에 `urls.py`를 생성한다.

```python
from django.urls import path
from . import views

app_name = '<앱 이름>'
urlpatterns = [
    path('<템플릿 이름>/', views.<템플릿 이름>, name='이름 값'),
]
```

```python
# 예시
path('dinnder/<str:menu>/<int:num>/', views.dinner, name='dinner'),
```



### `views.py`

- 위치 : `<앱 폴더> / views.py`

```python
from django.shortcuts import render

def dinner(request,menu,num):
    context = {
        'menu': menu,
        'num': num,
    }
    return render(reqeust, 'dinner.html', context)
```



<앱 폴더>/<templates>/<앱 폴더이름>

- installed apps에서 찾아갈 때 순서대로 찾아가는데, 찾아갈 수 있게 하기 위해서

```python
from django.shortcuts import render

def dinner(request,menu,num):
    context = {
        'menu': menu,
        'num': num,
    }
    return render(reqeust, 'pages/dinner.html', context)
```



## 2. 템플릿 상속



<프로젝트 폴더>/<templates>/base.html



```html
{% block <블럭 이름> %}
{% endblock %}
```

- block enter로 생성가능

- 블럭 내의 내용은 수정 가능하다.

```html
<body>
    <div class="container">
        {% block content %}
        {% endblock %}
    </div>
</body>
```

<프로젝트 폴더>/settings.py > TEMPLATES

```python
TEMPLATES = [
    ...
    'DIRS' : [BASE_DIR/'<프로젝트 이름'/'templates'],
    'APP_DIRS' :True,
    ...
]
```

- 템플릿을 가져올 때 DIRS의 폴더를 가장 먼저 조사하고 후에 앱폴더의 템플ㄹ릿을 조사한다.

dinner.html

```html
{% extends 'base.html' %}
{% block content %}
	<h2> 여기에 내용을 입력합니다. </h2>
{% endblock %}
```











```html
<a href="/pages/"></a>

<a href="/pages/index/"></a>
실제 해당 url로 이동
<a href="{% url 'pages:index'}"></a>
pages라는 이름의 앱에 있는 index라는 이름의 url로 이동
따라서, 어떠한 경로로 바뀌더라도 잘 따라간다.
```

```python
app_name = '<앱 이름>'
urlpatterns = [
    path('dinnder/<str:menu>/<int:num>/', views.dinner, name='dinner'),
]
```

