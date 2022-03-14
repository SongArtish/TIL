# Django Model

> 저장된 데이터베이스의 구조(layout)를 가리키며 django는 model을 통해 데이터에 접속하고 관리한다.

---

[TOC]

---



**ORM**

> Object Relational Mapping은 상호 호환되지 않는 우형의 시스템간에 데이터를 객체 지향 프로그래밍 언어를 사용하여 변환하는 프로그래밍 기법이다.
>
> python을 사용하는 Django를 통해 SQL이라는 프로그래밍 언어를 쓰는 DB를 사용할 수 있다. SQL의 절차적 접근은 C언어를 사용하는데 반해, ORM을 활용하면 python의 객체 지향 프로그래밍을 통해서 DB를 조작할 수 있다.



## Model

**`models.py` 정의**

```python
# articles/models.py
from django.db import models

class Article(models.Model): # 상속
    # id(pk)는 기본적으로 처음 테이블 생성시 자동으로 만들어진다.
    title = models.CharField(max_length=10) # 클래스 변수(DB의 필드)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**Django Model Field**

> `CharField`, `TextField`, `DateTimeField`, `DateField`,  `BooleanField`, `IntegerField`, `FloatField`, `AutoField`, `ImageField`, `FileField` 등

`CharField(max_length=None, **options)`

- 길이의 제한이 있는 문자열을 넣을 때 사용
- max_length가 필수인자
- 필드의 최대 길이, 데이터베이스와 django의 유효성 검사에서 활용
- `<input type="text">`의 형태로 출력됨

---

`TextField(**options)`

- 글자의 수가 많을 때 사용
- `<textarea>`의 형태로 출력됨

---

`DateTimeField(auto_now=False, auto_now_add=False, **options)`

- 최초 생성 일자: `auto_now_add=True`

  - django ORM이 최초 데이터 입력시에만 현재 날짜와 시간으로 갱신
  
- 최종 수정 일자: `auto_now=True`

  - django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신




## Migrations

>  모델에 생긴 변화를 Django가 반영하는 방법

`makemigrations`

- 모델을 변경한 것에 기반한 새로운 마이그레이션(설계도)을 만들 때 사용
- 생성된 마이그레이션 파일은 데이터베이스 스키마를 위한 버전관리 시스템이라고 할 수 있다.

```bash
$ python manage.py makemigrations
```

`migrate`

- 작성된 마이그레이션 파일들을 기반으로 실제 DB에 반영하는 작업
- `dp.sqlite3` 라는 데이터베이스 파일에 테이블을 생성
- 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룬다.

```bash
$ python manage.py migrate
```

`sqlmigrate`

- 해당 마이그레이션 파일이 SQL 문으로 어떻게 해석되어서 동작할지 미리 확인하기 위한 명령어

```bash
$ python manage.py sqlmigrate <앱 이름> <마이그레이션 숫자>
```

`showmigrations`

- 마이그레이션 파일들의 migrate 여부를 확인하기 위한 명령어

```bash
$ python manage.py showmigrations
```



**Model의 중요 3단계**

- `models.py` : 변경사항 발생 (생성/수정/삭제)

- `makemigrations` : 마이그레이션 만들기 (설계도)

- `migrate` : DB에 적용 (테이블 생성)





## Database API

> Django에서 제공하는 것으로, 데이터베이스를 편하게 조작할 수 있도록 도와준다.

**Django Shell**

> 일반 파이썬 shell에서는 Django 프로젝트 환경에 접근할 수 없으며, 이를 위해서는 django shell을 위한 설치 및 세팅이 필요하다.

- 아래는 `ipython`과 `django-extensions` 설치를 위한 명령어이다.

```bash
$ pip install ipython django-extensions
```

```python
# settings.py

INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```

```bash
$ python manage.py shell_plus
```

- 기본 shell은 시작 때마다 model을 import해야 하지만, `shell_plus`는 자동으로 import해준다.

```bash
$ python manage.py shell
```

```shell
>>> from articles.models import Article
>>> article = Article.objects.get(pk=1)
```



**DB API 구문**

```shell
<Class Name>.<Manager>.<QuerySet API>
```

```shell
# 예시
Article.objects.all()
```

**`objects` Manager**

- 여기서 manager는 중간 역할을 한다.
- Django는 기본적으로 모든 모델 클래스에 대해 `objects`라는 manager 객체를 자동 추가하며, 이 manager를 통해 특정 데이터를 조작(메서드)할 수 있다

**QuerySet API**

- DB로부터 데이터를 읽고, 필터/정렬 등을 수행한다. Query(질문)를 DB에게 던져서 CRUD한다.

- `shell`에서 QuerySet을 조회하면 다음과 같은 결과가 나온다.

```shell
In [1]: Article.objects.all()
Out[1]: <QuerySet []>
```

- `QuerySet` 조회 형식은  `model.py`에서 지정할 수 있다.

```python
# models.py
def __str__(self):
    return f'{self.pk}번 글의 제목은 {self.title}'
```

[다음내용은 CRUD에서](04 Django CRUD.md)



## 가상환경

> 각 가상 환경은 고유한 파이썬 환경을 가지며 독립적으로 설치된 패키지 집합을 가진다.

**가상 환경 지원 모듈**

- `venv` : Python 3.3 버전 이후 부터 기본모듈에 포함됨. [공식문서](https://docs.python.org/3/library/venv.html)
- `virtualenv` : Python 2 버전부터 사용해오던 가상환경 라이브러리, Python 3에서도 사용가능
- `conda` : Anaconda Python을 설치했을 시 사용할 수있는 모듈
- `pyenv` : pyenv의 경우 Python Version Manger임과 동시에 가상환경 기능을 플러그인 형태로 제공 (macOS)



**생성**

```bash
$ python -m venv <가상환경이름>
```

- `$ python -m venv venv` 권장 (`-m venv`는 venv라는 module을 사용한다는 뜻이다.)

> 프로젝트를 가상환경 폴더와 동일선상의 위치에서 생성한다. 
> Django는 `pip`를 글로벌 환경까지 찾아간다.
>
> ```bash
> $ django-admin startproject <프로젝트 이름> .
> ```
>
> - `.`(점)을 찍어 현재폴더에 프로젝트 폴더를 바로 생성

**활성화**

S가 대문자이니 주의! (`Tab`으로 자동완성 이용하는 것을 추천)

- Git Bash

```bash
$ source <가상환경이름>/Scripts/activate
```

- CMD

```bash
$ source <가상환경이름>\Scripts\activate.bat
```

- PowerShell

```bash
$ source <가상환경이름>\Scripts\Activate.ps1
```

- macOS

```bash
$ source <가상환경이름>/bin/activate
```

- 혹은 VS Code에서 `Ctrl` + `Shift` + `P` >  `Python: Select Interpreter`에서 해당 가상환경 설정후 `Terminal` 실행하기!

**비활성화**

```bash
$ deactivate
```



여기서, `.gitignore`를 하면 `venv`와 `DB`가 관리되지 않기 때문에, 다음의 패키지 관리와 `fixtures`를 이용한다.

**패키지 관리**

`pip freeze`

> 현재 환경에 설치된 패키지를 requirements format으로 출력

```bash
$ pip freeze > requirements.txt
```

- `>`는 redirect라는 의미 (pip를 freeze해서 requirements.txt로 보낸다.)

설치

```bash
$ pip install -r requirements.txt
```

---

**fixtures**

> Django가 데이터베이스로 import 할 수 있는 데이터 모음

`dumpdata`

- 특정 앱의 관련된 데이터베이스의 모든 데이터를 출력

```bash
$ python manage.py dumpdata app_name.ModelName [--options]
```

```bash
# 예시
$ python manage.py dumpdata articles.Article --indent 4 > articles.json
```

```bash
# admin 계정 정보 만들기
$ python manage.py dumpdata auth.User --indent 4 > users.json
```

- `[--options]` format의 default 값이 `json`이기 때문에 생략한다.
- `indent 4`는 4줄로 작성해주기 때문에 보기 편리해진다.

`loaddata`

- **fixtures 파일은 반드시 app 디렉토리 안에 fixtures 디텍토리에 위치해야한다.**

```bash
$ python manage.py loaddata fixtures_path
```

```bash
# 예시
$ python manage.py loaddata articles/articles.json
```

- `fixture/articles/articles.json` 의 데이터를 불러온다.
- 여러 개도 공백으로 띄워주면 가능하다.
- 이후 `makemigrations` 없이 `migrate`를 바로 진행하면 된다.



***Copyright* © Song_Artish**