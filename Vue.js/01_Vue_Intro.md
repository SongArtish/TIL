# Vue Intro

---

[TOC]

---



## Overview

자바스크립트 프레임워크에는 대표적으로 `React`, `Angular`, `Vue` 가 있다. `Vue.js`는 UI를 만들기 위한 progressive framework이다. `Vue.js`를 통해 동적으로 DOM을 조작할 수 있다. Vue.js의 특징은 다음과 같다.

- CSR(Client Side Rendering)
- SPA(Single Page Application)'



## 작성 순서

Vue.js의 작성 순서는 다음과 같다.

```markdown
1. Data
2. DOM
```



## MVVM 패턴

Vue.js는 `Model`, `View`, `ViewModel`의 **MVVM 패턴**을 가진다.

|               |                     |                             역할                             |
| :-----------: | :-----------------: | :----------------------------------------------------------: |
|   **Model**   | 자바스크립트 Object |                    화면에 표현되는 데이터                    |
|   **View**    |      DOM(HTML)      |                      사용자가 보는 화면                      |
| **ViewModel** |  모든 Vue Instance  | View에서 보여줄 데이터 정의 및 처리<br />Model과 상호작용하며 데이터 주고 받음 |



## 시작하기

npm을 이용하여 `vue-cli`를 설치한다.

```bash
$ npm install -g @vue/cli
```

[Vue.js 공식문서](https://kr.vuejs.org/v2/guide/index.html)를 참고하여 CDN을 가져온다.

```html
<!-- 개발버전, 도움되는 콘솔 경고를 포함. -->
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

```html
<!-- 상용버전, 속도와 용량이 최적화됨. -->
<script src="https://cdn.jsdelivr.net/npm/vue"></script>
```

이외에도 편리한 extension을 설치할 수 있다. 먼저 Chrome 웹 스토어 tool을 설치한다. 이 tool을 이용하면 Vue로 작성된 페이지가 어떻게 구성되었는지 확인할 수 있다.

```markdown
- Vue.js devtools
```

Chrome 개발자도구(`F12`)의 `Vue` 탭에서 해당 페이지의 구성을 확인할 수 있다. 만약, 로컬에서 작성한 `HTML`을 로드하였을 때 확장 프로그램이 실행되지 않는다면 `확장 프로그램 > 세부정보 > 파일 URL에 대한 액세스 허용`을 활성화해준다.

Vue.js 사용에 필요한 VS Code extension은 다음과 같다.

```markdown
- Vetur		// `Vue.js`의 자동 완성 등을 담당한다.
- Live Server	// VS Code에서 사용하는 서버로, 로컬 서버 변경을 자동 반영한다.
- Vue 3 Snippets	// Vetur에서 지원하지 않는 자동완성까지 적용
```

추가로, `Prettier`을 사용하면 편리하다. `Prettier`은 file >> preference >> setting or Ctrl + ,(comma)`에서 설정할 수 있다.



***Copyright* © 2020 Song_Artish**