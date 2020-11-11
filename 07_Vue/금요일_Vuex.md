# Vue SFC & Router

2020.11.11

> Vue Single File Component와 Router





node 설치

```bash
$ node -v
```



- `Node`를 설치하면 `npm`이 자동으로 설치된다.

- `bash` 창에서 Vue CLI를 설치하기 위해 다음의 명령어를 입력한다.

```bash
$ npm install -g @vue/cli
# g (global)
```

- 설치가 완료되면 잘 설치가 되었는지 버전을 확인한다.

```bash
$ vue --version
```





프로젝트 생성

```bash
$ vue create <프로젝트명>
```

- 이후 프로젝트 폴더로 이동해서 서버를 실행한다.

```bash
$ npm run serve
```



```bash
$ vue add router
```







- lodash 설치

```bash
$ npm install lodash
```



component 사용

1. 불러온다.
2. 등록한다.
3. 보여준다.



- 불러온다

```javascript
import HelloWorld from '@/components/HelloWorld.vue'
```

- 골뱅이 `@` 는 `/src` 위치를 나타낸다.
- 등록한다

```javascript
export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
```

- 보여준다.

```vue
<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>
```





- 다음과 같이 별명으로도 주소를 지정할 수 있다.

```vue
<router-link :to="{ name: 'TheLunch'}">TheLunch</router-link> |

```



## Pass Props & Emit Events

> 데이터 단방향 흐름
>
> - 부모에서 자식으로 흐른다. (Pass Props)
> - 자식...

![Pass Props & Emit Events](img/pass_props&emit_events.png)



- emit

```javascript
this.$emit(<이벤트>, <데이터>)
```



```javascript
this.$emit('input-change', event.target.value)
```







환경변수를 사용하여 API 키를 관리한다.

https://cli.vuejs.org/guide/mode-and-env.html#modes

```markdown
.env                # loaded in all cases
.env.local          # loaded in all cases, ignored by git
.env.[mode]         # only loaded in specified mode
.env.[mode].local   # only loaded in specified mode, ignored by git
```

```
# .env.local

VUE_APP_YOUTUBE_API_KEY=<API 키>
```



