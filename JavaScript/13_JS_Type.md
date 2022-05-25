# JavaScript 타입

---

[TOC]

---



## 기본 타입

원시 타입(Primitive Type), 원시값, 원시 자료형 타입이라고도 한다.

### Number

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

- `NaN` (Not a Number)은 연산 과정에서 잘못된 입력을 받았음을 나타내는 기호이다.



### String

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

- escape sequence를 <u>사용 할 수 없다</u>. (?)
  - 실제로 Chrome console창에 사용해보면 되는데?

```javascript
const nextSentence = `안녕
하세요`

console.log(nextSentence)
```



### Boolean

```javascript
true
false
```



### Empyty Value

> 값이 존재하지 않음을 나타내는 방식은 2가지가 있다.

**`undefined`**

- 값을 할당하지 않았을 때 JS가 자동으로 할당해주는 값

```javascript
let name
console.log(name)
```

**`null`**

- 값이 없음을 나타내기 위해 사용한다.

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



## 참조 타입

### Array

```javascript
const numbers = [1, 2, 3, 4]

numbers[0]
numbers[3]
// numbers[-1]
numbers.length
```

- 단, `-1` 인덱스는 사용할 수 없다. 양의 정수 인덱스만 사용할 수 있다.

**자주 사용하는 메서드**

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



### Object

key 값은 문자열 형태로 작성, value는 모든 형태가 작성 될 수 있다.

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

**요소 접근**

- dot notation

```javascript
person.name	// '홍길동'
person['name']	// '홍길동'
person['phone number']
person.pocket.phone
person['pocket'].phone
```

**Object 축약 문법**

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



### Function

JavaScript 함수에 대해서는 별도 TIL에서 다룬다.



***Copyright* © 2020 Song_Artish**
