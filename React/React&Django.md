# React-Django 연결하기

2021.03.22

---

[TOC]

---



## 1. Django Setup

- 먼저 Django를 설치한다.

```bash
$ pip install django
```

- 그리고 작업할 폴더에서 Django 프로젝트를 생성한다.
  - :white_check_mark: 현재 폴더 하위 폴더에 프로젝트를 생성할 경우 맨 마지막의 `.(점)`을 입력하지 않는다.

```bash
$ django-admin startproject <프로젝트명> .
```

- Django 프로젝트 내에서 필요한 앱들을 생성한다.
  - 아래의 명령어는 `manage.py` 파일이 위치한 폴더에서 실행한다.

```bash
$ python manage.py startapp <앱 이름>
```

- :ballot_box_with_check: 생성한 app은 `settings.py`에 등록해주어야한다! (자세한건 Django 문서를 참고한다.)



## 2. React Create Projects

- npm을 통해서 react를 설치한다.

```bash
$ npm install -g create-react-app
```

- 아래의 명령어를 통해 react 프로젝트를 생성한다.

```bash
$ create-react-app <프로젝트명>
```



## 3. Install API with DRF

> DRF(Django REST Framework)

- DRF를 설치한다.

```bash
$ pip install djangorestframework
```

- 그리고 `rest_framework`를 `settings.py`에 등록한다.

```python
# settings.py

INSTALLED_APPS = [
    'accounts',
    'rest_framework',	# 여기에 등록해준다.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



## 4. Django CORS Setup

> Django로 REST Api를 만들었다. 이제 Frontend랑 연결을 해야하는데, 이 때 CORS 오류가 발생하기 때문에 이와 관련한 설치/설정이 필요하다.

- 먼저 `django-cores-headers`를 설치한다.

```bash
pip install django-cors-headers
```

- 위에서 설치한 패키지를 아래와 같이 `settings.py`에 등록한다.
  - **설치한 앱**, **미들웨어**, 그리고 교차 출처 리소스 공유를 허락한 **서버 리스트**를 작성한다.

```python
# settings.py

## 1. INSTALLED_APPS
INSTALLED_APPS = [
    'accounts',
	'rest_framework',
    'corsheaders',	# CORS 관련 추가
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

## 2. MIDDLEWARE
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',    # CORS 관련 추가
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

## 3. CORS_ORIGIN_WHITELIST
CORS_ORIGIN_WHITELIST = [
 'http://127.0.0.1:8000',
 'http://127.0.0.1:8080',
 'http://127.0.0.1:8081',
]

CORS_ALLOW_CREDENTIALS = True
```



## 5. Use React Template

> Django 템플릿을 더 이상 사용하지 않기 때문에 Django `settings.py` 파일 내에 **static 경로 를 변경**해야 한다.

- `TEMPLATES > DIRS`에서 경로를 변경해준다.

```python
# settings.py
import os	# 맨 위에서 import 한다.

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, '<react 프로젝트명>', 'build'),	# 경로 변경
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- :ballot_box_with_check: 여기까지 설정하고 `python manage.py runserver`을 실행해보면 아직 템플릿이 변경되지 않은 것을 확인할 수 있는데, django 템플릿이 나오는 것이 정상이 맞다.



## 6. Django React Template Build

- React 템플릿을 적용하기 위해서는 경로를 명령어로 다시 한 번 알려줘야한다.
- 먼저 Django 프로젝트 내에 있는 `manage.py` 코드를 변경한다.
- 아래와 같이 중간에 `## React Template Build` 주석 사이의 코드를 추가해준다.

```python
# manage.py

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ari.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # execute_from_command_line(sys.argv)

    ## React Template Build
    try:
        if sys.argv[2] == 'react':
            project_root = os.getcwd()
            os.chdir(os.path.join(project_root, "<react 프로젝트명>"))
            os.system("npm run build")
            os.chdir(project_root)
            sys.argv.pop(2)
    except IndexError:
        execute_from_command_line(sys.argv)
    else:
        execute_from_command_line(sys.argv)
    ## React Template Build
```

- 마지막으로 `urls.py`를 수정한다.
  - `repath`와 `TemplateView`를 import한다.

```python
# 프로젝트폴더 > urls.py

from django.urls import path, include, re_path	# repath를 가져온다.
from django.views.generic import TemplateView	# TemplateView를 가져온다.

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('accounts.urls')),
    re_path(‘.*’, TemplateView.as_view(template_name=’index.html’))	# 추가해준다!
]
```



## 7. Execute

- 이제 아래와 같이 명령어를 입력하면, Django에서 React Template를 build하여 템플릿이 변경되는 것을 확인할 수 있다.

```bash
$ python manage.py runserver react
```



***Copyright* © 2021 Song_Artish**