# jQuery

2021.01.27

> HTML의 클라이언트 사이드 조작을 단순화 하도록 설계된 크로스 플랫폼의 **자바스크립트 라이브러리**

---

[TOC]

---



## 시작하기

### jQuery란?

> 오픈 소스 기반의 자바스크립트 라이브러리
>
> ```markdown
> ### 대표적인 자바스크립트 라이브러리
> 
> - 프로토타입(Prototype)
> - 도조(Dojo)
> - GWT(Google Web Toolkit)
> - MochiKit
> ```

**특징**

- 대부분의 브라우저에서 지원
- HTML DOM 조작 및 CSS 스타일링이 용이
- 애니메이션 효과 및 대화형 처리가 용이
- 짧은 코드로 구현 가능
- 다양한 플러그인이 존재하며 참고 문서가 많다.



### 기본 문법

> HTML 요소를 선택하고, 선택된 요소에 특정 동작을 설정하는 구조이다.

```javascript
$(선택자).동적함수();
```

- `$` 기호는 `jQuery`를 의미하며, jQuery에 접근할 수 있게 해주는 식별자이다.
- `선택자`를 이용하여 원하는 HTML 요소를 선택
- `동작함수`를 정의하여 선택된 요소에 원하는 동작을 설정
- 위의 `$()` 함수를 통해 생성된 요소를 `제이쿼리 객체`라고 한다.



### 라이브러리 추가

> 라이브러리를 추가 위한 방법은 대표적으로 아래의 4가지가 있다.

1. NPM 사용

```bash
npm install jquery
```

- [사이트](https://jquery.com/download/)를 들어가보면 `Yarn`이나 `Bower`를 통해서도 간편하게 라이브러리를 추가할 수 있다.

2. API 다운로드

- [다운로드 링크](https://jquery.com/download/)
- 파일은 `compressed(jquery.min.js)`, `uncompressed(jquery.js)` 2가지가 존재
- :white_check_mark: 배포할 때는 용량을 고려하여  min파일(compressed)를 사용하는 것이 좋다.

```html
<script src="js/jquery.js"></script>
```

3. CDN 이용

```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
```

4. 최신 버전의 jQuery url

```html
<script src="http://code.jquery.com/jquery-latest.js"></script>
```



### 코드 예시

```html
<!DOCTYPE html> 
<html> 
	<head> 
    	<meta charset="UTF-8"> 
        <title>hello_jQuery</title> 
        <script src="jquery-3.5.1.min.js"></script>
        <script type="text/javascript"> 
        	$(document).ready(function() {
            //웹페이지가 로드가 완료 후에 해당 함수를 실행합니다.
            	alert('1'); 
            }); 
           
        </script> 
	</head> 
<body> 
</body>
</html>
```



### Vue에서의 사용

> [참고사이트](https://joshua1988.github.io/vue-camp/legacy/jquery-to-vue.html#%EB%B7%B0-%EA%B0%9C%EB%B0%9C%EC%9E%90%EA%B0%80-%EB%A7%88%EC%A3%BC%ED%95%98%EB%8A%94-%ED%98%84%EC%8B%A4)

- :ballot_box_with_check: npm으로 제이쿼라룰 설치한 후 페이지에서 import 해준다.

  ```javascript
  import $ from 'jquery'
  ```

- :star: 제이쿼리의 선택자로 HTML 태그를 접근할 수 있는 시점은  `mounted 단계`이다 :exclamation:

- 예시

  ```vue
  <template>
    <div>
      <button id="btn">click me</button>
    </div>
  </template>
  
  <script>
  import $ from 'jquery';	// import
  
  export default {
    mounted() {
      $('#btn').click(function() {
        alert('hi');
      });
    }
  }
  </script>
  ```

  

***Copyright* © 2021 Song_Artish**