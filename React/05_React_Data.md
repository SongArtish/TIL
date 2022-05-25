# Data

---

[TOC]

---



## Overview

React는 **단방향 데이터 흐름(one-way data flow)**이라는 특징을 가지고 있다. 데이터 흐름이 하향식(top-down)이며, 데이터를 전달하는 주체가 부모 컴포넌트이다. 컴포넌트는 props를 통해 전달받은 데이터가 어디서 왔는지 알지 못한다.

![React Lifecycle](img/react_lifecycle.png)

`(출처: https://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/)`



## props

부모 컴포넌트가 자식 컴포넌트에 값을 전달할 때 사용한다.

- 컴포넌트의 속성(property)를 의미한다. 성별, 이름처럼 변하지 않는 **외부로부터 전달받은 값**이다.
- 상위 컴포넌트로부터 전달받은 값이다.
- **객체 형태**로 어떤 타입의 값도 props에 넣어서 전달할 수 있다.
- 읽기 전용(read-only)이다.

> **props 사용하기**

1. 하위 컴포넌트에 전달하고자 하는 값(data)과 속성을 정의한다.

2. props를 이용하여 정의된 값과 속성을 전달한다.

3. 전달받은 props를 렌더링한다.

   ```react
   function Parent() {
       return (
           <div className="parent">
               <h1>I am parent.</h1>
                {/* 2. 데이터 전달 */}
               <Child text={"I am the oldest child."} />
           </div>
       );
   };
   
   function Child() {
     return (
         <div className="child">
         	{/* 3. props 데이터 가져오기 */}
           <p>{props.text}</p>
         </div>
     );  
   };
   ```

> `props.children`을 이용하면 태그 사이의 value를 전달할 수 있다.

```react
function Child(props) {
  return (
      <div className="child">
          {/* 데이터 받기 */}
          <p>{props.children}</p>
      </div>
  );  
};
```





## state

컴포넌트의 사용 중 **컴포넌트 내부에서 변할 수 있는 값**으로 **상태**를 나타낸다.

- 시간 경과에 따른 데이터를 표현한다.
- 데이터 변경이 필요한 경우 `setState()` 함수를 통해 값을 변경한다.
- React 컴포넌트는 state가 변경되면 새롭게 호출되고, 리렌더링 된다.

> **useState 사용하기**

`useState`는 state hook이다.

```react
import { useState } from "react";
```

`useState`를 컴포넌트 안에서 호출한다. 이것은 "state"라는 변수를 선언하는 것과 같다.

```react
function CheckboxExample () {
    // const [state 저장 변수, state 갱신 함수] = useState(상태 초기 값)
    const [isChecked, setIsChecked] = useState(false);
    // 혹은
    const stateHookArray = useState(flase);
    const isChecked = stateHookArray[0];
    const setIsChecked = stateHookArray[1];
}
```

state 갱신 함수는 별도의 함수를 선언하여 호출한다.

```react
function CheckboxExample () {
    const [isChecked, setIsChecked] = useState(false);
    // 별도 함수를 선언
    const handleChecked = (event) => {
      setIsChecked(event.target.checked);  
    };
    return (
        <div className="App">
            <input type="checkbox" checked={isChecked} onChange={handleChecked} />
            <span>{isChecked ? "Checked!" : "Not checked"}</span>
        </div>
    );
}
```



## 사용하기

### 1. 데이터 정의

아래 항목 중 하나라도 만족하면 state가 아니다

- 부무로부터 props를 통해 전달받나?
- 시간이 지나도 변하지 않나?
- 컴포넌트 안의 다른 state나 props를 가지고 계산 가능한다?

### 2. State 위치 정하기

공통 소유 컴포넌트(공통의 부모)를 찾아 그 곳에 상태를 위치해야 한다.

### 3. 역방향 데이터 흐름 추가

역방향 데이터 흐름을 추가하는 것을 **State 끌어올리기(Lifting state up)**라고 한다. 상태를 변경시키는 함수(handler)를 하위 컴포넌트에 props로 전달해서 제어할 수 있다.

```react
let ParentComponent = () => {
    let [value, setValue] = useState('')
    let handleChangeValue = (newValue) => {
        setValue(newValue)
    }
    ...

}
        
let ChildComponent = ({handleButtonClick}) => {
	let handleClick = () => {
		handleButtonClick()
	}
    return (
    	<button onClick={handleClick}>Change Value</button>
    )
}
```



***Copyright* © 2022 Song_Artish**