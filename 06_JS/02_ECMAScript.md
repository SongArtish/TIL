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

#### 사용법

```javascript
const numbers = [1, 2, 3, 4]

numbers[0]
numbers[3]
// numbers[-1]
numbers.length
```

- 단, `-1` 인덱스는 사용할 수 없다. 양의 정수 인덱스만 사용할 수 있다.

#### 자주 사용하는 메서드

- `push` && `pop`

  ```javascript
  numbers.push('5') // 5 새로운 배열의 길이
  
  numbers.pop() // '5' 가장 마지막 요소
  ```

- `reverse` : 배열을 반대로 정렬

  ```javascript
  numbers.reverse() // [4, 1, 2, 1]
  ```

- `unshift` && `shift`

  - `unshift` : 배열의 앞에 추가

  ```javascript
  numbers.unshift('a')	// 5 새로운 배열의 길이
  numbers	// ['a' , 1, 2, 3, 4]
  ```

  - `shift` : 배열의 첫 요소를 제거

  ```javascript
  numbers.shift()	// 'a' 가장 처음 요소
  numbers
  ```

- `include` : `true` or `false`로 boolean 값을 반환

  ```javascript
  numbers.includes(1)
  ```

- `indexOf` : 배열의 특정 요소가 있는지 확인하고, 있으면 가장 첫번째로 찾은 요소의 index를 반환 (없으면 -1 반환)

  ```javascript
  numbers.indexOf(1)	// 0 번째 index 반환
  numbers.indexOf(0)	// 없으므로 -1 반환
  ```

- `join` : 문자열로 반환

  ```javascript
  numbers.join()	// "1,2,3,4"
  numbers.join('')	// "1234"
  numbers.join('-') // "1-2-3-4""
  ```



### 5.2 Object

#### 사용법

- key 값은 문자열 형태로 작성, value는 모든 형태가 작성 될 수 있다.

```javascript
const person = {
    name : '홍길동',
    'phone number' : '010-1234-1234',
    pocket : {
        phone : 'galaxy note 9',
        earphone : 'buzz live',
        'note book' : 'MacBook'
    }
}
```

- key 값에 공백이 있는 경우에는 `'phone number'`와 같이 문자열인 것을 표시해주어야한다.

#### 요소 접근

- dot notation

```javascript
person.name	// '홍길동'
person['name']	// '홍길동'
person['phone number']
person.pocket.phone
person['pocket'].phone
```



#### Object 축약 문법

- 객체를 정의할 때, key 값과 할당하는 변수의 이름이 같으면 축약이 가능하다.

```javascript
const books = ['python', 'JS']

const professor = {
    ggu : ['django', 'JS'],
    json : ['python']
}

const anything = null

const hphk = {
    /* 'books' : books,
    'professor' : professor,
    'anything' : anything, */
    books,
    professor,
    anything,
}

console.log(hphk)
```



```javascript
const userInformation = {
    name : 'kim',
    userId : 'ggu'
}
```

- ESS 이전

```java
const name = userInformation.name
const userId = userInformation.userId
```

- ES6+ 이후

```javascript
const { name } = userInformation
const { userId } = userInformation
```



```javascript
function getUserInfo (userInformation) {
    console.log(`userName = ${userInformation.name}`)
}

getUserInfo(userInformation)

function getUserInfo({ name }) {
    console.log(`username = ${name}`)
}
```



### 5.3 JSON 

> JavaScript Object Notation

- key -> value 처럼 생겼는데 실제로는 문자열
- Object처럼 쓰려면 Parsing 작업이 필요하다.



#### Object -> JSON(string)

```javascript
const jsonData = JSON.stringify({
    tea: '국화차',
    coffee: '아메리카노',
})

console.log(jsonData)	// {"tea":"국화차","coffee":"아메리카노"}
console.log(typeof jsonData)	// string
```



#### JSON(string) -> Object(parsing)

```javascript
const parseData = JSON.parse(jsonData)

console.log(parseData)	// {tea: "국화차", coffee: "아메리카노"}
console.log(typeof parseData)	// objects
```



### 5.4 Array Helper Method

> helper라는 일종의 라이브러리로 배열을 조작한다.

#### forEach :star:

- 주어진 `callBack`을 배열에 있는 각 요소를 오름차순으로 한번씩 실행한다.
  - `callBack` : 어떠한 사건이 일어났을 때 실행되는 함수
- :white_check_mark: return 값이 없다!

```javascript
arr.forEach(callback(element, index, array))
```

- 예시

```javascript
const colors = ['red', 'blue', 'white']

colors.forEach(function (color) {
    console.log(color)
})

// Arrow Functionf
colors.forEach(color => console.log(color))
```

- `forEach`는 return 값이 없다.

```javascript
const result = colors.forEach(color => console.log(color))
console.log(result)
```

- 실습1

```javascript
// 1. images 배열 안에 있는 정보 (height, width)를 곱해 넓이를 구하여 areas 배열에 저장하세요.
const images = [
    { height: 10, width: 30 },
    { height: 20, width: 90 },
    { height: 54, width: 32 }
]

const areas = []
images.forEach(image => areas.push(image.height * image.width))

console.log(areas)
```

- 실습2

```javascript
function handlePostsforEach() {
    const posts = [
        { id: 23, title: 'Daily JS News' },
        { id: 52, title: 'Code Refactor City' },
        { id: 105, title: 'The Brightest Ruby' }
    ]

    posts.forEach(post => console.log(post, post.id, post.title))
}

handlePostsforEach()
```



#### map

- 배열의 모든 요소에 대해 `callback`을 실행한다. 함수의 반환값을 요소로 하는 새로운 배열을 **반환**
  - :white_check_mark: return 값이 있다!
- 배열을 내가 원하는 다른 형식으로 바꿔야 할 때 쓴다.

```javascript
arr.map(callback(element, index, array))
```

- 예시

```javascript
const numbers = [1, 2, 3]

const mapNumbers = numbers.map(function (number) {
    return number * 2
})
console.log(mapNumbers)
```

- 실습1

```javascript
// 1. 숫자가 담긴 배열로 각 숫자들의 제곱근이 들어있는 새로운 배열을 만드세요.
const newNumbers = [4, 9, 16]

const sqrtNumbers = newNumbers.map(Math.sqrt)
console.log(sqrtNumbers)
```

- Math라는 라이브러리에서 `sqrt`를 가져온다.
- 실습2

```javascript
// 2. images의 요소들의 height 값만 저장되어 있는 배열 heights 를 만드세요.
const images = [
    { height: '34px', width: '39px' },
    { height: '54px', width: '19px' },
    { height: '83px', width: '75px' },
]

// answer
const heights = images.map(image => image.height)
console.log(heights)
```



#### filter

- `callback` 함수를 실행했을 때, 어떠한 테스트 혹은 <u>조건을 만족하는</u> 모든 요소를 모아서 <u>새로운 배열을 반환</u>한다.

```javascript
arr.filter(callback(element, index, array))
```

- 예시

```javascript
const products = [
    { name: 'cucumber', type: 'vegetable' },
    { name: 'banana', type: 'fruit' },
    { name: 'carrot', type: 'vegetable' },
    { name: 'apple', type: 'fruit' },
]

const fruits = products.filter(function (product) {
    return product.type === 'fruit'
})

console.log(fruits.name)
```

- 실습1

```javascript
// 1. numbers 배열 중 50보다 큰 값들만 모은 배열 filteredNumbers 을 만드세요.
const numbers = [15, 25, 35, 45, 55, 65, 75, 85, 95]

// answer
const filteredNumbers = numbers.filter(number => nuber > 50)

// const filteredNumbers = numbers.filter(function (number) {
//   return number >= 50
// })

console.log(filteredNumbers)
```

- 실습2

```javascript
// 2. users 배열에서 admin 레벨이 true인 user만 가진 filteredUsers 배열을 만드세요.
const users = [
    { id: 1, admin: false, name: 'eric' },
    { id: 2, admin: false, name: 'harry' },
    { id: 3, admin: true, name: 'john' },
    { id: 4, admin: false, name: 'jason' },
    { id: 5, admin: true, name: 'juan' },
]

// answer
const filteredUsers = users.filter(function (user) {
    return user.admin === true
})

console.log(filteredUsers)
```



#### reduce

- 배열 내의 숫자 총합, 평균 계산을 하나의 값으로 줄이는 동작

```javascript
arr.reduce(callback(acc, element, index.array), initialValue)
```

- `acc` : 누적 값
- `initialValue` : 초기 값

- 예시

```javascript
const tests = [90, 90, 80, 77]

const sum = tests.reduce(function (total, x) {
    return total + x
}, 0)  // 여기서 0 생략 가능

console.log(sum)
```

```javascript
// refactoring
const sum = tests.reduce((total, x) => total + x, 0)

// 평균
const sum = tests.reduce((total, x) => total + x, 0) / tests.length
```

- 실습

```javascript
    // 1. 배열에 담긴 중복된 이름을 {'이름': 수} 형태의 object로 반환하세요.
    const names = ['harry', 'jason', 'tak', 'tak', 'justin']

    // answer
    const countName = names.reduce(function (acc, name) {
      if ( name in acc ) {
        acc[name] ++  // acc를 object로 만든다.
      } else {
        acc[name] = 1 
      }
      return acc
    }, {})

    console.log(countName)
```

- :white_check_mark:`return`을 빼먹지 않도록 주의한다!



#### find

- `callback`을 만족하는 `첫번째 요소`를 찾아서 반환하며, 없으면 `undefined`를 반환한다.

```javascript
arr.find(callback(element, index, array))
```

- 예시

```javascript
const avengers = [
    { name: 'Tony Stark', age: 45 },
    { name: 'Steve Rogers', age: 32 },
    { name: 'Thor', age: 40 },
]

const avenger = avengers.find(function (avenger) {
    return avenger.name === 'Tony Stark'
})

// refactoring
const avenger = avengers.find(avenger => avenger.name === 'Tony Stark')


console.log(avenger)
```

- 실습

```javascript
// 1. people에서 admin 권한을 가진 요소를 찾으세요.
const people = [
    { id: 1, admin: false },
    { id: 2, admin: false },
    { id: 3, admin: true },
]

// answer
const person = people.find(function (person) {
    return person.admin === true
})

console.log(person)

// refactoring
const person = people.find(person => person.admin === true)

console.log(person)
```



#### some

> 배열 안의 요소 중 <u>단 하나라도</u> 조건을 만족한다면 true를 반환하면, 아니면 false를 반환한다.

```javascript
arr.some(callback(element, index, arr))
```

- 예시

```javascript
const arr = [1, 2, 3, 4, 5]

const result = arr.some(elem => elem % 2 === 0)  // true
console.log(result)
```

- 실습

```javascript
// 1. requests 배열에서 status가 pending인 요청이 있는지 확인하세요.
const requests = [
    { url: '/photos', status: 'complete' },
    { url: '/albums', status: 'pending' },
    { url: '/users', status: 'failed' },
]

// answer
const result = requests.some(element => element.status === 'pending')

console.log(result)
```



#### every

> 배열 안의 요소가 <u>모두</u> 조건을 만족해야 true를 반환하며, 아니면 false를 반환한다.

```javascript
arr.every(callback(element, index, arr))
```

- 예시

```javascript
const arr = [1, 2, 3, 4, 5]

const result2 = arr.every(elem => elem % 2 === 0)  // false
```

- 실습

```javascript
// 1. users 배열에서 모두가 submmited 인지 여부를 hasSubmitted 에 저장하세요.
const users = [
    { id: 21, submitted: true },
    { id: 33, submitted: false },
    { id: 712, submitted: true},
]

// answer
const hasSubmitted = users.every(element => element.submitted === true)
console.log(hasSubmitted)
```



***Copyright* © 2020 Song_Artish**

