# ECMAScript

2020.10.13

> 자바스크립트 표준화를 위해 만들어졌으며, 액션스크립트나 J스크립트 등 다른 구현체도 포함하고 있다.

---

[TOC]

---



## 1.  변수와 식별자

---

### 1.1 식별자

> 변수명은 식별자라고 하며 특정 규칙을 따른다.

- 반드시 문자, 달러, _로 시작해야 한다. 숫자로 시작할 수 없다. (`-`도 안된다.)
- 대소문자를 구분한다. 클래스명이 아니라면 시작 단어는 대문자 사용을 지양한다.
- 예약어도 사용 불가능한다. (class, const, let, var, await, case ...)

#### 식별자 작성 스타일

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



### 1.2 변수

#### let (변수)

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



#### const (상수)

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
foor.bar = 4
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



#### var (변수)

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

#### 정리

|              |    const    |     let     |      var       |
| :----------: | :---------: | :---------: | :------------: |
|  **재할당**  |      X      |      O      |       O        |
|  **재선언**  |      X      |      X      |       O        |
| **유효범위** | block scope | block scope | function scope |



### 1.3 Hoisting

> `var`로 선언된 변수가 선언 이전에 참조될 수 있는 현상

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



## 2. 타입과 연산자

---

### 2.1  Primitive (원시값, 원시 자료형) 타입

#### Number

```javascript
const a = 1
const b = -13
const c = 3.14
const d = 2.99e3
const e = Infinity
const f = -Infinity
const g = NaN

console.log(a, b, c, d, e, f, g)
```



#### String

```javascript
const sentence1 = '문자열'
const sentence2 = "문자열"

console.log(sentence1)
console.log(sentence2)
```

- 문자열 간의 덧셈이 가능하다

```javascript
const firstName = '구현'
const lastName = '김'

const fullName = firstName + lastName

console.log(fullName)
```

**escape sequence**

```javascript
const hello = "안녕 \n 하세요"

console.log(hello)
```



**Template Literal**

> ``(backtick)에 넣어준다.

```javascript
const name = '홍길동'

const sayHello = `${name}이 인사합니다.`
console.log(sayHello)
```

- escape sequence를 <u>사용 할 수 없다</u>.

```javascript
const nextSentence = `안녕
하세요`

console.log(nextSentence)
```



#### Boolean

```javascript
true
false
```



#### Empyty Value

- 값이 존재하지 않음을 나타내는 방식은 2가지가 있다.

- `undefined` - 값을 할당하지 않았을 때 JS가 자동으로 할당해주는 값

  ```javascript
  let name
  console.log(name)
  ```

- `null` = 값이 없음을 나타내기 위해 사용한다.

  ```javascript
  let name = null
  consol.log(name)
  ```

```javascript
typeof null
"objects"

typeof undefined
"undefined"
```



### 2.2 연산자

#### 할당 연산자

> 연산과 동시에 변수에 어떠한 값을 할당하는 연산자

```javascript
let c = 10

c += 10
console.log(c)

c -= 10
console.log(c)

c *- 10
console.log(c)

c /= 10
console.log(c)

c++
console.log(c) // 증강식 : 1을 더해주는 역할

c--
console.log(c) // 증감식 : 1을 빼주는 역할
```



#### 비교 연산자

> 두 값을 비교하기 위해 사용하며, `true` or `false`를 반환한다.

```javascript
2 < 3	// true
2 > 3	// false
```

- 문자열도 비교가 가능하다. 영어 소문자가 대문자보다 큰 값을 가진다.
- 알파벳은 오름차순으로 비교한다.

```javascript
'A' < 'a'
```



#### 동등 연산자 (`==`)

- 형변환 했을 때 같은 값이면 일치한다고 본다.

- JS는 자동으로 형변환을 해준다.

- :white_check_mark:단, 자동 형변환으로 인한 얘기치 못한 상황이 발생할 수 있으므로 동등연산자 사용은 지양한다.

  ```javascript
  const a = 1
  const b = '1'
  
  console.log(a == b)	 // true
  console.log(a == Number(b))
  ```



#### 일치 연산자 (`===`)

- 동등 연산자보다 엄격한 비교를 한다.

  ```javascript
  const a = 1
  const b = '1'
  
  console.log(a === b)	// false
  ```



#### 논리 연산자

- `and` &&

  ```javascript
  true && true	// true
  true && false	// false
  
  0 && 0	// 0
  1 && 0	// 0
  4 && 7	// 7
  ```

- `or` ||

  ```javascript
  true || false	// true
  false || true	// true
  
  1 || 0	// 1
  4 || 7	// 4
  ```

- `not` !

  ```javascript
  !true || false	// false
  ```



#### 삼항 연산자

- 가장 앞의 조건식이 참이면 `:`을 기준으로 작성한 앞의 값이 반환되고, 반대의 경우 `:`의 뒤의 값이 반환된다.

```javascript
true ? 1 : 2	// 1
false ? 1 : 2	// 2
```

```javascript
const result = 3.14 > 4 ? 'Yes' : 'No'
console.log(result)
```



## 3. 조건문과 반복문

---

### 3.1 조건문

`if`, `else if`, `else`

- if

```javascript
const name = 'kim'

if ( name === 'kim' ) {
    console.log('True')
}
```

- else if

```javascript
const name = 'kim'

if ( name === 'lee' ) {
    console.log('LEE')
} else if ( name === 'kim' ) {
    console.log('KIM')
} else {
    console.log(`${name}`)
}
```

- 위와 같이 ``${name}``으로 template iterary를 사용할 수도 있다.



#### switch

- 하나의 변수의 값에 따라 <u>분기</u>를 하는 조건문이다.

- Default 값을 넣을 수 있다!

  ```javascript
  const name = '홍길동'
  
  switch (name) {
      case 'admin' : {
          console.log('ADMIN')
      }
      case 'manager' : {
          console.log('MANAGER')
      }
      default : {
      	console.log(`${name}`)        
      }
  }
  ```

- `case`에 해당하는 값이 있다면, 그 내용을 실행하고 그 다음도 실행하면서 default에 정의한 내용도 함께 실행된다.

- `break`와 함께 사용한다.

  ```javascript
  const name = 'admin'
  
  switch (name) {
      case 'admin' : {
          console.log('ADMIN')
          break
      }
      case 'manager' : {
          console.log('MANAGER')
          break
      }
      default : {
      	console.log(`${name}`)        
      }
  }
  ```



### 3.2 반복문

#### while

> `while` 키워드 뒤에 오는 조건이 true인 동안 반복한다.

```javascript
let i = 0

while ( i < 6) {
    console.log(i)
    i++
}
```

#### for

```javascript
for (let i = 0; i < 6; i++ ) {
    console.log(i)
}
```

#### for of

- 배열에서 요소를 하나씩 순회하며 반복하는 반복문이다.

- 블럭 내에서 변수로 선언되기 때문이다.

  ```javascript
  const numbers = [1, 2, 3, 4]
  
  for (const number of numbers) [
      console.log(number)
  ]
  // 1, 2, 3, 4
  ```

#### for in

- object의 key값을 순회하는 반복문이다.

- 배열의 경우 **index 값**을 순회한다.

  ```javascript
  const numbers = [1, 2, 3, 4]
  
  for (const number in numbers) [
      console.log(number)
  ]
  // 0, 1, 2, 3
  
  const fruits = {
      a : 'apple',
      b : 'banana'
  }
  
  for (const key in fruits) {
      console.log(key)
      console.log(fruits[key])
  }
  ```

  - index 값을 순회하기 때문에 index 값이 나온다.



## 4. Functions

### 4.1 functions

#### 선언식

```javascript
function add (num1, num2) {
    return num1 + num2
}
add(1, 3)
```

#### 표현식

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

#### 기본인자

- 다음과 같이 인자의 default 값을 넘겨줄 수 있다.

```javascript
const greeting = function (name = '홍길동') {
    return name
}
```



### 4.2 선언식 vs 표현식

```javascript
console.log(typeof add)
console.log(typeof sub)
// add와 sub는 위에서 정의된 함수이다.
```

#### Hoisting

- 선언식에는 hoisting이 일어난다.

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



### 4.3 Arrow Function (`=>`)

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



## 5. Data Structure

### 5.1 Array





***Copyright* © 2020 Song_Artish**