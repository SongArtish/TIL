# 비동기

---

[TOC]

---



## Why Async?

비동기는 response에 관계 없이 작업을 계속 진행하기 때문에 시간이 절약되며 효율적이다.

- **Blocking**: 순차적으로 진행하며, 요청에 대한 결과가 동시에 일어난다. (synchronous)
- **Non-blocking**: 순차적으로 진행되지 않으며, 요청에 대한 결과가 동시에 일어나지 않는다. (asynchronous) 



## 비동기 함수 전달 패턴

1. Callback 패턴

```javascript
let request = 'caffelatte';
orderCoffeeAsync(request, function(response) {
    // response -> 주문한 커피 결과
    drink(response);
});
```

2. 이벤트 등록 패턴

```javascript
let request = 'caffelatte';
orderCoffeeAsync(request).onready = function(response) {
    // response -> 주문한 커피 결과
    drink(response);
};
```



## 주요 사례

- DOM Element의 **Event Handler**
  - Click, Keydown 등
  - 페이지 로딩 (DOMContentLoaded 등)
- 타이머
  - 타이머 API (`setTimeout` 등)
  - 애니메이션 API (requestAnimationFrame)
- 서버에 지원 요청 및 응답
  - fetch API
  - AJAX (XHR)



## 비동기의 3가지 방법

### 1. Callback

Callback 함수는 다른 함수의 인자로 넘어가는 함수를 의미한다. 비동기를 제어하기 위해서 사용한다.

```javascript
const printString = (string, callback) => {
    setTimeout(
        () => {
            console.log(string)
            callback() // 받은 콜백함수를 실행해줌
        },
        Math.floor(Math.random() * 100) + 1
    )
}

// 순서대로 콜백함수를 인자를 넣어줘서, 순차적으로 실행될 수 있게 함
const printAll = () => {
    printString("A", () => {
        printString("B", () => {
            printString("C", () => {})
        })
    })
}

printAll()
```

> **Callback error handling Design**. 

Callback 설계 시 에러 처리를 위해 아래와 같이 디자인한다.

```javascript
const callBack = (callback) => {
    // (err, data)를 인자로 받는다.
    getData((err,data) => {
        if (err) {
            // 에러가 발생한 경우, 데이터는 null로 넘겨준다.
            callback(err, null)
        }
        else {
            // data가 넘어온 경우, 에러는 null로 넘겨준다.
            callback(null, data)
        }
    })
}
```

### 2. Promise

`Promise` 는 비동기 작업의 최종 완료 또는 실패를 나타내는 객체로, `callback hell`을 해결해준다. (ES6에서 등장)

```javascript
const newPromise = new Promise() // Promise 선언
newPromise.resolve() // Go to next action
newPromise.reject() // Handle error
```

> - **`.then(callBack)`**
> - **`.catch(callBack)`**

```javascript
function questionToProfessor ('질문', solveQuestion) {
    .then (solveQuestion) // 성공했을 때
    .then (share) // 성공했을 때
    .catch (resolveMyError) // 실패했을 때
}
```

위에서 callback으로 작성한 `printString` 함수를 promise로 작성하면 아래와 같다.

```javascript
const printString = (string) => {
    // (resolve, reject)를 인자로 받는다.
    return new Promise((resolve, reject) => {
        setTimeout(
            () => {
                console.log(string)
                resolve()
            },
            Math.floor(Math.random() * 100) + 1
        )    
    })
    // Error Handling을 하려는 경우, try & catch를 통해 reject를 할 수도 있다.
}

const printAll = () => {
    printString("A")
    // Promise를 사용하면 .then으로 이어나갈 수 있음
    .then(() => {
        return printString("B")
    })
    .then(() => {
        return printString("C")
    })
}

printAll()
```

> **Chaining**

다음과 같이 특정 작업 수행을 성공했을 때, 다음의 요청을 promise 방식으로 chaining할 수 있다.

```javascript
axios.get('https://jsonplaceholder.typicode.com/todos/1')
        .then(function (res) {
        console.log(res)
        return res.data
    })
        .then(function (res) {
        console.log(res)
        return res.title
    })
        .then(function (res) {
        console.log(res)
    })
        .catch(function (err) {
    	console.log(err)
    })
```

> **Promise.all()**

`Promise.all()` 메서드는 순회 가능한 객체에 주어진 모든 프로미스가 이행한 후, 혹은 프로미스가 주어지지 않았을 때 이행하는 [`Promise`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise)를 반환합니다. 주어진 프로미스 중 하나가 거부하는 경우, 첫 번째로 거절한 프로미스의 이유를 사용해 자신도 거부합니다.

```javascript
const promise1 = Promise.resolve(3);
const promise2 = 42;
const promise3 = new Promise((resolve, reject) => {
  setTimeout(resolve, 100, 'foo');
});

Promise.all([promise1, promise2, promise3]).then((values) => {
  console.log(values);
});
// expected output: Array [3, 42, "foo"]
```

### 3. async & await

함수 앞에 `async`와 `await`를 붙여서 동기적으로 진행되도록 할 수 있다. (ES8+)

```javascript
const result = async () => {
    const one = await getOne()
    const two = await getTwo()
    ...
}
```

promise를 return하는 구문 앞에 await를 붙인다.

```javascript
async function getTodo2 () {
    console.log('1')
    await axios.get('https://jsonplaceholder.typicode.com/todos/1')
        .then(function (res) {
        console.log(res)
    })
    console.log('2')
}
getTodo2()
```



## 타이머 관련 API

> **setTimeout(callback, millisecond)**

일정 시간 후에 함수를 실행한다.

- argument: callback(실행할 callback 함수), millisecond(callback 함수 실행 전 기다려야 할 시간, 밀리초)
- return 값: 임의의 타이머 ID

```javascript
setTimeout(function () {
    console.log('1초 후 실행')
}, 1000)
// 123
```

> **setInterval(callback, millisecond)**

일정 시간의 간격을 가지고 함수를 반복적으로 실행

- argument: callback(실행할 callback 함수), millisecond(반복적으로 함수를 실행시키기 위한 시간 간격, 밀리초)
- return 값: 임의의 타이머 ID

```javascript
setInterval(function () {
    console.log('1초마다 실행')
}, 1000)
// 345
```

> **clearInterval(timerId)**

`setInterval()`로 반복 실행 중인 타이머를 종료

- argument: timerId(타이머 ID)
- return 값: 없음

```javascript
const timer = setInterval(function () {
    console.log('1초마다 실행')
}, 1000)
clearInterval(timer)
// 더 이상 반복 실행되지 않음
```

> **clearTimeout(timerId)**

`setTimeout()`으로 호출된 타이머를 종료

- argument: timeoutId(타이머 ID)
- return 값: None(`undefined`)



***Copyright* © 2022 Song_Artish**
