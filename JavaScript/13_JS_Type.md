# JavaScript 타입과 연산자

---

[TOC]

---



## Primitive 타입

원시값, 원시 자료형 타입

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



## 연산자

### 할당 연산자

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



### 비교 연산자

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



### 동등 연산자 (`==`)

- 형변환 했을 때 같은 값이면 일치한다고 본다.

- JS는 자동으로 형변환을 해준다.

- :white_check_mark:단, 자동 형변환으로 인한 얘기치 못한 상황이 발생할 수 있으므로 동등연산자 사용은 지양한다.

  ```javascript
  const a = 1
  const b = '1'
  
  console.log(a == b)	 // true
  console.log(a == Number(b))
  ```



### 일치 연산자 (`===`)

- 동등 연산자보다 엄격한 비교를 한다.

  ```javascript
  const a = 1
  const b = '1'
  
  console.log(a === b)	// false
  ```



### 논리 연산자

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



### 삼항 연산자

- 가장 앞의 조건식이 참이면 `:`을 기준으로 작성한 앞의 값이 반환되고, 반대의 경우 `:`의 뒤의 값이 반환된다.

```javascript
true ? 1 : 2	// 1
false ? 1 : 2	// 2
```

```javascript
const result = 3.14 > 4 ? 'Yes' : 'No'
console.log(result)
```



***Copyright* © 2020 Song_Artish**
