# React 라이프사이클

---

[TOC]

---



![react_lifecycle](img/react_lifecycle.png)



## React.Component

> [공식문서](https://ko.reactjs.org/docs/react-component.html)

React 컴포넌트 class를 정의하려면 `React.Component`를 상속받아야 한다.

```react
class Welcome extends React.Component {
    render () {
        return <h1>Hello, {this.props.name}</h1>
    }
}
```

`render()`는 React.Component의 하위 class에 반드시 정의해야 하는 메서드이다.



## Component Lifecycle

모든 컴포넌트는 여러 종류의 "생명주기 메서드"를 가지고 있다. 아래에서 자주 사용되는 생명주기 메서드는 **진하게 표시**되었다.

### Mount

아래 메서드들은 컴포넌트의 인스턴스가 생성되어 DOM 상에 삽입될 때 순서대로 호출된다.

- **`constructor()`**
- `static getDerivedStateFromProps()`
- **`render()`**
- **`componentDidMount()`**

:warning: `UNSAFE_componentWillMount()`는 기존에 사용되었지만 이제는 사용하면 안 된다.

### Update

props 또는 state가 변경되면 갱신이 발생한다. 아래 메서드들은 컴포넌트가 다시 렌더링될 때 순서대로 호출된다.

- `statc getDerivedStateFromProps()`
- `shouldComponentUpdate()`
- **`render()`**
- `getSnapsotBeforeUpdate()`
- **`componentDidUpdate()`**

:warning: `UNSAFE_componentWillUpdate()`, `UNSAFE_componentWillReceiveProps()`는 기존에 사용되었지만 이제는 사용하면 안 된다.

### Unmounting

마운트 해제. 아래 메서드는 컴포넌트가 DOM 상에서 제거될 때 호출된다.

- **`componentWillUnmount()`**



***Copyright* © 2022 Song_Artish**