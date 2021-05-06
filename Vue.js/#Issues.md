# Vue 이슈

> Vue 프로젝트를 하면서 겪었던 핵심적인 오류들을 정리하였다.

---

[TOC]

---



## axios 관련

### CORS 문제

- Vue에서 BE로 axios 요청을 보냈는데, 아래와 같이 CORS 에러가 발생하였다.
- Spring Boot에서는 CORS 허용 코드를 입력하였다.

```
Access to XMLHttpRequest at 'http://localhost:8080/create/' from origin 'http://localhost:8081' has been blocked by CORS policy:
```

**해결 방안**

- axios 요청을 보낼 때 아래와 같이 `Access-Control-Allow-Origin`을 `headers`에 추가해준다.

```javascript
headers: {
    "Access-Control-Allow-Origin": "*",
}
```

### 415 Error

>**415 Unsupported Media Type**
>
>요청한 미디어 포맷은 서버에서 지원하지 않습니다. 서버는 해당 요청을 거절할 것입니다.

- axios POST요청으로 데이터를 서버로 보냈는데, 415 에러가 반환되었다.

**해결 방법**

- headers에 `Content-Type`을 입력한다.
- 보내는 데이터(context)를 JSON 문자열로 변환한다.

```javascript
headers: {
    'Content-Type': 'application/json;charset=UTF-8',
},
data: JSON.stringify(context),
```



***Copyright* © 2021 Song_Artish**