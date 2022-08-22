# CSS 이슈

> 해결한 CSS 이슈를 정리한다.
>

---

[TOC]

---



## Background

### 1. 글자에 형광펜처럼 밑줄긋기

- 먼저 다음과 같이 전체 배경색을 적용하여 효과를 줄 수 있다.

![분홍색 밑줄 예시](img/0216_ul_pink.png)

```stylus
#underline_pink {
  background-color: #FF00DD;
  color: #fff;
}
```

- 다음과 같이 형광펜 같은 밑줄 느낌의 CSS를 적용할 수도 있다.

![노란색 밑줄 예시](img/0216_ul_yellow.png)

```stylus
#underline_yellow {
  background: linear-gradient(to top, #FFE400 50%, transparent 50%);
}
```



## Carousel

### 1. 이미지 크기를 고정하는 이슈

> Carousel에서 표시되는 크기가 다른 여러가지 이미지들의 크기를 일정하게 고정시킨다. (2021.02.09)

```markdown
#carousel #image #size #fix
```

- 전체 구조는 아래와 같다.

```html
<b-carousel
  id="carousel-1"
  v-model="slide"
  controls
  indicators
  background="#ababab"
  img-width="1024"
  img-height="480"
  style="text-shadow: 1px 1px 2px #333; width: 30em; height: 15em;"
  fade="true"
>
  <b-carousel-slide
    id="review_img"
    v-for="(item, index) in fileId"
    :key="index"   
    :img-src="url+`/review/download/` + item" 
  ></b-carousel-slide>
</b-carousel>
```

- 먼저 `<b-carousel>`의 스타일에서 고정하고자 하는 이미지 크기와 동일한 크기로 넓이와 높이를 설정해준다.
  - 여기서는 `width: 30em; height: 15em;`으로 설정하였다.
- 이후 이미지가 출력되는 `<img>` 태그 혹은 여기서는 `<b-carousel-slide>` 태그에 style 속성을 아래와 같이 설정한다.

```css
#review_img {
  top: 0;
  left: 0;
  min-width: 30em;
  min-height: 15em;
  max-width: 30em;
  max-height: 15em;
},
```

- `min-width`, `min-height`, `max-width`, `max-height` 값을 모두 설정하여 이미지 크기를 고정해준다.



## 기타

### 텍스트 드래그 방지

CSS를 통해 텍스트를 드래그 할 수 없도록 처리한다. 여기서는 클래스를 `stop-dragging`으로 정의하고, 해당 클래스에 CSS 코드 작성한다.

```css
.stop-dragging
{
  -ms-user-select: none; 
  -moz-user-select: -moz-none;
  -khtml-user-select: none;
  -webkit-user-select: none;
  user-select: none;
}
```



***Copyright* © 2021 Song_Artish**