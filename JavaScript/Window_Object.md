# Window 객체

2021.02.15

---

[TOC]

---



**Window 객체 계층구조**

![window 객체 내 주요 산하 객체들](img/window_objects.jfif)

`(출처: http://www.ktword.co.kr/test/view/view.php?nav=2&no=5991&sh=window+%EA%B0%9D%EC%B2%B4)`



## Properties

> [w3schools 자료](https://www.w3schools.com/jsref/obj_window.asp)를 참고하였다.

|    property     |                             설명                             |
| :-------------: | :----------------------------------------------------------: |
|    `closed`     |       창이 종료되었는지 여부를 나타내는 bolean 값 반환       |
| `defaultStatus` |       창의 상태표시줄의 텍스트를 반환하거나 설정한다.        |
|    `document    |                창의 document 객체를 반환한다.                |
| `frameElement`  |         현재 창의 삽입된 `<iframe>` 요소를 반환한다.         |
|    `frames`     |         현재 창에서 모든 `<iframe>` 요소를 반환한다.         |
|    `history`    |                창의 history 객체를 반환한다.                 |
|  `innerHeight`  |       창의 콘텐츠 영역(뷰포트)의 내부 높이를 반환한다.       |
|  `innerWidth`   |       창의 콘텐츠 영역(뷰포트)의 내부 너비를 반환한다.       |
|    `length`     |         현재 창의 `<iframe>` 요소의 객수를 반환한다.         |
| `localStorage`  | 데이터를 저장하는데 사용되는 로컬 스토리지 객체에 대한 참조를 반환한다. |
|   `location`    |                창의 location 객체를 반환한다.                |
|     `name`      |               창의 이름을 반환하거나 설정한다.               |
|   `navigator`   |               창의 navigator 객체를 반환한다.                |
|    `opener`     |            창을 생성한 창에 대한 참조를 반환한다.            |
|       ...       |                             ...                              |



## Methods

>[w3schools 자료](https://www.w3schools.com/jsref/obj_window.asp)를 참고하였다.

|      method       |                         설명                          |
| :---------------: | :---------------------------------------------------: |
|     `alert()`     |       메세지와 확인 버튼을 대화상자로 표시한다.       |
|     `atob()`      |       base-64로 인코딩 된 문자열을 디코딩한다.        |
|     `blur()`      |            현재 창에서 포커스를 제거한다.             |
|     `btoa()`      |            base-64로 문자열을 인코딩한다.             |
| `clearInterval()` |      `setInterval()`로 설정한 타이머를 제거한다.      |
| `clearTimeout()`  |     `setTimeout()`으로 설정한 타이머를 제거한다.      |
|     `close()`     |                   현재 창을 닫는다.                   |
|    `confirm()`    | 메시지 및 확인, 취소 버튼이 있는 대화상자를 표시한다. |
|     `focus()`     |                 현재 창을 포커스한다.                 |
|        ...        |                          ...                          |



## 1. location 객체

`location.href`

- 현재 윈도우의 url을 반환한다.

`location.href(url주소)`

- 새로운 페이지로 이동된다.
- 주소 히스토리가 기록된다.

`location.replace(url주소)`

- 기존페이지를 새로운 페이지로 변경시킨다.
- 주소 히스토리가 기록되지 않는다.



***Copyright* © 2021 Song_Artish**

