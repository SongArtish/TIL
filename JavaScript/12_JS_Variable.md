# JavaScript 변수와 식별자

---

[TOC]

---



## 1. 식별자

> 변수명은 식별자라고 하며 특정 규칙을 따른다.

- 반드시 문자, 달러, _로 시작해야 한다. 숫자로 시작할 수 없다. (`-`도 안된다.)
- 대소문자를 구분한다. 클래스명이 아니라면 시작 단어는 대문자 사용을 지양한다.
- 예약어도 사용 불가능한다. (class, const, let, var, await, case ...)

### 작성 스타일

- 기본적으로 camelCase로 작성한다. (lowcaseUppercase)

```javascript
// 숫자, 문자, boolean
let dog
let babyCat

// 배열 = 배열은 복수형으로 작성한다.
let animals

// 함수
function getPropertyName

// 이벤트 핸들러 - `on`으로 시작한다.
function onClick () {}
function onKeyown () {}

// boolean 반환 함수 - return 값이 true, false - is 로 시작한다.
function isAuthenticated () {}
```

- PascalCase로 자성되는 경우 - `클래스`, `생성자`

```javascript
class User {
	information(option) {
        this.name = option.name
    }
}

// 새로운 인스턴스를 생성하는 경우 `new`를 사용한다.
const people = new User({
    name: '홍길동',
})
```

- 대문자 스네이크 케이스 (SNAKE_CASE)
- 이러한 식별자는 값이 변하지 않는다는 것을 말한다.

```javascript
const API_KEY = 'api_key'
const PI = 3.14159265359
```



## 2. 변수

### let (변수)

> 값을 재할당 할 수 있는 변수를 선언하는 키워드

```javascript
let x = 1
x = 3
```

- 선언은 단 한 번만 가능하다. (`SyntaxError` 발생)

```javascript
// 다음과 같이 작성하여서는 안 된다.
/*
let x = 3
let x = 2 */
```

- 유효 범위가 블록을 기준으로 작성이 된다.
- 블록 유효 범위 : `if`, `for` 등 `() 중괄호` 내부를 가리킨다.

```javascript
let x = 1

if (x == 1) {
    let x = 2
    console.log(x)
}
console.log(x)
```



### const (상수)

> const는 재할당도 재선언도 불가능하다.

```javascript
// 오류가 발생한다.
/*
const x = 4
x = 3
console.log(x) */
```

- 선언한 특정 객체가 가지는 값을 재할당/재선언할 수 있다.

```javascript
const foo = {}
foo.bar = 4
console.log(foo)
console.log(foo.bar)
```

- 상수를 선언할 때는, 반드시 값을 초기화해줘야 한다.

```javascript
// 불가능
const a

// 반드시 값을 초기화 해주어야 한다.
const a = 3
```

- let과 같이 블록 유효 범위를 가진다.

```javascript
const num = 3

if (num == 3) {
    const num = 4
    console.log(num)
}
console.log(num)
```



### var (변수)

> ES6 이전에 사용하던 변수 선언 방식
>
> - 실제로 사용할 일은 절대 없지만, 예전 코드를 보기 위해 알아둔다.

- 재할당 및 재선언이 가능하다.
- 예기치 못한 상황을 발생시킬 수 있으므로 `절대 사용하지 않는다.`

```javascript
var x = 3
var x = 2
console.log(x)
```

- 함수 유효 범위를 가진다.

  ```javascript
  var x = 33
  let y = 11
  
  if ( x == 33 ) {
      var x == 2
      let y = 1
      console.log(x)
      console.log(y)
  }
  console.log(x)
  console.log(y)
  ```

### 정리

|              |    const    |     let     |      var       |
| :----------: | :---------: | :---------: | :------------: |
|  **재할당**  |      X      |      O      |       O        |
|  **재선언**  |      X      |      X      |       O        |
| **유효범위** | block scope | block scope | function scope |



## 3. Hoisting

> `var`로 선언된 변수가 선언 이전에 참조될 수 있는 현상 (끌어올리는 현상)

- hoisting은 우리가 활용하는 기술이 아니라 피해야 하는 상황이다.

  ```javascript
  console.log(name)
  
  var name = '홍길동'
  ```

- 위의 코드를 실행하면 다음과 같이 이해한다.

  ```javascript
  var name
  console.log(name)
  
  var name = '홍길동'
  ```

- let으로 작성했을 시

  ```javascript
  console log(name)
  
  let name = '홍길동'
  // const name = '홍길동'
  ```



***Copyright* © 2020 Song_Artish**

