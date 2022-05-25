# JavaScript 다양한 메서드

---

[TOC]

---





## Array Helper Method :star:

> helper라는 일종의 라이브러리로 배열을 조작한다.

### forEach :star:

- 주어진 `callBack`을 배열에 있는 각 요소를 오름차순으로 한번씩 실행한다.
  - `callBack` : 어떠한 사건이 일어났을 때 실행되는 함수
- :white_check_mark: return 값이 없다!

```javascript
arr.forEach(callback(element, index, array))
```

예시

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



### map

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



### filter

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



### reduce

- 배열 내의 숫자를 총합, 평균 등의 하나의 값으로 줄이는 동작

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



### find

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



### some

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



### every

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



### sort

> 배열의 요소를 적절한 위치에 정렬한 후 그 배열을 반환한다.

```javascript
// 예시
const months = ['March', 'Jan', 'Feb', 'Dec'];
months.sort();
console.log(months);
// expected output: Array ["Dec", "Feb", "Jan", "March"]

const array1 = [1, 30, 4, 21, 100000];
array1.sort();
console.log(array1);
// expected output: Array [1, 100000, 21, 30, 4]
```



## Array

### 배열인지 확인하기

```javascript
Array.isArray(arr)
```

`arr`가 배열인 경우 `true`를, 배열이 아닌 데이터 타입인 경우 `false`를 반환한다.

```javascript
const arr = [];
const str ="";
const obj= {};

console.log(Array.isArray(arr)) // --> true
console.log(Array.isArray(str)) // --> false
console.log(Array.isArray(obj)) // --> false
```



### 빈 배열 체크하기

```javascript
arr.length === 0
```

`arr === null`이 아닌, 길어가 0인지를 확인하여 빈 배열을 체크해준다.
더욱 정확하게 확인하기 위해서는 아래와 같이 활용할 수 있다.

```javascript
// arr가 배열이고, arr의 길이가 0인 경우
if (Array.isArray(arr) && arr.length === 0) {
    ...
}
```



### 배열 자르기

```javascript
arr.splice(start, (deleteCount))
```

`deleteCount`를 입력하지 않으면 start부터의 모든 요소를 제거하게 된다.

```
arr1 = [1, 2, 3, 4]

console.log(arr1.splice(1)) // --> [2, 3, 4]
console.log(arr1) // --> [1]

arr2 = [5, 6, 7, 8]
console.log(arr2.splice(1, 2)) // --> [6, 7]
console.log(arr2) // --> [5, 8]
```





## String

### 문자열을 숫자로 변환하기

```javascript
Number(str)
```

숫자가 아닌 문자나 undefined 등을 인자로 전달하면 `NaN(Not A Number)`를 리턴한다.

```javascript
const integer = Number('512')
const float = Number('5.12')
const str = Number('five')
const und = Number(undefined)

console.log(integer + '의 타입은 ' +  typeof integer) // --> 512의 타입은 number
console.log(float + '의 타입은 ' +  typeof float) // --> 5.12의 타입은 numbe
console.log(str + '의 타입은 ' +  typeof str) // --> NaN의 타입은 number
console.log(und + '의 타입은 ' +  typeof und) // --> NaN의 타입은 number
```





---



문자열 자르기



***Copyright* © 2022 Song_Artish**
