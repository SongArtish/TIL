# FastAPI



---

[TOC]

---



## FastAPI

A Web framework for developing RESTful APIs in Python.

비동기 처리를 사용하기 때문에 속도가 매우 빠르며(특히 fastapi+Postgres 사용 시), 마이크로 서비스 설계 시 유용하다. FastAPI를 통해 다음의 기능을 구현할 수 있다.

- GET POST 요청받기
- DB 입출력
- 회원인증
- 데이터 validation
- 웹소켓
- async/await
- type 넣기
- API 문서 자동생성



## 시작하기

먼저 fastapi를 설치한다.

```bash
pip install fastapi
```

그리고 "실시간 미리보기" 사용을 위해 uviorn을 설치한다.

```bash
pip install "uvicorn[standard]"
```



## 코드 작성하기

1. 다음과 같이 간단한 코드로 api 생성이 가능하다. 파일을 하나 생성(`main.py`)하고 아래 코드를 입력한다.

```python
# main.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return 'hello' # api 요청 시 return하는 값
```

2. `FileResponse`를 사용하면 html 파일를 return할 수도 있다.

```python
from fastapi.responses import FileResponse

@app.get("/file")
def file():
    return FileResponse('index.html')
```

3. 모델을 작성하고, 사용자의 post 요청을 처리할 수도 있다.

```python
# 모델 작성
from pydantic import BaseModel
class SampleModel(BaseModel):
    name :str
    phone :int

@app.post("/send")
def send(data : SampleModel):
    print(data)
    return '전송완료'
```

4. async/await를 활용하고, DB에 요청도 가능하다.

```python
# DB 접속

@app.get("/db")
async def getDB():
    await # DB 가져오기
    return # ~~
```



## API 문서 사용하기

서버 url 뒤에 `/doc`를 입력하면 바로 API 문서(Swagger)를 확인할 수 있다.

> 예를 들어 `127.0.0.1:8000/doc`에 접속

혹은 서버 url 뒤에 `/redoc`이라고 입력하면 다른 버전의 API 문저를 확인할 수 있다.

> 예를 들어 `127.0.0.1:8000/redoc`에 접속


***Copyright* © 2021 Song_Artish**