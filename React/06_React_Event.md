# React Event

---

[TOC]

---



## Event Handling

React의 이벤트 처리 방식은 DOM의 방식과 유사하나, 몇 가지의 문법 차이가 존재한다.

- 이벤트는 camelCase를 사용한다.
- JSX를 사용하여 문자열이 아닌 함수로 event handler(이벤트 처리 함수)를 전달한다.

```html
<!-- html 방식 -->
<button onclick="handleEvent()">Event</button>
```

```react
// React 방식
<button onClick={handleEvent}>Event</button>
```



## Event

### onChange

`<input>`, `<textarea>`, `<select>`와 같은 form 엘리먼트에서는 사용자의 입력 값을 제어하는데, 이렇게 값이 변경될 때 발생하는 이벤트이다. `onChange` 이벤트가 발생하면 `event.target.value`를 통해 이벤트 객체에 담겨 있는 `iput` 값을 가져올 수 있다.

```react
function NameForm () {
    const [name, setName] = useState("")
    const handleChange = (event) => {
        setName(event.target.value)
    }
    return (
        <div>
            <input type="text" value={name} onChange={handleChange}></input>
            <h1>{name}</h1>
        </div>
    )
}
```

### onClick

사용자가 `클릭`이라는 행동을 했을 때 발생하는 이벤트이다.

```react
function NameForm () {
    const [name, setName] = useState("")
    return (
        <div>
            <input type="text" value={name} onChange={(event) => setName(event.target.value)}></input>
            {/* 버튼 클릭 시 name을 알림창이 팝업되도록*/}
            <button onClick={() => alert(name)}>Button</button>
            <h1>{name}</h1>
        </div>
    )
}
```

:warning: 만약 `<button onClick={alert(name)}>Button</button>`과 같이 alert(name) 함수를 바로 호출하면 컴포넌트가 렌더링될 때 함수 호출 결과가 바로 적용된다. 따라서 위와 같이 **이벤트에 함수 자체를 전달**하도록 한다.



***Copyright* © 2022 Song_Artish**