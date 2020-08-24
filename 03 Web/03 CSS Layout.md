# CSS Layout

*****

[TOC]


*****



## CSS page layout techniques

> 웹 페이지에 포함되는 요소들을 취합하고, 그것들이 어느 위치에 놓일 것인지를 제어하는 기술.
>
> 1. display - block, inline, inline-block
> 2. position - static(default), relative, absolute, fixed
> 3. **Float**
> 4. **Flexbox**
> 5. **Grid**
> 6. 기타: Table layout, Multiple-column layout

*****



## 1. Float

> 자기 자신의 위치를 주변의 콘텐츠로부터 상대적으로 배치하는 속성이며, inline이나 텍스트 요소를 감싼다. Float된 이미지 좌, 우측 주변으로 텍스트를 둘러싸는 레이아웃을 위해 도입되었다.

### 1.1 Float 속성

- none : 기본값
- left : 요소를 왼쪽으로 띄움
- right : 요소를 오른쪽으로 띄움

```css
/* Float 예시 */
.left {
    float: left;
}
.right {
      float: right;
}
```

### 1.2 Float clear

> float 속성을 적용한 요소의 부모요소에 적용해 float를 무시한다.

```css
.clearfix::after {
      /* 빈 content를 만든다*/
      display: block;
      clear: both;
      content: "";
}
/* header 태그 다음에 가상 요소(::after)로 내용이 빈 블럭을 만들고*/
/* 이 가상 요소는 float left, right(both)를 초기화한다. */
```




![float와 flex의 차이](img\float_and_flex.jpg)

- column의 높이가 자동으로 맞춰진다.



## 2. Flexbox

> 요소 간 공간 배분과 정렬 기능을 위한 1차원(단방향) 레이아웃
>
> - 요소
>   - Flex Container (부모 요소)
>   - Flex Item (자식 요소)
> - 축
>   - main axis (메인축)
>   - cross axis (교차축)

```css
.flex-container {
    display: flex;
    display: inline-flex;
}
/*flex가 block이라면, inline-flex는 inline의 특성을 가지고 있다*/
```

![flex와 inline-flex](img\inline-flex.jpg)

### Flex에 적용하는 속성

### 2.1 배치 방향 설정 :  `flex-direction`

> 메인 축(main-axis) 방향을 변경한다. flexbox는 단방향 레이아웃이기 때문이다.

```css
flex-direction: row;		/* default */
flex-direction: row-reverse
flex-direction: column
flex-direction: column-reverse
```

### 2.2  메인축 방향 정렬 : ``justify-content``

```css
justify-content: flex-start;	/*default*/
justify-content: flex-end;
justify-content: center;
justify-content: space-between;	/* 좌우정렬: 컨텐츠 사이에 space를 넣고 균등정렬*/
justify-content: space-around;	/* 균등좌우정렬: 컨텐츠 좌우로 각각 space가 들어간다*/
justify-content: space-evenly;	/* 균등정렬: 컨텐츠 처음/끝은 그리고 사이에 space*/
```

![space 속성들 비교](img\space_attributes.jpg)

### 2.3 교차축 방향 정렬 : ``align-items`, `align-content`, `align-self`

> - content - 여러 줄을 한 단위로 적용
> - items - 한 줄 단위로 적용
> - self - 선택한 item 한 개에 적용

```css
align-content: flex-start;
align-content: flex-end;
align-content: center;
align-content: stretch;
align-content: space-between;
align-content: space-around;
```

```css
align-itmes: flex-start;	/* 크로스축 start만큼만 정렬 */
align-itmes: flex-end;
align-itmes: center;
align-itmes: baseline;		/* item들을 텍스트 baseline 기준으로 정렬.*/
```

```css
align-self: auto;
align-self: flex-start;
align-self: flex-end;
align-self: center;		/* 자식 요소 하나에만 정렬*/
align-self: baseline;
align-self: stretch;	/* item이 크로스축의 크기를 채우기 위해 늘어난다. */
```

### 2.4 기타: `flex-wrap`, `flex-flow`, `flex-grow`, `order`, ~~flex-shrink~~, ~~flex-basis~~

- `flex-wrap`: 남는 부분을 감싸고 아래로 떨어뜨린다.

```css
flex-wrap: wrap;
flex-wrap: wrap-reverse;
```
- `flex-flow` : flex-direction과 flex-wrap 축약형

```css
flex-flow: column wrap;
```
- `flex-grow` : 남은 여백을 분배하는 방법. 음수 값은 사용할 수 없다.

```css
flex-grow: 1;

.item1 {
    flex-grow: n;
}
.item2 {
    flex-grow: m;
}
/* 여백을 n+m 만큼 등분해서 각각 n, m만큼 준다.*/
```
- `order`: order 값을 매겨 순서를 이동한다. 음수 값을 사용할 수 있다.

```css
order: 0;		/* default */
order: 1;		/* order가 0인 항목들 뒷 순서로 이동한다.*/
order: -1;
```

[Flexbox 연습](https://flexboxfroggy.com/#ko) - Flexbox Frog를 통해 flexbox 활용방법을 익힌다.



## 3. Bootstrap

> 트위터에서 만든 front-end 오픈소스 라이브러리이다.
>

[Bootstrap Documentation](https://getbootstrap.com/docs/4.5/getting-started/introduction/) - 항상 documentation을 참고하여 활용하도록 한다.

### Bootstrap 시작하기

- CDN 코드 붙여넣기
- `.container` 박스 만들기

### Reset CSS

> 모든 HTML 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축된 규칙 세트.
>
> CSS를 초기화 하는 방법에는 2가지가 있다.
>
> 1. **reset CSS**: aggressive solution. 브라우저 자체 스타일을 모두 제거한다.
> 2. **Normalize CSS**: gentle solution. 웹 표준을 준수하는 방식이다.
>
> 현재는 Normalize CSS 를 중심으로 사용하고 여기에 적절한 Reset CSS 을 섞어 쓰라고 권장한다. Bootstrap 역시 noramlize 방식을 통해 CSS 초기화를 한다

### 3.1 CDN (Content Delivery Network)

> 컨텐츠 (CSS, JS, Image, Text 등)를 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템

```html
<!-- 사용방법 -->

<!-- css 파일은 head에서 link 태그로 가져온다.-->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

<!-- js(javascript) 파일은 body 끝나기 직전, script 태그로 가져온다.-->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
```

- 자바가 쓰이는 이유 - component 중 `Modal(검은화면 팝업 표시)` 등을 사용하기 위해서



### 3.2 Color

> 배경화면 색을 나타내는 class로는 `.bg-primary`, `.bg-seconday`, `.bg-success`, `.bg-info`, `.bg-warning`, `.bg--danger`, `.bg--light`, `.bg-dark` 등이 있다.

```html
<!-- 사용예시 -->
<h2>Color</h2>
<p class="text-primary">.text-primary</p>
<p class="text-secondary">.text-secondary</p>
<p class="text-success">.text-success</p>
```

### 3.3 spacing

| alphabet | full name |
| :------: | :-------: |
|    m     |  margin   |
|    p     |  padding  |

| alphabet |      full name      |
| :------: | :-----------------: |
|    t     |         top         |
|    b     |       bottom        |
|    l     |        left         |
|    r     |        right        |
|    x     | x-axis(left, right) |
|    y     | y-axis(top, bottom) |

| class name | rem  |  px  |
| :--------: | :--: | :--: |
|    mt-0    |  0   |  0   |
|    mt-1    | 0.25 |  4   |
|    mt-2    | 0.5  |  8   |
|    mt-3    |  1   |  16  |
|    mt-4    | 1.5  |  24  |
|    mt-5    |  3   |  48  |

- rem은 html(rout)의 기본 크기인 16px을 기준으로 한다.

```html
<!-- 사용예시 -->
<h2>Spacing</h2>
<div class="box sticky-top bg-primary"></div>
<div class="box sticky-top bg-success"></div>
<div class="box mt-3">margin-top 3</div>
<div class="box m-4">margin 4</div>
<div class="box mx-auto">margin x auto</div>
```

### 3.4 Responsive Web

> 별도의 기술 이름이 아닌, 같은 화면을 보는 다른 크기의 디바이스를 위한 웹 디자인에 대한 접근 방식, 반응형 레이아웃 작성에 도움이 되는 사례들의 모음 등을 기술하는데 사용되는 용어이다. 단일 소스로 multiuse 실현이 가능하다.
>
> - 예시) Media Queries, Flexbox, CSS Grid, The viewport meta tag



## 4. Bootstrap Grid System

> flexbox로 제작된 것으로, **`.container > .row > col-*`**으로 컨텐츠를 배치하고 정렬한다.
>
> - 12개의 column - 12가 약수가 많기 때문에
> - 5개의 grid breakpoints

```html
<!-- 기본 세팅 구조 -->
<div class="container">
    <div class="row">
        <div class="col"></div>
        <div class="col"></div>
        <div class="col"></div>
        ...
    </div>
</div>
```
- `<div class="container">`는 이하 요소를 중간으로 잡아주는 역할을 한다.

**`.row`**

- 각 column에는 공간 사이를 제어하기 좌우 padding 값이 있는데 이를 `gutter`라고도 한다.
- row의 margin 값과 gutter를 제거하려면 .row에 `.no-gutters` class를 사용한다.

```html
<!-- 사용예시 -->
<body>
  <div class="container">
    <h2 class="text-center">column</h2>
    <div class="row">
      <!-- 하나의 div가 12개의 col을 갖기 때문에 12개를 나눠서 크기를 갖는다.-->
      <div class="box col-1">1</div>
      <div class="box col-1">2</div>
      <div class="box col-1">3</div>
      <div class="box col-1">4</div>
      <div class="box col-1">5</div>
      <div class="box col-1">6</div>
      <div class="box col-1">7</div>
      <div class="box col-1">8</div>
      <div class="box col-1">9</div>
      <div class="box col-1">10</div>
      <div class="box col-1">11</div>
      <div class="box col-1">12</div>
      <!-- 13번 box는 12개 col을 초과하기 때문에 밑으로 내려간다.-->
      <div class="box col-1">13</div>
    </div>
    <hr>

    <div class="row">
      <div class="box col">1</div>
      <div class="box col">2</div>
      <div class="w-100"></div>
       <!-- width 100%인 가상의 요소를 만들어 강제로 줄을 바꿔준다.-->
      <div class="box col">3</div>
      <div class="box col">4</div>
    </div>
</body>
```



[구글뉴스](https://news.google.com/) - 대표적인 예시

### 4.1 레이아웃

#### 4.1.1 Breakpoint

- 입력한 size의 이상의 값들에 속성을 모두 적용한다!!!!!!

|    Size     | Grid options |     px     |
| :---------: | :----------: | :--------: |
| Extra Small |    (생략)    |    ~575    |
|    Small    |     `sm`     | 576~767px  |
|   Middle    |     `md`     | 768~991px  |
|    Large    |     `lg`     | 992~1199px |
| Extra Large |     `xl`     |   1200px   |

```html
<!-- 화면 사이즈에 따라 item의 크기를 다르게 설정하기-->
<div class="item col-4 col-sm-2">
	<p>576px 미만 4 <br> 576px 이상 2</p>
</div>
```

#### 4.1.2 Hiding Elements

> `.d-{ }-none` 형태로, `{ }`에는 breakpoint의 사이즈가 들어가며, 해당 스크린 사이즈에는 숨기는 역할을 한다.
>
> 반대의 요소로는 `.d-{ }-block`이 있다.

```html
.d-none		<!-- 모든 스크린 사이즈에서 숨김(hidden) -->
.d-block	<!-- 모든 스크린 사이즈에서 표시(visible) -->
```

```html
<div class="box bg-warning d-sm-non d-md-block"><보이나 안보이나/div>
<div class="box bg-success d-md-non d-xl-block">보이나 안 보이나</div>
```

#### 4.1.3 Display

```html
<!-- 사용예시 -->
<h2>Display</h2>
<div class="d-inline p-2 bg-primary text-white">d-inline</div>
<div class="box bg-warning d-sm-none d-md-block">보이나 안보이나</div>
<div class="d-flex justify-content-sm-between">small일 때는 space-btw</div>
```

```html
<!-- display에서 자주 쓰는 class -->
.fixed-top
.fixed-bottom
```

#### 4.1.4 Nesting

> 그리드 안에 그리드를 넣는 것으로, **`.row > .col-* > .row > .col-*`**의 방식으로 중첩이 가능하다.

### 4.2 Component (요소)

> bootstrap에서 많이 쓰는 component로는 `alert`, `button`, `dropdown`, `card`, `navs`, `navbar`, `form` 등등이 있다.

#### 4.2.1 offset

> `offset-{screen size}-{n}`에서 screen size에 따라 앞의 n칸을 비워준다(띄워준다).

```html
<div class=".col-md-4 .offset-md-4 .offset-lg-2"></div>
<!--화면 사이즈가 md 이상일 경우 앞 4칸을 offset하고, lg의 경우 앞 2칸을 offset한다(비워준다). -->
```

#### 4.2.2 button

```html
<button type="button" class="btn btn-primary">Primary</button>
<button type="button" class="btn btn-secondary">Secondary</button>
<button type="button" class="btn btn-success">Success</button>
<button type="button" class="btn btn-danger">Danger</button>
<button type="button" class="btn btn-warning">Warning</button>
<button type="button" class="btn btn-info">Info</button>
<button type="button" class="btn btn-light">Light</button>
<button type="button" class="btn btn-dark">Dark</button>

<button type="button" class="btn btn-link">Link</button>
```

#### 4.2.3 Nav

```html
<!-- bootstrap documentation 복붙 -->
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Dropdown
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
```

*Copyright* © Song_Artish