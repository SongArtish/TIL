# React Intro

---

[TOC]

---



## Overview

`React` is a JavaScript library for building user interfaces.

- MVC 프레임워크가 아니다!
- 시간 경과에 따른 데이터 표현이 가능하다.



## Features

리액트는 **선언형**이고, **컴포넌트 기반**이고, **다양한 곳에서 활용(범용성)**할 수 있다는 특징이 있다.

### 선언형 (Declarative)

한 페이지를 보여주기 위해 HTML, CSS, JS로 분리해서 작성하는 것이 아닌, 하나의 파일에 명시적으로 작성할 수 있게 `JSX`를 활용한 선언형 프로그램밍을 지향한다.

### 컴포넌트 기반 (Component-Based)

하나의 기능 구현을 위해 여러 종류의 코드를 묶어둔 컴포넌트 기반으로 개발한다. 컴포넌트를 분리함여 서로 <u>독립적</u>이고 <u>재사용 가능</u>하기 때문에, 기능 자체에 집중하여 개발할 수 있다. 유지 보수 및 유닛 테스트도 편리하다.

> 컴포넌트(Component)란?

하나의 기능 구현을 위한 여러 종류의 코드 묶음으로, 모든 리액트 애플리케이션은 최소 한 개의 컴포넌트를 가지고 있다. 애플리케이션 내부적으로는 root 역할의 최상이 컴포넌트가 있고, 이것이 자식 컴포넌트를 가지는 계층적 구조(트리 구조)이다.

### 범용성 (Learn Once, Write Anywhere)

JavaScript 프로젝트 어디에든 유연하게 적용될 수 있다. Facebook에서 관리되어 안정적이고, 가장 유명하며, 리액트 네이티브로 모바일 개발도 가능하다.



## 시작하기

**Create React App**은 React SPA를 쉽고 빠르게 개발할 수 있도록 만들어진 tool chain이다.

```bash
$ npx create-react-app <프로젝트명>
```

프로젝트 폴더 생성이 완료되면 프로젝트 폴더로 이동 후 아래 명령어를 입력한다.

```bash
$ npm start
```



## 폴더 구조

- `node_modules`: react 개발을 위한 패키지 저장소
- `package.json`: 패키지 목록
- `src`: react 필수 요소 파일 저장



***Copyright* © 2022 Song_Artish**