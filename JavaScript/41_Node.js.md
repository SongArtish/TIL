# Node.js

---

[TOC]

---



## Overview

[Node.js](https://nodejs.org/en/about/)는 비동기 이벤트 기반 자바스크립트 런타임이다.

> **런타임**은 프로그래밍 언어가 실행되는 환경을 의미한다.



## 모듈 사용법

**모듈**은 어떤 기능을 조립할 수 있는 형태로 만든 부분을 의미한다.

### 1. 내장 모듈

Node.js 모듈 목록은 [Node.js v14.17.0 Documentation](https://nodejs.org/dist/latest-v14.x/docs/api/)에서 확인할 수 있다. 자바스크립트 코드 가장 상단에 `require` 구문을 이용하면 다른 파일을 불러올 수 있다.

```javascript
const fs = require('fs')	// File System 모듈을 불러온다.
const dns = require('dns')	// DNS 모듈을 불러온다.
```

### 2. 3rd-party 모듈

3rd-party 모듈은 공식적으로 제공하는 built-in module이 아닌 모든 외부 모듈을 지칭한다. 3rd-party 모듈을 다운로드 받기 위해서는 npm을 사용해야 한다.

```bash
$ npm install <모듈>
```

`node_modules`에 모듈이 설치가 되면, `require` 구문을 통해 모듈을 사용할 수 있다.

```javascript
const <변수명> = require('<모듈>')
```



***Copyright* © 2022 Song_Artish**
