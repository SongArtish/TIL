# Vue Router

---

[TOC]

---



## Overview

Django의 `urls.py`에서 관리하던 url을 view에서 관리할 수 있도록 할 수 있다.



## 시작하기

Vue CLI로 router를 추가한다.

```bash
$ vue add router
```

history 모드에서 `Y`를 선택한 후 과정을 진행한다. 

```markdown
브라우저에서 지원하는 History API를 사용하면 주소 이동 없이 URI만 바꿀 수 있다.
```

설치가 완료되면, `src > router > index.js` 가 생성되며, url이 다음과 같이 router로 관리된다.

```javascript
// index.js
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

    ...

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



## 사용하기

component에 들어가는 요소는 `index.js`에서 다음과 같이 가져온다.

```javascript
// index.js
import Home from '../views/Home.vue'	// 1번 방법
import About from '@/views.About'	// 2번 방법
```

가져온 component를 등록한다.

```javascript
// index.js

const routes = [
  {
    path: '',
    name: 'Home',
    component: Home,
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
]
```

이렇게 router로 관리되는 url을 템플릿에서는 아래와 같이 사용할 수 있다!

```vue
<!-- App.vue -->
<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |	<!-- 1번 방법 -->
      <router-link :to="{ name: 'About'}">About</router-link> <!-- 1번 방법 -->
    </div>
    <router-view/>
  </div>
</template>
```

아래와 같이 `router push`로 클릭시 함수를 실행시켜 이동하게 할 수도 있다.

```html
<div @click="toHome">
    Home
</div>
```

```javascript
methods: {
    toHome: function () {
        this.$router.push({ name: 'Home' })
    }
}
```



## Dynamic Route Matching

동적 라우트 매칭

router 파일에서 아래와 같이 컴포넌트를 **등록**한다.

```javascript
// index.js
import User from '@/views/User'

const router = new VueRouter({
    routes: [
        { path: '/user/:id', component: User }
    ]
})
```

`router push`를 할 경우 아래와 같이 사용하여 위에서 정의한 페이지로 이동할 수 있다. `params`를 이용하여 변수를 URL로 **전달**한다.

```javascript
data: function () {
    return {
        user: 'bulgen'
    }
},
methods: {
    toUser: function () {
        this.$router.push({ name: 'Home', params { id: this.user }})
    }
}
```

- 전환되는 페이지에서는 다음과 같이 이전 페이지에서 받은 변수를 **사용**할 수 있다.

```javascript
this.$route.parmas.id
this.$route.params.address
this.$route.params.keyword
```

:ballot_box_with_check: **`params` vs `query`**

- `query`는 데이터가 주소창에 노출된다.
- `params`는 데이터를 주소창에 노출시키지 않고 넘겨준다!



***Copyright* © 2020 Song_Artish**
