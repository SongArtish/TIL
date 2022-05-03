# DOM 메서드

---

[TOC]

---



## Overview

| Element vs. Node | Desc.                                            |
| ---------------- | ------------------------------------------------ |
| Element          | 텍스트 노드를제외하고, 흔히 생각하는 태그만 지칭 |
| Node             | 태그 노드와 텍스트 노드 전체를 지칭              |



## 1. 부모/자식 찾기

**부모 요소 찾기**

```javascript
console.log(<요소>.parentElement)
```

**자식 요소 찾기**

```javascript
// <body>의 자식 요소 찾기
console.dir(document.body.children) // console.dir은 해당 요소의 객체 정보를 출력
```



## 2. Selection (선택)

유연성이 좋은 아래의 2개의 selector를 사용한다.

```
querySelector()
querySelectorAll()
```

|          유형          |                             구문                             |
| :--------------------: | :----------------------------------------------------------: |
|       단일 Node        | `document.getElementById(id)`<br />`document.querySelector(selector)` |
| HTML Collection (live) | `document.getElementsByTagName(tagName)`<br /> `document.getElementsByClassName(class)` |
|  Node List (non-live)  |            `document.querySelectorAll(selector)`             |



## 3. Manipulation (변경)

**텍스트 입력**

|      유형       |                  특징                   |
| :-------------: | :-------------------------------------: |
| **`innerText`** |                 텍스트                  |
| **`innerHTML`** | XSS공격에 취약점이 있으므로 사용시 주의 |

**속성 값 변경**

- **`element.style.backgroundColor`**
- `setAttribute(attributeName, value)`
- `getAttribute(attributeName)`

**요소 만들기**

- **`Document.createElement(tagName)`** : 특정 태그를 생성
- **`ParentNode.appendChild(Node)`** : 마지막 자식 요소로 추가
- **`ParentNode.removeChild(child Node)`** : 해당 요소를 제거



## <실습> DOM과 자바스크립트

> **Chrome Console 창**을 활용한다. Chrome Console 창은 `Ctrl` + `Shift` + `I`의 단축키로 실행할 수 있다.

**문서 불러오기**

- 다음과 같은 코드로 문서에 접근할 수 있다. `window`는 생략할 수 있다.

```javascript
window.document
document
```

**console 창 출력**

- `console.log()`를 통해 파이썬에서의 `print()`와 같이 원하는 요소를 console 창에 출력할 수 있다.

```javascript
> console.log('안녕')
  안녕
```

**주석 작성**

```javascript
// 한 줄 주석
/*
여러 줄 주석
*/
```

**변수 생성**

- `const`를 통해 변수를 생성할 수 있다.

```javascript
const mainBackgroud = document.querySelector('body')
const nav = document.querySelector('nav')
const header = document.querySelector('header')
const section = document.querySelector('section')
```

- `querySelector`를 이용해서 문서 내 특정 태그를 변수화할 수 있다.
- 여러개의 태그는 `querySelectorAll`을 통해 가져올 수 있다.

```javascript
const myDiv = document.querySelectorAll('div')
```

- 변수가 잘 생성되었는지 console 창에 한 번 출력해본다.

```javascript
console.log(mainBackgroud)
```

**id값 부여하기**

```javascript
mainBackgroud.id = 'main'
```

**클래스 부여하기**

- classlist를 찾아서 `classList.add`를 통해 변수에 특정 클래스를 부여할 수 있다.

```javascript
// console.dir(nav)

nav.classList.add('box-container')
header.classList.add('box-container')
section.classList.add('box-container')
```

**반복문 사용하기**

- 여러 개의 태그를 가져온 경우 (`querySelectorAll`) 다음과 같이 for문을 사용할 수 있다.

```javascript
// for문 : i는 0부터 len(myDiv)까지 i를 1씩 추가

for (let i = 0; i < myDiv.length; i++) {
    myDiv[i].classList.add('box-item')    
}
```

**Array Help Method**

- `forEach`를 활용해서도 위의 작업을 수행할 수 있다.

```javascript
myDiv.forEach(function (div) {
    div.classList.add('box-item')
})
```

**버튼 만들기**

- 특정 태그 내의 태그를 선택하는 경우, `form > input`과 같이 해당 태그를 지정할 수 있다.

```javascript
const myButton = document.querySelector('form > input')
myButton.classList.add('button')
myButton.value = '제출'
```

**CSS 스타일링**

- `<요소>.style.<스타일속성> = '<스타일 값>'`으로 지정할 수 있다.

```javascript
li1.style.cursor = 'pointer'
li2.style.color = 'blue'
li3.style.background = 'red'
```

- 다음과 같이도 CSS 스타일링을 할 수 있다. 기존의 CSS와 다소 차이가 있으므로 주의해서 작성한다.

```javascript
const myInput = document.querySelector('#name')
console.log(myInput)
myInput.style.marginTop = '10px'
myInput.style.padding = '10px'

const mySelect = document.querySelector('#region')
mySelect.style.display = 'block'
mySelect.style.margin = '10px'
mySelect.style.padding = '10px'
mySelect.style.borderRadius = '20px'
```

- `#name`은 id 선택자를 나타낸다.

**이미지 삽입**

- src에서 `https://`를 넣지 않으면 이미지가 페이지에서 업로드 되지 않는다.

```javascript
const myImage = document.querySelector('nav > a > img')
myImage.src = 'https://zzu.li/ssafy-image'
myImage.width = '600'
// myImage.style.width = '600px'
```

**footer 넣기**

```javascript
const myFooter = document.createElement('footer')
const myBody = document.querySelector('body')
myBody.appendChild(myFooter)
myFooter.innerText = 'Google 설문지를 통해 비밀번호를 제출하지 마세요.'

myFooter.classList.add('footer', 'box-container')
// myFooter.classList.remove('box-container')
```

**외부 파일 불러오기**

- `index.js` 만들기

```js
// index.js
console.log(window)
```

- HTML 문서에서는 다음과 같이 외부 js 파일을 불러올 수 있다.

```javascript
<script src="index.js"></script>
```



***Copyright* © 2022 Song_Artish**
