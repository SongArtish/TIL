# Django Static & Media

---

[TOC]

---



## Static

> 정적 파일(static files)은 웹 사이트의 구성 요소 중에서 image, css, js 파일과 같이 해당 내용이 고정되어, 응답을 할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일을 말한다.

- 일반적인 경로를 입력하면 HTML에서 접근할 수 없으므로, servinng file을 통해 접근하도록 한다!
- 기본 static 경로 : `app_name/static/app_name/images/`
- 진행 중 적용이 안된다면 서버를 재시작한다.



**이미지 넣기**

```python
# settings.py (Default 값)

STATIC_URL = '/static/'
```

```django
<!-- templates에서 로드하기 -->

{% extends 'base.html' %}
{% load static %}

<!-- 물리적 파일의 경로를 나타낸다. -->
<img src="{% static 'articles/images/sample.png' %}" alt="sample">
```

- static 파일이 보이지 않으면, server를 한 번 껐다가 켜준다.





### Static Files

위치 : `settings.py`

- `STATIC_ROOT` (배포 할 때 사용!)
  - collectstatic이 **배포**를 위해 정적 파일을 수집하는 절대 경로
  - collectstatic : 프로젝트 배포 시 흩어져 있는 정적 파일들을 모아 특정 디렉토리로 옮기는 작업
- `STATIC_URL` (기본)
  - STATIC_ROOT에 있는 정적 파일을 참조 할 때 사용할 URL
- `STATICFILES_DIRS`
  - **app내의 static 디렉토리 경로를 사용하는 것 외에 추가적인 정적 파일** 경로 정의

```python
# settings.py

STATIC_URL = '/static/'
STATICFILES_DIR = [ BASE_DIR / 'crud' / 'static']
```

```django
<!-- base.html -->
  {% block css %}{% endblock %}
</head>

<!-- template -->
{% block css %}
<link rel="stylesheet" href="{% static 'stylesheets/style.css'%}">
{% endblock %}
```



## Media

> 미디어 파일 (media files)은 사용자가 웹에서 업로드 하는 정적 파일이다. (image, pdf, video 등)



### Media Files 

위치 : `settings.py`

- `MEDIA_ROOT`
  - 사용자가 업로드 한 파일을 보관(저장)할 디렉토리의 절대(물리적) 경로
- `MEDIA_URL`
  - MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL (사용자가 접근할 수 있는 경로)
  - 업로드 된 파일의 주소 (URL)를 만들어 주는 역할

MEDIA_URL 및 STATIC_URL은 서로 다른 값을 가져야 한다.



**Model 작성**

```python
# articles/ models.py

class Article(models.Model):
    ...
    image = models.ImageField(blank=True)
    image = models.ImageField(blank=True, upload_to='%y/%m/%d/')

    # blank - 유효성 검사, 사용자가 데이터를 입력하지 않아도 무방
    # null - DB의 해당 column이 null 값을 가져도 된다.
    # upload_to - 업로드 한 날짜별로 저장 폴더 생성(?)
```

> - `image = models.FileField()`
> - `image = models.ImageField()`
>   - ImageField가 FileField보다 이미지를 더 잘 관리할 수 있다.

- `ImageField` 를 사용하기 위해서는 `Pillow`라는 pip를 설치해야 한다.

```bash
$ pip install Pillow
```

- Model을 수정했으므로, `makemigrations`, `migarte`을 한다.

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- 기본 `<form>` 태그는 문자열만 인코딩 하기 때문에, 이미지를 업로드 할 수 있도록 하기 위해서 다음과 같이 **인코딩 타입**을 설정한다.

```django
<!-- form.html -->
  <form action="" method="POST" enctype = "multipart/form-data">
```

- 요청정보에 담겨는 있는 파일을 `request.FILES`라는 인자를 통해 `<form>` 태그에 넘겨준다.

```python
# articles/views.py
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        ...
```

- 템플릿에서 다음과 같이 이미지의 정보를 불러올 수 있다.

```django
<!-- articles/detail.html -->

{% if article.image %}
    <img src="{{ article.image.url }}" alt="{{ article.image }}">
    <p>{{ article.image }}</p>
    <p>{{ article.image.name }}</p>
    <p>{{ article.image.url }}</p>
    <p>{{ article.image.path }}</p>
{% endif %}
```



### Media 파일 제공 설정 (개발단계)

> [Managing Static Files](https://docs.djangoproject.com/en/3.1/howto/static-files/)

**MEDIA_URL 설정**

```python
# settings.py

import os
# 실제 파일이 저장되는 폴더 : [](괄호)를 사용하지 않는 것이 특징!
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')	# 혹은 이렇게 작성해도 된다! (이렇게 작성된 예시가 더 많다.)
# 사용자가 접근하는 url 경로
MEDIA_URL = '/media/'
```

```python
# <프로젝트 폴더>/urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- 제일 밑의 `static(...)` 이하의 코드가 제일 중요하다.
- `STATIC_URL`과 `MEDIA_URL`을 혼동하지 않도록 주의한다 !

```django
<!-- 만약 article에 이미지가 있으면 (if 구문 매우 직관적)-->
  {% if article.image %}
    <img src="{{ article.image.url }}" alt="{{ article.image }}">
  {% endif %}
```

**UPDATE**

- update를 할 경우에는 form에 기존 데이터가 있어야 하므로 `request.FILES` 인자를 넣어준다.

```python
# articles/views.py
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
```

- python에서 `키워드 인자`는 제일 마지막에 넣어줘야 한다. (인자 순서 주의!)



### Media 파일 불러오기

- 위에서 `settings.py`에 아래와 같이 **MEDIA_URL**을 작성하였다.

```python
# settings.py
# 사용자가 접근하는 url 경로
MEDIA_URL = '/media/'
```

- 따라서 이를 이용하여 파일에 접근하면된다.

```python
<img src="/media/{{ book.thumbnail_url }}">
```

- :white_check_mark: 참고로 여기서 `{{}}` 안에 들어있는 것은 변수이다.



## <참고>  이미지 썸네일 형태로 저장하기 + 확장자를 변경하여 용량 줄이기

`piilkit` pip를 설치한 후, `django-imagekit`라는 pip를 설치한다. (반드시 순서를 지킬 것!)

```bash
$ pip install pilkit
```

```bash
$ pip install django-imagekit
```

- `imagekit`를 `settings.py`에 추가

```python
# settings.py

INSTALLED_APPS = [
    ...
    'imagekit',
]
```

```python
# models.py

from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Article(models.Model):
    ...
    image = ProcessedImageField(
        blank = True,
        # Thumbnail(저장크기 x축, y축)
        processors = [Thumbnail(200, 300)],
        # format : 원하는 확장자로 변경
        format = 'JPEG',
        # 'quality' : JPEG의 퀄리티 변경
        options = {'quality':90},
    )
```



***Copyright* 2020 © Song_Artish**