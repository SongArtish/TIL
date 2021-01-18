# Vue 기초

2020.11.09

> 자바스크립트 프레임워크에는 대표적으로 `React`, `Angular`, `Vue` 가 있으며, `Vue.js`는 UI를 만들기 위한 progressive framework이다. `Vue.js`를 통해 동적으로 DOM을 조작할 수 있다.

---

[TOC]

---



## 개념

Vue.js는 특징으로는 CSR (Client Side Rendering), SPA (Single Page Application) 등이 있으며, `Vue.js`의 작성 순서는 다음과 같다.

 ```markdown
1. Data
2. DOM
 ```

- :ballot_box_with_check: Vue.js는 `Model`, `View`, `ViewModel`의 **MVVM 패턴**을 가진다.

  |               |                     |                             역할                             |
  | :-----------: | :-----------------: | :----------------------------------------------------------: |
  |   **Model**   | 자바스크립트 Object |                    화면에 표현되는 데이터                    |
  |   **View**    |      DOM(HTML)      |                      사용자가 보는 화면                      |
  | **ViewModel** |  모든 Vue Instance  | View에서 보여줄 데이터 정의 및 처리<br />Model과 상호작용하며 데이터 주고 받음 |



## 시작하기

**설치하기**

> 자세한 건 [SFC문서](03_SFC.md)의 Intro 파트를 참조한다.

- 먼저 `node.js`를 설치한다.
- 그리고 다음의 명령어로 `vue-cli`를 설치한다.

```bash
$ npm install -g @vue/cli
```



**extensions 설치하기**

- Chrome 웹 스토어 tool 설치

  ```markdown
  - Vue.js devtools
  ```

  > 해당 페이지가 Vue로 작성되었다면 Vue로 어떻게 구성되었는지 보여준다.

  

  - :heavy_check_mark: 로컬에서 작성한 `HTML`을 로드하였을 때 확장 프로그램이 실행되지 않는다면 `확장 프로그램 > 세부정보 > 파일 URL에 대한 액세스 허용`을 활성화해준다!

- VSCode extension

  ```markdown
  - Vetur
  ```

  > `Vue.js`의 자동 완성 등을 담당한다.
  
  ```markdown
  - Live Server
  ```
  
  > `Eclipse`에서 사용하는 extension으로 VS Code에서 사용하는 서버이다. 로컬 서버 변경 자동 반영
  
  ```markdown
  - Vue 3 Snippets
  ```
  
  > Vetur에서 지원하지 않는 자동완성까지 적용
  
  ```markdown
  - Prettier
  ```
  
  > `file >> preference >> setting or Ctrl + ,(comma)`

**CDN**

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

### 1. Data

> Vue 앱의 상태 데이터를 정의하는 것으로, Vue template에서 interpolation을 통해 접근할 수 있다.

#### 1.1 객체 생성

```javascript
const app = new Vue({
 el: "#app",
 data: {}
})
```

#### 1.2 Data Binding

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

#### 예시

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





### 2. 반복문

> `v-for=""`
>
> - v-for 사용 시 반드시 `:key` 속성을 각 요소에 작성해야 한다.

- `todoList`에서 각각 `todo`를 가져와서 `content` 만 표시해준다.

```html
<ul v-for="todo in todoList">
    <li>{{ todo.content }}</li>
</ul>
```



### 3. 조건문

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



### 4. v-show

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





### 5. v-bind

>`v-bind:`
>
>:ballot_box_with_check: shortcut : **`:`**

#### 5-1 HTML 표준속성 binding

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



#### 5-2 Class Binding

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



### 6. v-on 메서드

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



### 7. v-model

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



### 8. v-text  & v-html

`v-text`는 텍스트 그대로 렌더링하는 반면, `v-html`은 태그를 렌더링한다.

#### 8.1 v-text

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

#### 8.2 v-html

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

#### 예시

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





### 9. filters

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



### 10. computed & watch

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

#### 10-1. computed

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

#### 10-2. watch

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



## <참고> Lifecycle Hooks

> 각 Vue 인스턴스는 생성될 때 일련의 초기화 단계를 거친다. 그 과정에서 사용자 정의 로직을 실행할 수 있는 `라이프사이클 훅`도 호출된다.
>
> [공식문서](https://kr.vuejs.org/v2/api/#%EC%98%B5%EC%85%98-%EB%9D%BC%EC%9D%B4%ED%94%84%EC%82%AC%EC%9D%B4%ED%81%B4-%ED%9B%85)를 통해 각 라이프사이클 훅의 상세 동작을 확인할 수 있다.

**API 가져오기**

- `created`를 통해 어플리케이션의 초기 데이터를 API 요청을 통해 불러올 수 있다.

```javascript
export default {
    data: function () {
        return {
            imgSrc: '',
        }
    },
    methods: {
        getImg: function () {
            axios.get(API_URL).then(response => {
                this.imgSrc = response.data.src
            })
        },
    },
    created: function () {	// Vue 인스턴스가 생성되면
        this.getImg()		// 이미지 데이터를 불러온다.
    },
}
```

```html
<template>
	<div id="app">
        <img v-if="imgSrc" :src="imgSrc"/>
        <p v-else>Image Loading..</p>
    </div>
</template>
```

예시 : 랜덤한 고양이 사진을 불러오는 코드를 작성한다.

```html
<div id="app">
    <h1>Cat Image</h1>
    <!-- <img v-if="imgUrl" :src="imgUrl" />
<p v-else>Image Loading..</p> -->
    <button @click="getImg">Get Cat</button>
    <hr>
    <img v-for="image in images" :src="image">
</div>

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
    const app = new Vue ({
        el: "#app",
        data: {
            // imgUrl: ''
            images: [],
        },
        methods: {
            getImg: function () {
                // console.log(this)
                axios.get("https://api.thecatapi.com/v1/images/search")
                // 중첩되어 있는 function에서는 되도록이면 arrow function(=>)을 사용한다!!
                    .then(response => {
                    // console.log(this)
                    // this.imgUrl = response.data[0].url  // 데이터의 위치는 꼭 확인해주도록 한다!
                    this.images.push(response.data[0].url)
                })
            },
        },
        created: function () {	// Vue 인스턴스가 생성되면
            this.getImg()		// 이미지 데이터를 불러온다.
        },
    })

    // function (respose) {}를 하면 위 & 아래의 this가 다르다!!
    // 따라서 response => 를 사용한다.
</script>
```



## <실습> todo List 만들기

```html
<!--
1. autofocus 할 수 없나?
2. const STORAGE_KEY = 'vue-todo-app'    // :star: STORAGE_KEY를 왜 이렇게 정의해주는거지??
3. local stroage 어디에 저장되는 거지?\
  => 내 컴퓨터에 저장한다.
-->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .completed {
      text-decoration: line-through;
      color: gray;
    }
  </style>
</head>
<body>

  <div id="app">
    <select v-model="status">
      <option value="all">전체</option>
      <option value="inProgress">진행중</option>
      <option value="completed">완료</option>
    </select>
    <!-- :star: autofocus -->
    <input type="text" v-model="content" autofocus>   <!-- 렌더링 되는 과정에서 focus될 때가 있고, 안 될 때가 있다. 테스트용이라서 문제가 생기는 것 같다!-->
    <button @click="addTodo">+</button>
    <br>
    <ul v-for="todo in todoListByStatus" :key="todo.date">  <!-- key 값에 고유값을 부여한다. --> 
    <!-- todoListByStatus라는 함수는 return 값을 반환하기 때문에 하나의 배열로서 호출한다. -->
      <li>
        <input type="checkbox" :checked="todo.completed" @click="toggleCompleted(todo)">  <!-- 매개변수는 다음과 같이 넘겨준다. -->
        <span :class="{completed : todo.completed}">{{ todo.content }}</span>
      </li>
    </ul>
    <br>
    <button @click="deleteCompleted">완료된 할 일 지우기</button>
  </div>
  

  <!-- Vue CDN-->
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    // local storage로 내보내기 & 불러오기
      // 불변하는 값을 정의할 때는, 모두 대문자를 사용한다.
    const STORAGE_KEY = 'vue-todo-app'    // 데이터를 로컬에 저장할 때, {key, value} 형태로 저장하는데 이때 데이터를 value에 저장하며 key에 아무거나 적당한 값을 넣어준다. (임의의 문자열 값)
    const storageTodo = {
      // 불러오는 함수는 보통 fetch로 정의
      fetch: function () {
        // 문자열 => JSON
        return JSON.parse(localStorage.getItem(STORAGE_KEY)) || []  // or 연산 - localStorage에 해당 key 값의 항목이 없으면(false)이면 [] (빈 배열)을 불러온다.
      },
      save: function (todoList) {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(todoList))  // setItem(key, value)
      }
    }


    const app = new Vue ({
      el: '#app',
      data: {
        content: "",
        status: 'all',  // 기본값은 all로 설정해준다.
        // todoList: [],
        todoList: storageTodo.fetch() // storageTodo라는 변수의 fetch() 함수를 불러온다.
      },
      computed: {
        todoListByStatus: function () {
          return this.todoList.filter(todo => {
            // 만약 지금 상태가 inProgress라면, todo.completed가 false인 값들만 모은 배열을 return
            if (this.status === "inProgress") {
              return !todo.completed
            } else if (this.status === "completed") {
              return todo.completed
            } return true   // true를 return하면 원래 자신이 가지고 있던 값을 반환한다.
          })
        }
      },
      methods: {
        addTodo: function () {
          const todo = {
            // this는 Vue instance를 바라본다!!
            content: this.content,
            completed: false,
            date: new Date().getTime(),
          }
          this.todoList.push(todo)
          this.content = ''
        },
        toggleCompleted: function (todo) {
          // false일 때 true, true일 때 false
          todo.completed = !todo.completed
        },
        deleteCompleted: function () {
          this.todoList = this.todoList.filter(todo => !todo.completed) // arrow function
        }
      },
      // todoList의 변화를 감시하여 local storage에 저장한다.
      watch: {
        todoList: {
          handler: function (todoList) {
            storageTodo.save(todoList)
          },
          deep: true  // (deepcopy와 같이) todoList의 내부요소까지 바뀌는 것을 감시한다.
        }
      }
    })
  </script>
</body>
</html>
```





***Copyright* © 2020 Song_Artish**