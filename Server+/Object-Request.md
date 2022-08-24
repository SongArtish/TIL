# Request 객체

---

[TOC]

---

## Request 객체

Request 객체는 요청을 다루는 내장 객체이다.



## Request 객체에서 데이터 받아오기

> JavaScript, Axios, Express.js를 사용하는 경우를 예시로 살펴본다.

### 💡 req.body

JSON과 같은 데이터를 받을 때 사용한다.

```javascript
// axios로 요청보내기
await axios.({
  url: "http://localhost:8080",
  method: "POST",
  data: {
    title: "hello",
    content: "hello world",
  }
})
```

서버에서 받을 때는 아래와 같이 설정해주어야 한다. (express 4.16.0 버전 이상)

```javascript
const express = require("express")

app.use(express.json());
app.use(express.urlencoded({ extended: true }))
```

위와 같이 설정 후 req.body로 값을 받을 수 있다.

```javascript
exports.createPost = async (req, res, next) => {
  console.log(req.body); // { title: "hello", content: "hello world" }
  // ...
};
```

### 💡 req.params

예를 들어 `http://localhost:8080/post/1?name=kim`이라는 url이 있고, 서버 라우터가 다음과 같을 때

```javascript
router.get("/:id", function)
```

req.params의 값은 `{id: 1}`이다.

```javascript
exports.getPostDetail = async (req, res, next) => {
  console.log(req.params); // { id: 1 }
  // ...
};
```

### 💡 req.query

위와 동일하게 `http://localhost:8080/post/1?name=kim`이라는 url이 있고, 서버 라우터가 다음과 같을 때

```javascript
router.get("/:id", function)
```

req.quey의 값은 `{name: "kim"}`이다.

```javascript
exports.getPostDetail = async (req, res, next) => {
  console.log(req.query); // { name: "kim" }
  // ...
};
```



***Copyright* © 2022 Song_Artish**