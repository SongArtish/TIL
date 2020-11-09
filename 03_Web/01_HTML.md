# HTML (Hyper Text Markup Language)

2020.08.10

> 웹 페이지를 작성하기 위한 언어로, 웹 컨텐츠의 의미와 구조를 정의하는 마크업 언어이다. 파일 형식은 `.html`. 현재의 웹 표준은 W3C와 WHATWG를 따른다.

*****

[TOC]

*****



## 시작하기 전

[MDN 공식문서](https://developer.mozilla.org/ko/)

###  HTML Convention

1. 공백은 넣지 않는다.
2. 쌍따옴표(`""`)를 사용한다.
3. 기본적으로 소문자로 작성한다. (그런 것 같다.)



###  HTML 개발 환경 설정

1. Text Editor (VS Code) **extension** 설치

- `Open in browser` - `alt`+`B` 키를 누르면 바로 해당 html을 열 수 있다.
- `Auto rename tag` - tag 이름 변경 시 위 아래 태그를 매치시켜준다.
- `Highlight matching tag` - 매치되는 tag를 highlight 해준다.
- 참고) `material theme icons` - 폴더/파일 아이콘을 변경하여 가독성을 높여준다.

2. Chrome 개발자 도구 접근 (3가지 방법)

   1) `Ctrl` + `Shift` + `I`

   2) 마우스 우클릭 > 검사

   3) `F12`

   - inspect button(inspector)로 요소들 확인



## 1. HTML 기초

**Hyper**

- 텍스트 등의 정보가 동일 선상에 있는 것이 아니라 다중으로 연결되어 있는 상태

**Hyper Text**

- 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근 할 수 잇는 텍스트
- 하이퍼 텍스트가 쓰인 기술등 중 가장 중요한 2가지 (http, html)

**Markup Language**

> 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어이며, 프로그래밍 언어와는 다르게 단순하게 데이터를 표현한다.

- 특정 텍스트에 역할을 부여하는, 따라서 "마크업을 한다" 라고 하는 건 제목이 제목이라하고 본문이 본문이라고 마킹을 하는 것
- ex) h1 tag는 단순히 글자가 커지는 것이 아니라 의미론적으로 그 페이지에서 가장 핵심 주제를 의미하는 것



## 2. HTML 기본 구조

```html
<!DOCTYPE html>
<html lang="KO">
<head>
    <meta charset="UTF-8">    <!-- character set을 의미, 문자 인코딩 방식 -->
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

|       요소        |                             내용                             |                             구성                             |
| :---------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| `<!DOCTYPE html>` |             이 문서가 html 타입이라는 것을 명시              |                                                              |
|     `<html>`      |                       HTML 최상위 요소                       |                          head, body                          |
|     `<head>`      | 해당 문서 정보를 담고 있으며<br />브라우저에 나타나지 않는다. | 문서 제목, 문자코드(인코딩),<br />CSS선언, 외부로딩파일 지정 등 |
|     `<body>`      |  브라우저 화면에 나타나는 정보로<br />실제 내용에 해당한다.  |                                                              |
|     *`<meta>`     | <Open Graph Protocol><br />HTML 문서의 메타 데이터를 통해 문서 정보 전달 |                                                              |



### DOM(Document Object Model) 트리

> DOM은 문서의 구조화된 표현(structured representation)을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공하여 그들이 문서 구조, 스타일, 내용 등을 변경할 수 있게 도움을 준다. 웹 페이지의 객체 지향 표현.

```html
<!-- 다음은 DOM으로 2개의 자식 태그가 있다. -->
<body>
    <h1> 웹문서 </h1>
    <ul>
        <li>HTML</li>
        <li>CSS</li>
    </ul>
</body>
```

### 1) 요소 (element)

>  HTML의 요소는 태그와 내용(contents)로 구성되어 있다. 요소는 중첩될 수 있다.

```html
<h1>contents</h1>
```

- 내용이 없는 태그들: `br`, `hr`, `img`, `input`, `link`, `meta`

### 2) 속성(attribute)

> `속성명=속성값`의 형태로 입력한다. 태그별로 사용할 수 있는 속성은 다르며, 태그와 상관없이 사용 가능한 속성들(html global attribute)도 있다.

```html
<a href="https://gooogle.com"></a>
```

#### HTML Global Attribute

> 모든 HTML 요소가 공통으로 사용할 수 있는 속성 (몇몇 요소에는 아무 효과 없을 수 있다)

```
id, class, hidden, lang, style, tabindex, title
```



## 3. HTML 문서 구조화(Tag)

### 1) 시맨틱 태그 (Semantic Tag)

> 브라우저, 검색엔진, 개발자 모두에게 콘텐츠의 의미를 명확히 설명하는 태그. HTML5에서 등장한 <u>의미론적 요소</u>를 담는 태그로, 가독성과 접근성을 높인다. 시맨틱 태그에는 총 13개가 있다. (Non-Semantic Tag는 `div`, `span` 등이 있다.)
>
> - header: 문서 전체나  섹션의 헤더 (머릿말 부분)
> - nav: 네비게이션
> - aside: 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
> - section: 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
> - article: 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
> - footer: 문서 전체나 섹션의 푸터(마지막 부분)

```html
<!-- 예시 -->
<header>
    <nav></nav>
</header>
<section>
    <article></article>
    <article></article>
</section>
<footer></footer>
```

***** 시맨틱 웹

> 웹에 존재하는 수많은 웹페이지들에 메타데이터를 부여하여, 기존의 단순한 데이터 집합이었던 웹페이지를 '의미'와 '관련성'을 가지는 거대한 데이터베이스로 구축하고자 하는 발상.

### 2) 인라인 / 블록 요소

- 블록 요소 - 자리 전체를 차지한다.

- 인라인 요소 - 컨텐츠만큼만 너비를 차지

### 3) 그룹 컨텐츠

- `<p>`
- `<hr>` : 헤드라인
- `<ol>`, `<ul>`
- `<pre>`, `<blockquote>` : `<pre>`는 사용하지 않는다.
- `<div>`

```html
<!-- 리스트 -->
<ul>
    <li></li>
</ul>
<ol>
    <li></li>
</ol>
```

- `<ol>`(ordered list), `<ul>`(unordered list) > (하위항목) `<li>`

### 4) 텍스트 관련 요소

- `<a>`
- `<b>` vs `<strong>` : bold를 의미. `<b>`는 보여지는 것만, `<strong>`은 의미론적으로 굵게 
- `<i>` vs `<em>` : 이탤릭체. `<i>`는 보여지는 것만, `<em>`은 의미론적
- `<span>`
- `<br>` : 줄을 바꿀 때 사용한다.
- `<img>` - 이미지를 불러올 때 사용한다. (자세한 설명은 밑의 <u><참고></u>에 정리되어 있다.)

### 5) 테이블

- `<tr>`, `<td>`, `<th>`

- `<thead>`, `<tbody>`, `<tfoot>`
- `<caption>`
- 셀 병합 속성: colspan, rowspan
- scope 속성
- `<col>`, `<colgroup>`

### 6) form 

> 서버에서 처리할 데이터를 제공하는 역할(웹페이지 입력 양식)을 한다. 기본 속성으로는 <u>action</u>(데이터를 어디로 보낼지 설정="url")과 <u>mehod(GET, POST)</u>가 있다. GET은 데이터를 가지고 오는 요청이며, POST는 DB와 관련있다.

```html
<form action="" mehod=""></form>
```

- `<form>` 태그 안에 있는 요소들을 그룹화할 때 사용한다.

### 7) input

> 다양한 타입을 가지는 <u>입력 데이터 필드</u>이다. `<input>` 요소 동작은 type에 따라서 달라진다.(자세한 것은 [mdn](https://developer.mozilla.org/ko/)을 참고한다.) 
>
> (1) type="**text**" : 텍스트를 입력받는다.
>
> (2) type="**radio**" : 옵션 중 하나만 선택 가능
>
> (3) type="**checkbox**" : 옵션에서 복수 선택 가능
>
> (4) type="**email**" : 이메일 타입만 입력 받을 수 있다.
>
> (5) type="**password**" :  입력시 입력 값을 별 모양으로 표시한다.
>
> (6) type="**reset**" : form tag 안에 있는 input tag들에 작성한 모든 내용 reset
>
> (7) type="**button**" : 아무 효과가 없는 버튼이 생성되어 보여진다. 단지 UI적인 관점. (`<a>`로 링크와 연결하여 사용가능하다?)
>
> `<input>`의  공통 속성에는 name, placeholder, required, autofocus 등과 같은 것들이 있다.
>
> - `autofocus` : 접속시 사용자의 자동위치를 설정한다.
> - `placeholder` : input 자리에 미리보기 메시지가 표시되게 할 수 있다.
> - `value` : input 자리에 값 자체가 들어간다.

```html
<태그>
    <label for=""></label><br>
    <input type="" id="" autofocus>
</태그>
```

- `<label>` : 서식 입력 요소의 캡션이다. for는 id와 연결되어 있어야 하며, id 값은 항상 (변수명과 같이)고유한 값이어야 한다.

- :white_check_mark:`<input name="name">`에서 name을 지정하고 view 함수에서 `request.POST.get('name')`으로 입력한 데이터를 가져올 수 있다!

## <참고> 태그 정리

### 1) `<a></a>`

> 하이퍼링크를 걸어주는 태그이며, 2가지 속성이 있다.
>
> - `href`: 클릭시 이동 할 링크
> - `target`: 링크를 여는 방법
>   - `_self`: 현재 페이지 (기본값)
>   - `_blank`: 새 탭
>   - `_parent`: 부모 페이지로, iframe 등이 사용된 환경에서 쓰인다.
>   - `_top`: 최상위 페이지로, iframe 등이 사용된 환경에서 쓰인다.
>   - `프레임이름`: 직접 프레임이름을 명시해서 사용할 수도 있다.

```html
<a href="https://www.naver.com">Go NAVER</a>
```

### 2) `<img>`

> 이미지를 보여주는 태그이며, 주요 속성은 다음과 같다.
>
> - `src` : 이미지의 경로
> - `alt` : 대체 텍스트(이미지가 보여지지 않을 경우 표시)
> - `width` : 이미지의 가로 크기
> - `height`: 이미지의 세로 크기
> - `loading` : 이미지 로딩 방식

```html
<!-- 1. 절대경로 -->
<img src="C:\Users\windows 10\Desktop\TIL\ssafy\images\my_photo.png" alt="ssafy">

<!-- 2. 상대경로 -->
<img src="..\images\my_photo.png" alt="ssafy" width="300px">	
```

### 3) `<select>`와 `<option>`

> `<select>`는 드랍다운 목록을 만들 때 사용하며, `<option>`은 드랍다운 목록의 항목을 만든다. `<option>`의 속성은 다음과 같다.
>
> - `value` : 서버에 전송될 값. value 값이 없을 경우에는, contents의 내용이 서버에 전달된다.
>   (contents는 사용자에게 표시하는 용도이고 서버에 전달할 값은 value 안에 넣어준다)
> - `label` : 옵션에 대한 짧은 설명으로, 드롭다운 리스트에 표시된다.
> - `selected` : 미리 선택된 옵션이 드롭다운 목록에서 맨 먼저 표시된다.
> - `disabled` : 옵션이 비활성화되어 선택할 수 없게 된다.

```html
<label for="region">지역을 선택해주세요.</label><br>
<select name="region" id="region">
    <option value="">선택</option>
    <option value="경성">서울</option>
    <option value="대전">대전</option>
    <option value="광주" disabled>광주</option>
    <option value="구미">구미</option>
</select>
</label>
```

### 4) ` <div>`와 `<span>`

> 1. ` <div>는 박스 형태로 영역이 설정되며, `<span>`은 줄 단위로 영역이 설정되기 때문에 배경색의 길이가 다르다. (영역이 다르다)
> 2. `<div>`는 줄 바꿈이 되지만, `<span>` 태그는 옆으로 붙는다. 결국 영역을 지정하는 방식의 차이가 있다.

- :heavy_check_mark:**TIP** `#app` + `Enter`을 입력하면 다음과 같이 id가 app인 `<div>` 태그가 자동완성되어 생성된다.

```html
  <div id="app"></div>
```



### 5) `<hr>`

> 가로줄을 넣는 태그로 `<hr style="border: 선종류 선굵기 선색상">`으로 속성을 지정한다.
>
> - 선종류: solid, dotted, dashed, double, groove, ridge, inset, outset
>
> 가로줄에 길이를 지정하고 정렬할 수도 있다.

```html
<!-- <hr> 예시 -->
<hr align="left" style="border: solid 10px green; width: 50%;">
```



*Copyright* © Song_Artish

