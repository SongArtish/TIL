# Vue 문법

---

[TOC]

---



## 1. Data

> Vue 앱의 상태 데이터를 정의하는 것으로, Vue template에서 interpolation을 통해 접근할 수 있다.

### 객체 생성

```javascript
const app = new Vue({
 el: "#app",
 data: {}
})
```

### Data Binding

- `el`을 통해서 html의 데이터를 Vue 인스턴스로 가져올 수 있다.

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

예시

```html
<div id="app">{{ message }}</div>
<script>
const app = new Vue ({
    el: '#app',
    data: {
        message: 'Hello SSAFY!',
    },
    methods: {
        greetings: function () {
            console.log(this.message)
        }
    }
})
</script>
```

- `new Vue`로 객체를 생성하고 `el`라는 속성에 아이디 값(`#-`)을 입력한다.
- :ballot_box_with_check: ​ Vue 객체 내 다른 함수에서 `this` 키워드를 통해 접근할 수 있다.
- :ballot_box_with_check: `#app` + `Enter`를 누르면 id가 app인 `<div>` 태그를 생성할 수 있다.





## 2. 반복문

> `v-for=""`
>
> - v-for 사용 시 반드시 `:key` 속성을 각 요소에 작성해야 한다.

- `todoList`에서 각각 `todo`를 가져와서 `content` 만 표시해준다.

```html
<ul v-for="todo in todoList">
    <li>{{ todo.content }}</li>
</ul>
```



## 3. 조건문

> `v-if=""`, `v-else-if=""`, `v-else`
>
> 조건문에 따라 렌더링 여부를 결정한다.

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



## 4. v-show

> 항상 렌더링하며 조건문에 따라 노출 여부를 결정한다.
>
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



## 5. v-bind

>`v-bind:`
>
>:ballot_box_with_check: shortcut : **`:`**

### HTML 표준속성 binding

> HTML 요소의 속성에 Vue의 상태 데이터를 값으로 할당한다.

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

### Class Binding

> Object의 형태로 사용하면 value가 true인 key가 class 바인딩 값으로 할당된다.

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



## 6. v-on 메서드

> `v-on:`
>
> `v-on` 메서드는 특정 이벤트가 발생했을 때, 주어진 코드가 실행된다. JS의 eventListener와 같은 역할을 한다.
>
> :ballot_box_with_check: shortcut : **`@`**

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



## 7. v-model

> `v-model`은 HTML form 요소의 값과 데이터를 양방향 바인딩한다.

|     메서드     |                             설명                             |
| :------------: | :----------------------------------------------------------: |
|  v-model.lazy  | 요소에 input 이벤트 대신 change 이벤트 이후 데이터와 동기화한다. |
|  v-model.trim  |        바인딩 된 값의 앞뒤 공백을 자동으로 제거한다.         |
| v-model.number |        바인딩 된 값을 숫자 타입으로 자동 형변환한다.         |

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



## 8. v-text  & v-html

`v-text`는 텍스트 그대로 렌더링하는 반면, `v-html`은 태그를 렌더링한다.

### v-text

>주어지는 값을 요소의 innerText로 할당하며, 내부적으로는 interpolation 문법이 v-text로 컴파일된다.

```html
<div id="app">
    <p v-text="message"></p>
</div>

<script>
const app = new Vue ({
    el: '#app',
    data: {
        message: 'Hello SSAFY!',
    },
})
</script>
```

### v-html

> 주어진 값을 요소의 innerHTML로 할당한다. (텍스트를 실제 HTML 태그로 만들어준다.)
>
> :white_check_mark: 단, `v-html`은 주의해서 사용한다!
>
> - XSS 공격으로 쉽게 이어질 수 있으므로 매우 위험할 수 있다.
> - 임의의 사용자로부터 입력 받은 내용은 v-html에 '절대' 사용하면 안된다.

```html
<div id="app" v-html="message"></div>

<script>
const app = new Vue ({
    el: '#app',
    data: {
        message: '<script>alert("hi")</script>',
    },
})
</script>
```

예시

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



## 9. filters

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



## 10. computed & watch

```markdown
## computed 속성
- "선언형 프로그래밍" 방식
- 계산해야 하는 목표 데이터를 정의하는 방식
- 특정 데이터를 직접적으로 사용/가공하여 다른 값을 만들 때 주로 사용

## watch 속성
- "명령형 프로그래밍" 방식
- 감시할 데이터를 지정하고 그 데이터가 바뀌면 이런 함수를 실행하라는 방식
- 특정 데이터의 변화 상황에 맞춰 다른 data 등이 바뀌어야 할 때 주로 사용
```

### computed

> 데이터를 기반으로 하는 계산된 속성
>
> - 반드시 return(반환값)이 있어야 한다.
> - 함수의 형태로 정의하지만 함수가 아닌 함수의 반환값이 바인딩 된다.
> - 참조하는 데이터의 값이 바뀌는 순간에만 함수가 다시 실행된다.

```html
<div id="app"> 
	<p>{{ num }}</p>
	<p>{{ doubleNum }}</p>
</div>

<script>
const app = new Vue ({
    el: '#app',
    data: {
        num: 2,
    },
    computed: {
        doubleNum: function () {
            return num * 2
        },
    },
})
</script>
```

### watch

> 데이터를 감시하고, 데이터에 변화가 일어났을 때 실행되는 함수

```html
<div id="app"> 
	<p>{{ num }}</p>
	<button @click="num++">add</button>
</div>

<script>
const app = new Vue ({
    el: '#app',
    data: {
        num: 2,
    },
    watch: {
        num: function () {
            console.log(this.num, 'changed')
        },
    },
})
</script>
```



***Copyright* © 2020 Song_Artish**