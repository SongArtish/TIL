# npm

> Node Package Manager

---

[TOC]

---



## node로 js파일 실행하기

`node` 명령어를 사용하여 js파일을 실행할 수 있다.

```shell
$ node <파일명>
```



## npm

- node.js 생태계의 패키지 매니저



## package.json

- npm 모듈을 활용하기 위해 해당 모듈에 대한 정보를 담는 파일
- 프로그램 실행을 위해 필요한 모듈, 프로그램 실행 방법, 테스트 방법 등이 명시되어 있다.

```json
// package.json
{
  // 프로젝트에 대한 정보
  "name": "test-project",
  "version": "1.0.0",
  "description": "A Vue.js project",
  "main": "src/main.js",
  "private": true,
  // CLI에서 사용가능한 명령어
  "scripts": {
    "dev": "webpack-dev-server --inline --progress --config build/webpack.dev.conf.js",
    "start": "npm run dev",
    "unit": "jest --config test/unit/jest.conf.js --coverage",
    "test": "npm run unit",
    "lint": "eslint --ext .js,.vue src test/unit",
    "build": "node build/build.js"
  },
  // 실행과 관련된 dependency
  "dependencies": {
    "vue": "^2.5.2"
  },
  // 프로그램 실행과 관계없는 오로지 개발을 위해 필요한 dependency
  "devDependencies": {
    "autoprefixer": "^7.1.2",
    "babel-core": "^6.22.1",
    "babel-eslint": "^8.2.1",
	...
  },
  "engines": {
    "node": ">= 6.0.0",
    "npm": ">= 3.0.0"
  },
  "browserslist": ["> 1%", "last 2 versions", "not ie <= 8"]
}

```

### dependencies

`package.json`에 명시되어 있는 모듈 정보는 `npm install` 명령어를 통해서 한 번에 다운로드 받을 수 있다.

```shell
$ npm install
```

아래의 옵션을 입력하면 install 실행 시 자동으로 devDependencies에 추가된다.

```shell
$ npm install mocha --save-dev
```

- 여기서 mocha는 테스트를 위해 필요한 모듈이다.

### scripts

`scripts` 부분에 명시된 명령어는 **npm script**라고 부르며 다음과 같이 사용할 수 있다.

```shel
$ npm run <스크립트명>
```

주로 다음과 같은 작업들을 scripts 항목에 기술한다.

```json
{
    "scripts": {
        "start": "node index.js",
        "test": "mocha test/index.test.js",
        "lint": "eslint"
    }
}
```

| 실행 스크립트 | 작업 내용       |
| ------------- | --------------- |
| npm run start | node.js 앱 실행 |
| npm run test  | 테스트 실행     |
| npm run lint  | 코드 검사       |



***Copyright* © 2022 Song_Artish**
