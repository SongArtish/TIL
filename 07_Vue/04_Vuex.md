# Vuex

2020.11.13

> Vue.js 애플리케이션에 대한 상태 관리 패턴 + 라이브러리 (중앙 집중식 저장소)

---

[TOC]

---



## 상태관리패턴

```markdown
Vuex는 모든 컴포넌트를 트리에 상관없이 상태(data)에 액세스하거나 동작을 트리거 할 수 있게 해주는 라이브러리이며 중대형 규모의 SPA에 적합하다.
```

**Vuex Concept**

![Vuex Concept](img/vuex_concept.png)

- `state`: 앱을 작동하는 원본 소스이다.
- `view` : 상태의 선언적 매핑
- `action` : 뷰에서 사용자 입력에 대해 반응적으로 상태를 바꾸는 방법



## 용어

### :black_large_square: State

> 중앙에서 관리하는 모든 `데이터(data)`

### :black_large_square: Getter

> 저장소의 상태를 기준으로 계산해야 하는 값

- `computed`와 유사하며, 실제 상태(data)를 변경하지는 않는다.

### :black_large_square: Mutations

> State를 변경하는 로직
>
> - 동기적인 작업
> - 메서드 호출 : `commit`
> - 첫 번째 인자 : `state`

- 상태를 변경시키기 때문에 첫 번째 인자로 항상 state를 받는다.

```javascript
mutations: {
    <함수명>: function (state, <매개변수>) {
        <코드블럭>
    }}
```

### :black_large_square: Action

> state를 직접 변경하지 않고 mutations에 정의된 메서드를 호출해서 변경한다. (데이터 fetch 및 처리 & 가공)
>
> - 비동기 작업
> - 메서드 호출 : `dispatch`
> - 첫 번째 인자 : `context`

```javascript
actions: {
    <함수명>: function (context, <매개인자>) {
        <코드블럭>
    }}
```



## <실습> Todo List 만들기

### :arrow_forward: 시작하기

:star: **Vuex 생성하기**

1. **Vue CLI를 통한 생성**

```bash
$ vue add vuex
```

- `store > index.js`가 생성된다.
- `modules`를 지우고 `getters`를 입력해준다.

```javascript
// index.js
export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  }
})
```

2. **직접 생성**

>이러한 방법도 있기는 하지만 우리는 Vue CLI를 활용해서 간단하게 작업한다.

- `src > store > index.js` 파일을 생성해준다.
- `index.js` 파일의 뼈대를 작성한다.

```javascript
// index.js

import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  }
})
```

- `main.js` 파일에 생성한 `store`를 등록해준다.

```javascript
// main.js

import store from './store'

new Vue({
  store,	// store 추가
  render: h => h(App)
}).$mount('#app')
```

**참고**

- 다음의 명령어를 통해 Vue 프로젝트를 관리하기 위한 GUI 환경을 사용할 수도 있다.

```bash
$ vue ul
```

:star: **자바스크립트 파일 실행**

```bash
$ node <파일명>.js
```



### :arrow_forward: 컴포넌트 생성

- `component` 폴더에 다음의 3개의 vue 파일을 만들어준다.
  - `Todo.vue`
  - `TodoForm.vue`
  - `TodoList.vue`



### :arrow_forward: 데이터 작성

- `index.js`에 state(데이터)를 작성해본다.

```javascript
state: {
    todos: [
        {title: '할일1', completed: false},
        {title: '할일2', completed: false},
    ]
},
```



### :arrow_forward: 데이터 가져오기

```javascript
$store.state.<데이터명>
```

- `TodoList.vue`에서는 아래와 같이 데이터를 가져온다.

```vue
    <Todo 
    v-for="(todo, idx) in $store.state.todos"
    :key="idx"
    :todo="todo"
    />
```

- key 값을 필요로하기 때문에 `:key="idx"`도 정의해준다.
- `:todo="todo"`로 데이터를 하위 컴포넌트로 내려준다.

또한 `computed`를 통해서도 데이터를 가져올 수 있다.

```javascript
  computed: {
    todos: function () {
      return this.$store.state.todos
    }
```

- 마지막으로 `TodoList.vue`에서 `Todo.vue`로 내려준 데이터를 받아준다.

```javascript
// Todo.vue
  props: {
    todo: Object, // props validation
  }
```



### :arrow_forward: 항목 추가하기 (mutation)

:star: **mutation**

> mutation은 상태를 변경시키기 때문에 첫 번째 인자로 항상 state를 받는다.
>
> - mutation의 함수는 `All_Capital`, `Snake_Case`로 표현하는게 컨벤션이다.

- mutation은 다음과 같이 작성한다.

```javascript
// 작성 예시
  mutations: {
    CREATE_TODO: function () {
      console.log('CREATE TODO CALL!')
    }
```

- mutation을 부를 때는 `commit`을 사용한다.
  - `this.$store`이 반환하는 데이터 중 mutation의 데이터는 `commit` 안에 존재한다.

```javascript
// 호출 예시
    createTodo: function () {
      console.log(this.$store.commit)
    }
```

- mutation의 상태에 데이터를 추가하는 로직을 작성한다.

```javascript
// index.js
  mutations: {
    CREATE_TODO: function (state, todoItem) {
      // console.log(state, todoItem)
      state.todos.push(todoItem)
    }
```

- `TodoForm.vue`에서 위의 로직을 받아와서 실행하는 함수를 작성한다.

```javascript
// TodoForm.vue
    createTodo: function () {
      const todoItem = {title: this.todoTitle, completed: false}
      this.$store.commit('CREATE_TODO', todoItem)
      this.todoTitle = ''	// commit을 하고는 비워준다.
    }
```

- 해당 함수가 `enter`와 버튼 `click`이라는 이벤트가 발생했을 때 실행되도록 `v-on`으로 묶어준다.
- 또한 `<input>` 태그의 데이터를 조작할 수 있도록 `v-model`을 `<input>` 태그에 달아준다.

```vue
<!-- TodoForm.vue -->
<input type="text" v-model="todoTitle" @keypress.enter="createTodo" autofocus>
<button @click="createTodo">Add</button>
```



### :arrow_forward: 항목 추가하기 (action)

> action은 state를 직접 변경하지 않고 mutation에 정의된 메서드를 호출해서 변경한다. (데이터 fetch 및 처리 & 가공)
>
> ```javascript
> <함수명>: function (context, <매개인자>) {
>     context.commit('<mutations의 함수명', <매개인자>)
> }
> ```

:star: **action**

- action은 첫 번째 인자로 `context`를 넣어준다.
- 아래는 action에서 `commit` 메서드로 mutation을 부르는 로직이다.

```javascript
// index.js
  actions: {
    createTodo: function (context, todoItem) {
      // console.log(context)
      context.commit('CREATE_TODO', todoItem)
    }}
```

- action을 호출할 때는 `dispatch`를 사용한다.

```javascript
$store.dispatch('<actions의 함수>', 매개인자)
```

- `action`의 함수를 호출하여 다음과 같이 Todo List의 항목을 추가해주는 로직을 작성한다.

```javascript
// TodoForm.vue

    createTodo: function () {
      const todoItem = {title: this.todoTitle, completed: false}
      // this.$store.commit('CREATE_TODO', todoItem)
      this.$store.dispatch('createTodo', todoItem)
      this.todoTitle = ''
    }
  }
```



### :arrow_forward: 공백일 때는 데이터가 추가되지 않도록 처리 (trim)

:star: **trim 메서드**

> trim 메서드를 통해서 공백일 때는 데이터가 추가되지 않도록 설정할 수 있다.
>
> ```javascript
> <데이터>.trim()
> ```
>
> ```javascript
> <<태그명> v-model.trim="<데이터명>">
> ```

- 아래와 같이 title이 존재하며(`&&`) 공백이 아닌 경우 데이터가 추가되도록 코드를 작성한다.

```javascript
// TodoForm.vue      
	if (todoItem.title && todoItem.title.trim()) {
        this.$store.dispatch('createTodo', todoItem)
      }
```

- `v-model.trim=`도 사용할 수 있다.

```vue
<input type="text" v-model.trim="todoTitle" @keypress.enter="createTodo" autofocus>
```

```javascript
if (todoItem.title) {
    this.$store.dispatch('createTodo', todoItem)
}
```



### :arrow_forward: <참고> destructuring 문법

> 비구조화 문법을 통해서 편리하게 데이터를 가져올 수 있다.
>
> ```javascript
> // 기본 문법
> const commit = context.commit
> // destructuring 문법
> const { state, commit } = context
> console.log(state, commit())
> ```

- 기본 방법

```javascript
// 1. 하나 하나 할당
const commit = context.commit
const state = context.state

console.log(commit()) // 안녕하세요 commit!
console.log(state) // { todo: '할 일 1' }
```

- destructuring 문법
  - 여러개를 가져올 경우, 순서가 필요없다!

```javascript
//2. 이름으로 가져온다.
const { state, commit } = context
console.log(commit()) // 안녕하세요 commit!
console.log(state) // { todo: '할 일 1' }
```

- 비구조화 문법을 통해서 `createTodo` 함수를 간단하게 작성할 수 있다!

```javascript
// TodoForm.vue
    createTodo: function ({ commit }, todoItem) {
      commit('CREATE_TODO', todoItem)
    }
```



### :arrow_forward: Delete 버튼 만들기

- vuex의 `mutations`에 데이터를 삭제하는 코드를 작성한다.

  - :ballot_box_with_check: `indexOf`메서드 : 해당 데이터를 index 값을 가져온다.

  - :ballot_box_with_check: `splice` 메서드 : 기존 배열의 시작점부터 n개의 요소를 삭제한다.

    ```javascript
    array.splice(start[, deleteCount[, item]])
    ```

```javascript
// index.js
  mutations: {
    DELETE_TODO: function (state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    }},
```

- `actions`에 `mutations`의 `DELETE_TODO`라는 함수를 가져오는(`commit`) `deleteTodo`라는 함수를 작성한다.

```javascript
// index.js
  actions: {
    deleteTodo: function ({commit}, todoItem) {
      commit('DELETE_TODO', todoItem)
    }}
```

- 위에서 작성한 actions의 `deleteTodo`라는 함수를 `Todo.vue`에서 가져와준다.

```javascript
// Todo.vue
  methods: {
    deleteTodo : function () {
      // console.log('Delete!')
      this.$store.dispatch('deleteTodo', this.todo)
    }}
```

- 버튼을 클릭하면 해당 데이터 삭제 함수가 실행될 수 있도록 `v-on`을 넣어준다.

```vue
<!-- Todo.vue -->
<button @click="deleteTodo">Delete</button>
```



### :arrow_forward: 완료 여부 표시하기

- 아래와 같이 mutation에 Todo의 완료 상태를 변경하는 함수를 생성한다.
  1. todos 배열을 반복하며 꺼내지는 todo 요소가 넘어온 todoItem과 동일한지 체크!
  2. 동일하다면, 그 요소의 completed 상태를 반대로 (`!todo.completed`) 변경하여 return
  3. 동일하지 않다면, 그대로 return

```javascript
// index.js > mutations

    UPDATE_TODO_STATUS: function (state, todoItem) {
      // 1. todos 배열을 반복하며
      state.todos = state.todos.map((todo) => {
        // 2. 꺼내지는 todo 요소가 넘어온 todoItem과 동일한 경우
        if (todo === todoItem) {
          // 3. 그 요소의 completed를 반대로 바꿔서 return
          return {
            ...todo,	// spread 문법
            completed: !todo.completed
          }
        }
        // 4. 같지 않은 경우는 todo를 그대로 return
        return todo
      })
    }
```

- 그리고 이 함수를 가져와 실행하는 함수를 action에 작성해준다. (`updateTodoStatus`라는 함수)

```javascript
// index.js > actions

    updateTodoStatus: function ({commit}, todoItem) {
      commit('UPDATE_TODO_STATUS', todoItem)
    }
```

- 컴포넌트에서 action의 함수를 dispatch를 통해 호출한다.

```javascript
// Todo.vue
    updateTodoStatus: function () {
      this.$store.dispatch('updateTodoStatus', this.todo)
    }
```

- 아래와 같이 완료 여부에 따라서 줄을 그어주는 style을 적용한다.

```vue
<!-- Todo.vue > <template> -->
<span :class="{ completed: todo.completed }" @click="updateTodoStatus">{{ todo.title }}</span>

<!-- Todo.vue > <style> -->
<style scoped>	
  .completed {
    text-decoration: line-through;
  }
</style>
```

- <!-- scoped : 이 범위에서만 한정시킬 때 사용한다. -->



### :arrow_forward: <참고> spread 문법

> 기호 : **`...`**
>
> `...`으로 가져오는 데이터의 변화하지 않는 값을 대체할 수 있다. 반복을 줄임으로 생산성을 높일 수 있다.

- 예시

```javascript
// 데이터
const todoItem = {
  todo: '첫 번째 할 일',
  dueDate: '2020-12-25',
  importance: 'high',
  completed: false
}
```

- `todoItem > completed` 값만 변경한다고 하면 아래와 같이 작성할 수 있다.

```javascript
// spread 문법 예시
const myUpdateTodo2 = {
  ...todoItem,
  completed: true,
}
```



### :arrow_forward: 데이터 개수 계산하기

:star: **getter**

> `getter`는 `computed`와 유사한 동작을 하는데, 이를 활용해서 Todo의 데이터의 전체, 완료항목, 미완료항목을 계산한다.

- getters에서 아래와 같이 `filter`와 `length`를 사용하여 항목의 개수를 반환하는 함수를 생성한다.

```javascript
// index.js > getters

  getters: {
    // 전체 항목 개수
    allTodosCount: function (state) {
      return state.todos.length
    },
   	// 완료 항목 개수
    completedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === true
      }).length
    },
    // 미완료 항목 개수
    uncompletedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed ===false
      }).length
    }}
```

- getters에서 작성한 함수를 컴포넌트에서 불러온다.
- `computed`에 넣어서 계산을 하는 함수를 작성한다.

```javascript
// App.vue > computed
  computed: {
    allTodosCount: function () {
      return this.$sotre.getters.allTodosCount
    },
    completedTodosCount: function () {
      return this.$store.getters.completedTodosCount
    },
    uncompletedTodosCount: function () {
      return this.$store.getters.uncompletedTodosCount
    }
  }
```

- 템플릿에서 `computed`에 작성한 함수를 불러와 표시한다.

```vue
<!-- App.vue -->
<h2>전체 할 일 : {{ allTodosCount }}</h2>
<h2>완료 된 일 : {{ completedTodosCount }}</h2>
<h2>완료되지 않은 일 : {{ uncompletedTodosCount }}</h2>
```



### :arrow_forward: <참고> `mapState` & `mapGetters`

> `mapState`와 `mapGetters`를 활용해서 컴포넌트에서 편리하게 mapping 할 수 있다.

:star: **`mapState`** : state를 mapping

```javascript
import { mapState } from 'vuex'

computed: {
    ...mapState({
        '<컴포넌트에서 정의할 이름>' : '<status에서 가져온 변수명>'
    })
}
```

- 예시

```javascript
// TodoList.vue
import { mapState } from 'vuex'

  computed: {
    // 1. 기존 방식
    todos: function () {
      return this.$store.state.todos
    }
    // 2. mapState 사용
    ...mapState({
      'todos' : 'todos'
    })
    // 3. mapState 더욱 간단하게
   ...mapState([
      'todos'
    ])
  }
```

- :white_check_mark: 단, mapState를 더욱 간단하게 사용할 때는 `{}`가 아닌 `[]`를 사용한다는 것에 주의한다!!



:star: **`mapGetters`** : getter를 mapping

```javascript
import {mapGetters } from 'vuex'

computed: {
    ...mapGetters(['<가져올 함수명>'])
}
```

- 예시

```java
// App.vue
import { mapGetters } from 'vuex'
  computed: {
    // 1. 기존 방식
    allTodosCount: function () {
      return this.$sotre.getters.allTodosCount
    },
    completedTodosCount: function () {
      return this.$store.getters.completedTodosCount
    },
    uncompletedTodosCount: function () {
      return this.$store.getters.uncompletedTodosCount
    }
    // 2. mapGetters를 간단하게 사용
    ...mapGetters([
      'allTodosCount',
       'completedTodosCount',
       'uncompletedTodosCount'
    ])
  }
```

- `mapGetters` 역시 `mapState`처럼 `...mapGetters({'allTodosCount':'allTodosCount})`의 방식으로 사용할 수도 있다!



### :arrow_forward: 로컬에 데이터 저장 (vuex-persistedstate 모듈)

:star: **vuex-persistedstate 모듈**

>vuex의 상태/데이터를 지속시켜주는 모듈이다. [사이트](https://www.npmjs.com/package/vuex-persistedstate) 참조

**설치하기**

```bash
$ npm install vuex-persistedstate
```

**적용하기**

- vuex에서 설치한 모듈을 가져와서 `export default new Vuex.Store({})`의 요소로 `plugins`를 추가해준다.

```javascript
// index.js (모듈 가져오기)
import createPersistedState from "vuex-persistedstate"
```

```javascript
// index.js
export default new Vuex.Store({
    state: {},
    getters: {},
    mutations: {},
    actions: {},
    plugins: [createPersistedState()] // plugins 항목을 추가해준다.
})
```

- 그리고 서버를 시작해서 데이터를 작성/수정/삭제한다.
- 새로고침을 해보면 데이터가 그대로 남아있는 것을 확인할 수 있다.



## :exclamation: 오류 디버깅

### Vuex 설치 오류

```bash
$ vue add vuex
```

- 위의 명령어를 통해 Vuex를 설치하려고 하는데 아래의 오류가 발생했다.

```
ERROR  Error: The package.json file at 'C:\Users\bulge\Documents\Python Scripts\07_Vue\02_vuex\1113_workshop\src\package.json' does not exist
```

> - 검색 해보니 `npm ini`을 해주라는 설명이 있었다.
>
> ```bash
> $ npm init
> ```
>
> - :exclamation: 하지만 이 방법은 문제를 해결해 주지 않았다.
> - 위의 코드는 `npm`을 현재의 위치에 다시 생성해주는 코드인데, 내 문제와 같은 경우에는 원인이 달랐다.

- 위의 에러는 bash 창 현재 위치에 package.json이 없기 떄문에 일어나는 오류이다.
- 따라서 bash 창의 위치를 확인해준다.



***Copyright* © 2020 Song_Artish**