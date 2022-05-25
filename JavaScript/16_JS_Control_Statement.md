# JavaScript 조건문과 반복문

---

[TOC]

---



## 조건문

### if, else if, else

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



### switch

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



## 반복문

### while

> `while` 키워드 뒤에 오는 조건이 true인 동안 반복한다.

```javascript
let i = 0

while ( i < 6) {
    console.log(i)
    i++
}
```

### for

```javascript
for (let i = 0; i < 6; i++ ) {
    console.log(i)
}
```

### for of

- 배열에서 요소를 하나씩 순회하며 반복하는 반복문이다.

- 블럭 내에서 변수로 선언되기 때문이다.

  ```javascript
  const numbers = [1, 2, 3, 4]
  
  for (const number of numbers) [
      console.log(number)
  ]
  // 1, 2, 3, 4
  ```

### for in

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



***Copyright* © 2020 Song_Artish**
