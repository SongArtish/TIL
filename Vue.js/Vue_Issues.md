# Vue 이슈

> Vue 프로젝트를 하면서 겪었던 핵심적인 오류들을 정리하였다.

---

[TOC]

---



## vue-cli 관련

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



## Vuex 관련

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



## axios 관련

### CORS 문제

- Vue에서 BE로 axios 요청을 보냈는데, 아래와 같이 CORS 에러가 발생하였다.
- Spring Boot에서는 CORS 허용 코드를 입력하였다.

```
Access to XMLHttpRequest at 'http://localhost:8080/create/' from origin 'http://localhost:8081' has been blocked by CORS policy:
```

**해결 방안**

- axios 요청을 보낼 때 아래와 같이 `Access-Control-Allow-Origin`을 `headers`에 추가해준다.

```javascript
headers: {
    "Access-Control-Allow-Origin": "*",
}
```

### 415 Error

>**415 Unsupported Media Type**
>
>요청한 미디어 포맷은 서버에서 지원하지 않습니다. 서버는 해당 요청을 거절할 것입니다.

- axios POST요청으로 데이터를 서버로 보냈는데, 415 에러가 반환되었다.

**해결 방법**

- headers에 `Content-Type`을 입력한다.
- 보내는 데이터(context)를 JSON 문자열로 변환한다.

```javascript
headers: {
    'Content-Type': 'application/json;charset=UTF-8',
},
data: JSON.stringify(context),
```



## JavaScript 관련

### `.js` import가 안 될 때

- 다른 외부 `.js` 파일을 Vue 프로젝트에서 import를 하려고 하는데 되지 않았다.

**해결 방법**

- 먼저 import할 컴포넌트에서 아래와 같이 코드를 작성하여 가져와준다.

```javascript
// CardPlay.vue
import CMRotate from '@/assets/js/CMRotate.js'
```

- 그리고 해당 `.js` 파일의 제일 아래에 `export`문을 작성하여 내보낼 수 있도록 한다.

```javascript
// .CMRotate.js
export default CMRotate;
```



## CSS 관련

### 로컬 이미지 가져오기

- Vue의 `<style>` 태그에서 로컬이미지를 가져오는데, 기존에 사용해보았던 문법으로 시도해 보았지만 어려움이 있었다.

**해결 방법**

- 다음과 같은 문법을 사용한다.

```css
background-image: url("~@/assets/bgs/create_hall.png");
```

### autofocus 미작동

- Vue에서 `$router.push`로 이동하는 경우 `<input>` 태그의 `autofocus` 속성이 작동하지 않았다.

**해결방법**

> 사용자 지정 디렉티브 관련 [Vue 공식문서](https://kr.vuejs.org/v2/guide/custom-directive.html)

- 먼저 사용자 지정 디렉티브를 등록한다.

```javascript
  directives: {
    focus: {
      inserted: function (el) {
        el.focus()
      }
    },
  },
```

- `<input>` 태그에 `v-focus`로 연결해준다.

```html
<input v-focus>
```



***Copyright* © 2021 Song_Artish**