# Django Intro

2020.08.14.



*****

[TOC]

*****



## Django

> `Flask`와 더불어 대표적인 Python Web Framework로 요청을 보내고 응답을 받는 서버를 만든다. 일반적인 static web과 비교해, Django는 Dynamic Web Application Program이다. 모델-뷰-컨트롤러(MVC)라는 소프트웨어 디자인 패턴을 따르고 있으며, 명칭은 MTV(Model-Template-View)를 사용한다.
>
> - `Flask`는 micro framework로 더 작은 스케일의 프로젝트에 많이 사용되는 편이다.

**기본 세팅**

- python version 3.7 확인

- VS Code에서 `Django` extension을 설치한다.
  `Ctrl`+`Shift`+`P` > `Preference: Open Settings(JSON)`에 코드를 붙여준다. (`files.associations`, `emmet`)

**설치**

```bash
$ pip install django
$ pip install django==2.1.15	# 특정 버전 설치
```

- 설치 후 다음의 명령어를 통해 설치 확인한다.

```bash
$ pip list
$ python -m django --version
```

**MTV 패턴**

> Model - 데이터를 관리
>
> Template - 사용자가 보는 화면
>
> View - 중간 관리자

![MTV 패턴](img\django_how.png)



## Project

### 프로젝트 생성

> Django 서버를 만든다.
>
> 위치: `<원하는 폴더>`

```bash
$ django-admin startproject <프로젝트 이름>
```

- 프로젝트 이름 작성시, <단어_단어> 형식을 권장 (하이픈, 기본 모듈명 등 사용불가)

**Internationalization**

> 위치: `<프로젝트 폴더>/setting.py > LANGUAGE_CODE (제일 밑)`

```python
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

**서버 실행**

> 위치: `<프로젝트 폴더>`

```bash
$ python manage.py runserver
```

- 서버 종료 시에는 `Ctrl` + `C` 키를 사용한다.

---

### 프로젝트 구조

**`__init__.py`**

- 빈 파일
- Python에서 이 디렉토리를 하나의 패키지로 다루도록 지시.

**`settings.py`**

- 웹사이트의 모든 설정을 포함
- 생성한 모든 앱을 등록하는 곳이며, static files의 위치, DB 세부 설정 등을 작성

**`urls.py`**

- 사이트의 url과 view의 연결을 지정

**`wsgi.py`**

- Web Server Gateway Interface
- 창고 앱이 웹서버와 연결 및 소통하는 것을 도움

**`asgi.py`**

- Asynchronous Server Gateway Interface (new in 3.0)
- Django 어플이 비동기식 웹 서버와 연결/소통하는 것을 도움



## Application

### 앱 생성

> 위치: `<프로젝트 폴더>`

```bash
$ python manage.py startapp <앱 이름>
```

- 앱 이름은 복수형으로 사용하는 것이 권장된다. (ex. articles)

---

### 앱 등록

> 위치: `<프로젝트 폴더>/settings.py > INSTALLED_APPS (33번째 줄)`

```python
# 앱 작성 순서

INSTALLED_APPS = [
    # 1. Local Appes
    'articles',
    # 2. Third Party Apps
    'haystack',
    # 3. Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- 등록 후 `python manage.py runserver`를 입력해 오류가 발생하지 않았는지 확인

**`Trailing Comma`**

- 리스트/딕셔너리의 마지막 요소 뒤에도 `,`(콤마)를 붙인다. (없어도 오류가 나는 것은 아니다.)

---

### 앱 구조

**`admin.py`**

- 관리자용 페이지 관련 기능을 작성 하는 곳.

**`apps.py`**

- 앱의 정보가 있는 곳으로 수정할 일은 없다.

**`models.py`**

- 앱에서 사용하는 Model(Database)를 정의하는 곳.

**`tests.py`**

- 테스트 코드를 작성하는 곳.

**`views.py`**

- view가 정의 되는 곳. 



***Copyright* © Song_Artish**

