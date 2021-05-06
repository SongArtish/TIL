# Pug

> 요새 가장 핫한 **Node Express Template Engine**

2021.05.06

---

[TOC]

---



## 개념

- HTML을 PUG 문법으로 작성하면 HTML로 변환해준다.
- express의 패캐지 `view engine`이다.

### 특징

- 마크업 문법보다 코드량이 적어 생산성이 좋다
- JS 연산 결과를 쉽게 보여줄 수 있다.
- 정적인 부분과 동적인 부분을 구분할 수 있다.



## 설치하기

- **npm** 명렁어로 설치한다.

```bash
npm install pug
```

- 설치 후, ` views`라는 폴더를 생성하고 `.pug` 확장자의 파일을 만들어서 사용할 수 있다.
- **Vue**에서는 root폴더에 **webpack.config.js**파일을 생성하고 아래와 같이 코드를 입력한다.

```javascript
module.rules = {
  test: /\.pug$/,
  loader: 'pug-plain-loader'
}
```



## 문법

> **PUG**에서는 **탭**이 매우 중요하다.

- 아래와 같이 탭을 하면 안에 자식 노드가 형성된다.
- 탭을 안하면 동등한 형제 노드가 된다.

```html
//main.pug

doctype html
html
	head
		title Wetube
	body
		main
			block content
	footer
		span &copy: WeTube

```



***Copyright* © 2021 Song_Artish**