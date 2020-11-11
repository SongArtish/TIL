# SFC

2020.11.11

> `SFC(Single File Component)`는 화면의 특정 영역에 대한 HTML, CSS, JavaScript 코드를 하나의 파일(.vue)에서 관리하는 형태이다.

---

[TOC]

---



## 개념

### 1. Component

> 컴포넌트는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 일컫는다. (재사용 가능한 코드)

- 목적: 유지, 보수, 재사용성
- Vue 컴포넌트 === Vue 인스턴스 === `.vue` 파일

---

```markdown
그렇다면 SFC 형태로 어떻게 개발할까?
```

---

### 2. npm

>`npm(Node Package Manager)`는 자바스크립트 프로그래밍 언어를 위한 패키지 관리자이며, 자바스크립트 런타임 환경 `Node.js`의 기본 패키지 관리자이다.

**설치하기**

- `bash` 창에서 Vue CLI를 설치하기 위해 다음의 명령어를 입력한다.

```bash
$ npm install -g @vue/cli
```

- 위 명령어에서, `g`는 global에 설치한다는 것을 의미한다!



### 3. Node.js

> `JavaScript Runtime Environment`로, 자바스크립트를 브라우저 밖에서 실행할 수 있는 새로운 환경을 제공한다.

**다운로드**

- [node.js 사이트](https://nodejs.org/ko/)에서 안정성이 높은 구버전을 다운로드한다.
- 단, 설치시 `Tools for Native Modules`의 체크박스는 체크하지 않는다!!
- 다운로드가 완료되면 버전을 체크해준다.

```bash
$ node -v
```

- `Node`를 설치하면 `npm`이 자동으로 설치된다.

```bash
$ npm -v
```



### 4. Babel

> 파편화된(크로스 브라우징 이슈) JavaScript 문법을 `변환/변역`하기 위해 존재하는 도구 (`compiler`)



### 5. Webpack

>모듈 간의 의존성 문제를 해결하기 위해 존재하는 도구 (`bundler`)



## <실습> SFC 기본

### 시작하기

**설치하기**

- `Vue CLI`를 설치한다.

```bash
$ npm install -g @vue/cli
```

- `package.json`에 들어있는 모듈 패키지를 설치한다.

```bash
$ npm install
```

**프로젝트 생성**

```bash
$ vue create <프로젝트명>
```

- 다음의 3가지 옵션을 표시되는데, 그 중 첫 번째 `[Vue 2]`를 선택하고 `Enter`를 누른다.

```bash
Vue CLI v4.5.8
? Please pick a preset:
> Default ([Vue 2] babel, eslint)
  Default (Vue 3 Preview) ([Vue 3] babel, eslint)
  Manually select features
```

- 이후 프로젝트 폴더로 이동해서 서버를 실행한다.

```bash
$ npm run serve
```

### Router 추가

>Django의 `urls.py`에서 관리하던 url을 view에서 관리할 수 있도록 할 수 있다.

- Vue CLI로 router를 추가한다.

```bash
$ vue add router
```

- history 모드에서 `Y`를 선택한 후 과정을 진행한다.

:ballot_box_with_check: `src > router > index.js` 가 생성된다.

- url이 다음과 같이 router로 관리된다.

```javascript
// index.js
const routes = [
  {
    path: '/',	// url 주소
    name: 'Home',
    component: Home	// 컴포넌트
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]
```

- component에 들어가는 요소는 `index.js`에서 다음과 같이 정의된다.

```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
```

- 이렇게 router로 관리되는 url을 템플릿 =에서는 아래와 같이 사용할 수 있다!

```vue
<!-- App.vue -->
<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div>
</template>
```

- 아래와 같은 방법으로도 url 주소를 작성할 수 있다.

```html
<router-link :to="{ name: 'TheLunch'}">TheLunch</router-link> |
```



### 컴포넌트 등록

```markdown
1. 가져온다
2. 등록한다
3. 보여준다
```

1. **가져온다**

```javascript
import HelloWorld from '@/components/HelloWorld.vue'
```

- 골뱅이 `@` 는 `/src` 위치를 나타낸다.

2. **등록한다**

```javascript
export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
```

3. **보여준다**.

```vue
<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>
```



### view 작성

- `src > views`에서 vue 파일을 생성한다.
- vue 파일은 대문자 작성을 원칙으로 한다.

```markdown
### 예시
- Home.vue
- TheLotto.vue
- TheLunch.vue
```

- 작성한 vue 파일에서 `vue`를 입력하고 자동완성으로 `<vue> with default.vue` + `Enter` 입력하여 기본 구조를 만들어준다.
- `index.js`의 `routes`에 path, name, component를 등록한다.

```javascript
import Practice from '../views/Practice.vue'

const routes = [
   {
    path: '/practice',
    name: 'Practice',
    component: Practice
  }
]
```

- view에서도 템플릿에 `<div>` 태그와 name을 입력해준다.

```vue
<template>
  <div>	<!-- <div> 태그 만들기-->
    
  </div>
</template>

<script>
export default {
  name: 'Practice',	// el 대신
}
</script>

<style>

</style>
```



### 데이터 입력

- SFC에서 `Data`는 데이터를 return하는 함수 형식으로 입력해야 한다.

```javascript
data: function () {
    return {
        lunch: ['국밥', '짜장면', '햄버거'],
        selectedLunchMenu: '',
    }
},
```

- 결국, 다음과 같이 데이터를 입력한다.

```javascript
export default {
  name: 'TheLunch',
  data: function () {
    return {
      lunch: ['국밥', '짜장면', '햄버거'],
      selectedLunchMenu: '',
    }
  },
  methods: {
    pickOneInLunchMenu: function () {
      const randomIndex = _.random(this.lunch.length - 1)
      // console.log(randomIndex)
      this.selectedLunchMenu = this.lunch[randomIndex]
    }
  }
}
```



### lodash 설치

- npm에 lodash를 설치한다.

```bash
$ npm install lodash
```

- view의 `<script>` 태그 안에서 `lodash`를 import 한다.

```javascript
import _ from 'lodash'
```



## Pass Props & Emit Events

> 데이터 단방향 흐름
>
> - 부모에서 자식으로 흐른다. (Pass Props)
> - 자식은 이벤트로 부모에게 데이터를 전달 할 수 있다. (Emit Events)

![Pass Props & Emit Events](img/pass_props&emit_events.png)

:star: 내일 수업을 듣고 props와 emit을 작성하는 방법을 상세히 적는다.

### 1. Props

- props로 부모의 데이터를 받을 때는, 데이터 형을 지정해준다.

```vue
props: {
    app: Object
},
```



### 2. Emit

- emit을 할 때는 다음과 같이 코드를 작성한다.

```javascript
this.$emit(<이벤트>, <데이터>)
```

- 예시

```javascript
this.$emit('input-change', event.target.value)
```



## <실습> Youtube 검색 사이트 만들기

> `여기에는 내용추가가 필요합니다.`

### API 키 관리

- 환경변수를 사용하여 API 키를 관리한다. [사이트](https://cli.vuejs.org/guide/mode-and-env.html#modes)를 참조한다.

```markdown
.env                # loaded in all cases
.env.local          # loaded in all cases, ignored by git
.env.[mode]         # only loaded in specified mode
.env.[mode].local   # only loaded in specified mode, ignored by git
```

- 프로젝트 최상위 폴더 안에 **`.env.local`**이라는 파일을 생성한 후, 아래와 같이 입력한다.
- :white_check_mark: 내용은 반드시 `VUE_APP_`으로 시작해야하며, 띄워쓰기를 하지 않아야한다!

```
VUE_APP_YOUTUBE_API_KEY=<API 키>
```





## :exclamation: 오류 디버깅

### vue-cli-service 은(는) 내부 또는 외부 명령 실행할 수 있는 프로그램 또는 배치 파일이 아닙니다

**해결방안1** : Vue CLI 재설치

- Vue CLI를 제거 후 재설치 한다.

```bash
$ npm uninstall vue-cli -g
```

```bash
$ npm install -g @vue/cli
```

**해결방안2** : npm 확인

- 프로젝트에 `node_modules` 폴더가 있는지 확인한다.
- 있다면 지우고 npm을 다시 설치한다.

```bash
$ npm install
```



***Copyright* © 2020 Song_Artish**

