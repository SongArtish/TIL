# React 프로젝트 Github Pages 배포하기

---

[TOC]

---



## GitHub Pages

GitHub Pages는 GitHub Repository를 이용해 웹 사이트를 무료로 호스팅해주는 서비스이다. 

사용자가 GitHub Repository에 자신의 웹 프로젝트 빌드 결과물을 업로드하면 GitHub가 그 결과물을 호스팅해준다.



## Git Repository 최신화

GitHub에 Repository를 생성하고 `git push`를 통해 원격 저장소에 최신화된 React 프로젝트를 업로드한다.



## gh-pages 패키지 설치

`gh-pages` 패키지를 설치한다.

```bash
npm install gh-pages
```



## package.json 수정

package.json 파일에 `"homepage": "https://{GitHub username}.github.io/{Repository name}"`를 추가한다.

```json
// package.json
    ...
    "browserslist": {
        "production": [
        ">0.2%",
        "not dead",
        "not op_mini all"
        ],
        "development": [
        "last 1 chrome version",
        "last 1 firefox version",
        "last 1 safari version"
        ]
    },
    "homepage": "https://{GitHub username}.github.io/{Repository name}" // 추가
    ...
```

package.json의 scripts 부분에 `"deploy": "gh-pages -d build", "predeploy": "npm run build"`를 추가해준다

```json
// package.json
...
 "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "deploy": "gh-pages -d build",
    "predeploy": "npm run build"
  },
...
```

- npm run build: 현재 프로젝트 코드를 빌드한다.
- gh-pages -d build: build 디렉토리 (-d)에 있는 파일을 GitHub Pages에 업로드한다.



## GitHub Pages에 빌드 결과물 업로드

최종적으로 빌드 결과물을 GitHub Pages에 업로드하기 위해 아래 명령어를 입력한다.

```bash
npm run deploy
```

명령어 처리가 끝나고, package.json의 `homepage`에 입력했던 주소로 접속하면 프로젝트가 성공적으로 배포된 것을 확인할 수 있다.



***Copyright* © 2022 Song_Artish**