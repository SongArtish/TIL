# Plugins

---

[TOC]

---



## 사용법

> [vue-js-toggle-button](https://www.npmjs.com/package/vue-js-toggle-button)을 등록하고 사용하는 법을 다룬다.

### npm 설치

- 먼저 Node 패키지를 설치한다.

```bash
npm install vue-js-toggle-button --save
```

### 플러그인 등록

- :ballot_box_with_check: 플러그인은 `src > main.js`에서 등록해준다!!

```javascript
// main.js

import ToggleButton from 'vue-js-toggle-button'
Vue.use(ToggleButton)
```



## bootstrap-vue

- bootstrap npm을 설치한다.

```bash
$ npm install vue bootstrap-vue bootstrap
```

- 해당 패키지를 등록한다. 자세한 내용은 [공식홈페이지](https://bootstrap-vue.org/docs)를 참조한다.
- CDN을 사용할 경우, `index.html`에 넣어준다.
- :white_check_mark: Vue에서는 npm으로 관리하기 때문에 되도록이면 CDN을 사용하지 않는 편이 좋다!!



## packery

> draggable한 레이아웃을 디자인할 수 있다.
>
> [github](https://github.com/metafizzy/packery)

![packery](img/packery.png)



## vue-burger-menu

> 좌/우에 햄버거 메뉴바를 만든다.
>
> [github](https://github.com/mbj36/vue-burger-menu)

![vue-burger-menu](img/vue-burger-menu.png)



## vue-glide-js

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



## vue-js-toggle-button

> 심미적인 토글 버튼을 가져올 수 있다.
>
> [github](https://github.com/euvl/vue-js-toggle-button#readme)

![vue-js-toggle-button](img/vue-js-toggle-button.png)



## vue-select

> 깔끔한 드랍다운 선택창을 가져올 수 있다.
>
> [github](https://github.com/sagalbot/vue-select)

![vue-select](img/vue-select.png)



## vue-slick-carousel

> `이미지 넘기기` 등에 사용할 수 있는 슬라이드 기능을 가져올 수 있다.
>
> [github](https://github.com/gs-shop/vue-slick-carousel)

![vue-slick-carousel](img/vue-slick-carousel.png)



***Copyright* © 2021 Song_Artish**