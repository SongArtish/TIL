# <실습> Vue CLI 프로젝트

---

[TOC]

---



## :arrow_forward: 시작하기

**설치하기**

- `Vue CLI`를 설치한다.

```bash
$ npm install -g @vue/cli
```

- `package.json`에 들어있는 모듈 패키지를 설치한다.

```bash
$ npm install
```

- 혹은 다음의 명령어도 사용할 수 있다.

```bash
$ npm i
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



## :arrow_forward: 컴포넌트 등록

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



## :arrow_forward: view 작성

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
  - `<template>` 태그 안에 하나 이상의 태그가 존재해야 한다!

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



## :arrow_forward: 데이터 입력

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



## :arrow_forward: 클릭 이벤트 발생

- HTML에서 사용할 경우, @click 혹은 v-on:click 디렉티브를 사용할 수 있었다.
- Component의 경우, v-on:click.native의 형태로 native 이벤트라는 사실을 명시해 줘야한다.



## :arrow_forward: lodash 설치

- npm에 lodash를 설치한다.

```bash
$ npm install lodash
```

- view의 `<script>` 태그 안에서 `lodash`를 import 한다.

```javascript
import _ from 'lodash'
```



***Copyright* © 2020 Song_Artish**

