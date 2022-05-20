# AJAX

---

[TOC]

---



## Overview

AJAX는 Asynchronous JavaScript And XMLHttpRequest의 약자로, **JavaScript, DOM, Fetch, XMLHttpRequest 등의 다양한 기술을 사용하는 웹 개발 기법**이다. AJAX의 가장 큰 특징은 웹 페이지에 필요한 부분에, **필요한 데이터만 비동기적으로 받아와** 화면에 그려낼 수 있다는 것이다.



## 핵심 기술

AJAX를 구성하는 핵심 기술은 **JavaScript와 DOM**, 그리고 **Fetch**이다.

전통적인 웹 어플리케이션은 `<form>` 태그를 이용해 서버에 요청을 하고, 그 응답은 새로운 웹 페이지로 제공받아야 했다. 하지만, Fetch를 사용하면 페이지를 이동하지 않아도 서버로부터 필요한 데이터를 받아올 수 있다. 또한, JavaScript에서 DOM을 사용해 조작할 수 있기 때문에, **Fetch를 통해 필요한 데이터만 가져와 DOM에 적용**시켜, 새로운 페이지로 이동하지 않고 기존 페이지에서 필요한 부분만 변경할 수 있다.

### XHR과 Fetch

Fetch의 등장 이전에는 표준화된 XHR(XMLHttpRequest)을 사용했다. 그러나 XHR은 cross-site 이슈 등의 불편함이 있고, 그에 비해 Fetch는 간편함, promise 지원 등의 장점을 가지고 있기 때문에 오늘날에는 XHR보다 Fetch를 많이 사용한다.

```javascript
// XHR 예제
var xhr = new XMLHttpRequest()
xhr.open('get', 'http://localhost:3000/messages')

xhr.onreadystatechange = function() {
    // readyState 4: 완료
    if (xhr.readyState !== 4) return
    // status 200: 성공
    if (xhr.status === 200) {
        console.log(xhr.responseText)	// 서버로부터 온 응답
    } else {
        console.log(xhr.status)	// 요청 도중 에러 발생
    }
}
xhr.send()	// dycjd wjsthd
```

Fetch는 XHR의 단점을 보완한 새로운 Web API이며, XML보다 가볍고 JavaScript와 호환되는 JSON을 사용한다.

```javascript
// Fetch 예제
fetch('http://localhost:3000/messages')
	.then((response) => {
    return response.json()
	})
	.then((json) => {
    ...
	})
```

이 외에도 Axios와 같은 라이브러리도 존재하며 경우에 따라 적절한 것을 선택하여 사용하면 된다.



## 특징

AJAX는 다음과 같은 **장점**이 있다.

- 서버에서 HTML을 완성하여 보내주지 않아도 필요한 데이터를 비동기적으로 가져와 브라우저 화면 일부만 업데이트하여 렌더링 할 수 있다.
- XHR이 표준화되면서 브라우저에 상관 없이 AJAX를 사용할 수 있게 되었다.
- 유저 중심 어플리케이션 개발 AJAX를 사용하면, 필요한 일부분만 렌더링하기 때문에 빠르고 더 많은 상호작용이 가능한 어플리케이션을 만들 수 있다.
- AJAX에서는 필요한 데이터를 텍스트 형태(JSON, XML 등)로 보내면 되기 때문에 비교적 데이터의 크기가 작으며, 더 작은 대역폭을 가진다.

하지만 다음과 같은 **단점**은 존재한다.

- Search Engine Optimization(SEO)에 불리
- 뒤로 가기 버튼을 누르면, AJAX에서는 이전 상태를 기억하지 않기 때문에 사용자가 의도한 대로 동작하지 않는다. 이를 위해 별도로 History API를 사용해야 한다.



***Copyright* © 2022 Song_Artish**