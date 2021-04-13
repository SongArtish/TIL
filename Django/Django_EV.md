# Django 환경변수

2021.04.06

---

[TOC]

---



## 환경변수

> 환경변수랑 **프로세스가 컴퓨터에서 동작하는 방식에 영향을 미치는 동적인 값들의 모임**을 뜻한다.

Django에서 환경변수를 사용하기 위해 다음의 2가지 방법을 이용할 수 있다.

1. 외부 패키지 이용
2. json 파일 이용 방법



## 외부 패키지 이용

### 1. 환경변수 분리 패키지 설치

- 아래의 명령어로 pip를 설치한다.

```bash
$ pip install django-dotenv
```

### 2. 환경변수 파일 및 변수 작성

- `manage.py`가 위치한 폴더에 **.env**라는 이름의 파일을 생성한다.
  - `<Project DIR> > .env`
- 작성 예시

```
EMAIL_HOST_USER = "won-ideal"
EMAIL_HOST_PASSWORD = "idealkr!"
```

### 3.환경변수 호출

- 환경변수가 필요한 파일에서 아래와 같이 변수를 호출한다.

```python
import os

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
```

### 4. manage.py 선언

- `manage.py`에서 아래와 같이 선언해준다.

```python
# manage.py

import dotenv

if __name__ == "__main__":
    dotenv.read_dotenv()
    main()
```



## json 파일 이용

### 1. secrets.json 파일 생성

- 아래와 같이 JSON 형식의 파일을 생성한다.
  - `{"Key": "Value"}` 형식으로 작성한다.
  - `,(콤마)`를 꼭 넣어준다.

```json
// secrets.json

{
    "SECRET_KEY": "sl29t0vlvn12fn",
    "API_KEY": "a0dfn39n92n24fh6w3"
}
```

### 2. 환경변수 호출

- 아래와 같이 환경변수를 호출해준다.
  - `get_secret("secrets.json file key")`

```python
# settings.py

import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())


# Keep secret keys in secrets.json
def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")
```



## Python 파일 이용

- 파이썬 파일을 생성하여 사용할 환경 변수를 선언한다.

```python
# env.py

API_KEY = "a0dfn39n92n24fh6w3"
```

- 아래와 같이 환경변수 파일을 호출한다.

```python
from .env import API_KEY

api_key = API_KEY
```

- 마지막으로 **반드시** `env.py` 파일을 `.gitignore`에 등록해준다.



***Copyright* © 2021 Song_Artish**