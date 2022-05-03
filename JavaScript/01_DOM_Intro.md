# Document Object Model

---

[TOC]

---



## Overview

HTML 문서의 **구조와 관계를 객체(Object)로 표현**한 모델

- HTML, XML 등과 같은 문서를 다루기 위한 언어 독립적인 문서 모델 인터페이스
- JavaScript를 이용해서 DOM 구조에 접근
- 잘 구조화된 문서는 `DOM Tree` 구조를 얻어낼 수 있음
- document라는 전역변수로 접근이 가능



## 주요 객체

- `window` : DOM을 표현하는 창. 가장 최상위 객체(모든 객체의 부모 객체) - :white_check_mark:생략 가능!
- `document` : 페이지 콘텐츠의 Entry Point 역할을 하며, <body> 등과 같은 수많은 다른 요소들을 포함
- `navigator, location, history, screen`



## JavaScript 적용

```html
<script src="index.js"></script>
```

DOM으로 HTML을 조작할 수 있다. HTML에 `<script>` 태그를 삽입하여 적용할 수 있으며, `<script>` 요소가 있으면 **웹 브라우저는 HTML 해석을 잠시 멈춘 후 `<script>` 요소를 먼저 실행**한다.

`<script>` 태그를 추가하는 방법은 크게 2가지가 있다.

- `<head>` 태그 안에 삽입하는 경우

  ```html
  <head>
      ...
      <title>Document</title>
      <script src="<js 파일명"></script>
  </head>
  ```

- `<body>` 태그 마지막에 삽입하는 경우

  ```html
  <body>
      ...
      <script src="<js 파일명"></script>
  </body>
  ```



***Copyright* © 2022 Song_Artish**
