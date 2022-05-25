# JavaScript 함수

---

[TOC]

---



## Overview

### 선언식

```javascript
function add (num1, num2) {
    return num1 + num2
}
add(1, 3)
```

### 표현식

- 일반적으로 표현식은 익명 함수로 작성한다.
- `익명함수`는 표현식에서만 사용 가능하다!

```javascript
const sub = function (num1, num2) {
    return num1 - num2
}
sub (1, 1)
```

- 익명함수가 아닌, 함수에 이름을 지정해줄 수도 있지만 잘 쓰지 않는다.

```javascript
const mySub = function namedSub (num1, num2) {
    return num1 - num2
}
mySub(3, 1)
// namedSub(3, 1)을 사용할 수 없다!
```

### 기본인자

- 다음과 같이 인자의 default 값을 넘겨줄 수 있다.

```javascript
const greeting = function (name = '홍길동') {
    return name
}
```



## Hoisting (선언식 vs 표현식)

```javascript
console.log(typeof add)
console.log(typeof sub)
// add와 sub는 위에서 정의된 함수이다.
```

- 선언식에는 **hoisting**이 일어난다.

```javascript
add(2, 7)

function add (num1, num2) {
    return num1 + num2
}
```

- 표현식은 함수를 변수에 할당했고, 일종의 변수처럼 작동한다.

```javascript
sub(1, 3)

const sub = function (num1, num2) {
    return num1 - num2
}
```

- var로 function 선언시

```javascript
var sub
sub(1, 3)

var sub = function (num1, num2) {
    return num1 - num2
}
```



## Arrow Function (`=>`)

> function과 중괄호를 생략하여 코드를 줄이기 위해 고안된 단축 문법

1. function 생략 가능

2. 함수의 매개변수가 하나밖에 없다면 `()` 생략 가능

3. 함수의 body  {} 안에 들어가는 표현식이 하나면 {} return 생략 가능

   ```javascript
   const arrow = function (name) {
       return `${name}입니다`
   }
   
   // 1. function 생략
   const arrow = (name) => {
       return `${name}입니다`
   }
   
   // 2. () 생략
   const arrow name => {
       return `${name}입니다`
   }
   
   // 3. {}, return 생략 가능
   const arrow = naem => `${name}입니다`
   ```



## 일급객체

first class citizen

1. **변수에 할당** 가능
2. 다른 **함수의 인자**로 전달 가능
3. 다른 함수의 **결과로서 리턴** 가능



***Copyright* © 2020 Song_Artish**
