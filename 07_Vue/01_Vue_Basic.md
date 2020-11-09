# Vue 기초

2020.11.09

> 자바스크립트 프레임워크에는 대표적으로 `React`, `Angular`, `Vue` 가 있으며, `Vue.js`는 UI를 만들기 위한 progressive framework이다. `Vue.js`를 통해 동적으로 DOM을 조작할 수 있다.

---

[TOC]

---



## 개념

> Vue.js는 특징으로는 CSR (Client Side Rendering), SPA (Single Page Application) 등이 있으며, `Vue.js`의 작성 순서는 다음과 같다.
>
> ```markdown
> 1. Data
> 2. DOM
> ```



**MVVM 패턴**

> Vue.js는 `Model`, `View`, `ViewModel`의 MVVM 패턴을 가진다.
>
> - **Model** : `자바스크립트 Object`
> - **View** - `DOM(HTML)`
> - **ViewModel** - `모든 Vue Instance`



## 시작하기

**설치하기**

- Chrome 웹 스토어 tool 설치

  ```markdown
  - Vue.js devtools
  ```

  > 해당 페이지가 Vue로 작성되었다면 Vue로 어떻게 구성되었는지 보여준다.
>
  > - :heavy_check_mark: `HTML`을 로드하였을 때 확장 프로그램이 실행되지 않는다면 `확장 프로그램 > 세부정보 > 파일 URL에 대한 액세스 허용`을 활성화해준다!

- VSCode extension

  ```markdown
  - Vetur
  ```

  > `Vue.js`의 자동 완성 등을 담당한다.

**시작하기**

> [Vue.js 공식문서](https://kr.vuejs.org/v2/guide/index.html)

- Chrome 개발자도구(`F12`)의 `Vue` 탭에서 해당 페이지의 구성을 확인할 수 있다.

- CDN을 공식문서에서 가져온다.

```html
<!-- 개발버전, 도움되는 콘솔 경고를 포함. -->
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

```html
<!-- 상용버전, 속도와 용량이 최적화됨. -->
<script src="https://cdn.jsdelivr.net/npm/vue"></script>
```



## 기초 문법

### 1. 객체 생성

- `new Vue`로 객체를 생성하고 `el`라는 속성에 아이디 값(`#-`)을 입력한다.

```javascript
const app = new Vue({
      el: "#app",
    })
```

- 예시 : HTML
  - :heavy_check_mark: `#app` + `Enter`를 누르면 id가 app인 `<div>` 태그를 생성할 수 있다.

```html
<div id="app"></div>
<div id="app2"></div>
```

- 예시 : JS 객체 생성

```javascript
// 1. 인스턴스 생성 (다소 비효율적인 방식)
vueInstanceObject = {
    // el(element)은 vue 인스턴스의 속성
    el: "#app",
}
const app = new Vue(vueInstanceObject)

console.log(app)
console.log(app.$el)	// app.$el => div#app
// `$`로 `Vue.js`에서 인스턴스 속성을 가져올 수 있다.
```

- 실제적으로는 아래와 같은 방법으로 객체를 생성한다.

```javascript
// 2. 인스턴스 생성
const app2 = new Vue({
    el: "#app2",
})
```



### 2. Data Binding

- 아래와 같이 데이터들을 묶어줄 수 있다.

```javascript
const app = new Vue({
    el : "#app",
    data : {
        message1: "Hello, World!",
        message2: "Hello, Vue.js!",
        todoList: [
            {id: 1, content: "todo1", completed: true},
            {id: 2, content: "todo2", completed: true},
            {id: 3, content: "todo3", completed: false},
            {id: 4, content: "todo4", completed: 'pending'},
        ]
    }
})
```



### 3. 반복문

> `v-for=""`

- `todoList`에서 각각 `todo`를 가져와서 `content` 만 표시해준다.

```html
<ul v-for="todo in todoList">
    <li>{{ todo.content }}</li>
</ul>
```



### 4. 조건문

> `v-if=""`, `v-else-if=""`, `v-else`

```html
<ul v-for="todo in todoList">
    <li v-if="todo.completed === true">
        완료: {{ todo.content }}
    </li>
    <li v-else-if="todo.completed === 'pending'">
        진행중 : {{ todo.content }}
    </li>
    <li v-else>
        미완료: {{ todo.content }}
    </li>
</ul>
```



### 5. v-bind

>`v-bind:`
>
>`v-bind`로 **HTML 표준속성** 혹은 **클래스**를 binding할 수 있다.
>
>:ballot_box_with_check: shortcut : **`:`**

**HTML 표준속성 binding**

```html
<div id="app">
    <span v-bind:title="myMessage">{{ myMessage }}</span>
    <hr>
    <a v-bind:href="myUrl" target="_blank">Go to Google!</a>
    <hr>
    <img v-bind:src="myImage" alt="">
</div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
    const app = new Vue({
        el: "#app",
        data: {
            myMessage: 'HTML의 title 속성으로 볼 수 있습니다.',
            myUrl: "https://google.com",
            myImage: "https://picsum.photos/200/300",
        }
    })
</script>
```

- `v-bind:`는 `:`으로 shortcut을 제공한다.

```html
<div id="app">
    <!-- shortcut 제공 (v-bind -> :) -->
    <span :title="myMessage">{{ myMessage }}</span>
    <hr>
    <a :href="myUrl" target="_blank">Go to Google!</a>
    <hr>
    <img :src="myImage" alt="">
</div>
```



**Class Binding**

- todo가 isCompleted 될 때, complete 속성을 활성화한다.

```html
<ul>
    <li v-for="todo in todos" :class="{ complete: todo.isCompleted }">
        {{ todo.title }}
    </li>
</ul>
```

- 여러개의 class도 vue에서 적용할 수 있다.

```html
<h2 :class="[isCompleted, isBackground]">
    Hello Vue.js
</h2>
```

```javascript
const app = new Vue({
    el: "#app",
    data: {
        myMessage: 'HTML의 title 속성으로 볼 수 있습니다.',
        myUrl: "https://google.com",
        myImage: "https://picsum.photos/200/300",
        todos: [
            {id: 1, title: 'todo1', isCompleted: true},
            {id: 2, title: 'todo2', isCompleted: false},
        ],
        isCompleted: 'complete',
        isBackground: 'my-background-color'
    }
})
```



### 6. v-on 메서드

> `v-on:`
>
> `v-on` 메서드는 JS의 eventListener와 같은 역할을 한다.

```html
<div id="app">
    <button v-on:click="alertMessage">Click!</button>
    <hr>
    <h2>{{ counter }}</h2>
    <button v-on:click="addOne">Click!</button>
    <hr>
    <input type="text" @keyup.enter="onInputChange">
</div>
```

```javascript
const app = new Vue({
    el: "#app",
    data: {
        message: "Hello Vue.js",
        counter: 0,
    },
    methods: {
        alertMessage: function () {
            alert('Hello Vue.js')
        },
        addOne: function () {
            // this로 counter 값에 접근할 수 있다.
            this.counter += 1
        },
        onInputChange: function () {
            console.log('enter!')
        }
    }
})
```



### 7. v-model

> `v-model`은 속성과 데이터를 **양방향**으로 변경시킨다.

```html
  <div id="app">
    <h2>1. Input -> Data</h2>
    <h3>{{ myMessage }}</h3>
    <input type="text" @keyup="onInputChange">

    <h2>1-2. Input <-> Data</h2>
    <h3>{{ myMessage2 }}</h3>
    <input type="text" @keyup="onInputChange2" :value="myMessage2">

    <h2>2. Input <-> Data</h2>
    <h3>{{ myMessage3 }}</h3>
    <!-- 다음과 같이 사용하면 양방향!!-->
    <input type="text" v-model="myMessage3">
    
    <h2>3. Checkbox</h2>
  </div>
```

```javascript
const app = new Vue({
    el: "#app",
    data: {
        myMessage: '',
        myMessage2: '',
        myMessage3: '',
        checked: true,
    },
    methods: {
        onInputChange: function () {
            // 자동으로 생성되는 event 안에 입력 값
            this.myMessage = event.target.value
        },
        onInputChange2: function () {
            this.myMessage2 = event.target.value
        }
    }
})
```



### 8. v-text, v-html

> `v-text`는 텍스트 그대로 렌더링하는 반면, `v-html`은 태그를 렌더링한다.
>
> :white_check_mark: ​단, `v-html`은 주의해서 사용한다!

- :heavy_check_mark: `ul>li*3` + `Enter`로 `<li>` 태그가 3개 포함된 `<ul>` 태그를 생성할 수 있다.

```html
<div id="app">
    <!-- ul>li*3 -->
    <ul>
        <li v-text="myMessage"></li>
        <li v-html="myMessage"></li>
        <li>{{ myMessage }}</li>
    </ul>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
    const app = new Vue({
        el: "#app",
        data: {
            myMessage: '<li>Hello Vue.js</li>',
        }
    })
</script>
```



### 9. v-show

> `v-if`는 조건에 맞지 않으면 렌더링을 하지 않는 반면, `v-show`는 렌더링은 하고 표시를 하지 않는다.
>
> |              | 렌더링 비용 | 토글 비용 |
> | :----------: | :---------: | :-------: |
> |  **v - if**  |    낮음     |   높음    |
> | **v - show** |    높음     |   낮음    |

```html
<div id="app">
    <h2>1. v-if</h2>
    <p v-if="isTrue">
        v-if - true
    </p>
    <p v-if="isFase">
        v-if - false
    </p>
    <hr>

    <h2>2. v-show</h2>
    <p v-show="isTrue">
        v-show - true
    </p>
    <p v-show="isFalse">
        v-show - flase
    </p>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
    const app = new Vue({
        el: "#app",
        data: {
            isTrue: true,
            isFalse: false,
        }
    })
</script>
```



### 10. filters

> Vue 객체의 `filters` 속성을 활용하여 원하는 데이터 값만 필터링할 수 있다.

```html
<div id="app">
    <p>{{ numbers | getOddNums | underTen }}</p>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
    const app = new Vue({
        el: "#app",
        data: {
            numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        },
        filters: {
            getOddNums: function (nums) {
                const oddNums = nums.filter(num => {
                    return num % 2
                })
                return oddNums
            },

            underTen: function (nums) {
                const underTen = nums.filter( num => {
                    return num <= 10
                })
                return underTen
            }
        }
    })
</script>
```



## :star: Lodash

> `_.method`
>
> Low Dash(`_`)를 사용하기 때문에 붙여진 이름이다.

- [Lodash 공식홈페이지](https://lodash.com/)에서 CDN을 가져온다. 

```html
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.20/lodash.min.js"></script>
```



### 기초 문법

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


console.log('-----------------3-1. range---------------')
//3. range - Vanilla X
// Lodash
const nums1 = _.range(4)
const nums2 = _.range(1, 5)
const nums3 = _.range(1, 7, 2)

console.log(nums1) // [0, 1, 2, 3]
console.log(nums2) // [1, 2, 3, 4]
console.log(nums3) // [1, 3, 5]

console.log('-----------------3-2. random---------------')
//3-2. random - Vanilla ?
const randomNum1 = _.random(0, 5)
const randomNum2 = _.random(5)
const randomNum3 = _.random(1.2, 5.2)

console.log(randomNum1)
console.log(randomNum2)
console.log(randomNum3)


console.log('-----------------3-3. sampleSize---------------')
//3-3. sampleSize - Vanilla ?
const result = _.sampleSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6)
console.log(result)

// 정렬까지
const sortedResult = _.sortBy(result)
console.log(sortedResult)
```



### 예시

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



***Copyright* © 2020 Song_Artish**

