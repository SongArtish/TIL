# Data

---

[TOC]

---



## Overview

React에서 데이터를 전달하는 방법에 대해서 다룬다.

![React Lifecycle](img/react_lifecycle.png)

`(출처: https://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/)`



## props

부모 컴포넌트가 자식 컴포넌트에 값을 전달할 때 사용한다. (읽기 전용)

아래는 props를 사용하는 간단한 예시이다. `App` 컴포넌트의 자식 컴포넌트로 `Name` 컴포넌트가 있으며, `first`와 `last`라는 데이터를 `this.props`로 전달받는다.

```react
// App.js
import React from 'react'

class Name extends React.Component {
  render () {
      // 2. 데이터를 받는다
      const { first, last } = this.props;
      return (
        // 3. 데이터를 사용한다
        <span>Name : {first} {last}</span>
      );
    }
}

// 1. 데이터를 선언한다
Name.defaultProps = {
  first: "Song",
  last: "zero"
};

function App () {
  return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <Name />
        </header>
      </div>
  )
}

export default App;
```

아래와 같이 `App` 컴포넌트에서 상속받은 변수를 `Name` 컴포넌트에서 props로 받을 수도 있다.

```react
class Name extends React.Component {
  render () {
      const { first, last } = this.props;
      return (
        // 3. 데이터를 사용한다
        <span>Name : {first} {last} (aka. {this.props.nick})</span>
      );
    }
}

Name.defaultProps = {
  first: "Song",
  last: "zero"
};

class App extends React.Component {
  render () {
    // 1. 데이터를 선언한다
    let nick = 'Artish'
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          {/* 2. 데이터를 상속한다 */}
          <Name nick={nick} />
        </header>
      </div>
    )
  }
}
```



## state

자기 자신이 가지고 있는 값이다.

- 시간 경과에 따른 데이터를 표현한다.
- 데이터 변경이 필요한 경우 `setState()` 함수를 통해 값을 변경한다.

아래는 state를 사용하는 간단한 예시이다. `App` 컴포넌트에서 state를 정의하고, state의 데이터를 `Name` 컴포넌트에 상속한다.

```react
// App.js
class Name extends React.Component {
  render () {
      const { first, last } = this.props;
      return (
        // 3. 데이터를 사용한다
        <span>Name : {first} {last} (aka. {this.props.nick})</span>
      );
    }
}

Name.defaultProps = {
  first: "Song",
  last: "zero"
};

class App extends React.Component {
  // 1. 데이터를 선언한다
  state = {
    nick: "Artish"
  }
  render () {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          {/* 2. 데이터를 상속한다 */}
          <Name nick={this.state.nick} />
        </header>
      </div>
    )
  }
}

export default App;
```

- 아래와 같이 state를 사용할 수도 있다.

```react
class Hello extends React.Component {
  render () {
    return (
      // 3. 데이터를 사용한다
      <div>Hello, my name is {this.props.name}.</div>
    )
  }
}

class App extends React.Component {
  constructor(props) {
    super(props);
    // 1. 데이터를 선언한다
    this.state = {
      name: 'Songzero'
    };
  }
  render () {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          {/* 2. 데이터를 상속한다 */}
          <Hello name={this.state.name} />
        </header>
      </div>
    )
  }
}
```



***Copyright* © 2022 Song_Artish**