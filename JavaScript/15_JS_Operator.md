# JavaScript 연산자

---

[TOC]

---



## 할당 연산자

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



## 비교 연산자

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



## 동등 연산자 (`==`)

- 형변환 했을 때 같은 값이면 일치한다고 본다.

- JS는 자동으로 형변환을 해준다.

- :white_check_mark:단, 자동 형변환으로 인한 얘기치 못한 상황이 발생할 수 있으므로 동등연산자 사용은 지양한다.

  ```javascript
  const a = 1
  const b = '1'
  
  console.log(a == b)	 // true
  console.log(a == Number(b))
  ```



## 일치 연산자 (`===`)

- 동등 연산자보다 엄격한 비교를 한다.

  ```javascript
  const a = 1
  const b = '1'
  
  console.log(a === b)	// false
  ```



## 논리 연산자

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



## 삼항 연산자

- 가장 앞의 조건식이 참이면 `:`을 기준으로 작성한 앞의 값이 반환되고, 반대의 경우 `:`의 뒤의 값이 반환된다.

```javascript
true ? 1 : 2	// 1
false ? 1 : 2	// 2
```

```javascript
const result = 3.14 > 4 ? 'Yes' : 'No'
console.log(result)
```



## Spread 연산자

Spread Operator를 사용하면 배열, 문자열, 객체 등 반복 가능한 객체(iterable object)를 개별 요소로 분리할 수 있다. 연결, 복사 등의 용도로 활용도가 높다.

```javascript
let arr1 = [1, 2, 3]
let arr2 = [4, 5, 6]
let arr = [...arr1, ...arr2] // --> [1, 2, 3, 4, 5, 6]
```

### Array Concatenation

기존에는 두 개의 배열을 결합하는 데 `concat` 메서드를 사용했지만, spread 연산자를 이용하면 보다 깔끔하게 배열 병합이 가능하다.

```javascript
let arr1 = [1, 2]
let arr2 = [4, 5, 6]
let arr = [0, ...arr1, 3, ...arr2] // --> [0, 1, 2, 3, 4, 5, 6]
```

### Array Copy

JavaScript에서 기존 배열을 새로운 변수에 할당하는 경우, 새로운 배열은 기존 배열을 **참조**한다. Spread 연산자를 이용하면 배열을 복사할 수 있다.

```javascript
let arr = [1, 2, 3]
let arr1 = arr	// 기존 배열 arr를 참조함
let arr2 = [...arr]	// 기존 배열
```

### Function Parameter

함수를 호출할 때 함수의 parameter를 spread operator로 작성한 형태를 **Rest Parameter**라고 부른다. Rest 파라미터를 사용하면 함수의 파라미터로 오는 값들을 모아서 **배열**에 집어넣는다.

```javascript
let add(...rest) = () => {
    let sum = 0
    for (let el of rest) {
        sum += el
    }
    return sum
}
```

### Function Argument

함수를 호출(call)할 때 spread operator를 사용하여, 배열 형태에서 바로 함수 인자로 넣어줄 수 있다.

```javascript
var nums = [3, 5, 2, 3]
Math.min(...nums)	// --> 2
```

### Object Copy & Update

객체에서 spread 연산자를 이용하여 객체를 복사하거나 property를 업데이트(override)할 수 있다.

```javascript
var currentState = { name: '철수', species: 'human'};
currentState = { ...currentState, age: 10}; 

console.log(currentState)// {name: "철수", species: "human", age: 10}

currentState = { ...currentState, name: '영희', age: 11}; 
console.log(currentState); // {name: "영희", species: "human", age: 11}
```

### Destructuring

Spread 연산자는 배열/객체에서 destructuring에 사용될 수 있다.

```javascript
var a, b, rest;
[a, b] = [10, 20];

console.log(a); // 10
console.log(b); // 20

[a, b, ...rest] = [10, 20, 30, 40, 50];

console.log(rest); // [30,40,50]

({a, b, ...rest} = {a: 10, b: 20, c: 30, d: 40});
console.log(a); // 10
console.log(b); // 20
console.log(rest); // {c: 30, d: 40}
```



***Copyright* © 2022 Song_Artish**
