# DOM CRUD

---

[TOC]

---



## Create

- **createElement**를 사용하여 새로운 element를 만들 수 있다.

```javascript
// div element를 만든다
document.createElement('div')
```



## Append

- **append**를 사용해 부모 노드에 자식 노드를 추가할 수 있다.

```javascript
// 생성한 div를 트리 구조와 연결한다
const exampleDiv = document.createElement('div')
document.body.append(exampleDiv)
```

-  **appendChild** 메서드는 `append` 메서드와는 다르게 오직 Node 객체만 받을 수 있으며, 한 번에 오직 하나의 노드만 추가할 수 있다.



## Read

- **querySelector**의 <u>첫 번째 엘리먼트만</u>을 가져오며, selector로는 아래 3가지를 가장 많이 사용한다.

```javascript
// 1. HTML 태그
const example = document.querySelector("div")
// 2. id
const example = document.querySelector("#example")
// 3. class
const example = document.querySelector(".example")
```

- **querySelectorAll**은 여러 개의 엘리먼트를 한 번에 가져오기 위해 사용한다.

```javascript
const examples = document.querySelectorAll('.example')
```

- 오래된 방식 중 **getElementById**라는 메서드가 있으며, 하나의 요소만 가져온다.

```javascript
const example = document.getElementById('example')
```



## Update

- **textContent**을 사용하면 비어있는 엘리먼트에 문자열을 입력할 수 있다.

```javascript
const exampleDiv = document.querySelector('#example-div') // <div></div>
exampleDiv.textContent = 'This is an exmple div tag.'
```

- **classList.add**를 이용해 엘리먼트에 클래스를 추가할 수 있다.

```javascript
exampleDiv.classList.add('exampleDiv')
```

- :ballot_box_with_check: `setAttribute`라는 메소드를 사용하여 엘리먼트에 class, id 외에 다른 attribute를 추가할 수 있다.



## Delete

- **remove**를 사용하면 위치를 알고 있는 엘리먼트를 삭제할 수 있다.

```javascript
const container = document.querySelector('#container')
const exampleDiv = document.createElement('div')
container.append(exampleDiv)
exampleDiv.remove() // 엘리먼트를 삭제할 수 있다.
```

- `innterHTML`을 이용하면 여러 개의 자식 엘리먼트를 간단히 지울 수 있다.

```javascript
// id가 container인 엘리먼트 아래의 모든 엘리먼트를 지운다.
document.querySelector('#container').innterHTML = ''
```

- :warning: 단, 위 메서드는 보안 상 몇 가지 문제점을 가지고 있으며, 이는 **removeChild** 메소드로 대신할 수 있다.

```javascript
const container = document.querySelector('#container')
while (container.children.length > 1) {
    container.removeChild(container.lastChild)
}
```

- 또는 직접 클래스 이름이 example인 엘리먼트만 찾아서 지울 수도 있다.

```javascript
const examples = document.querySelectorAll('.example')
examples.forEach(function (example) {
    example.remove()
})
// or
for (let example of examples) {
    example.remove()
}
```



***Copyright* © 2022 Song_Artish**
