# CSS (Cascading Style Sheets)

> 스타일, 레이아웃 등을 통해 문서(HTML)를 표시하는 방법을 지정하는 언어

*****

[TOC]

*****



## 1. 기초 문법

### 1.1 CSS 구문

- `선택자(Selector) - h1
- 속성(property): 값(value); = 선언(Declaration)

```html
<style>
    h1{
        color: blue;
        font-size: 15px;
    }
</style>
```

### 1.2 CSS 정의 방법

#### 1.2.1 인라인 \(inline)

> 해당 태그에 직접 `style` 속성을 활용

```html
<!-- 예시 -->
<body>
    <h1 style="color: blue; font-size: 100px;">Hello</h1>
</body>
```

#### 1.2.2 내부 참조(embedding) 

> head 태그 내에 `<style>`에 지정

```html
<!-- 예시 -->
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        h1 {
            color: blue;
            font-size: 100px;
        }
    </style>
</head>
```

#### 1.2.3 외부 참조(link file)

> 외부 CSS 파일을 `<head>`내 `<link>`를 통해 불러오기

```html
<!-- 예시 -->
<head>
    <title>mySite</title>
    <link rel="stylesheet" href="mystyle.css"
</head>
```



## 2. CSS Selectors

> HTML 문서에서 특정한 요소를 선택하여 스타일링 하기 위해서는 반드시 선택자(Selector)라는 개념이 필요하다.

### 2.1 선택자 종류

> 1. 기초 선택자  - 전체 선택자, 타입 선택자, 클래스 선택자, 아이디 선택자, 속성 선택자
> 2. 고급 선택자 - 자식 선택자, 자손 선택자, 형제 선택자, 인접 형제 선택자
> 3. 의사 클래스(pseudo class)

#### 2.1.1 전체 선택자

```css
* {
    color: red;
}
```

#### 2.1.2 타입 선택자

- 


```css
h2 {
	color: orange;
}
```
#### 2.1.3 클래스(class) 선택자

> 클래스 선택자는 마침표( .) 문자로 시작 하며 해당 클래스가 적용된 문서의 모든 항목을 선택

```css
.green {
    color: green
}
```

- 클래스 선택자가 설정된 `<div>` 태그 생성시, `.class_name`+`Enter`를 통해 생성할 수 있다.

#### 2.1.4 아이디(id) 선택자

> id 선택자는 샵(#)으로 시작하며, 문서 당 한 번만 사용할 수 있다.

```css
#purple {
    color: purple
}
```

#### 2.1.5 속성 선택자

```css
/* 예시 */
p {
	font-size: 30px;
}
```

#### 2.1.6 복합 선택자

- 자손 선택자: `selector A` `(blank)` `selector B`
- 자식 선택자: `selector A` > `selector B`

```css
/* 자손 선택자: class 박스 내 모든 p 태그를 의미 */
.box p {
    font-size: 30px
}
/* 자식 선택자: 클래스 박스 바로 안에 있는 p 태그를 의미 */
.box > p {
    font-size: 30px
}
```

#### 2.1.7 형제, 인접 형제 선택자

#### 2.1.8 의사 클래스(pseudo class)

- 링크, 동적 의사 클래스
- 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트 속성 선택자




### 2.2 CSS 적용 우선순위(cascading order)

#### 2.2.1 중요도(Importance)  

- `!important`
- 사용하지 않는 편이 좋다!

#### 2.2.2 우선 순위 (Specificity)

- inline/ id 선택자/ class 선택자 / 속성 선택자/ 요소 선택자/소스 순서
- 모두 `class` 선택자로 작성하는 것이 좋다

### 2.3 CSS 상속

> CSS는 상속을 통해 부모 요소의 속성(property)을 ~~모두~~ 자식에게 상속한다.
>
> - 상속 되는 속성: Text 관련 요소(font, color, text-align), opacity, visibility 등
> - 상속 되지 않는 속성:  Box model 관련 요소(width, height, margin, padding, border, box-sizing, display), position 관련 요소(position, top/right/bottom/left, z-index) 등

**`> p:nth-child(n)`과 `> p:nth-of-type(n)`**

```html
<!-- 예시 -->
<!-- p:nth-child(n) -->
<style>
    /* el:nth-child는 부모의 모든 자식들 중에 n번째인 요소가 "특정 el일 때" (아닐 경우 미출력) */
    /* id=ssafy의 자식 요소(>) 중 p의 (:) */
    #ssafy > p:nth-child(2) {
        color: red;
        }
</style>

<!-- p:nth-of-type(n) -->
<style>
    /* el:nth-of-type은 부모의 자식들 중 el요소들 중 n번째 */
    #ssafy > p:nth-of-type(2) {
        color: red;
        }
</style>

<!-- body -->
#ssafy>h2+p*4

<div id="ssafy">
    <h2>어떻게 선택 될까?</h2>
    <p>첫번째 단락</p>
    <p>두번째 단락</p>
    <p>세번째 단락</p>
    <p>네번째 단락</p>
</div>
```

- nth-child(n)은 부모 요소의 모든 자식 요소 중 n번째 태그를 지정하는 반면, 
  nth-of-type(n)은 부모 요소들의 특정 자식 요소 중  n번째 태그를 지정한다.



## 3. CSS 단위

### 3.1 (상대) 크기 단위

- px (픽셀) : 고정적인 단위. html 기본 폰트 사이즈는 16px이다.
- % ㅣ 백분율 단위. 가변적인 레이아웃에서 자주 사용
- em : 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가진다. 부모에 대해 상대적이기 때문에 상속의 영향을 받는다.
- rem : 최상위 요소인 html(root em, 16px)의 사이즈를 기준으로 배수 단위를 가지며, 상속의 영향을 받지 않는다.
- Viewport 기준 단위 : vw, vh, vmin, vmax (태블릿, 모바일 등의 디바이스에 적용할 때 사용)

### 3.2 색상 단위

3.2.1 색상 키워드

> 색상 키워드는 대소문자를 구분하지 않는 식별자로, red, blue, black처럼 특정 색을 나타낸다.

3.2.2 RGB 색상

- `#` + 16진수 표기법
- rgb() 함수형 표기법
- `a`는 alpha(투명도)가 추가된 것이다.

3.2.3 HSL 색상

> 색상, 채도, 명도를 통해 특정 색상을 표현하는 것. 마찬가지로 `a`는 alpha(투명도)가 추가된 것이다.

```html
<!-- black을 나타내는 다양한 방법 -->
p {color: black; }
p {color: #000; }
p {color: #000000; }
p {color: rgb(0, 0, 0); }
p {color: hsl(120, 100%, 0); }

p {color: rgba(0, 0, 0, 0.5); }
p {color: hsla(120, 100%, 0.5);}
```

### 3.3 CSS 문서 표현

3.3.1 텍스트

- 변형 서체(vs <b>, <i> vs <strong>, <em>)
- ~~자간, 단어 간격, 행간 , 들여쓰기~~
- ~~기타 꾸미기~~

3.3.2 컬러(color), 배경(background-image, background-color)

3.3.3 목록 꾸미기



## 4. CSS Box Model

### 4.1 Box Model

> 웹 디자인은 contents를 담을 box model을 정의하고 CSS 속성을 통해 스타일(배경, 폰트와 텍스트 등)과 위치 및 정렬을 지정하는 것.

![Box Model](img/css_box_model_box.png)

- Margin: 테두리 바깥의 외부 여백. 배경색을 지정할 수 없다.

```html
.margin {
	margin-top: 10px;
	margin-right: 20px;
	margin-bottom: 30px;
	margin-left: 40px;
}
```

- Border: <u>테두리 영역</u>

  > - border-style:solid;	- 실선
  > - border-style: dashed;    - 점선
```html
.border {
	border-width: 2px;
	border-style: dashed;
	border-color: black;
}

.border {
	border: 2px dashed balck;
}
```
- Padding: 테두리 안쪽의 내부 여백. 요소에 적용된 배경색, 이미지는 padding까지 적용

```html
.margin-padding{
	<!-- auto를 넣으면 가운데 정렬(좌우 값을 자동으로) -->
	margin: 0 auto;
	padding: 30px;
}
<!-- shorthand를 통해서 표현 가능하다.>
<!-- 순서는 상/우/하/좌 순으로 시계방향이다. -->
.margin-1 {margin:10px;}	<!-- 상하좌우 -->
.margin-2 {margin:10px 20px;}	<!-- 상하/좌우 -->
.margin-3 {margin:: 10px 20px 30px;}	<!-- 상/좌우/하 -->
.margin-4 {margin: 10px 20px 30px 40px;}	<!-- 상/우/하/좌(시계방향) -->
```

- Content: 글이나 이미지 등 요소의 실제 내용

### 4.2 box-sizing

> 기본적인 box-sizing의 대상은 **content-box**(Padding도 제외)이다.  다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원하며, 그 경우 box-sizing을 border-box로 설정한다.

### 4.3 마진 상쇄(Margin collapsing)

> block의 top 및 bottom margin이 때로는 (결합되는 마진 중 크기가) 가장 큰 한 마진으로 결합(combine, 상쇄(collapsed))된다. 때문에 인접 형제 요소 간의 margin이 겹쳐서 보일 때가 있다.



## 5. Display

> display CSS 속성은 요소를 블록과 인라인 요소 중 어느 쪽으로 처리할지와 함께 자식 요소를 배치할 때 사용할 레이아웃을 설정한다.

### block 레벨 요소와 inline 레벨 요소

- block 레벨 요소: `div / ul`, `ol`, `li / p / hr/ form` 등
- inline 레벨 요소: `span / a / img/ input`, `label / b`, `em`, `i`, `strong` 등

### 5.1 `blcok`

> 줄 바꿈이 일어나는 요소. 화면 크기 전체의 가로 폭을 차지하며 안에 inline 레벨 요소가 들어갈 수 있다. (line-height - 텍스트의 상하여백)
>
> - 수평 정렬: `margin-right: auto;`, `margin-left: auto;`, `margin-right: auto; margin-left: auto;`

### 5.2 `inline`

> 줄 바꿈이 일어나지 않는 행의 일부 요소. content 너비만큼 가로 폭을 차지하며, width, height, margin-top, margin-bottom을 지정할 수 없으며 상하 여백은 line-height로 지정한다.
>
> - 수평 정렬: `text-align: left;`, `text-align: right;`, `text-align:center;`
> - `vertical-align` : 형제 요소와  수직 정렬
> - `line-height:` : 줄 높이를 지정(글자의 높이를 지정). 한 줄인 경우, height와 같은 px 값을 지정하면 위아래 가운데 정렬이 된다.
>   두 줄의 경우 height(px)/2를 해주면 위아래 가운데 정렬이 된다.

### 5.3 `inline-block`

> block과 inline 레벨 요소의 특징을 모두 갖는다. inline처럼 한 줄에 표시 가능하며, block처럼 width, height, margin 속성을 모두 지정할 수 있다.

### 5.4 none

> 해당 요소를 화면에서 사라지게 하며 요소의 공간조차 사라지게 한다. 
>
> - `visibility: hidden;`은 해당 요소를 화면에서 사라지게는 하나 공간은 사라지지 않는다.



## 6. Position

### 6.1 `static` (default value)

> 기본적인 요소의 배치 순서에 따른다(좌측 상단). 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치된다.

```html
div {
	height: 100px;
	width: 100px;
	background-color: #9775fa;
	color: black;
	line-height: 100px;
	text-align: center
}
```

`static` 이외는 좌표 property(`top`, `bottom`, `left`, `right`)를 사용하여 이동이 가능 (음수 값도 가능)

### 6.2 `relative` (상대 위치)

> 상위 요소 중 relative 인 요소 위치를 기준으로 움직인다. static 위치를 기준으로 이동. (박스의 경우 왼쪽 꼭지점을 기준으로)

```html
.relative {
	position: relative;
	top: 100px;
	left: 100px;
}
```

### 6.3 `absolute` (절대 위치)

> static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동. 단, 과거 위치는 삭제한다.

```html
.parent {
	position: relative;
}
.absolute-child {
	position: absolute;
	top: 50px;
	left: 50px;
}
```

### 6.4 `fixed` (고정 위치)

> 부모 요소와 관계 없이 브라우저를 기준으로 이동. 스크롤시에도 항상 같은 곳에 위치

```html
.fixed {
	position: fixed;
	bottom: 0;
	right: 0;
}
```

### 6.5 `sticky`

> `position: static`상태와 비슷한 흐름에 따르지만 스크롤 위치가 임계점에 이르면 `position: fixed`와 같이 박스를 화면에 고정할 수 있는 속성이다. 예를 들어 `top: 0`을 설정하면 스크롤을 내리다 top=0의 위치에 이르면 그곳에서 fixed된 상태가 된다.

### 6.6 `z-index`

> 요소의 앞뒤 배치를 정의하는 것.

*Copyright* © Song_Artish