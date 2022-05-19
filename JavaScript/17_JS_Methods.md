# JavaScript 다양한 메서드

---

[TOC]

---



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

## 전개 구문, 스프레드 연산자

```javascript
function sum(x, y, z) {
  return x + y + z;
}

const numbers = [1, 2, 3];

console.log(sum(...numbers));
// expected output: 6

console.log(sum.apply(null, numbers));
// expected output: 6

```



문자열 자르기



***Copyright* © 2020 Song_Artish**
