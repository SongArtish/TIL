# Server & Client

2020.11.16

> Server(DRF) & Client(Vue.js)에 대해서 학습한다.

---

[TOC]

---



## 1. Server & Client

### 1.1 개념

-  **서버**는 클라이언트에게 네트워크를 통해 `정보`나 `서비스`를 제공하는 컴퓨터 시스템이다.
-  **클라이언트**는 ⓛ 서버에 맞게 요청을 제공하고 ② 서버의 응답을 사용자에게 표현한다.

|    개념    |             역할              |
| :--------: | :---------------------------: |
| **Server** |     서버에 맞게 요청 제공     |
| **Client** | 서버의 응답을 사용자에게 표현 |



### 1.2 SOP

Same-Origin Policy

> `동일 출처 정책`은 같은 출처에서만 리소스를 공유한다.
>
> - 두 URL의 `프로토콜`, `포트`, `호스트`가 모두 같아야 동일한 출처라고 정의한다.

```markdown
## flow
- 동일 출처 정책(SOP) 때문에 서로 다른 출처에서 리소스를 공유하려고하면, 외부서버에 요청한 데이터를 브라우저에서 보안목적으로 차단한다.
- 따라서, 서로 다른 출처에서 온 `DRS`와 `Vue.js`의 리소스를 공유하기 위해서는 교차 출처 자원 공유(CORS)를 설정해주어야 한다.
```



### 1.3 CORS :star:

Cross-Origin Resource Sharing

> `교차 출처 자원 공유`는 다른 출처(origin)에서 온 리소스를 공유하는 행위이다. 

- 이는 서버측(우리는 `DRS`)에서 지정해주어야 한다. 자세한건 [github 문서](https://github.com/adamchainz/django-cors-headers)를 참조한다.





## <실습> 서버를 DB로 사용하기 (CORS )

> 클라이언트에서 서버의 URL에 접근하여 자원을 서로 공유한다.

**CORS 설정**

> 자세한건 [github 문서](https://github.com/adamchainz/django-cors-headers)를 참조한다.

- `django-core-headers` pip를 설치한다.

```bash
$ python -m pip install django-cors-headers
```

- `settings.py`에 앱을 등록해준다.

```python
# settings.py
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]
```

- `MIDDLEWARE`도 등록하는데, 미들웨어가 실행되는 순서가 있으므로 가능한 위에 위치시킬 수 있도록 한다.

```python
MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    ...
]
```

- 출처를 허용해줄 URL을 `settings.py`에 선언해준다.

```python
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080',	# 출처를 허용해줄 URL
]
```

:ballot_box_with_check: DRF Server에서 Vue에서의 요청을 허용하기 위해, `ALLOWED_HOSTS` 목록에도 Vue의 주소를 등록해줘야 한다. (배포전에는 필요없다!)



**serializer 정의하기**

- serializer를 사용하기 위해서는 `django rest framework` pip가 설치되어 있어야한다.
- `models.py`와 `serializers.py`를 작성한다. DRS에서는 `id`값이 자동으로 생성되는 것을 체크한다.
- `views.py`에는 반드시 `@api_view()`가 있어야한다.



**생성 시 함수 실행하기**

- Vue 인스턴스 생성과 동시에 함수를 실행하기 위해서는, 다음과 같이 `created`를 다른 함수들과 같은 위계에 작성하면 된다.

```javascript
// TodoList.vue

methods: {
  getTodos: function () {},
  deleteTodo: function () {},
  updateTodoStatus: function () {},    
  created: function () {	// 같은 위계에 작성
    this.getTodos()
  }
}
```



**CreateTodo 함수 로직**

- 해당 router를 이름으로 이동하는 로직을 확인한다.

```javascript
// CreateTodo.vue

createTodo: function () {
      const todoItem = {
        title: this.title,
      }

      if (todoItem.title) {
        axios.post(`${SERVER_URL}/todos/`, todoItem)
          .then((res) => {
            // console.log(res)
            this.$router.push({ name: 'TodoList' })	// 체크
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },
  }
```



**Delete 함수 로직**

- Delete 함수는 다음과 같이 작성한다.
- `findIndex`와 `splice` 메서드 사용 방법을 참고한다.

```javascript
// TodoList.vue
    deleteTodo: function (todo) {
      axios.delete(`http://127.0.0.1:8000/todos/${todo.id}/`)
        .then((res) => {
          const targetTodoIdx = this.todos.findIndex((todo) => {	// findIndex 메서드
            return todo.id === res.data.id
          })
          this.todos.splice(targetTodoIdx, 1)	// splice 메서드
        })
        .catch((err) => {
          console.log(err)
        })
    },
```



**url을 변수로 관리하기**

- Vue 프로젝트 폴더 안에 `.env.local` 파일 생성

```
// .env.local
VUE_APP_SERVER_URL=http://127.0.0.1:8000
```

- 해당 파일을 vue 파일에서 가져와서 사용한다.

```javascript
// CreateTodo.vue, TodoList.vue

const SERVER_URL = process.env.VUE_APP_SERVER_URL

axios.post(`${SERVER_URL}/todos/`, todoItem)
```

- `env.local` 파일을 설정한 후 반드시 서버를 껐다 켜준다.



## 2. Authentication & Authorization

|             개념              |                   역할                   |  HTTP 상태코드   |
| :---------------------------: | :--------------------------------------: | :--------------: |
|   **Authentication (인증)**   |      자신이라고 주장하는 유저 확인       | 401 Unauthorized |
| **Authorization (권한/허가)** | 유저가 자원에 접근할 수 있는지 여부 확인 |  403 Forbidden   |



### JWT

Jason Web Token

> 이러한 인증을 세션/토큰 기반인 JWT를 이용한다. JWT를 사용하는 이유는 다음과 같다.
>
> - 서버에 저장하지 않아도 된다.
> - 확장성

|              .              |     Session      |          JWT          |
| :-------------------------: | :--------------: | :-------------------: |
|  **인증 수단의 저장 위치**  |      Server      |        Client         |
| **인증 수단의 정보 민감성** | Low (session id) | High (self-contained) |
|        **유효 기간**        |        Y         |           Y           |



## <실습> Account 관리하기

**JWT Auth 설정**

> [문서](https://jpadilla.github.io/django-rest-framework-jwt/)를 참조한다.

- pip를 설치한다.

```bash
$ pip install djangorestframework-jwt
```

- url을 작성한다.

```python
# accounts/urls.py
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # ...
    path('api-token-auth/', obtain_jwt_token),
]
```

- 수업을 위해 만료 기한을 1일로 설정해준다.

```python
# settings.py

# JWT additional settings
import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
}
```

**decorators 설정**

> 인증이 필요한 곳에 decorators를 설정한다.

**요청 보내기**

> axios 요청을 보낼 때 `headers`에 담아서 요청을 보낸다.



***Copyright* © 2020 Song_Artish**