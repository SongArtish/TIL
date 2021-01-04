# Project Deploy

2020.11.13

> `Netlify`라는 정적 웹 포스트 사이트를 통해 작성한 프로젝트를 배포한다.

---

[TOC]

---



## 준비하기

- 작성한 Vue 프로젝트에서 다음의 명령어를 입력한다.

```bash
$ npm run build
```

- 폴더 구조 상단에 `dist` 폴더가 생성된다.



## 배포하기

> [Netlify](https://www.netlify.com/) 사이트에서 진행한다.

- 사이트 로그인 후 페이지의 `Sites` 배너를 클릭한다.
- `site 폴더` (Vue 폴더 구조에서는 `dist` 폴더)를 사이트에 Drag and Drop 한다.

**설정하기**

- 배포된 사이트 url을 클릭한다.
- `site settings > site details > change sitename`에 들어가면 사이트 주소를 변경할 수 있다.



## 관리하기

> 배포한 사이트 관리하기

- `Sites` 배너 메뉴를 클릭한다.
- 우측 상단 `New site from Git` 버튼을 클릭한다.
- `Continuous Deployment > Github`에서 프로젝트를 가져온다.
- 이후 아래와 같이 입력한다.

---

Build command

```
npm run build
```

Publish Directory

```
dist/
```

---

- `유튜브 검색 사이트 프로젝트`의 경우 API 키 값이 필요하기 때문에 아래의 단계도 진행해준다.

  -  `Advanced build settings`에서 환경변수를 설정해준다.

    Key

    ```
    VUE_APP_YOUTUBE_API_KEY
    ```

    Value

    ```
    <Youtube API Key 값>
    ```

---

- 이후 `git push`를 해주면 사이트에서 자동으로 프로젝트를 building 해준다.



***Copyright* © 2020 Song_Artish**