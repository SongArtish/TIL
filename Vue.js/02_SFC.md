# SFC

---

[TOC]

---



## Overview

SFC(Single File Component)는 화면의 특정 영역에 대한 HTML, CSS, JavaScript 코드를 하나의 파일(.vue)에서 관리하는 형태이다.



## 개념

### 1. Component

> 컴포넌트는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 일컫는다. (재사용 가능한 코드)

- 목적: 유지, 보수, 재사용성
- Vue 컴포넌트 === Vue 인스턴스 === `.vue` 파일

---

```markdown
그렇다면 SFC 형태로 어떻게 개발할까?
```

### 2. npm

`npm(Node Package Manager)`는 자바스크립트 프로그래밍 언어를 위한 패키지 관리자이며, 자바스크립트 런타임 환경 `Node.js`의 기본 패키지 관리자이다.

**설치하기**

- `bash` 창에서 **Vue CLI**를 설치하기 위해 다음의 명령어를 입력한다.

```bash
$ npm install -g @vue/cli
```

- 위 명령어에서, `g`는 global에 설치한다는 것을 의미한다!
- 설치 후 vue 버전을 확인해본다.

```bash
$ vue --version
```

![](img/webpack.png)

### 3. Node.js

[node.js 사이트](https://nodejs.org/ko/)에서 안정성이 높은 구버전을 다운로드한다. 단, 설치시 `Tools for Native Modules`의 체크박스는 체크하지 않는다!!

다운로드가 완료되면 버전을 체크해준다.

```bash
$ node -v
```

Node`를 설치하면 `npm`이 자동으로 설치된다.

```bash
$ npm -v
```

### 4. Babel

파편화된(크로스 브라우징 이슈) JavaScript 문법을 `변환/변역`하기 위해 존재하는 도구 (`compiler`)

### 5. Webpack

모듈 간의 의존성 문제를 해결하기 위해 존재하는 도구 (`bundler`)



## Vue CLI 프로젝트 구조

### `node_modules`

> `npm`으로  node.js 환경의 여러 의존성 모듈

- :white_check_mark: 절대로 git으로 관리해서는 안된다!

### `public/index.html`

> Vue 앱의 뼈대가 되는 html 파일

- `main.js`에서 `$mount('#app')` 마운트의 대상이 되는 DOM Element가 존재한다.
- 실제 배포를 하기 우해 `npm run build`한 결과물은 이 html 문서 한 장에 모두 묶이게 된다.

### `package.json`

> 모듈들을 기록해 놓는 공간이다. [문서](https://docs.npmjs.com/cli/v6/configuring-npm/package-json) 참조

- 다음의 명령어를 통해 `package.json`에 기록되어 있는 `node_modules`를 설치한다.

  ```bash
  $ npm install (혹은 i)
  ```

### `package-lock.json`

>`node_modules` 에 설치되는 모듈과 관련해서 모든 의존성을 알아서 설정한다. (패키지 버전을 고정) [문서](https://docs.npmjs.com/cli/v6/configuring-npm/package-lock-json) 참조

- `npm install` 명렁어에 생성된다.

### `babel.config.js`

> 바벨 설정과 관련된 내용이 들어가는 파일

### `src/assets/`

> webpack에 의해 빌드된 정적 파일이 관리되는 공간

### `src/components/`

> 하위 컴포넌트가 작성되는 공간

### `src/App.vue`

> 최상위 컴포넌트

### `src/main.js`

> Webpack이 빌드를 시작할 때 가장 먼저 불러오는 진입점으로, 실제 단일 파일에서 DOM과 Data를 연결 했던 것과 동일한 작업이 이루어지는 파일
>

- Vue 전역에서 활용 할 모듈을 등록할 수 있는 파일



***Copyright* © 2020 Song_Artish**

