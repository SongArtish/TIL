# Node Manager

---

[TOC]

---



## NVM (Node Version Manager)

`node.js`의 다양한 버전을 관리하는 프로그램이다. :warning: Window 환경에서는 nvm을 사용할 수 없다.

### Install

1. nvm 설치

   ```shell
   # ubuntu에서 설치
   $ wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash
   ```

2. 설치 확인

   ```shell
   $ nvm --version
   ```

   - 버전이 잘 나온다면 NVM 설치를 성공한 것이다.

   - :ballot_box_with_check: nvm이 설치되었음에도 `Command 'nvm' not found, did you mean:`과 같은 문구가 발생한다면 아래의 명령어를 입력한다.

     ```shell
     $ source $HOME/.nvm/nvm.sh
     ```

3. node.js 설치

   ```shell
   $ nvm install --lts
   ```

   ```shell
   $ node -v
   ```

### 간단한 사용법

아래의 명령어로 현재 nvm을 통해 설치한 node version을 확인할 수 있다.

```shell
$ nvm ls
```

특정 버전의 node를 설치하고 싶다면 아래 명령어를 사용한다.

```shell
$ nvm install <버전>
# nvm install 12.18.3
```

사용 중인 node version을 다른 버전으로 변경하고 싶을 때는 아래의 명령어를 입력한다.

```shell
$ nvm use <버전>
# nvm use 14.15.5
```





## NPM (Node.js Package Manager)

node.js 생태계의 패키지 매니저

### package.json

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
