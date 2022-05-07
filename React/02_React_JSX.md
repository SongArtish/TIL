# JSX

> JavaScript XML

---

[TOC]

---



## Overview

React에서 UI를 구성할 때 사용하는 문법으로 **JavaScript를 확장한 문법**이다. 이 문법을 이용해서 React 엘리먼트를 만들 수 있다.

브라우저가 바로 실행할 수 있는 JavaScript 코드가 아니기 때문에 **Babel을 이용해서 JSX를 JavaScript로 컴파일** 해주어야 한다. 컴파일 후, JavaScript를 브라우저가 읽고 화면에 렌더링할 수 있다.

DOM에서 JavaScript를 사용하기 위해서는 JavaScript와 HTML을 연결하기 위한 작업이 필요하지만, React에서는 JSX를 이용해서 DOM 코드보다 더욱 **명시적으로 코드를 작성할 수 있다.** JavaScript 문법과 HTML 문법을 동시에 이용해 기능과 구조를 한눈에 확인할 수 있다.

```react
// App.js
import React from "react";
import "./styles.css";

function App() {
  const name = {
    firstName: "React",
    lastName: "JSX"
  };

  function formatName(name) {
    return name.firstName + " " + name.lastName;
  }
  // JSX 없이 활용한 React
  return React.createElement("h1", null, `Hello, ${formatName(name)}!`);

  // JSX 를 활용한 React
  return <h1>Hello, {formatName(name)}!</h1>;
}

export default App;
```

JSX 없이도 React 요소를 만들 수는 있지만, 코드가 복잡하고 가독성이 떨어지게 된다.



## 문법

1. **하나의 엘리먼트 안에 모든 엘리먼트가 포함**되어야 한다.

```react
// 옳은 문법
<div>
	<div>div1</div>
    <div>div2</div>
</div>
// 잘못된 문법
<div>div1</div>
<div>div2</div>
```

2. 엘리먼트 클래스 사용 시, **className**으로 표기한다.

```react
// 옳은 문법
<div className="hello">Hello</div>
// 잘못된 문법
<div class="hello">Hello</div>
```

:warning: class로 작성하게 되면 React에서는 이를 html 클래스 속성 대신 자바 스크립트 클래스로 받아들이게 된다.

3. JavaScript 표현식 사용 시 , **중괄호(`{}`)**을 사용한다.

```react
function App () {
    const name = 'Song Artish';
    return {
        <div>
        	Hello, {name}
        </div>
    };
}
```

4. **사용자 정의 컴포넌트는 대문자로 시작**한다. (PascalCase)

```react
// 옳은 문법
function Hello () {
    return <div>Hello!</div>;
}
function HelloWorld () {
    return <Hello />;
}
// 잘못된 문법
function hello () {
    return <div>Hello!</div>;
}
function HelloWorld () {
    return <hello />;
}

```

:warning: 소문자로 시작하게 되면 일반적인 HTML 엘리먼트로 인식하게 된다.

5. **조건부 렌더링에는 삼항연산자를 사용**한다.

```react
<div>
	{
        (1+1 === 2) ? (<p>정답</p>) : (<p>오답</p>)
    }
</div>
```

6. 여러 개의 HTML 엘리먼트를 표시할 때, `map()` 함수를 사용한다.

```react
const books = [
    {id: 1, title: 'title 1', content: 'content 1'},
    {id: 2, title: 'title 2', content: 'content 2'}
]

function Book() {
    const content = books.map((book) =>
        // map 함수를 사용할 때는 반드시 "key" JSX 속성을 넣어준다.
    	<div key={book.id}>
        	<h3>{book.title}</h3>
            <p>{book.content}</p>
        </div>
    );
    return {
        <div>
        	{content}
        </div>
    }
}
```

:warning: 렌더링 한 항목에 대한 안정적인 ID가 없다면, 최후의 수단으로 <u>항목의 인덱스를 key로 사용</u>할 수 있습니다.

```react
const todoItems = todos.map((todo, index) =>
  // Only do this if items have no stable IDs
  <li key={index}>
    {todo.text}
  </li>
);
```



***Copyright* © 2022 Song_Artish**
