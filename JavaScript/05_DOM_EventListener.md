# EventListener

---

[TOC]

---



## Event 객체

사용자 입력(`onclick`, `onkeyup`, `onscroll` 등)을 trigger로 발생한 이벤트 정보를 담은 객체



## EventListener

```javascript
EventTarget.addEventListener(type, listener)
```

1. EventTarget : 이벤트 감지를 위한 요소
2. addEventListener : EventTarget에 이벤트를 등록할 때 사용하는 이벤트 핸들러
3. type : 이벤트 종류
4. listener : (콜백 함수) 이벤트가 발생하면 실행되는 함수 - 매개변수 `() 괄호`를 넣지 않아도 된다!

- `addEventListener`: 이벤트를 등록할 수 있다.
- `removeEventListener`: 이벤트를 삭제할 수 있다.

```javascript
// 예시: 클릭을하면 alert 창을 발생하도록 하는 event
const btn = document.querySelector('button')
btn.addEventListener('click', function () {
    alert('Button Clicked!')
})
```



## Event 정의

다양한 방법으로 event 함수를 정의할 수 있다.

```javascript
btn.onclick = function () {
    console.log('clicked');
}
```

```javascript
btn.addEventListener('click', function () {
    console.log('clicked');
});
```

```javascript
function handler () {
    console.log('clicked');
}
btn.onclick = handler;
// handler();가 아니니 주의!
```



## Event의 종류

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



***Copyright* © 2022 Song_Artish**
