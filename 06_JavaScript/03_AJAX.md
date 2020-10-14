# AJAX

2020.10.14

> **Asynchronous JavaScript And XML**는 XMLHttpRequest 객체를 사용하여 `비동기`를 통해 사용자의 event가 있으면 전체 페이지가 아닌 일부분만을 업데이트 할 수 있게 해준다.

:star: **학습목표 : 자바스크립트 비동기 처리** :star:

---

[TOC]

---



:star: **概要図**​ :star:

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



## :ballot_box_with_check: How JavaSciprt works?

|          |         작동 원리         |                   설명                    |
| :------: | :-----------------------: | :---------------------------------------: |
| **핵심** | **Asynchronous** (비동기) |            기다려주지 않는다.             |
| **이유** |     **Single Thread**     |       왜냐하면 혼자서 일하기 때문에       |
| **방법** |      **Event Loop**       | 이벤트 루프에 기반한 메커니즘으로 일한다. |





## 핵심 : Asynchronous (비동기)

---

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



## 방법 : Event Loop

---

### 용어

- Call Stack
  
  ```markdown
  요청이 들어올 때마다 해당 요청을 순차적으로 처리하는 Stack(LIFO) 형태의 자료 구조 (함수 호출 기록)
  ```

- Web API (Browser API)

  ```markdown
  JavaScript 엔진이 아닌 브라우저 영역에서 제공하는 API
  ```

- Task Queue

  ```markdown
  Callback 함수가 대기하는 Queue(FIFO) 형태의 자료 구조
  ```

- Event Loop

  ```markdown
  Call Stack에 현재 실행 중인 Task가 없는지 확인하고 Task Queue에 Task가 있는지 확인
  ```

```javascript
console.log('Hi')

setTimeout(function ssafy () {
    console.log('SSAFY 4th')
}, 3000)  // 3000ms = 3s

console.log('Bye')
```



### Callback Function

> 다른 함수의 인자로 넘어가는 함수

- 예시 : `addEventListener`

```javascript
const btn = document.querySelector('button')

btn.addEventListener('click' , function () {
    alert('Button Clicked!')
})
```



### Promise

> `Promise` 는 비동기 작업의 최종 완료 또는 실패를 나타내는 객체로, `callback hell`을 해결해준다. (ES6에서 등장)
>
> - **`.then(callBack)`**
> - **`.catch(callBack)`**

```javascript
function questionToProfessor ('질문', solveQuestion) {
    .then (solveQuestion) // 성공했을 때
    .then (share) // 성공했을 때
    .catch (resolveMyError) // 실패했을 때
}
```



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



## 통신객체 : Axios :star:

> **Promise** based HTTP client for the browser and node.js

- 요청을 할 때 쓰는 라이브러리로 직관적으로 요청을 보낼 수 있다.
- 결국 내부적으로는 XHR을 날리는 것이다.

**CDN 가져오기**

- [Axios Github](https://github.com/axios/axios) 에서 CDN을 가져와서 붙여준다.
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

**Chaining**

- 다음과 같이 특정 작업 수행을 성공했을 때, 다음의 요청을 promise 방식으로 chaining할 수 있다.

```javascript
axios.get('https://jsonplaceholder.typicode.com/todos/1')
        .then(function (res) {
        console.log(res)
        return res.data
    })
        .then(function (res) {
        console.log(res)
        return res.title
    })
        .then(function (res) {
        console.log(res)
    })
        .catch(function (err) {
    	console.log(err)
    })
```



### async & await 

> 동기적인 것처럼 보이게 코드를 작성할 수 있다. (ES8+)

- promise를 return하는 구문 앞에 await를 붙인다.

```javascript
async function getTodo2 () {
    console.log('1')
    await axios.get('https://jsonplaceholder.typicode.com/todos/1')
        .then(function (res) {
        console.log(res)
    })
    console.log('2')
}
getTodo2()
```

- 기본 axios 요청은 비동기 요청이다.

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



## <실습> 좋아요 기능 비동기 처리하기

### 전체 과정 보기

> 아래의 일련의 과정에서의 코드는 `articles/index.html`, `articles/views.py`에서 작성되는 코드이다.

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
- `querySelectorAll`로 클래스 선택자를 가져온다. (`querySelector`는 작동하지 않는다. form 태그 내 여러 요소가 있어서 그런건가?) (질문)

```javascript
const forms = document.querySelectorAll('.like-form')
```

**4. Event Listener 생성**

- EventListener를 만들어준다.
- form 태그의 기본 submit 기능을 `.preventDefault()`로 막아준다.

```javascript
forms.forEach(function (form) {
    form.addEventListener('submit', function (event) {
        // 기본으로 잡혀있는 event를 막아준다.
        event.preventDefault()
        console.log(event)
    })
})
```

**5. 통신객체 axios 생성**

- axios가 POST요청을 좋아요 url에 요청을 보내도록 다음과 같은 형태의 코드를 작성한다.

```javascript
forms.forEach(function (form) {
        form.addEventListener('submit', function (event) {
          // ...
          axios.post('http://127.0.0.1:8000/articles/???/like/')
        })
      })
```

**6. [데이터 속성](https://developer.mozilla.org/ko/docs/Learn/HTML/Howto/%EB%8D%B0%EC%9D%B4%ED%84%B0_%EC%86%8D%EC%84%B1_%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)을 사용하여 데이터 받기**

- 데이터 속성을 사용하여 HTML에 저장된 데이터를 `<script>` 태그 내로 전달받는다.
- 먼저 `<form>` 태그에서 데이터 속성을 만들어준다.

```html
<form class="d-inline like-form" data-article-id="{{ article.pk }}">
```

- 넘어온 정보가 event에 저장되어 있으므로, event에서 정보를 가져온다.

```javascript
const articleId = event.target.dataset.articleId
```

- data 이후의 이름을 camelCase로 만들어주는 것을 확인할 수 있다.

**7. templates literal로 데이터 입력**

- `template literal`로 변수를 가져온다. (:white_check_mark: backtick을 url에 씌우고 `$`와 `{}`를 다음과 같이 씌워준다.)

```javascript
axios.post(`http://127.0.0.1:8000/articles/${articleId}/like/`)
```

**8. CSRF 토큰 처리**

- 다음 코드를 EventListener 내에 붙여준다. (`사이트에서 검색 후 복붙한 코드`)

  ```java
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  // 속성 값의 value(CSRF Token)을 가져온다.
  ```

- `header` 정보가 3번째 위치 이므로 `{}`을 빼먹지 말고 중간에 넣어서 다음과 같은 코드를 작성한다.

  ```javascript
  axios.post(`http://127.0.0.1:8000/articles/${articleId}/like/`, {}, {
      headers : {
          'X-CSRFToken' : csrftoken
      }})
  ```

**9. view 함수 작성**

- `liked`를 `True` or `False 값으로 넘겨준다.
- return 값은 `redirect`가 아닌 `JsonResponse`로 응답값을 작성한다.

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
    const count = res.data.count
    const liked = res.data.liked
    })
```

**11. 버튼 속성 가져오기**

- `<button>` > `<i>` 태그에 id값을 넣어준다.

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

**12. 좋아요 인원 표시 만들기**

- `좋아요 인원 표시` 문구를 `<p>`태그의 `<span>` 태그 안에 넣은 후, `<script>` 태그에서 가져오기 위해 id 값을 넣어준다.
- 왜 굳이 `p > span` 태그에 넣는 것일까?? (질문)

```html
<p>
    <span id="like-count-{{ article.pk }}">
        {{ article.like_users.all|length }} 명이 이 글을 좋아합니다.<br>
    </span>
</p>
```

- id 선택자로 가져와서 template literal로 가져와서 반응하도록 작성한다.

```javascript
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



***Copyright* © 2020 Song_Artish**