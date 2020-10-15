# JavaScript DOM

2020.10.12

:star: **학습목표 : 자바스크립트를 통한 DOM 조작**:star:

---

[TOC]

---



## 0. Intro

**자바스크립트의 역사**

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



## 1. DOM

> **문서 객체 모델(`Document Object Model`)**은 HTML, XML 등과 같은 문서를 다루기 위한 언어 독립적인 문서 모델 인터페이스다. 문서 구조, 스타일, 내용 등을 변경할 수 있도록 도우며, 구조화된 노드와 오브젝트로 문서를 표현한다. 잘 구조화된 문서는 `DOM Tree` 구조를 얻어낼 수 있다.

**주요 객체**

- `window` : DOM을 표현하는 창. 가장 최상위 객체(모든 객체의 부모 객체) - :white_check_mark:생략 가능!
- `document` : 페이지 콘텐츠의 Entry Point 역할을 하며, <body> 등과 같은 수많은 다른 요소들을 포함
- `navigator, location, history, screen`



## 2. DOM과 자바스크립트

> DOM에서는 `<script></script>`  태그 안에 자바스크립트 코도를 작성할 수 있다.



### 2.1 Selection (선택)

> 우리는 유연성이 좋은 아래의 2개의 selector를 사용한다.
>
> ```
> querySelector()
> querySelectorAll()
> ```

|          유형          |                             구문                             |
| :--------------------: | :----------------------------------------------------------: |
|       단일 Node        | `document.getElementById(id)`<br />`document.querySelector(selector)` |
| HTML Collection (live) | `document.getElementsByTagName(tagName)`<br /> `document.getElementsByClassName(class)` |
|  Node List (non-live)  |            `document.querySelectorAll(selector)`             |



### 2.2 Manipulation (변경)

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



## 3. 자바스크립트 문법

> 해당 내용 삭제. 자세한 것은 [ECMAScript](02_ECMAScript.md) 참고



## 4. EventListener

> **"특정 이벤트가 발생하면, 할 일을 등록하자"**
>
> ```javascript
> EventTarget.addEventListener(type, listener)
> ```
>
> 1. EventTarget : 이벤트 감지를 위한 요소
> 2. addEventListener : EventTarget에 이벤트를 등록할 때 사용하는 이벤트 핸들러
> 3. type : 이벤트 종류
> 4. listener : (콜백 함수) 이벤트가 발생하면 실행되는 함수 - 매개변수 `() 괄호`를 넣지 않아도 된다!
>
> [DOM MDN 문서](https://developer.mozilla.org/ko/docs/Web/Events)

### 4.1 `addEventListener`

- 예시 : 다음과 같이 클릭을 하면 alert 창을 열리도록 하는 event를 만들 수 있다.

```javascript
const btn = document.querySelector('button')
btn.addEventListener('click', function () {
    alert('Button Clicked!')
})
```



### 4.2 `removeEventListener`

- `removeEventListener`을 통해 이벤트를 삭제할 수도 있다.



### 4.3 Event의 종류

- `click` : 포인팅 장치 버튼(모든 버튼; 주번튼만 해당될 예정)이 엘리먼트에서 눌렸다가 놓였을 때
- `mouseover` : 포인팅 장치가 리스너가 등록된 엘리먼트나 그 자식 엘리먼트의 위로 이동했을 때
- `mouseout` : 포인팅 장치가 리스너가 등록된 엘리먼트 또는 그 자식 엘리먼트의 밖으로 이동했을 때
- `keypress` : 쉬프트, Fn, CapsLock을 제외한 키가 눌린 상태일 때(연속적으로 실행됨)
  - 현재는 잘 사용하지 않음!
- `keydown` : 키를 눌렸을 때
- `keyup` : 키 누름이 해제될 때
- `load` : 리소스와 그 의존 리소스의 로딩이 끝났을 때
- `scroll` : document view나 element가 스크롤되었을 때
- `change` : 파일이 주어진 저장소에서 생성, 수정, 삭제될 때



## <실습> EventListener

**경고창 만들기** : `click`

- 이것은 잘 활용하는 방법은 아니다.

```html
  <script>
    const alertMessage = function () {
      alert('안녕하세요!')
    }
  </script>
```

```html
  <button onclick="alertMessage()">나를 눌러봐!</button>
```

- 따라서 다음과 같이 사용한다.

```javascript
const myButton = document.querySelector('#myButton')
myButton.addEventListener('click', alertMessage)
```

- 여기서 `#myButton`은 id가 `myButton`인 태그를 가져온 것이다.

**입력 값 가져오기 : `keydown`**

- :white_check_mark:`event.target.value`로 입력 값을 받아 올 수 있다!

```javascript
const myTextInput = document.querySelector('#myTextInput')
    // function () 은 익명 함수를 넘기는 것이다.
    myTextInput.addEventListener('keydown', function (event) {
      // console.log(event)
      // console.log(event.target.value)
      const myParagraph = document.querySelector('#myParagraph')
      myParagraph.innerText = event.target.value
    })
```

**입력 값에 따라 색상 바꾸기 : `keydown`**

```javascript
const changeColorInput = document.querySelector('#changeColorInput')
changeColorInput.addEventListener('keydown', function () {
    const h2 =document.querySelector('h2')
    h2.style.color = event.target.value
})
```

**submit의 기본 동작 막기**

- :white_check_mark: **`.preventDefault()`**로 기본 동작을 막을 수 있다. 자세한 건 수요일 수업에서 다룬다.

```javascript
const form = document.querySelector('#myForm')
form.addEventListener('submit', function (event) {
    console.log(event)
    console.log(event.cancelable)
    event.preventDefault()
})
```



## <실습> To-Do List 만들기

```html
<!-- HTML body 구조 -->
<body>
  <input type="text">
  <button>Todo!</button>
  <ul></ul>
    
  <script>  
  </script>
</body>
```

```javascript
const button = document.querySelector('button')
    
button.addEventListener('click', function () {
    const input = document.querySelector('input')
    const content = input.value

    const li = document.createElement('li')
    li.innerText = content
    // li.innerText = todo

    const ul = document.querySelector('ul')
    ul.appendChild(li)

    input.value = ''
})
```

- 함수를 정의해준다.

```javascript
const button = document.querySelector('button')

function addTodo () {
    const input = document.querySelector('input')
    const content = input.value

    const li = document.createElement('li')
    li.innerText = content
    // li.innerText = todo

    const ul = document.querySelector('ul')
    ul.appendChild(li)

    input.value = ''
}

button.addEventListener('click', addTodo)
```

**enter를 치면 등록하는 기능**

```javascript
const input = document.querySelector('input')

input.addEventListener('keydown', function (event) {
    if (event.code === 'Enter') {
        addTodo()
    }
})
```

- `Enter`로 입력하면 한글 특수상의 오류가 발생하기 때문에, 현재의 단계에서는 일단 `keypress`로 입력해준다.

**Create, READ 기능**

```javascript
    const button = document.querySelector('button')
    const input = document.querySelector('input')


    function addTodo () {
      const content = input.value
      
      if (content !== '') {
        const li = document.createElement('li')
        li.innerText = content
    
        const ul = document.querySelector('ul')
        ul.appendChild(li)

        input.value = ''
      } else {
        alert('빈 값 안됨!!!')
      }

    }
	
	// 이벤트 등록
    button.addEventListener('click', addTodo)
    input.addEventListener('keydown', function (event) {
      if (event.code === 'Enter') {
        addTodo()
      }
    })
```

**Delete 기능**

```html
<style>
    .done {
      text-decoration: line-through;
    }
</style>
```

```javascript
li.addEventListener('click', function (event) {
          event.target.classList.toggle('done')
        })

const deleteButton = document.createElement('button')
deleteButton.innerText = 'X'
deleteButton.style.marginLeft = '10px'
li.appendChild(deleteButton)

deleteButton.addEventListener('click', function () {
    li.remove()
})
```

- 2번째 줄의 `event.target` 대신에 `li` 혹은 `this`를 사용할 수도 있다.



***Copyright* © 2020 Song_Artish**