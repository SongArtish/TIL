# Node.js 내장 모듈

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
- 자세한 내용은 Node Server TIL 참고



***Copyright* © 2022 Song_Artish**
