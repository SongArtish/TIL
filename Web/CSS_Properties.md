# CSS 속성

> 자주 쓰는 혹은 헷갈리는 CSS 속성을 정리한다.
>
> - `abc순`으로 정리한다!!

---

[TOC]

---



## overflow

> 컨텐츠가 너무 커서 요소의 블록 서식 맥락에 맞출 수 없을 때의 처리법을 지정한다.
>
> - [참고사이트](https://developer.mozilla.org/ko/docs/Web/CSS/overflow)

- `visible`: Default. 넘친 컨텐츠는 상자 밖으로 보여진다.
- `hidden`: 넘친 컨텐츠는 잘려지고 보여지지 않는다.
- `scroll`:  넘친 컨텐츠는 잘리고, 스크롤바가 생겨서 스크롤해서 볼 수 있게된다. 필요하지 않더라도 가로/세로 스크롤바가 모두 생긴다.
- `auto`: 넘칠경우 스크롤바가 자동으로 생긴다. 가로/세로 필요한 부분에만 생긴다.

예시

```css
/* 키워드 값 */
overflow: visible;
overflow: hidden;
overflow: clip;
overflow: scroll;
overflow: auto;
overflow: hidden visible;

/* 전역 값 */
overflow: inherit;
overflow: initial;
overflow: unset;
```

- :white_check_mark: `overflow-x`, `overflow-y`로 overflow를 가로/세로 각각 제어할 수도 있다.

  - 예시

    ```css
    div.container1 {
        overflow-x: scroll;
        overflow-y: hidden;
    }
    
    div.container2 {
        overflow-x: auto;
        overflow-y: scroll;
    }
    ```

    

## text-align

> 텍스트의 정렬 방향을 지정한다.

- `left`: 왼쪽 정렬
- `right`: 오른쪽 정렬
- `center`: 중앙 정렬
- `justify`: 양쪽 정렬 (자동 줄바꿈시 오른쪽 경계선 부분 정리)

사용법 예시

```css
#box1 { text-align: right; }
#box2 { text-align: left; }
#box3 { text-align: center; }
```



## white-space

> 스페이스와 탭, 줄바꿈, 자동줄바꿈을 처리하는 속성이다.
>
> - 상속 O, 애니메이션 X
> - [참고사이트](https://developer.mozilla.org/ko/docs/Web/CSS/white-space)

- `normal`: 연속 공백을 하나로 합친다. 개행 문자도 다른 공백 문자와 동일하게 처리하며, 한 줄이 너무 길어서 넘칠 경우 자동으로 줄을 바꾼다.
- `nowrap`: 연속 공백을 하나로 합친다. 줄 바꿈은 `<br>` 요소에서만 일어난다.
- `pre`: 연속 공백을 유지한다. 줄 바굼은 개행 문자와 `<br>` 요소에서만 일어난다.
- `pre-wrap`: 연속 공백을 유지한다. 줄 바꿈은 개행 문자와 `<br>`요소에서 일어나며, 한 줄이 너무 길어서 넘칠 경우 자동으로 줄을 바꾼다.
- `pre-line`: 연속 공백을 하나로 합친다. 줄 바꿈 개행 문자와 `<br>`요소에서 일어나며, 한 줄이 너무 길어서 넘칠 경우 자동으로 줄을 바꿉니다.
- `break-spaces`: (아래 차이점을 제외하면 `pre-wrap`과 동일하다.)
  - 연속 공백이 줄의 끝에 위치하더라도 공간을 차지한다.
  - 연속 공백의 중간과 끝에서도 자동으로 줄을 바꿀 수 있다.
  - 유지한 연속 공백은 `pre-wrap`과 달리 요소 바깥으로 넘치지 않으며, 공간도 차지하므로 박스의 본질 크기(`min-content`, `max-content`)에 영향을 준다.

|                | 개행 문자 | 스페이스, 탭 | 자동 줄 바꿈 | 줄 끝의 공백 |
| :------------: | :-------: | :----------: | :----------: | :----------: |
|    `normal`    |   병합    |     병합     |      예      |     제거     |
|    `nowrap`    |   병합    |     병합     |    아니오    |     제거     |
|     `pre`      |   유지    |     유지     |    아니오    |     유지     |
|   `pre-wrap`   |   유지    |     유지     |      예      |     넘침     |
|   `pre-line`   |   유지    |     병합     |      예      |     제거     |
| `break-spaces` |   유지    |     유지     |      예      |   줄 바꿈    |



***Copyright* © 2021 Song_Artish**