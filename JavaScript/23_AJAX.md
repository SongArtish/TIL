# AJAX

---

[TOC]

---



## Overview

AJAX(Asynchronous JavaScript And XMLHttpRequest)는 JavaScript, DOM, Fetch, XMLHttpRequest 등의 다양한 기술을 사용하는 웹 개발 기법이다. AJAX의 가장 큰 특징은 웹 페이지에 필요한 부분에, **필요한 데이터만 비동기적으로 받아와** 화면에 그려낼 수 있다는 것이다.

```markdown
학습목표 : 자바스크립트 비동기 처리

## AJAX
핵심 : 비동기 처리
이유: Single Thread이기 때문에
방법: Event Loop
    
- 직관적으로 보이게 처리하기 위해 `Promise`라는 객체를 사용한다.
- 그 중에서도 `Axios`라는 라이브러리를 사용한다.
- [참고] `async & await`를 활용해서 동기적인 것처럼 보이게 코드를 작성할 수 있다.
```





## 핵심 기술

AJAX를 구성하는 핵심 기술은 **JavaScript와 DOM**, 그리고 **Fetch**이다.

전통적인 웹 어플리케이션은 `<form>` 태그를 이용해 서버에 요청을 하고, 그 응답은 새로운 웹 페이지로 제공받아야 했다. 하지만, Fetch를 사용하면 페이지를 이동하지 않아도 서버로부터 필요한 데이터를 받아올 수 있다. 또한, JavaScript에서 DOM을 사용해 조작할 수 있기 때문에, **Fetch를 통해 필요한 데이터만 가져와 DOM에 적용**시켜, 새로운 페이지로 이동하지 않고 기존 페이지에서 필요한 부분만 변경할 수 있다.



### 1) JavaScript & DOM

|     작동 원리     |                       설명                       |
| :---------------: | :----------------------------------------------: |
| **Asynchronous**  |        비동기, 기다려주지 않는다. (핵심)         |
| **Single Thread** |       왜냐하면 혼자서 일하기 때문에 (이유)       |
|  **Event Loop**   | 이벤트 루프에 기반한 메커니즘으로 일한다. (방법) |

#### 핵심 : Asynchronous

```javascript
// 비동기1 : setTimeout
function sleep3Seconds () {
    console.log('잘잤다!')
}

console.log('이제 잘거다!')
setTimeout(sleep3Seconds, 3000)
console.log('학교간다!')
```

```javascript
// 비동기2 : request
const xhr = new XMLHttpRequest()

xhr.open('GET', 'https://jsonplaceholder.typicode.com/todos/1')
xhr.send()

const res = xhr.response
console.log(res) // ''

xhr.onload = function () {
    if (xhr.status === 200) {
        const res = xhr.response
        console.log(res)
        // const title = JSON.parse(res).title
        // console.log(title) // 결과
    }
}
```

#### 방법 : Event Loop

> 자세한 내용은 [Async(비동기) TIL](#)을 참고한다.

- **Call Stack**: 요청이 들어올 때마다 해당 요청을 순차적으로 처리하는 Stack(LIFO) 형태의 자료 구조 (함수 호출 기록)

- **Web API (Browser API)**: JavaScript 엔진이 아닌 브라우저 영역에서 제공하는 API

- **Task Queue**: Callback 함수가 대기하는 Queue(FIFO) 형태의 자료 구조

- **Event Loop**: Call Stack에 현재 실행 중인 Task가 없는지 확인하고 Task Queue에 Task가 있는지 확인

```javascript
console.log('Hi')

setTimeout(function ssafy () {
    console.log('SSAFY 4th')
}, 3000)  // 3000ms = 3s

console.log('Bye')
```

- 첫 번째와 3번째 함수의 경우 특별한 작업 없이 실해 후 종료된다.
- setTimeout 함수의 경우 Web API를 통해 3초를 카운트한다. 그 후, setTimeout의 callback 함수가 Task Queue로 이동한다. Event Loop가 Call Stack이 비어있음을 확인한 후, Task Queue에 있던 callBack을 Call Stack으로 옮겨 작업을 마무리한다.



### 2) XHR과 Fetch

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



## 통신객체 : XHR

> **XMLHttpRequest**는 AJAX 프로그래밍에 주로 사용되는 요청방식으로, 전체 페이지의 새로고침 없이도 URL로부터 데이터를 받아오며, 이는 웹 페이지가 사용자가 하고 있는 것을 방해하지 않으면서 페이지의 일부를 업데이트할 수 있도록 해준다.

- 우리는 XHR 대신 [AXIOS](##5. Axios)를 사용한다!

```javascript
//1. XHR
//1-1.
const xhr = new XMLHttpRequest()

xhr.open('GET', 'https://jsonplaceholder.typicode.com/todos/1')
xhr.send()

const res = xhr.response
console.log(res)

//1-2.
xhr.onload = function () {
    if (xhr.status === 200) {
        const res = xhr.response
        console.log(res) // 결과
    }
}

```



## 통신객체 : axios :star:

> **Promise** based HTTP client for the browser and node.js

- 요청을 할 때 쓰는 라이브러리로 직관적으로 요청을 보낼 수 있다.
- 결국 내부적으로는 XHR을 날리는 것이다.

**CDN 가져오기**

- [axios Github](https://github.com/axios/axios) 에서 CDN을 가져와서 붙여준다.
- 아래 2개의 CDN은 배포 회사만 다를 뿐이므로, 2개 중 하나만 붙여주면 된다.

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

**가져온 데이터를 promise에 저장하기**

```javascript
const promise = axios.get('https://jsonplaceholder.typicode.com/todos/1')
    console.log(promise)
```

기본 axios 요청은 비동기 요청이다.

```javascript
//3-1. 기본 axios 요청
function getTodo () {
    console.log('1')
    axios.get('https://jsonplaceholder.typicode.com/todos/1')
        .then(function (res) {
        console.log(res.data.title)
    })
    console.log('2')
}
getTodo()
```



## 특징

AJAX는 다음과 같은 **장점**이 있다.

- 서버에서 HTML을 완성하여 보내주지 않아도 필요한 데이터를 비동기적으로 가져와 브라우저 화면 일부만 업데이트하여 렌더링 할 수 있다.
- XHR이 표준화되면서 브라우저에 상관 없이 AJAX를 사용할 수 있게 되었다.
- 유저 중심 어플리케이션 개발 AJAX를 사용하면, 필요한 일부분만 렌더링하기 때문에 빠르고 더 많은 상호작용이 가능한 어플리케이션을 만들 수 있다.
- AJAX에서는 필요한 데이터를 텍스트 형태(JSON, XML 등)로 보내면 되기 때문에 비교적 데이터의 크기가 작으며, 더 작은 대역폭을 가진다.

하지만 다음과 같은 **단점**은 존재한다.

- Search Engine Optimization(SEO)에 불리
- 뒤로 가기 버튼을 누르면, AJAX에서는 이전 상태를 기억하지 않기 때문에 사용자가 의도한 대로 동작하지 않는다. 이를 위해 별도로 History API를 사용해야 한다.



## <실습> 좋아요 기능 비동기 처리하기

### 전체 과정 보기

> 아래의 일련의 과정에서의 코드는 `articles/index.html`, `articles/views.py`에서 작성되는 코드이다. (Django)

**1. form태그 조정**

- `<form>` 태그의 `action`과 `method` 속성을 지운다.

```html
<form class="d-inline">
```

**2. axios CDN 입력**

- 사용자가 작성한 `<script>` 태그 위에 axios CDN을 넣어준다.

```javascript
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```

**3. form태그 가져오기**

- `<script>`에서 `<form>` 태그를 가져오기 위해 `<form>` 안에 `like-form`이라는 클래스 이름을 지정해준다.

```html
<form class="d-inline like-form">
```

- 클래스 선택자로 form태그를 가져온다.
- `querySelectorAll`로 클래스 선택자를 가져온다. (for문을 돌면서 form이 여러개이기 때문이다!)

```javascript
const forms = document.querySelectorAll('.like-form')
```

**4. Event Listener 생성**

> 좋아요 버튼을 클릭하면, ~ 한다.

- EventListener를 만들어준다.
- form 태그의 기본 submit 기능을 `.preventDefault()`로 막아준다.

```javascript
// 모든 form 말고 각각의 요소들에게 클릭시 이벤트를 만들어줘야한다.
forms.forEach(function (form) {
    // form은 forms에서 가져오는 각각의 요소
    form.addEventListener('submit', function (event) {
        // 기본으로 잡혀있는 event를 막아준다.
        event.preventDefault()
        //console.log(event)
    })
})
```

**5. 통신객체 axios 생성**

- axios가 **POST요청**을 좋아요 url에 요청을 보내도록 다음과 같은 형태의 코드를 작성한다.

```javascript
forms.forEach(function (form) {
        form.addEventListener('submit', function (event) {
          // ...
          axios.post('http://127.0.0.1:8000/articles/???/like/')
        })
      })
```

- 다음과 같이 코드를 작성할 수도 있다.

```javascript
// 기존
axios.post('http://127.0.0.1:8000/articles/???/like/')
// 다른 방법
axios({
    method : 'post',
    url : 'http://127.0.0.1:8000/articles/???/like/',
})
```

- `???` 부분은 나중에 template literal로 채워줄 부분을 의미한다.

**6. `article.pk` 데이터 받기**

> [데이터 속성](https://developer.mozilla.org/ko/docs/Learn/HTML/Howto/%EB%8D%B0%EC%9D%B4%ED%84%B0_%EC%86%8D%EC%84%B1_%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)을 사용하여 HTML에 저장된 데이터를 `<script>` 태그 내로 전달받는다.

- 먼저 `<form>` 태그에서 데이터 속성을 만들어준다.
- `data-` 뒤에 만들어줄 데이터 이름을 `- (하이픈)`을 연결해서 만들어준다. (pk 대신 id라는 이름을 쓰는 것이 좋다.)

```html
<form class="d-inline like-form" data-article-id="{{ article.pk }}">
```

- 넘어온 정보가 event에 저장되어 있으므로, event에서 정보를 가져온다.
- `data-` 이후의 이름을 `camelCase` (`articleId`)로 만들어주는 것을 확인할 수 있다.

```javascript
const articleId = event.target.dataset.articleId

// 다음의 코드도 가능하다.
// 정의하는 변수명의 가져오는 데이터의 키값과 같을 때 생략이 가능하다.
// const { articleId } = event.target.dataset
```

**7. templates literal로 데이터 입력**

- `template literal`로 변수를 가져온다. (:white_check_mark: backtick을 url에 씌우고 `$`와 `{}`를 다음과 같이 씌워준다.)

```javascript
axios.post(`http://127.0.0.1:8000/articles/${articleId}/like/`)
```

**8. CSRF 토큰 처리**

- 다음 코드를 붙여준다. ([사이트](https://docs.djangoproject.com/en/3.1/ref/csrf/)에서 검색 후 복붙한 코드)

  ```java
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  // 속성 값의 value(CSRF Token)을 가져온다.
  ```

- 그리고 headers 정보를 가져와야하는데, `X-CSRFToken`에 넣어야 한다는 규칙이 있으므로 document를 참조한다.

```javascript
headers : {'X-CSRFToken' : csrftoken}
```

- `headers` 정보가 3번째 위치 이므로 `{}`을 빼먹지 말고 중간에 넣어서 다음과 같은 코드를 작성한다.

  ```javascript
  axios.post(`http://127.0.0.1:8000/articles/${articleId}/like/`, {}, {
      headers : {
          'X-CSRFToken' : csrftoken
      }})
  ```
  
  ```javascript
  // 다음과 같이 작성할 수도 있다.
  axios({
      method : 'post',
      url : `http://127.0.0.1:8000/articles/${articleId}/like/`,
      headers : {'X-CSRFToken' : csrftoken}
  })
  ```

**9. DOM 조작 (view 함수 작성)**

> DOM을 통해 javascript에 대한 요청에 JSON형태의 응답을 하도록 view 함수의 코드를 수정해준다.

- `liked`를 `True` or `False 값을 통해서 boolean으로 DOM을 조작한다.
- return 값은 `redirect`가 아닌 `JsonResponse`로 응답값을 수정한다.

```python
# articles/views.py

from django.http import JsonResponse

@require_POST
def like(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        user = request.user

        if article.like_users.filter(pk=user.pk).exists():
        # if user in article.like_users.all():
            article.like_users.remove(user)
            liked = False
        else:
            article.like_users.add(user)
            liked = True
        like_status = {
            'liked' : liked,
            # 좋아요 개수
            'count' : article.like_users.count(),
        }
        return JsonResponse(like_status)
        # return redirect('articles:index')
    return redirect('accounts:login')
```

**10. chaining**

- `.then`을 작성하여 post 요청이 성공하였을 떄의 작업 코드를 입력해준다.

```javascript
axios.post(`http://127.0.0.1:8000/articles/${articleId}/like/`, {}, {
    headers : {
        'X-CSRFToken' : csrftoken
    }})
    .then(function (res) {
    // reponse(res)가 가지고 있는 data에서 데이터를 가져온다.
    const count = res.data.count
    const liked = res.data.liked
    })
```

- 위의 코드를 다음과 같이 간단하게 작성할 수도 있다.

```javascript
// 1
const { liked } = response.data
const { count } = response.data

// 2
const { liked, count } = response.data
```



**11. 버튼 속성 가져오기**

- 버튼 속성을 가져오기 위해 `<button>` > `<i>` 태그에 id값을 넣어준다. (각각의 분기의 button > i 태그에 넣어준다.)

```html
<button class="btn btn-link">
    <i id ="like-{{ article.pk }}" class="fas fa-heart fa-lg" style="color:crimson;"></i>
</button>
```

- button의 i  태그를 id선택자로 가져와서 liked에 따라서 스타일을 분기해준다.

  ```javascript
  // liked True/False에 따라서 색상 style 넣기
  
  const likeIconColor = document.querySelector(`#like-${articleId}`)
  
  if (liked) {
      likeIconColor.style.color = 'crimson'
  } else {
      likeIconColor.style.color = 'black'
  }
  ```

  - 위의 코드를 다음과 같이 **삼항연산자**를 이용하여 간단하게 코드를 작성할 수도 있다.

  ```javascript
  document.querySelector(`#like-${articleId}`).style.color = liked ? 'crimson' : 'black'
  ```

  - 가져온 태그의 class 속성을 변경할 때는 다음과 같이 `replace` 메서드를 사용한다.

  ```javascript
  const button // ...
  button.classList.replace('btn-secondary', 'btn-primary')
  ```
  
  - :white_check_mark: `classList.toggle()` : 클래스값이 있는지 체크하고 없으면 더하고 있으면 제거한다.
  
  ```javascript
  button.classList.toggle('btn-primary')
  button.classList.toggle('btn-secondary')
  ```

**12. 좋아요 인원 표시 만들기**

- `좋아요 인원 표시` 문구를 `<p>`태그의 `<span>` 태그 안에 넣은 후, `<script>` 태그에서 가져오기 위해 id 값을 넣어준다.
- 왜 굳이 `p > span` 태그에 넣는 것일까?? (질문 - `<span>` 없이 `<p>`에만 작성해도 상관은 없다.)

```html
<p>
    <span id="like-count-{{ article.pk }}">
        {{ article.like_users.all|length }} 명이 이 글을 좋아합니다.<br>
    </span>
</p>
```

- id 선택자로 가져와서 template literal로 반응하도록 작성한다.
- :white_check_mark: reponse.data로부터 데이터를 받아왔는지 확인한다!!

```javascript
// const { is_followed, followers, followings } = response.data

const likeCount = document.querySelector(`#like-count-${articleId}`)

likeCount.innerText = `${count} 명이 이 글을 좋아합니다.`
```



### 전체 코드 보기

**articles/index.html**

```html
<!-- articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">Articles</h1>
  <a href="{% url 'articles:create' %}">NEW</a>
  <hr>
  {% for article in articles %}
    <p><b>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></b></p>
    <p>글 번호: {{ article.pk }}</p>
    <p>글 제목: {{ article.title }}</p>
    <p>글 내용: {{ article.content }}</p>
    <form class="d-inline like-form" data-article-id="{{ article.pk }}">
      {% csrf_token %}
      {% if user in article.like_users.all %}
        <button class="btn btn-link">
          <i id ="like-{{ article.pk }}" class="fas fa-heart fa-lg" style="color:crimson;"></i>
        </button>
      {% else %}
        <button class="btn btn-link">
          <i class="fas fa-heart fa-lg" style="color:black;"></i>
        </button>
      {% endif %}
    </form>
    <p>
      <span id="like-count-{{ article.pk }}">
        {{ article.like_users.all|length }} 명이 이 글을 좋아합니다.<br>
      </span>
    </p>
    <a href="{% url 'articles:detail' article.pk %}">[detail]</a>
    <hr>
  {% endfor %}

    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    
<script>
      const forms = document.querySelectorAll('.like-form')

      forms.forEach(function (form) {
        form.addEventListener('submit', function (event) {
          // 기본으로 잡혀있는 event를 막아준다.
          event.preventDefault()
          const articleId = event.target.dataset.articleId
          const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

          axios.post(`http://127.0.0.1:8000/articles/${articleId}/like/`, {}, {
            headers : {
              'X-CSRFToken' : csrftoken
            }})
          .then(function (res) {
            const count = res.data.count
            const liked = res.data.liked
            // liked True/False에 따라서 색상 style 넣기

            const likeIconColor = document.querySelector(`#like-${articleId}`)
            const likeCount = document.querySelector(`#like-count-${articleId}`)

            likeCount.innerText = `${count} 명이 이 글을 좋아합니다.`

            if (liked) {
              likeIconColor.style.color = 'crimson'
            } else {
              likeIconColor.style.color = 'black'
            }
          })
        })
      })
    </script>
{% endblock %}
```

**articles/views.py**

```python
# articles/views.py

from django.http import JsonResponse

@require_POST
def like(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        user = request.user

        if article.like_users.filter(pk=user.pk).exists():
        # if user in article.like_users.all():
            article.like_users.remove(user)
            liked = False
        else:
            article.like_users.add(user)
            liked = True
        like_status = {
            'liked' : liked,
            # 좋아요 개수
            'count' : article.like_users.count(),
        }
        return JsonResponse(like_status)
        # return redirect('articles:index')
    return redirect('accounts:login')
```



***Copyright* © 2022 Song_Artish**