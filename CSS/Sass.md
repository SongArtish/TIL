# Sass

> Syntactically Awesome Style Sheets

2021.04.23

---

[TOC]

---



## Sass

>  하나의 CSS Preprocessor(전처리기)

- CSS 문법과 유사
- 선택자의 중첩(Nesting), 조건문, 반복문, 다양한 단위(unit)의 연산 등 사용 가능



## SCSS

> Sass의 3버전에서 새롭게 등장학 SCSS는 CSS 구문과 완전히 호환되도록 새로운 구문을 도입해 만든 Sass의 모든 기능을 지우너하는 CSS 상위집합(superset)

- `{}`(중괄호)와 `;`(세미콜론)의 유무

Sass

```css
.list
	width: 100px
	float: left
	li
		color: red
		background: url("./image.jpg")
		&:last-child
			margin-right: -10px
```

SCSS

```css
.list {
    width: 100px;
    float: left;
    li {
        color: red;
        background: ulr("./image.jpg");
        &:last-child {
            margin-right: -10px;
        }
    }
}
```



## npm에서의 사용

- npm에서 sass를 사용하기 위해서는 다음과 같이 패키지를 설치해주어야 한다.

```bash
$ npm i sass-loader
```

```bash
$ npm i node-sass
```



***Copyright* © 2021 Song_Artish**