# <실습> Youtube 검색 사이트 만들기

---

[TOC]

---





## Overview

![](img/youtube_project_structrue.png)

## :arrow_forward: 시작하기

> Youtube API 키를 발급받는다.

- [Google API Console](https://console.developers.google.com/)에 접속하여 로그인
- `YouTube Data API v3` 검색 후 다운로드
- 왼쪽 상단 `Google APIs` 로고 옆에 프로젝트를 생성한다.
- 메뉴 > API 및 서비스 > 사용자 인증 정보 > API 발급
- 발급된 API 키의 `이름` 클릭
- 세부사항에서 `선택한 API`에서 `Youtube Data API v3` 선택 후 저장

## :arrow_forward: 컴포넌트 생성

- 구조에 따라 컴포넌트를 생성하고 `App.vue`에서 하위 컴포넌트들을 등록해준다. (가져오기, 등록하기, 보여주기!!!)

## :arrow_forward: Input 데이터 가져오기 (emit)

- input 태그에서 `v-on`으로 이벤트와 실행할 함수를 등록한다.

```vue
<!-- SearchBar.vue -->
<input type="text" @keyup.enter="onEnter">
```

- 실행할 함수가 상위 컴포넌트에 데이터를 emit하도록 정의해준다.

```javascript
onEnter: function (event) {
    this.$emit('search', event.target.value)
}
```

- 상위 컴포넌트에서 emit되어 온 데이터를 받아준다.

```vue
<!-- App.vue -->
<SearchBar @search="onSearch" />
```

- `onSearch` 함수를 정의해준다.

```javascript
methods: {
    onSearch: function (text) {
        console.log(text)
    }
}
```

## :arrow_forward: axios 설치 및 작성

> [Youtube API 사이트](https://developers.google.com/youtube/v3/docs/search/list?hl=ko) 문서를 참조한다.

- axios를 모듈로 설치한다.

```bash
$ npm install --save axios
```

- axios를 스크립트에서 불러온다.

```javascript
import axios from 'axios'
```

- API_URL을 가져와서 변수로 작성한다.

```javascript
// App.vue
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
```

- axios 요청을 하는 코드를 작성한다.

```javascript
axios.get(url, params)	// 필수 매개인자가 필요하다.
```

- [문서](https://developers.google.com/youtube/v3/docs/search/list?hl=ko)를 참고해서 필수 매개인자를 다음과 같이 작성한다.

```javascript
// App.vue
onSearch: function (text) {
      axios.get(API_URL, {
        params: {
          key: '',
          part: 'snippet',
          type: 'video',
          q: text
        }
      })
    }
```

- `key` 값은 노출이 되면 안되기 때문에 다음의 과정으로 관리한다.

## :arrow_forward: API 키 관리

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

- 그래서 다음과 같이 `vue` 파일에서 key 값을 가져온다.

```javascript
// App.vue
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
```

## :arrow_forward: axios 로직 완성하기

- `video`라는 데이터를 정의해준다.

```javascript
data: function () {
    return {
      videos: []
    }
```

- 그리고 promise 객체로 axios 로직을 완성해준다.

```javascript
// App.vue
onSearch: function (text) {
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: text
        }
      }).then (res=>
      // console.log(res.data.items)
      this.videos = res.data.items
      .catch(err => console.log(err))
    }
```

## :arrow_forward: Props

- 데이터를 넘겨준다.

```vue
<!-- App.vue -->
<VideoList videos="videos" />
```

- 하위 컴포넌트에서 데이터를 받아준다.

```javascript
// VideoList.vue
props: {
  videos: Array
}
```

## :arrow_forward: VideoListItem (하위 컴포넌트) 생성 및 Props

- `VideoListItem`이라는 vue 파일을 생성한다.
- `VideoList.vue`의 하위 컴포넌트로 등록한다.
- `VideoList`에서 받아온 

```vue
VideoListItem 
        v-for="(video, idx) in videos"
        :key="idx"
      /> <!-- 키 값이 없기 떄문에 오류가 발생한다. -->
```

```vue
        v-for="video in videos"
        :key="video.etag"
```

- 결국,  `:key`은 키 값으로 쓸 고유값을 넘겨주면 되는 것이다.

## :arrow_forward: 비디오 리스트 표시하기

- 받아온 `video`의 데이터 구조를 확인하고 다음과 같이 코드를 작성한다.
- :white_check_mark: 데이터 구조를 꼭 확인하도록 한다!!

```vue
<!-- VideoListItem.vue > <template> -->
<li>
    <img :src="video.snippet.thumbnails.default.url" alt="">
    <span>{{ video.snippet.title  }}</span>
</li>
```

- `:src`의 값이 너무 길기 때문에 `computed`를 사용해서 다음과 같이 코드를 작성할 수도 있다.

```javascript
// VideoListItem.vue > <script>
computed: {
    imgSrc: function () {
      return this.video.snippet.thumbnails.default.url
    }
  }
```

```vue
<!-- VideoListItem.vue > <template> -->
<img :src="imgSrc" alt="">
```

## :arrow_forward: filters 적용

> `video.snippet.title`을 출력하면 이상한 문자들이 같이 출력되는데, 이를 없애주기 위해서 filter를 적용한다.

- 먼저 `lodash`를 불러온다.

```javascript
// VideoListItem.vue
import _ from 'lodash'
```

- filters 메서드를 사용해서 `unEscape`라는 함수를 선언해준다.

```javascript
filters: {
    unEscape: function (text) {
        return _.unescape(text)
    }
```

- 생성해준 filters 함수는 다음과 같이 적용할 수 있다.

```vue
<span>{{ video.snippet.title | unEscape  }}</span>
```



## :arrow_forward:  최하위 컴포넌트 데이터  emit

> 앞서 했던 emit 로직을 그대로 적용하여, 최하위의 `VideoListItem.vue`의 selectedVideo라는 데이터를 `App.vue`로 올려준다.

- 먼저 최하위 컴포넌트에 emit할 이벤트를 만들어준다.

```vue
<li @click="selectVideo">
    <img :src="imgSrc" alt="">
    <span>{{ video.snippet.title | unEscape  }}</span>
</li>
```

- 올려준다 (`VideoListItem -> VideoList`)

```javascript
// VideoListItem.vue
methods: {
    selectVideo: function () {
        this.$emit('select-video', this.video)
    }
}
```

- 받아준다.

```vue
<!-- VideoList.vue -->
      <VideoListItem 
        v-for="video in videos"
        :key="video.etag"
        :video="video"
        @select-video="selectVideo"
      />
```

- 이벤트를 받는 함수를 생성해주고 `App.vue` 로 다시 emit해준다. (`VideoList -> App`)

```javascript
// VideoList.vue
methods: {
    selectVideo: function (video) {
        this.$emit('select-video', video)
    }
```

- `App.vue`에서 받아준다.

```vue
<!-- App.vue -->
<VideoList :videos="videos" @select-video="selectVideo" />
```

- 이벤트 emit으로 받은 데이터를 저장해줄 데이터를 생성한다.

```javascript
// App.vue
selectedVideo: '',
```

- 이후, emit 이벤트를 받는 함수를 생성해준다.

```javascript
// App.vue
selectVideo: function (video) {
    this.selectdVideo = video
}
```

## :arrow_forward: detail에 비디오 prop

> `VideoDetail.vue` 파일에 `VideoListItem`으로부터 받은 `selectedVideo`파일을 prop한다.

- 보내준다. (`App -> VideoDetail`)
  - `App.vue`의 `selectedVideo`를 `VideoDetail.vue`에 `video`라는 이름으로 보내준다.

```vue
<!-- App.vue -->
<VideoDetail :video="selectedVideo" />
```

```javascript
// App.vue
data: function () {
    return {
        selectedVideo: null,	// 보내줄 selectedVideo는 null 값을 입력해준다.
        videos: [],
    }
```

- 받아준다.

```javascript
props: {
    video: Object
},
```

## :arrow_forward: `<iframe>` 태그 사용

> `<iframe>` 태그를 이용하여 detail을 표시한다. (@`VideoDetail.vue`)
> [IFrame Player API 문서](https://developers.google.com/youtube/player_parameters?hl=ko)
>
> - `<iframe>`에 로드할 동영상의 주소를 다음과 같은 형식을 가진다.
>
> ```
> https://www.youtube.com/embed/VIDEO_ID
> ```

- `VideoDetail.vue`의 `<template>` 태그에는 다음과 같이 코드를 작성하면 된다.

```vue
<!-- VideoDetail.vue --> <!-- 완성코드 -->
<div v-if="video">
    <iframe :src="videoURI" frameborder="0"></iframe>
    <h1>{{ video.snippet.title | unEscape }}</h1>
    <p>{{ video.snippet.description | unEscape }}</p>
</div>
```

- 더 나은 처리를 위해서 아래의 3가지 디테일한 처리를 해준다.

### (1) 비디오 표시

- `App.vue`에서 `selectedVideo`는 기본적으로 null 값으로 정의한다.

```javascript
selectedVideo: null,	// 보내줄 selectedVideo는 null 값을 입력해준다.
```

- 이러한 비디오가 없을 경우에는 `VideoDetail`에서 표시하지 않도록 조건문을 추가해준다.

```vue
<div v-if="video">
```

### (2) videoURI computed

- `computed` 속성을 활용하여 `videoURI`의 값을 리턴해준다.

```javascript
computed: {
    videoURI: function () {
        const { videoId } = this.video.id
        // const videoId = this.video.id.videId
        return `https://www.youtube.com/embed/${videoId}`	 // backtick
    }
},
```

```vue
<iframe :src="videoURI" frameborder="0"></iframe>
```

### (3) filter

- 위에서와 같이 `lodash`를 불러온 후, filter로 title을 처리해준다.

```javascript
import _ from 'lodash'
filters: {
    unEscape: function (text) {
        return _.unescape(text)
    }
}
```

```vue
<h1>{{ video.snippet.title | unEscape }}</h1>
<p>{{ video.snippet.description | unEscape }}</p>
```

## :arrow_forward: 스타일링 (CSS)

- 이후 자유롭게 스타일링하면 된다.



***Copyright* © 2020 Song_Artish**

