# Effect Hook

---

[TOC]

---



## Side Effect

함수 내에서 어떤 구현이 함수 외부에 영향을 끼치는 경우, 해당 함수는 Side Effect(부수 효과)가 있다고 이야기한다.

```javascript
let hello = 'hello'
let changeHello = () => {
    hello = 'bye'
}
changeHello()	// chageHello는 Side Effect를 발생시킨다
```

> **Pure Function**

순수 함수(Pure Function)란, 오직 함수의 입력만이 함수의 결과에 영향을 주는 함수이다. 순수 함수는 입력으로 전달된 값을 수정하지 않으며, 만약 결과를 예측할 수 있다면 순수 함수가 아니다.

```javascript
let upper(str) = () => {
    return str.toUpperCase()	// 원본을 수정하지는 않는다.
}
```

React 컴포넌트에서의 대표적인 Side Effect는 다음과 같다.

- 타이머 사용 (`setTimeout`)
- 데이터 가져오기 (`fetch API`, `localStorage`)



## Effect Hook

`useEffect`는 컴포넌트 내에서 side effect를 실행할 수 있게 하는 hook이다. 매번 새롭게 컴포넌트가 **렌더링**될 때(컴포넌트 생성 시, 새 props 전달 시, state 변경 시) Effect Hook이 실행된다.

```react
useEffect(함수)	// 컴포넌트가 렌더링될 때마다 함수가 실행된다.
```

Hook을 사용할 때에는 몇 가지 주의할 사항이 있다.

- 최상위에서만 Hook을 호출한다.
- React 함수 내에서 Hook을 호출한다.



## 조건부 Effect 발생

`useEffect`의 두 번째 인자는 **배열(dependency array, 종속적 배열)**로, 이 배열은 **어떤 값의 변경이 일어날 때를 의미하는 조건**을 담고 있다.

```react
useEffect(함수, [value1, value2, ...])
```

단, 빈 배열을 넣는 경우에는 컴포넌트가 처음 생성될 때 **단 한 번만 Effect 함수가 실행**된다.

```react
useEffect(함수, [])	// 컴포넌트가 처음 생성될 때만 effect 함수 실행
useEffect(함수)	// 컴포넌트가 렌더링될 때마다 effect 함수 실행
```



***Copyright* © 2022 Song_Artish**