# Django Form

2020.09.14.

> Django 프로젝트의 주요 **유효성 검사 도구**들 중 하나로 공격 및 우연한 데이터 손상에 대한 중요한 방어수단

**역할**

1. 랜더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성
3. 클라이언트로부터 받은 데이터 수신 및 처리

---

[TOC]

---

## 사전준비 :apple:

### 1. 가상환경 생성

폴더에서 `git bash`를 실행해 가상환경 생성

```bash
python -m venv venv
```



### 2. 프로젝트 생성

```bash
$ django-admin startproject <프로젝트 이름> .
```

- 명령대상객체, 명령어, 프로젝트 이름, 현재 폴더



### 3. `VS Code` 가상환경 설정

**인터프리터 설정**

`Ctrl` + `Shift` + `P` 버튼을 누른 후 `>Select Interpreter`에서 생성한 가상환경 선택

**CLI 명령어로 실행**

- 단, terminal이 종료될 경우 가상환경도 종료되기 때문에 주의!

```bash
$ source venv/Scripts/activate
```

- `source`는 bash의 내부 명령어로 명령어 뒤에 오는 파일을 읽어서 파일 내용 실행하는 역할.

종료하기

```bash
$ deactivate
```



### 4.  pip 설치

**터미널에서 설치**

```bash
$ pip install django
```

**`requirements.txt` 설치**

```bash
$ pip install -r requirements.txt
```

- pip야 설치해! 어떻게? `requirements.txt`를 읽어서(`read`) !



### 5.  앱 생성

```bash
$ python manage.py startapp <앱이름>
```



### 6. 앱 등록

`settings.py`

```python
INSTALLED_APPS = [
    'articles',
]
```



### 7. base 템플릿 만들기

위치 : `<프로젝트 폴더>/ <templates>/ base.html` 생성

```html
<!-- base.html -->
<body>
  <div class="container">
  {% block content %}
  {% endblock  %} 
  </div>
</body>
```

- `base.html`에 `block` 생성

 **템플릿 등록**

```python
# settings.py

TEMPLATES = [
    'DIRS' : [BASE_DIR / '<프로젝트 이름>' / 'templates'],
]
```



### 8. 앱 경로 등록

```python
# <프로젝트 폴더>/urls.py

from django.urls import path, include

urlpatterns = [
    path('articles/', include('articles.urls'))
]
```



### 9. 앱 폴더 `urls.py` 만들기

- 앱 이름 설정
- 페이지 `url`, `view 함수`, `name` 설정

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # INDEX 페이지를 위한 url, view, name 설정
    path('index/', views.index, name = 'index'),
]
```



### 10. view함수 만들기

```python
# views.py

def index(request):
    # articles/index/ 로 접근하면, 아래의 html 페이지를 보여준다.
    return render(request, 'articles/index.html')
```



### 11. 템플릿 만들기

위치 : `<앱 폴더> / <tempaltes> / <앱 이름> / index.html`

- `base.html`을 extends 하기
- block 넣기

```html
<!-- index.html -->

{% extends 'base.html' %}
{% block content %}
  <h1>INDEX PAGES</h1>
{% endblock  %}
```



### 12. Model 만들기

- `model`을 import 해서 상속받아 모델을 작성한다.

```python
# models.py

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```



### 13. 마이그레이션

- Model 설계도 생성

```bash
$ python manage.py makemigrations
```

- migrate로 설계도를 DB에 반영

```bash
$ python manage.py migrate
```



### 14. 서버 실행

```bash
$ python manage.py runserver
```



## Form Class

> [Working with forms](https://docs.djangoproject.com/en/3.1/topics/forms/)
> form 내 field, field 배치, 디스플레이 widget, label, 초기값, 유효하지 않는 field에 관련된 에러메시지 결정
> 사용자의 데이터를 받을 때 해야 할 과중한 작업(데이터 유효성 검증, 필요시 입력된 데이터 검증 결과 재출력, 유효한 데이터에 대해 요구되는 동작 수행 등)과 반복 코드를 줄여줌

### Form 선언

앱 폴더 내에 `forms.py` 파일 생성 
(파일명이 `forms.py`일 필요는 없지만, 권장)

```python
# articles/forms.py

from django import forms
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
```
```python
# articles/views.py

# forms.py에서 가져오기
from .forms import ArticleForm

def new(request):
    # 인스턴스 생성
    form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)
```

```django
<!-- html에서의 form 사용 -->

<form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>
```



### Form Rendering Options

- `{{ form.as_table }}` : `<tr>` 태그에 담아 각 필드를 테이블 행으로 렌더링
- `{{ form.as_p }}` : `<p>` 태그에 담아 각 필드를 단락(paragraph)으로 렌더링
- `{{ form.as_ul }}` : `<ul>` 태그에 담아 각 필드를 list item으로 렌더링

**템플릿 세분화**

> Custom에 용이하기 때문에!

1. Manual Method

```django
<form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <div>
        {{ form.title.errors }}
        {{ form.title.label_tag }}
        {{ form.title }}
    </div>
    <div>
        {{ form.content.errors }}
        {{ form.content.label_tag }}
        {{ form.content }}
    </div>
    <input type="submit">
</form>
```

2. Looping Method

```django
<form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {% for field in form%}
        {{ field.errors }}
        {{ field.label_tag }}
        {{ field }}
    {% endfor %}
    <input type="submit">
  </form>
```



### Form Fields

- [Form fields](https://docs.djangoproject.com/en/3.1/ref/forms/fields/)는 입력 유효성 검사 논리를 처리하며 템플릿에서 직접 사용된다.

```python
# articles/forms.py	

from django import forms

class ArticleForm(forms.Form):
    # dropbox의 목록 만들기
    REGION_A = 'Seoul'
    REGION_B = 'Daejeon'
    # tuple 형태로 넣어준다 (DB가 받을 값, 사용자 출력 값)
    REGIONS = [
        (REGION_A, '서울'),
        (REGION_B, '대전'),
    ]
 	# !!key 값을 'Seoul'과 같이 str으로 넣어주면 작동하지 않는다!!
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
    region = forms.ChoiceField(choices=REGIONS, widget=forms.RadioSelect)
```





## Model Form

> Django에서는 model을 통해 model에서 이미 정의한 필드를 Form Class로 만들 수 있다. [ModelForm 공식문서](https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/)

```python
# articles/forms.py

from django import forms
from .models import Article

# model을 통해서 클래스 생성하기
class ArticleForm(forms.ModelForm):
    # 메타클래스 작성 - ModelForm을 정의하기 위한 Model
    class Meta:
        # Article 모델을 통해서 만들고
        model = Article
        # 필드는 모든 것을 가지고 올 것이다.
        fields = '__all__'
```



### Widget

> [Widget](https://docs.djangoproject.com/en/3.1/ref/forms/widgets/#module-django.forms.widgets)은 Django의 HTML input 요소를 표현한다.
>
> - 위젯은 반드시 form fields에 할당된다.

```python
# widget 예시
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title', 
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        # 에러 메시지 설정
        error_messages={
            'required': 'Please enter your content'
        }
    )
    
    class Meta:
        model = Article
        fields = '__all__'

```



### Create

- `Model Form`을 통해서 기존의 `new`와 `create` 앱을 하나의 앱으로 통합할 수 있다.

```python
# articles/views.py

from .forms import ArticleForm	# forms.py에서 가져오기

def create(request):
    # 다른 요청 메서드가 많기 때문에 먼저 POST 조건구문
    # http method가 POST 일때
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # Model에 대한 유효성 검사
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    # GET (http method가 POST가 아닌 다른 method일 때)
    else:
        form = ArticleForm()
    context = {
        # 1. is_valid에서 내려온 form : 에러 메시지 포함
        # 2. else 구문에서 내려온 form
        'form': form,
    }
    return render(request, 'articles/new.html', context)

```

```django
<!-- articles/create.html -->

{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">CREATE</h1>
  <!-- action이 비워있으면, 자신에게 action-->
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```

- `<input>` 태그에 데이터를 공백으로 작성 후 에러 메시지 출력 확인하기



### Update

- `request.POST` : 사용자가 form을 통해 전송한 데이터
- `instance` 인자 : 수정 대상이 되는 객체

```python
# articles/urls.py
    path('<int:pk>/update/', views.update, name='update'),
```

```python
# articles/views.py

# update 대상이 있어야하므로, pk(index) 값을 가져온다
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':    # update
        # form 인스턴스를 생성한다.
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:   # edit
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        'article' : article,
    }
    return render(request, 'articles/update.html', context)
```

```django
<!-- articles/update.html -->

{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">UPDATE</h1>
  <!-- action을 비우면 원래의 페이지로 보내게 된다 -->
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:detail' article.pk %}">[back]</a>
{% endblock %}

```

```django
<!-- articles/detail.html -->

<a href="{% url 'articles:update' article.pk %}">UPDATE</a><br>
```

- `detail.html` 페이지에서 update 버튼을 추가해준다.



### Delete

```python
# articles/urls.py

path('<int:pk>/delete/', views.delete, name='delete'),
```

```python
# articles/views.py

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('article:detail', article.pk)
```

```html
<!-- articles/detail.html -->

<form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
</form>
```

- `detail.html`페이지에서 delete 버튼을 추가해준다.



### <참고> Form과 Model Form의 차이점

**Form**

- 어떤 모델에 저장해야 하는지 알 수 없기 경우, 유효성 검사를 하고 실제로 DB에 저장할 때는  `cleaned_data` 와 `article = Article(title=title, content=content)` 를 사용해서 따로 `.save()` 를 해야 한다.
- Form Class가 `cleaned_data` 를 딕셔너리로 만들어서 제공해 주고, 우리는 `.get` 으로 가져와서 Article 을 만드는데 사용한다.

**Model Form**

- Django 가 해당 모델에서 양식에 필요한 대부분의 정보를 이미 정의한다.



## Bootstrap Form

> [공식문서](https://getbootstrap.com/docs/4.5/components/forms/)

### i ) 필수 Class 직접 입력

- `form-group`, `form-control` 이 2가지 class name이 핵심이다.

```django
<!-- form-group -->

...
<h2>Bootstrap Form</h2>
<form action="" method="POST">
  {% csrf_token %}
  {% for field in form %}
    <div class="form-group">
      {{ field.errors }}
      {{ field.label_tag }} 
      {{ field }}
    </div>
  {% endfor %}
  <button class="btn btn-primary">작성</button>
</form>
```

```python
# form-control

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget = forms.TextInput(attrs={
            'class' : 'my-title form-control',
            'placeholder' : 'Enter the title',
            'maxlength' : 10,
        })
```

- Error 메시지는 Bootstrap을 다음과 같은 활용할 수 있다.

```django
<form action="" method="POST">
  {% csrf_token %}
  {% for field in form %}
    {% if field.errors %}
      {% for error in field.errors %}
        <div class="alert alert-warning" role="alert">{{ error|escape }}</div>
      {% endfor %}
    {% endif %}
    <div class="form-group">
      {{ field.label_tag }} 
      {{ field }}
    </div>
  {% endfor %}
  <button class="btn btn-primary">작성</button>
</form>
```



### ii ) Bootstrap 라이브러리 설치

```bash
$ pip install django-bootstrap4
```
- settings.py 에 등록

```python
# settings.py
INSTALLED_APPS = [
    'bootstrap4',
]
```

- `base.html`에 `load`와 `cdn`을 붙혀넣어준다.

```django
<!-- articles/base.html -->

<!-- 제일 상단에-->
{% load bootstrap4 %}

<!-- cdn : head 부분 -->
{% bootstrap_css %}

<!-- cdn : body 아래 부분 -->
{% bootstrap_javascript jquery='full' %}
```

- 템플릿에서는 다음과 같이 적용할 수 있다.

```django
<!-- articles/update.html -->

{% extends 'base.html' %}
<!-- 상속 아래부분에 load를 넣는다. -->
{% load bootstrap4 %}

{% block content %}
  ...
  <form action="" method="POST">
    {% csrf_token %}
    <!-- {{ form.as_p}}를 대신해서 -->
    {% bootstrap_form form layout='horizontal' %}
    <!-- <input type="submit">를 대신해서 -->
    {% buttons submit="Submit" reset="Cancel" %}{% endbuttons %}
  </form>
{% endblock %}
```



## View decorator

[View decorators](https://docs.djangoproject.com/en/3.1/topics/http/decorators/)

> 데코레이터(decorator)란 어떤 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 '연장'하게 해주는 함수이다.
>
> - Django는 다양한 HTTP 기능을 지원하기 위해 뷰에 적용 할 수있는 여러 데코레이터를 제공



### Allowed HTTP methods

> [4가지 종류] 
> `require_http_methods([**요청 방식 리스트])`
> `require_GET()`
> `require_POST()`
> `require_safe()`
>
> - 공식문서에서는 `require_GET()`보다 `require_safe()`를 사용하기를 권장한다.

**`require_http_methods()`**

- view가 특정한 요청 method만 허용하도록 하는 데코레이터

```python
# views.py

from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def my_view(request):
	pass
```

**`require_POST()`**

- view가 POST 메서드 요청만 승인하도록 하는 데코레이터

```python
# views.py 예시
# 데코레이터 활용하면 다음과 같이 변경 가능
from django.views.decorators.http import require_POST

@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```

- url로 `delete` 시도 후 (1) 405 에러페이지 (2) terminal 로그 확인하기



***Copyright* © Song_Artish**