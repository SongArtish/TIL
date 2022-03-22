# Django-MySQL 연결하기

2021.03.29

> Django에서 기본적으로 제공되는 내장DB인 sqlite3가 아닌, 외부의 MySQL 데이터베이스에 연결하는 방법에 대해 알아본다.

---

[TOC]

---



## 1. MySQL 서버 구축

> Django-MySQL 연결을 시작하기에 앞서 MySQL을 설치하고 서버에 연결한다.

- 이 부분에 대해서는 [MySQL 서버 구축하기 문서](../DB/MySQL_Server.md)를 참고한다.



## Database (Schema) 생성

- MySQL에서 스키마를 생성한다.

  ```mysql
  CREATE DATABASE <스키마명>;
  ```

- 해당 스키마를 MySQL에서 사용한다.

  ```mysql
  USE <스키마명>;
  ```

  

## 2. `settings.py` 설정

먼저 Django 프로젝트의 `settings.py`에서 DB 연결을 설정하고 있는 **DATABASES** 파트를 아래와 같이 수정한다.

- 아래 예시를 바탕으로 각각의 항목에 올바른 값을 입력한다.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ari', # Database (Schema) Name
        'USER': 'ari',
        'PASSWORD': '****',	# 비밀번호 값 입력
        'HOST': '*.io',	# 작성
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}
```

- 이후 `makemigrations`, `migrate`를 진행한다.



## 3. 유지 및 보수

DB 테이블 및 필드를 변경할 경우 아래의 절차를 거쳐야한다.

1. `models.py`에서 모델/필드 값 변경

2. `<App 폴더>/migrations/000x_xxxx.py` 파일 모두 삭제

   - 예시 `0001_initial.py`

3. MySQL에서 아래의 명령어 작성 후 실행

   ```mysql
   DROP schema <스키마명>;
   CREATE schema <스키마명>;
   ```

4. Django에서 migration 과정 진행하기

   ```bash
   $ python manage.py makemigrations
   $ python manage.py migrate
   ```

   

***Copyright* © 2021 Song_Artish**