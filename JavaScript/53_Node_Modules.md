# Node Modules

---

[TOC]

---



## FS 모듈

**File System 모듈**은 Node.js의 내장 모듈이다.

```javascript
const fs = require("fs");
```

### 파일 읽기

filename의 파일의 [options]의 방식으로 읽은 후 callack으로 전달된 함수를 호출한다. (비동기적)

```javascript
fs.readFile(filename, [options], callback)
```

### 파일 쓰기

filename의 파일에 [options]의 방식으로 data 내용을 쓴 후 callback 함수를 호출한다. (비동기적)

```javascript
fs.writeFile(filename, data, [options], callback)
```

**filename**의 파일에 **[options]**의 방식으로 **data** 내용을 쓴다. (동기적)

```javascript
fs.writeFileSync(filename, data, [options])
```



## HTTP 모듈

- 공식 문서: https://nodejs.org/dist/latest-v14.x/docs/api/http.html

### 서버 생성

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



***Copyright* © 2022 Song_Artish**
