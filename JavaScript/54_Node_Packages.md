# Node 패키지

---

[TOC]

---



## Overview

> 모듈 vs 패키지 vs 라이브러리 vs 프레임워크

- **Module**
  - 프로그램을 구성하는 소스코드가 들어 있다. (함수)
  - 모듈은 재사용이 가능하며, import를 통해서 호출할 수 있다.
- **Package**
  - 여러 모듈의 묶음으로, 특정 기능과 관련된 여러 모듈을 하나의 상위 폴더에 넣은 것이다.
  - npm을 통해 설치한다.
- **Library**
  - 패키지와 모듈의 묶음으로, 공통으로 사용될 수 있는 특정한 기능들을 모듈화 한 것이다. (바로 실행 가능)
- **Framework**
  - 여러 패키지를 모아 하나의 프로그램을 구동할 수 있는 묶음이다.
  - 폴더 트리가 존재하며, 정해진 폴더 안에서 ㅏㄱ업을 해야 프로그램이 돌아간다.



## dotenv

Dotenv is a zero-dependency module that loads environment variables from a `.env` file into [`process.env`](https://nodejs.org/docs/latest/api/process.html#process_process_env).

```bash
npm i dotenv
```

- 공식 문서: https://www.npmjs.com/package/dotenv

설치 후 `.evn` 파일을 프로젝트 root 폴더에 만들고 환경 변수로 관리할 데이터를 입력한다.

```
S3_BUCKET="YOURS3BUCKET"
SECRET_KEY="YOURSECRETKEYGOESHERE"
```

js 파일에서 아래와 같이 환경 변수의 데이터를 가져올 수 있다.

```javascript
require('dotenv').config()
console.log(process.env) // remove this after you've confirmed it working
console.log(process.env.S3_BUCKET)
```



## mysql

A pure node.js JavaScript Client implementing the MySQL protocol.

```bash
npm install mysql
```

- 공식 문서: https://github.com/mysqljs/mysql

사용법 예시는 다음과 같다.

```javascript
var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'me',
  password : 'secret',
  database : 'my_db'
});

connection.connect();

connection.query('SELECT 1 + 1 AS solution', function (error, results, fields) {
  if (error) throw error;
  console.log('The solution is: ', results[0].solution);
});

connection.end();
```



## nodemon

nodemon is a tool that helps develop Node.js based applications by automatically restarting the node application when file changes in the directory are detected.

```bash
npm install -g nodemon
```

- 공식 문서: https://www.npmjs.com/package/nodemon

설치 후, 아래 명령어를 통해 서버를 실행하면 코드가 바뀔 떄마다 자동으로 재시작을 해준다.

```bash
nodemon --watch <실행 서버 경로>
nodemon --watch server/server.js
```

혹시나 프로젝트 폴더의 `index.js`가 아닌 다른 파일을 서버 파일로 지정한 경우, `package.json`에서 `main` 값을 변경해준다.

```json
// package.json
{
  "name": "mini-node-server",
  "version": "1.0.0",
  "description": "mini=node-server",
  "main": "server/server.js",	// 서버 파일 경로를 수정해준다.
  ...
}
```



***Copyright* © 2022 Song_Artish**
