# Vue Frameworks

2021.01.21

---

[TOC]

---



## Vue Bootstrap

> [Vue Bootstrap 사이트](https://bootstrap-vue.org/docs)

- 먼저 패키지를 설치한다.

  ```bash
  npm install vue bootstrap bootstrap-vue
  ```

- `main.js`에 bootstrap을 등록해준다.

  ```javascript
  import Vue from 'vue'
  import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
  
  // Import Bootstrap an BootstrapVue CSS files (order is important)
  import 'bootstrap/dist/css/bootstrap.css'
  import 'bootstrap-vue/dist/bootstrap-vue.css'
  
  // Make BootstrapVue available throughout your project
  Vue.use(BootstrapVue)
  // Optionally install the BootstrapVue icon components plugin
  Vue.use(IconsPlugin)
  ```

  

## Vue Glide

> [Vue Glide 사이트](https://www.npmjs.com/package/vue-glide-js)

- 먼저 패키지를 설치한다.

  ```bash
  npm i vue-glide-js
  ```

- `main.js`에 bootstrap을 등록해준다.

  ```javascript
  import Vue from 'vue'
  import App from './App.vue'
  import VueGlide from 'vue-glide-js'
  import 'vue-glide-js/dist/vue-glide.css'
   
  Vue.use(VueGlide)
   
  new Vue({
    el: '#app',
    render: h => h(App)
  })
  ```




## Vue Burger Menu

> [Github 페이지](https://github.com/mbj36/vue-burger-menu)
>
> 이외 관련 프레임워크 [참고](https://morioh.com/p/fcf1194d47e5)

- 먼저 패키지를 설치한다.

  ```bash
  npm install vue-burger-menu --save
  ```

- 기본적으로 페이지의 `<script>` 태그에서 아래와 같이 입력하면 사용할 수 있다.

  ```javascript
  import { Slide } from 'vue-burger-menu'  // import the CSS transitions you wish to use, in this case we are using `Slide`
  
  export default {
      components: {
          Slide // Register your component
      }
  }
  ```

- 위의 Github 페이지에서 다양한 사용법을 확인할 수 있다.



***Copyright* © 2021 Song_Artish**