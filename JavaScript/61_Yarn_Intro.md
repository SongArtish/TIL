# Yarn Intro

---

[TOC]

---



## Overview

Facebook에서 만든 JavaScript 패키지 매니저



## 시작하기

설치 방법은 다양하다. Windows에서는 먼저 Chocolatey를 통해서 설치할 수 있다.

```bash
$ choco install yarn
```

npm으로 설치할 수도 있다.

```bash
$ npm install -g yarn
$ yarn --version
```



## 간단한 명령어

:arrow_forward: 프로젝트 초기화: 프로젝트를 시작할 때 초기화를 하며, `package.json`을 생성한다.

```bash
$ yarn init
```

:arrow_forward: `package.json`으로부터 dependencies를 설치한다.

```bash
$ yarn
# or
$ yarn install
```

:arrow_forward: 의존성 모듈을 설치한다.

```bash
$ yarn add [package]
$ yarn add [package]@[version]
$ yarn add [package]@[tag]
```

`devDependencies`, `peerDependencies`, `optionalDependencies`와 같은 다른 범주의 의존성을 추가하는 경우, 다음과 같이 할 수 있다.

```bash
$ yarn add [package] --dev
$ yarn add [package] --peer
$ yarn add [package] --optional
```

:arrow_forward: 의존성 모듈 업그레이드나 제거는 `upgrade`, `remove` 명령어를 사용한다.

```shell
$ yarn upgrade [package]
$ yarn remove [package]
```

:arrow_forward: 중복 설치된 패키지들을 정리해준다.

```bash
$ npm dedupe
```



## yarn.lock

`yarn.lock` 파일은 설치된 모듈의 버전을 저장해 어디서나 같은 버전과 구조의 의존성을 가지게 한다. yarn에서는 자동으로 `yarn install` 때 마다 `yarn.lock`이 생성된다. (`package-lock.json`과 비슷한 기능을 한다.)



***Copyright* © 2022 Song_Artish**
