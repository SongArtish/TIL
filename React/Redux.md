# Redux

2022.03.29

---

[TOC]

---



## Overview

[공식 문서](https://redux.js.org/introduction/getting-started)

- Vuex와 마찬가지로 **상태 관리를 위한 라이브러리**
- 클라이언트 앱의 복잡성을 제어하기 위한 하나의 state 제어 수단

> **Redux와 React contextAPI는 언제 사용하면 좋을까?**
>
> - **React contextAPI**: 컴포넌트의 통합 데이터를 관리하는 경우
> - **Redux**: 서버에서 가져온 데이터로 새로운 결과물을 만드는 경우



## 시작하기

**React 프로젝트 시작 단계인 경우**

```bash
$ npx create-react-app <프로젝트명> --template redux
```

**React 프로젝트 진행 단계인 경우**

- Redux를 프로젝트에 추가한다.

```bash
$ npm i redux
```

- Redux를 React 프로젝트에 추가한다.

```bash
$ npm i react-redux
```

- Chrome 확장 프로그램 설치와 연동하기 위해 tool kit을 설치한다.
  - Store 값이 바뀌는 상태를 쉽게 확인 가능
  - 개발 단계에서만 사용하는 경우 `-D` 옵션 추가

```bash
$ npm i -D redux-devtools
```



## 간단한 사용법

여기서 작성되는 예시는 `src > redux` 폴더 안에서 파일을 생성하여 진행한다. 먼저 `store.js` 파일을 생성하고, reducer를 store에 등록해준다.

```javascript
// store.js
import { createStore } from "redux"
import rootReducer from "./rootReducer"

const store = createStore(rootReducer)

export default store
```

reducer 파일을 만든다. reducer 파일에서는 state와 action을 정의한다.

```javascript
// rootReducer.js
const initialState = {
    dogData: ['hello', 'bye', 'baby'],
}

const rootReducer = (state = initialState, action) => {
    // console.log(state)  // --> {dogData: Array(3)}
    switch (action.type) {
        case "SET_DOGS":
            return {...state, dogData: [...state.dogData, action.payload]}
        default:
            return state
    }
}

export default rootReducer
```

다음으로는 action을 받을 파일을 만든다.

```javascript
// actions.js
export const setDogs = data => ({
    type: "SET_DOGS",
    payload: data
})
```

`App.js` 파일에서 state를 받아서 사용한다. 또한, dispatch를 이용하여 데이터를 변경한다.

```javascript
// App.js
...
// redux의 데이터를 받아오기 위해 사용한다.
import { connect } from "react-redux";
// action을 가져온다.
import { setDogs } from "./redux/actions";

// state를 가져와주는 함수를 정의한다.
const mapStateToProps = state => {
  return {
    dogData: state.dogData,
  };
};

// 데이터를 변경(dispatch)하는 함수를 정의한다.
const mapDispatchToProps = dispatch => {
  return {
    setDogs: dog => dispatch(setDogs(dog)),
  };
}

// 데이터를 받아준다.
function App({ dogData, setDogs }) {

  let clickHandler = () => {
    // 함수에서 state의 값을 변경하는 함수를 사용한다.
    setDogs('hello dog')
    console.log(dogData)
  }

  return (
    ...
}

// export를 변경한다.
// export default connect(mapStateToProps)(App)
export default connect(mapStateToProps, mapDispatchToProps)(App)
// export default connect(null, mapDispatchToProps)(App);
```



## 기본 용어

### 1) Action

- **상태에 변화가 필요한 경우** action을 일으켜야 한다.
- Action은 <u>object로 표현</u>되며 <u>type 필드를 반드시 가지고 있어야</u> 한다.

```javascript
{
   type: 'LEARN_REDUX',
   data: {
       id: 1,
       text: '리덕스 배우기'
   }
}
```

**활용**

- `.../actionTypes.js` 파일에 action을 지정해두고, `import`해서 사용한다.

```javascript
// 액션 정의 : .../actionTypes.js 

// 액션명은 대문자로 입력
export const ADD_TODO = 'ADD_TODO'
export const TOGGLE_TODO = 'TOGGLE_TODO'
export const SET_VISIBILITY_FILTER = 'SET_VISIBILITY_FILTER'

{
  type : ADD_TODO,
  text : 'build my first Redux app',
  index : 33, // 고유인덱스를 사용하기도함.
}
```

```javascript
// 액션을 사용할 곳
import  { ADD_TODO, TOGGLE_TODO, SET_VISIBILITY_FILTER } from '경로/actionTypes'
```

### 2) Action Creator

- 액션 생성함수는 **액션 객체를 만들어주는 함수**이다.
- 화살표 함수로도 표현 가능

```javascript
function learnRedux(data) {
 return {
   type: 'LEARN_REDUX',
   data,
 }
}
```

### 3) Reducer

> 변화를 일으키는 것

- <u>현재 상태와 액션 객체를 받아</u>, 필요하다면 **새로운 상태를 return**하는 함수
- 일종의 event listener

```javascript
const initialState = {
 counter: 1,
}
function reducer(state = initialState, action) {
 switch (action.type) {
   case INCREMENT:
     return {
       counter: state.counter + 1,
     }
   default:
     return state
 }
}
```

### 4) Store

- 하나의 프로젝트에는 하나의 store만 가질 수 있음
- Store에는 state가 들어있음

### 5) Dispatch

- Store 내장 함수
- **액션 객체를 넘겨줘서 상태를 업데이트**하는 유일한 방법

### 6) Subscribe

- Store 내장 함수
- listener 함수를 parameter로 넣어 호출하면 상태가 업데이트될 때마다 호출됨
- 일종의 event listener

### 7) Selector

- **상태 값을 가져올 때** 사용
- cf. 일반적인 vanilla.js의 redux에서는 store 내장함수인 getState를 사용



## 상태 변화 흐름

> **Component -> Action -> Reducer -> Store**

### Component

- 화면에 보여지는 앱(view)
- `dispatch`[Component-> Action]: 액션을 발생시킴
- ex) 고객

### Action

- 상태 변화를 일으키기 위해 액션은 바뀔 부분을 지시하고, 그런 변경에 필요한 데이터를 제공한다.
- `handle`[Action-> Reducer]: action에 정의되어 있는 내용이 reducer에 의해 핸들링됨
- ex) 원하는 물품을 선택해 주문한다.

### Reducer

- 이전 상태(state), Action을 받아서 변화를 일으킴
- `update`[Reducer-> Store]: 핸들링에 따라서 상태 값이 업데이트됨
- ex) 직원이 주문을 받고 물품을 가져와 포장한다.

### Store

- 현재 상태, Reducer 등 상태에 관한 데이터를 store에 담는다.
- `subscribe` [Store-> Component]: 업데이트된 store를 subscribver를 통해 실시간으로 받아와서 사용
- ex) 현재 고객의 정보와 물품은 모두 택배 회사의 서버에 저장되어 있다.



## Redux의 3가지 규칙

1. 하나의 어플리케이션 안에는 하나의 store를 갖는다.
2. 상태는 read-only이다.
3. Reducer는 순수한 함수여야 한다.



***Copyright* © 2022 Song_Artish**