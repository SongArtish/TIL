# CSS (Cascading Style Sheets)

> 스타일, 레이아웃 등을 통해 문서(HTML)를 표시하는 방법을 지정하는 언어

```python
Index

1. 기초 문법
2. CSS Selector
3. CSS 단위
4. CSS Box Model
5. CSS Block vs Inline
6. CSS Position
```



## 1. 기초 문법

### CSS 구문

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

### CSS 정의 방법

#### (1) 인라인 \(inline)

> 해당 태그에 직접 `style` 속성을 활용

```html
<!-- 예시 -->
<body>
    <h1 style="color: blue; font-size: 100px;">Hello</h1>
</body>
```

#### (2) 내부 참조(embedding) 

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

#### (3) 외부 참조(link file)

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

#### 2.1.1 기초 선택자

- 전체 선택자, 타입 선택자
- 클래스 선택자, 아이디 선택자, 속성 선택자

```html
<style>
    /* 이것은 전체 선택자입니다. */
    * {
      color: red;
    }
    /* 이것은  타입 선택자입니다.*/
    h2 {
      color: orange;
    }
</style>
```

```html
<style>
	 /* 이것은 클래스 선택자입니다. */
    .green {
      color: green
    }
    /* id 선택자는 샵(#)으로 시작한다. (id 선택자는 문서내에서 단 한 번만 사용한다!) */
    #purple {
      color: purple
    }
</style>
```

#### 2.1.2 고급 선택자

- 자식 선택자, 자손 선택자
- 형제, 인접 형제 선택자

```html
<style>
	/* 이것은 자식 선택자입니다. */
    /* 클래스 박스 바로 안에 있는 p 태그를 의미한다. */
    .box > p {
      font-size: 30px
    }
    /* 이것은 자손 선택자입니다. (class 박스 내 모든 p 태그를 의미한다.) */
    .box p {
      color: blue
    }
</style>
<!-- -------------------------------------- -->
<body>
    <div>
    box content
    <div class="box">
      <p>지역 목록</p>
    </div>
</body>
```

#### 2.1.3 의사 클래스(pseudo class)

- 링크, 동적 의사 클래스
- 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트 속성 선택자 (등)

- 입력입력입력 찾아보기



### 2.2 CSS 적용 우선순위(cascading order)

#### 2.2.1 중요도(Importance)  

- `!important`
- 사용하지 않는 편이 좋다!

#### 2.2.2 우선 순위 (Specificity)

- 인라인/ id 선택자/ class 선택자 / 속성 선택자/ 요소 선택자

#### 2.2.3 소스 순서

### 2.3 CSS 상속

> CSS는 상속을 통해 부모 요소의 속성(property)을 ~~모두~~ 자식에게 상속한다.
>
> - 상속 되는 속성: Text 관련 요소(font, color, text-align), opacity, visibility 등
> - 상속 되지 않는 속성:  Box model 관련 요소(width, height, margin, padding, border, box-sizing, display), position 관련 요소(position, top/right/bottom/left, z-index) 등

#### `> p:nth-child(n)`과 `> p:nth-of-type(n)`

```html
<!-- 예시 -->
<!-- p:nth-child(n) -->
<style>
    #ssafy > p:nth-child(2) {
        color: red;
        }
</style>

<!-- p:nth-of-type(n) -->
<style>
    #ssafy > p:nth-of-type(2) {
        color: red;
        }
</style>
```

- nth-child(n)은 부모 요소의 모든 자식 요소 중 n번째 태그를 지정하는 반면, 
  nth-of-type(n)은 부모 요소들의 특정 자식 요소 중  n번째 태그를 지정한다.



## 3. CSS 단위

### 3.1 (상대) 크기 단위

- px (픽셀) - (html 기본 폰트 사이즈는 16px이다.)
- %
- em : 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐 (부모에 대해 상대적)
- rem : 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
- Viewport 기준 단위 : vw, vh, vmin, vmax (태블릿, 모바일 등의 디바이스에 적용할 때 사용)

### 3.2 색상 단위

3.2.1 색상 키워드

3.2.2 RGB 색상

- `#` + 16진수 표기법
- rgb() 함수형 표기법

3.2.3 HSL 색상

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

![Box Model](C:\Users\bulge\Documents\SSAFY\TIL\03 Web\img\css_box_model_box.png)

- Margin: 테두리 바깥의 외부 여백. 배경색을 지정할 수 없다.

```html
.margin {
	margin-top: 10px;
	margin-right: 20px;
	margin-bottom: 30px;
	margin-left: 40px;
}
```

- Border: 테두리 영역
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

> 인접 형제 요소 간의 margin이 겹쳐서 보이는 것



## 5. CSS Block vs Inline

### 5.1 block 레벨 요소와 inline 레벨 요소

- block 레벨 요소: `div / ul`, `ol`, `li / p / hr/ form` 등
- inline 레벨 요소: `span / a / img/ input`, `label / b`, `em`, `i`, `strong` 등

### 5.2 display

5.2.1 `display`: `block`

> 줄 바꿈이 일어나는 요소. 화면 크기 전체의 가로 폭을 차지하며 안에 inline 레벨 요소가 들어갈 수 있다. (line-height - 텍스트의 상하여백)
>
> - 수평 정렬: `margin-right: auto;`, `margin-left: auto;`, `margin-right: auto; margin-left: auto;`

5.2.2 `display`: `inline`

> 줄 바꿈이 일어나지 않는 행의 일부 요소. content 너비만큼 가로 폭을 차지하며, width, height, margin-top, margin-bottom을 지정할 수 없으며 상하 여백은 line-height로 지정한다.
>
> - 수평 정렬: `text-align: left;`, `text-align: right;`, `text-align:center;`

5.2.3 `display`: `inline-block`

> block과 inline 레벨 요소의 특징을 모두 갖는다. inline처럼 한 줄에 표시 가능하며, block처럼 width, height, margin 속성을 모두 지정할 수 있다.



## 6. CSS Position

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

> static 위치를 기준으로 이동 (상대 위치)

```html
.relative {
	position: relative;
	top: 100px;
	left: 100px;
}
```

### 6.3 `absolute` (절대 위치)

> static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (절대 위치). 단, 과거 위치는 삭제한다.

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

> 부모 요소와 관계 없이 브라우저를 기준으로 이동 (고정위치). 스크롤시에도 항상 같은 곳에 위치

```html
.fixed {
	position: fixed;
	bottom: 0;
	right: 0;
}
```

*Copyright* © Song_Artish