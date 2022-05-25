# JavaScript Intro

---

[TOC]

---



## Overview

**JavaScript의 역사**

> 파편화 & 표준화의 여파로 Cross Browsing Issue가 있었다. 표준화를 위한 노력(ex. jQuery)으로 현재는 Vanilla JavaScript를 사용하게 되었다.

**브라우저에서 할 수 있는 일**

|                        작업                         |                       설명                        |
| :-------------------------------------------------: | :-----------------------------------------------: |
|              **[DOM 조작](##1. DOM)**               |                  문서(HTML) 조작                  |
|                    **BOM 조작**                     | navigator, screen, location, frames, history, XHR |
| **JavaScript Core([ECMAScript](02_ECMAScript.md))** |     자료 구조(Object, Array), 조건 표현, 순회     |

**브라우저가 html을 처리하는 방법**

1. Parse : 문자열을 해석
2. Style : 스타일링
3. Layout : 실제 브라우저 화면에 배치



## ES6

> **ECMAScript(ES)**는 표준화를 위해 만들어졌으며, 액션스크립트나 J스크립트 등 다른 구현체도 포함하고 있다.

뒤에 숫자는 버전을 의미하며, `ES5`는 2009년, `ES6`는 2015년에 출시되었다. ES6의 주요 문법은 다음과 같다.

1. let, const 키워드: 재선언 불가, 재할당 가능한 let 변수 선언 키워드와 상수 선언 키워드 const가 추가되었다.

2. Templete Literal

3. Object Literal

4. Arrow Function

5. 구조 분해 할당: 객체/배열의 값을 해체한 후, 개별 값을 변수로 새로 할당할 수 있다.

   ```javascript
   const arr = [1, 2, 3]
   const [one, two, three ] = arr
   ```

6. Promise

7. Class

8. String Method: `includes`, `startsWith`, `endsWith`

9. Multi-line String: 백틱을 사용하여 여러 줄의 문자열을 사용할 수 있게 되었다.

10. Default Parameter

11. Module: 모듈은 모듈 스코프를 가지며, import와 export 키워드를 이용하여 사용한다.

    ```javascript
    <script type="module" src="lib.mjs"></script>
    ```

12. Spread Operator: 배열, 문자열, 객체 등 반복 가능한 객체(Iterable Object)를 개별 요소로 분리할 수 있다.



## Coding Style Guide

다음과 같이 자바스크립트에서 스타일 가이드가 있다.  [공식문서](https://standardjs.com/rules-kokr.html)

- 들여쓰기시 **2칸 공백사용**을 사용한다.

- 함수 선언 괄호 앞에 공백을 추가한다.

  ```javascript
  function name (arg) { ... }
  ```

- 항상 `==` 대신 `===`을 사용한다. (불일치는 `!==`로 표현한다.)



## <참고> ASI

> Automatic Semicolon Insertion

원래 자바스크립트의 문장이 끝나는 지점에 `세미콜론(;)`을 찍어줘야하지만, 자동으로 세미콜론을 찍어주는 기능이다.



***Copyright* © 2020 Song_Artish**