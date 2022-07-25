# Node Server

---

[TOC]

---

## Overview

http 모듈을 사용하여 간단한 웹 서버를 구현할 수 있다.

- 공식 문서: https://nodejs.org/dist/latest-v14.x/docs/api/http.html

## 서버 생성

node 웹 서버 애플리케이션은 `createServer`를 이용하여 웹 서버 객체를 만들어야 한다. 

```javascript
const http = require('http')

const server = http.createServer((request, response) => {
    // 여기서 작업이 진행된다!
})
```

이 서버로 오는 HTTP 요청마다 `createServer`에 전달된 함수가 한 번씩 호출된다. `createServer`가 반환한 `Server` 객체는 `EventEmitter`이고 여기서는 `server` 객체를 생성하고 리스너를 추가하는 축약 문법을 사용한 것이다.

```javascript
const server = http.createServer()
server.on('request', (request, response) => {
    // 여기서 작업이 진행된다!
})
```

## 데이터 처리

```javascript
const http = require('http');

http.createServer((request, response) => {
  const { headers, method, url } = request;
  let body = [];
  request.on('error', (err) => {
    console.error(err);
  }).on('data', (chunk) => {
    body.push(chunk);
  }).on('end', () => {
    // 여기서 `body`에 전체 요청 바디가 문자열로 담겨있다.
    body = Buffer.concat(body).toString();
    // 이 요청에 응답하는 데 필요한 어떤 일이라도 할 수 있다.
    response.writeHead(200, defaultCorsHeader);
    response.end(body)
  });
}).listen(8080); // 이 서버를 활성화하고 8080 포트로 받는다.

const defaultCorsHeader = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Accept',
  'Access-Control-Max-Age': 10
};
```

`server.listen`은 아래와 같이 분리할 수도 있다.

```javascript
const PORT = 5000;
const ip = 'localhost';

server.listen(PORT, ip, () => {
  console.log(`http server listen on ${ip}:${PORT}`);
});
```

***Copyright* © 2022 Song_Artish**
