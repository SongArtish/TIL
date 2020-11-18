# Lodash

2020.11.09

> 기능적 프로그래밍 패러다임을 사용하여 일반적인 프로그래밍 작업을위한 유틸리티 기능을 제공하는 JavaScript 라이브러리이다. Low Dash(`_`)를 사용하기 때문에 붙여진 이름이다.

---

[TOC]

---



## 시작하기

> `_.method`

- [Lodash 공식홈페이지](https://lodash.com/)에서 CDN을 가져온다. 

```html
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.20/lodash.min.js"></script>
```

- :white_check_mark: `node` 패키지를 사용할 때는 CDN 사용을 자제한다!!
- `node` 패키지 사용시에는 설치한다.

```bash
$ npm install lodash
```

- 그리고 다음과 같이 가져온다.

```javascript
// vue파일
import _ from 'lodash'
```



## 기초 문법

### 1. reverse

```javascript
console.log('-----------------1. reverse---------------')
//1. reverse - Vanilla O
// Vanilla
const array1 = [1, 2, 3, 4]
const reversedArray1 = array1.reverse()
console.log(reversedArray1)

// Lodash
const array2 = [1, 2, 3, 4]
const reversedArray2 = _.reverse(array2)
console.log(reversedArray2) // [4, 3, 2, 1]
```



### 2. sort

```javascript
console.log('-----------------2. sort---------------')
//2. sort - Weird Operation in Vanilla 
// Vanilla 
const numbers1 = [10, 1, 3, 7, 4]
// numbers1.sort()
// console.log(numbers1)
// [1, 10, 3, 4, 7]과 같이 문자열로 정렬한다.

numbers1.sort(function (num1, num2) {
    return num1 - num2
})
console.log(numbers1)

// Lodash
const numbers2 = [10, 1, 3, 7, 4]
const sortedNumbers2 = _.sortBy(numbers2)
console.log(sortedNumbers2)
```

- 기존에 Vanilla에 존재하는 `.sort()` 메서드를 사용하면, [1, 10, 3, 4, 7]`과 같이 숫자를 문자열로 인식해서 정렬한다.



### 3. range

```javascript
console.log('-----------------3-1. range---------------')
//3. range - Vanilla X
// Lodash
const nums1 = _.range(4)
const nums2 = _.range(1, 5)
const nums3 = _.range(1, 7, 2)

console.log(nums1) // [0, 1, 2, 3]
console.log(nums2) // [1, 2, 3, 4]
console.log(nums3) // [1, 3, 5]
```

- :white_check_mark: `range`는 `(a, b)`에서 b-1까지의 범위를 포함한다.



### 4. random	

```javascript
console.log('-----------------3-2. random---------------')
//3-2. random - Vanilla ?
const randomNum1 = _.random(0, 5)
const randomNum2 = _.random(5)
const randomNum3 = _.random(1.2, 5.2)

console.log(randomNum1)
console.log(randomNum2)
console.log(randomNum3)
```

- :white_check_mark: `random`은 `(a, b)`에서 b의 값까지 범위에 포함한다.



### 5. sampleSize

```javascript
console.log('-----------------3-3. sampleSize---------------')
//3-3. sampleSize - Vanilla ?
const result = _.sampleSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6)
console.log(result)

// 정렬까지
const sortedResult = _.sortBy(result)
console.log(sortedResult)
```



## 예시

```html
<div id="app">
    <h2>1. 점심 메뉴 추천</h2>
    <button @click="pickOneInLunchMenu">점심 메뉴 좀 추천해줘!</button>
    <p>오늘의 점심 메뉴는 {{ selectedLunchMenu }}</p>
    <hr>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.20/lodash.min.js"></script>
<script>
    const app = new Vue({
        el: "#app",
        data: {
            lunch: ['짬뽕', '짜장면', '탕수육'],
            selectedLunchMenu: "",
        },
        methods: {
            pickOneInLunchMenu: function () {
                const randomIndex = _.random(this.lunch.length - 1)
                this.selectedLunchMenu = this.lunch[randomIndex]
            }
        }
    })
</script>
```

```javascript
<div id="app">
    <h1>점심메뉴</h1>
<button @click="pickLunch">Pick One</button>
<p>{{ menu }}</p>
<hr>
    <h1>로또</h1>
<button @click="getNums">Get Lucky Numbers</button>
<p>{{ lotto }}</p>
</div>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.20/lodash.min.js"></script>
<script>
    const app = new Vue ({
        el: "#app",
        data: {
            menu: '',
            lunch: ["치킨", "스시", "차슈동", "차돌짬뽕", "오징징징어", "1일1깡 새우깡"],
            lotto: ''
        },
        methods: {
            pickLunch: function () {
                const randomIndex = _.random(this.lunch.length-1)
                this.menu = this.lunch[randomIndex]
            },
            getNums: function () {
                // this.lotto = _.sampleSize(_.range(1, 46), 6)

                // 배열 초기화
                this.lotto = []
                // lotto 배열이 6개가 될 때까지
                while (this.lotto.length < 6) {
                    const num = _.random(1, 45)
                    // 만약 1 ~ 45 중 무작위 하나가 lotto 배열에 없다면
                    if  (!this.lotto.includes(num)) {
                        // lotto에 push
                        this.lotto.push(num)
                    }
                }
            }
        }

    })

</script>
```



***Copyright* © 2020 Song_Artish**

