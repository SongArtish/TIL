# <실습> TodoList 만들기

---

[TOC]

---



## 개요

1. DRF Todo를 관리할 서버 생성

   1-1. Todo 조회 및 생성

   - model 및 serializer 작성

   1-2. Todo 수정 및 삭제

   - view 함수 작성

   2-1. 회원가입 로직 생성

   2-2. 로그인 로직 -> JWT를 활용한 로그인

   - JWT 사용법 숙지

2. Todo를 보여줄 Vue 프로젝트 생성

   1-1. Vuex & Vue Router 사용 여부 결정

   - Vue Router를 포함한 Vue 프로젝트 생성

   1-2. 전체 목록 메인 페이지에 불러오기

   1-3. Todo 생성하기

   1-4. Todo 수정 및 삭제하기

   

**가상환경 생성**

> 필요에 따라 가상환경을 생성하여 프로젝트를 진행한다.

- `venv`라는 이름의 가상환경을 생성한다.

```bash
$ python -m venv venv
```

- 가상환경을 실행한다.

```bash
$ source venv/Scripts/activate
```



## 1.1 Todo - Server

### 시작하기

**django**

- `django`를 설치한다.

```bash
$ pip install django
```

**DRF**

- `djangorestframework`를 설치한다. 자세한건 [사이트](https://www.django-rest-framework.org/)를 참조한다.

```bash
$ pip install djangorestframework
```

- DRF 앱을 등록한다.

```python
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

**<참고> freeze**

- 프로젝트를 시작하기전 `requirements.txt`를 미리 만들어준다.

```bash
$ pip freeze > requirements.txt
```

**<참고> Django extension**

- VS Code에서 `Django` (1.0.0) extension을 설치하면 편하다!!
- 자동 완성 기능 등을 제공한다.



### 1.1.1 Django 프로젝트 생성

- DRF 서버로 사용할 Django 프로젝트 `drf_server`를 생성한다.

```bash
$ django-admin startproject drf_server
```

- 서버가 잘 실행되는지 확인한다.

```bash
$ python manage.py runserver
```

### 1.1.2 앱 생성

- `todos` 앱을 생성한다.

```bash
$ python manage.py startapp todos
```

- 앱을 등록한다.

```python
# settings.py

INSTALLED_APPS = [
    'todos'
    ...
]
```

- :white_check_mark: 이외 `settings.py`의 시간, 언어 등을 설정한다.

### 1.1.3 앱 url 등록

- 프로젝트 폴더의 `urls.py`에 앱의 url을 등록한다.

```python
# drf_server/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')),
]

```

- todos 앱에 `urls.py` 파일을 생성해주고 코드를 작성한다.

```python
# todos/urls.py

from django.urls import path
from . import views

urlpatterns = [
]

```

### 1.1.4 모델 등록

- `Todo` 모델을 생성한다.

```python
# todos/models.py

from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
```

- 모델을 생성했기 때문에 migration을 진행해준다.

```bash
$ python manage.py makemigrations
```

```bash
$ python manage.py migrate
```

### 1.1.5 serializer 생성

> serializer를 통해 JSON형태로 데이터를  보여줄 예정이다.

- todos에 `serializers.py` 파일 생성하고 코드를 작성한다.

```python
# todos/serializers.py

from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ('id', 'title', 'completed',)
```

### 1.1.6 Todo 조회 & 생성 logic

- url을 작성한다.

```python
# todos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list_create),
]
```

- `views.py`에서 로직을 작성한다.

```python
# todos/views.py

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

@api_view(['GET', 'POST'])
def todo_list_create(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)   # 받아오는 객체가 여러개!
        return Response(serializer.data)
    else:
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```

- 서버를 실행해서 사이트에서 todo 생성을 테스트해본다.
- 데이터는 아래와 같이 JSON의 형태로 입력하여야 하며, 반드시 쌍따옴표(`""`)를 사용하여야 한다.

```json
{
"title" : "todo 1"
}
```

### 1.1.7 Todo 수정 & 삭제 logic

- url을 작성한다.

```python
# todos/urls.py

urlpatterns = [
    path('', views.todo_list_create),
    path('<int:todo_pk>/', views.todo_update_delete),	# variable routing
]
```

- `views.py`에서 함수를 작성한다.

```python
# todos/views.py

from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, todo_pk):
    # todo = Todo.objects.get(pk=todo_pk)
    todo = get_object_or_404(Todo, pk=todo_pk)

    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        todo.delete()
        return Response({'id' : todo_pk})   # 삭제된 데이터의 id 값을 보여준다.
```



## 1.2 Todo - Client

### 시작하기

- `Vetur`라는 VS Code extension을 설치한다.
- `node.js` 프로그램을 설치한다.
- `Vue CLI`를 설치한다.

```bash
$ npm install -g @vue/cli
```

- 설치가 잘 되어 있는지 확인한다.

```bash
$ node -v
```

```bash
$ vue --version
```

### 1.2.1 Vue 프로젝트 생성

- `Vue-client`라는 이름의 Vue 프로젝트를 생성한다.
  - 제일 처음의 default 옵션을 설정하고 프로젝트 생성을 진행한다.

```bash
$ vue create vue-client
```

- Vue 프로젝트 폴더로 이동해서 서버를 실행해본다.

```bash
$ cd vue-client
$ npm run serve
```

- 라우터를 추가한다.

```bash
$ vue add router
```

- 필요없는 view와 router 주소에 추가된 내용 등을 제거해준다.



### 1.2.2 컴포넌트 만들기

- `App.vue`에서 생성한 컴포넌트로 이동할 수 있는 링크를 생성한다.

```vue
<!-- App.vue -->
<router-link to="/">TodoList</router-link> |
<router-link to="/about">CreateTodo</router-link>
```

- `views/todos/TodoList.vue`를 생성하고 뼈대를 작성한다.

```vue
<!-- views/todos/TodoList.vue -->

<template>
  <div>
    <h2>TodoList</h2>
  </div>
</template>

<script>
export default {
  name: 'TodoList'
}
</script>
```

- 생성한 컴포넌트를 router에 등록해준다.

```javascript
// router/index.js
import TodoList from '@/views/todos/TodoList'

const routes = [
  {
    path: '/',
    name: 'TodoList',
    component: TodoList
  }
]
```



### 1.2.3 하위 컴포넌트 생성

- `App.vue`에 하위 컴포넌트로 이동하는 경로를 만들어준다.
  - :white_check_mark: 이름으로 찾아가기 위해서는 꼭 `v-bind`를 붙여주어야한다.

```vue
<!-- App.vue -->
      <router-link :to="{ name: 'TodoList' }">TodoList</router-link> |
```

- `CreateTodo.vue` 라는 이름의 하위 컴포넌트 파일을 생성한다.

```vue
<!-- views/todos/CreateTodo.vue -->

<template>
  <div>
    <h2>CreateTodo</h2>
  </div>
</template>

<script>
export default {
  name: 'CreateTodo'
}
</script>
```

- 컴포넌트를 router에 등록해준다.

```javascript
// index.js
import CreateTodo from '@/views/todos/CreateTodo'

const routes = [
  ...
  {
    path: '/create',	// 앞에 슬래시(/)를 꼭 붙여주어야 한다!!
    name: 'CreateTodo',
    component: CreateTodo
  }
]
```

- `App.vue`에 이동할 수 있는 링크를 만들어준다.

```vue
<!-- App.vue -->
      <router-link :to="{ name: 'CreateTodo' }">CreateTodo</router-link>
```



### 1.2.4 `.env.local` 관리

> `.env.local`이라는 파일을 통해 여러번 호출되는 값을 변수로 사용해서 관리할 수 있다.

- 클라이언트 프로젝트 폴더의 최상위에 `.env.local`이라는 파일을 생성한다.
- 관리할 변수 (여기서는 url주소)를 입력한다.

```
// .env.local
VUE_APP_SERVER_URL=http://127.0.0.1:8000
```

- 컴포넌트에서는 다음과 같은 코드로 불러올 수 있다.

```javascript
process.env.VUE_APP_SERVER_URL
```

- 예시

```javascript
const SERVER_URL = process.env.VUE_APP_SERVER_URL
```



### 1.2.5 axios 설치하기

- 다음의 명령어로 `axios` 모듈 패키지를 설치한다.

```bash
$ npm install axios
```

- axios는 `<script>` 태그 내에서 다음과 같이 호출해 사용할 수 있다.

```javascript
// 예시
import axios from 'axios'
```



### 1.2.6 전체 목록 불러오기

- `v-for`를 활용해 todos 전체 목록을 출력한다.
  - `:key`를 반드시 정의해주어야 한다!

```vue
<!-- TodoList.vue -->
  <div>
    <h2>TodoList</h2>
    <ul>
      <li 
        v-for="todo in todos"
        :key="todo.id"
      >
        {{ todo.title }}
      </li>
    </ul>
  </div>
```

- `todos`를 받을 데이터를 정의해준다.

```javascript
// TodoList.vue
name: 'TodoList',
  data: function () {
    return {
      todos: [],
    }
  },
```

- 해당 함수를 작성한다.

```javascript
// TodoList.vue
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

 methods: {
    getTodo: function () {
      axios.get(`${SERVER_URL}/todos/`)
      .then(res => console.log(res))
      .catch(err => console.log(err))
    }
  }
```

- :white_check_mark: url 마지막에 `/` (슬래시)를 꼭 넣어줄 수 있도록 주의한다 :exclamation::exclamation:
- 페이지가 생성될 때 함수가 작동할 수 있도록 만들어준다.

```javascript
// TodoList.vue
  created: function () {
    this.getTodo()
  }
```

- 하지만, 아래와 같이 보안 처리 때문에 오류가 발생하는 것을 확인할 수 있다.

![XMLHttpRequest Error](img/XMLHttpRequest_Error.jpg)



### 1.2.7 CORS 처리

> 서로 다른 출처의 자원은 공유하지 못하도록 기존 정책이 설정되어 있다. CORS 처리를 통해 서로 자원을 공유할 수 있도록 설정해준다. 자세한 내용은 [문서][https://github.com/adamchainz/django-cors-headers]를 참조한다.

- 서버에 pip를 설치한다.

```bash
$ python -m pip install django-cors-headers
```

- 해당 pip를 `settings.py`에 등록해준다.

```python
# settings.py

INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]
```



### 1.2.8 데이터 생성하기

> 다음의 작업은 `CreateTodo.vue` 파일에서 진행한다.

- 데이터를 입력받을 `title`이라는 변수를 생성한다.

```vue
<!-- CreateTodo.vue -->

<template>
  <div>
    <h2>CreateTodo</h2>
    <input type="text" v-model="title">
  </div>
</template>

<script>
export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: ''
    }
  }
}
</script>
```

- `Enter`를 눌렀을 때 작동할 함수를 달아준다.

```vue
<!-- CreateTodo.vue -->
    <input type="text" v-model="title" @keypress.enter="createTodo">
```

- 입력한 데이터를 server와 통신할 함수를 작성한다.

```javascript
// CreateTodo.vue
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

  methods: {
    createTodo: function () {
      const todoItem = {
        title: this.title
      }

      axios.post(`${SERVER_URL}/todos/`, todoItem)
          .then((response) => {
            console.log(response)
          })
          .catch((error) => {
            console.log(error)
          })
    }
  }
```

- :white_check_mark: 여기서 console 창에 오류가 발생할 경우, 서버를 껐다가 켜준다.
- POST 요청을 보내 성공적으로 데이터를 생성했을 경우 리스트 페이지로 넘어갈 수 있도록 처리해준다.
  - :ballot_box_with_check: `thsi.$router.push` 기억하기!!

```javascript
// CreateTodo.vue

      axios.post(`${SERVER_URL}/todos/`, todoItem)
          .then(() => {
            // console.log(response)
            // 해당 이름인 router의 주소로 보내버린다.
            this.$router.push({ name: 'TodoList'})
      })
```



### 1.2.9 Delete 버튼 만들기

- 각각의 todo 아이템에 삭제 버튼을 달아준다.

```vue
<!-- TodoList.vue -->
      <li 
        v-for="todo in todos"
        :key="todo.id"
      >
        {{ todo.title }}
        <button @click="deleteTodo(todo)">DeleteTodo</button>
      </li>
```

- 버튼에 넣은 함수를 작성해준다.
- delete 요청을 보내 삭제한 후, 현재의 list에서도 해당 값을 id 값으로 찾아서 삭제해준다. (동기화 문제!)

```javascript
// TodoList.vue
    deleteTodo: function (todo) {
      axios.delete(`${SERVER_URL}/todos/${todo.id}/`)
        .then(res => {
          // console.log(res)
          // for문을 돌아서 id 값을 찾는 것과 같다.
          const idx = this.todos.findIndex(todo => {
            return todo.id === res.data.id
          })
          this.todos.splice(idx, 1)
        })
        .catch(err => console.log(err))
    }
```



### 1.2.10 update 버튼 만들기

- `updateTodo`라는 함수를 제목을 클릭했을 때 실행될 수 있도록 달아주고, 함수에 `todo`인자를 넘겨준다.

```vue
<!-- TodoList.vue -->
        <span @click="updateTodo(todo)">{{ todo.title }}</span>
```

- 함수를 만들어준다.

```javascript
// TodoList.vue
const todoItem = {
        title: todo.title,
        completed: !todo.completed
      }
axios.put(`${SERVER_URL}/todos/${todo.id}/`, todoItem)
        .then((res) => {
          console.log(res)
          todo.completed = !todo.completed
        })
        .catch((err) => {
          console.log(err)
        })
    }
```

- 스타일을 정의해준다.

```vue
<!-- TodoList.vue -->
        <span 
        @click="updateTodo(todo)"
        :class="{ completed : todo.completed }"
        >{{ todo.title }}</span>

<style>
 .completed {
   text-decoration: line-through;
   color: gray;
 }
</style>
```



## 2.1 Accounts - Server

### 2.1.1 accounts 앱 생성

- `accounts` 앱을 생성한다.

```bash
$ python manage.py startapp accounts
```

- User 모델을 정의한다.

```python
# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

- 새롭게 정의한 User 모델과 앱을 `settings.py`에 등록해준다.

```python
# settings.py

INSTALLED_APPS = [
    'accounts',
    ...
]

AUTH_USER_MODEL = 'accounts.User'
```

- url을 등록한다.

```python
# drf_server/urls.py

    path('accounts/', include('accounts.urls')),

```

- accounts 폴더 내에 `urls.py` 파일을 만들고 url 뼈대를 작성한다.

```python
# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
]
```

- accounts 앱 폴더 내에 `serializers.py`라는 파일을 생성하고 User 모델에 대한 serializer를 생성해준다.

```python
# accounts/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
```



### 2.1.2 User - Todo 모델 참조

- `Todo` 모델에 `User` 모델을 참조하는 `user`라는 1:N 관계의 필드를 정의해준다.

```python
# todos/models.py

from django.db import models
from django.conf import settings

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='todos')	# 정의해준다.
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
```

- 여기서 모델을 수정했으므로 `todos/migrations/0001_initial.py`, `db.sqlite3` 파일을 삭제하고 migration을 다시 진행한다.



### 2.1.3 todo 생성시 user 정보 담기

- view 함수를 수정하여 todo 인스턴스 생성시 user 정보가 함께 저장될 수 있도록 로직을 변경한다.

```python
# todos/views.py

@api_view(['GET', 'POST'])
def todo_list_create(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(request.user.todos, many=True)	## 여기도
        return Response(serializer.data)
    else:
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)	## 여기를 수정해준다!!
            return Response(serializer.data)
```

- 리스트를 표시할 때는, 해당 유저의 todos만 보여준다.
- todo 생성시 user 정보를 담아준다.



### 2.1.4  Signup 로직

- 먼저 url을 생성한다.

```python
# accounts/urls.py

urlpatterns = [
    path('signup/', views.signup)
]
```

- :white_check_mark: 비밀번호 hashing 작업을 거친다.
- signup 함수 로직을 작성한다.
  - :white_check_mark:`api_view`를 꼭 달아주어야 한다!!

```python
# accounts/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import UserSerializer

@api_view(['POST'])
def signup(request):
    # Client에서 보내온 정보 받기
    password = request.data.get('password')
    passwordConfirmation = request.data.get('passwordConfirmation')

    # 비밀번호 일치 여부 확인
    if password != passwordConfirmation:
        return Response({'error' : '비밀번호가 일치하지 않습니다.'})

    # 사용자가 보낸 데이터로 UserSerializer를 통해 데이터 생성
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        # 그냥 저장하고 끝내면 비밀번호 유출
        user = serializer.save()
        # 비밀번호 hashing
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data)
```



## 2.2 Accounts - Client

### 2.2.1 회원가입 컴포넌트 생성

- `views/accounts/SignUp.vue` 파일 생성한다.

```vue
<!-- SignUp.vue -->
<template>
  <div>
    <h2>SignUp</h2>
  </div>
</template>

<script>
export default {
  name: 'SignUp'
}
</script>
```

```javascript
// index.js

import SignUp from '@/views/accounts/SignUp'
const routes = [
    ...
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  }]
```

- 주소를 변경하여 App 별로 관리할 수 있도록 한다.

```javascript
// index.js

const routes = [
  {
    path: '/todos',
    name: 'TodoList',
    component: TodoList
  },
  {
    path: '/todos/create',
    name: 'CreateTodo',
    component: CreateTodo
  },
  {
    path: '/accounts/signup',
    name: 'SignUp',
    component: SignUp
  }
]
```

- `App.vue`에 링크를 달아준다.
- `|` 파이프 문자를 넣어준다.

```vue
<!-- App.vue -->

      <router-link :to="{ name: 'SignUp' }">SignUp</router-link>
```

### 2.2.2.회원가입 템플릿 작성

- 템플릿을 작성한다.

```vue
<!-- SignUp.vue -->

<div>
    <h2>SignUp</h2>
    <div>
      <label for="username">username : </label>
      <input type="text" id="username" autofocus>
    </div>
    <div>
      <label for="password">password : </label>
      <input type="password" id="password">
    </div>
    <div>
      <label for="passwordConfirmation">passwordConfirmation : </label>
      <input type="password" id="passwordConfirmation">
    </div>
  </div>
```

- 데이터 틀을 딕셔너리 형태로 만들어준다.

```javascript
// SignUp.vue

data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: ''
      }}}
```

- 해당 데이터를 `<input>` 태그에 `v-model`로 달아준다.
  - :heavy_check_mark: 데이터를 불러올 때 `credentials.username` 등의 형태로 불러와야 한다는 것에 주의한다.

```vue
<!-- SignUp.vue -->
      <input type="text" id="username" v-model="credentials.username" autofocus>
      <input type="password" id="password" v-model="credentials.password">
      <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation" @keypress.enter="signup">
```

- `signup`이라는 함수를 작성한다.

```javascript
// SignUp.vue

import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

  methods: {
    signup: function () {
      // axios 요청을 보낼 것이다. signup -> user Create -> post
      axios.post(`${SERVER_URL}/accounts/signup/`, this.credentials)
        .then(() => {
         // console.log(response)
          this.$router.push({ name: 'Login' })	// 변경해준다!!
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
```



### 2.2.3 JWT 발급

> `존왓탱`
>
> 로그인 로직 처리를 위해 선행되는 단계로, Json Web Token을 발급한다. [공식 사이트](https://jpadilla.github.io/django-rest-framework-jwt/)를 참고한다.

- 먼저 pip를 설치한다.

```bash
$ pip install djangorestframework-jwt
```

- 등록한다. (이건 dummy로 등록하는 코드이다!)

```python
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}
```

- 사용한다.
  - `obtain_jwt_token`도 하나의 view 함수라고 할 수 있다.

```python
# accounts/urls

from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    ...
    path('api-token-auth/', obtain_jwt_token),
]
```



### 2.2.4 로그인 템플릿 작성

- `views/accounts/Login.vue` 파일을 생성한다.

- 뼈대를 만든다.

```vue
<!-- Login.vue -->
<template>
  <div>
    <h2>Login</h2>
  </div>
</template>

<script>
export default {
  name: 'Login'
}
</script>
```

- 컴포넌트를 router에 등록한다.

```javascript
// index.js
import Login from '@/views/accounts/Login'
const routes = [
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  }
]
```

- `App.vue`에서 링크도 달아준다.

```vue
<!-- App.vue -->
      <router-link :to="{ name: 'Login' }">Login</router-link>
```

- `Login.vue`의 템플릿을 작성한다.

```vue
<!-- Login.vue -->
  <div>
    <h2>Login</h2>
    <div>
      <label for="username">username : </label>
      <input type="text" id="username" v-model="credentials.username" autofocus>
    </div>
    <div>
      <label for="password">password : </label>
      <input type="password" id="password" 
      v-model="credentials.password"
      @keypress.enter="login"
      >
    </div>
  </div>
```

- 데이터를 작성한다.

```javascript
// Login.vue
data: function () {
    return {
      credentials: {
        username: '',
        password: ''
      }
    }
  }
```

- 함수를 작성한다.

```javascript
// Login.vue
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

  methods: {
    login: function () {
      axios.post(`${SERVER_URL}/accounts/api-token-auth`, this.credentials)
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
```



### 2.2.4 login 상태에 따른 분기

- `App.vue`에 `login` 데이터를 생성한다.

```javascript
// App.vue

data: function () {
    return {
        login: false
    }
}
```

- Vue가 생성될 때 localStorage에서 토큰이 있는지 확인하고 `login` 데이터의 값을 변경해준다.

```javascript
// App. vue
  created: function () {
    const token = localStorage.getItem('jwt')

    if (token) {
      this.login = true
    }
  }
```

- 다음으로 로그인 여부에 따른 분기를 템플릿에서 작성해준다.

```vue
<!-- App.vue -->
<span v-if="login">
    <router-link :to="{ name: 'Login' }">Login</router-link>
    <router-link :to="{ name: 'SignUp' }">SignUp</router-link>
</span>
<span v-else>
    <router-link router-link @click.native="logout" to="#">Logout</router-link>
</span>
```



### 2.2.5 JWT 값 저장

>`localStorage.setItem`

- 먼저 JWT 만료 시간을 변경해준다.
  - 여기서는 연습을 위해서 `days=1`으로 넉넉하게 변경한다.

```python
# settings.py

import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
}
```

- 토큰을 localStorage에 넣어준다.
  - `jwt`이라는 임의의 이름으로 저장해준다.

```javascript
// Login.vue

    login: function () {
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
        .then((res) => {
          // console.log(res)
          localStorage.setItem('jwt', res.data.token)	// 여기여기
          this.$router.push({ name : 'TodoList'})	//
        })
        .catch((err) => {
          console.log(err)
        })
    }
```



### 2.2.6 token 보내기

> `localStorage.getItem`

- `getToken` 이라는 함수를 생성한다.

```javascript
// TodoList.vue
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
```

- 아래의 함수를 모든 `axios` 요청에서 매개변수로 넘겨준다.

```javascript
// TodoList.vue

const config = this.getToken()
axios.get(`${SERVER_URL}/todos/`, config)	//	 이거
axios.delete(`${SERVER_URL}/todos/${todo.id}/`, config)
axios.put(`${SERVER_URL}/todos/${todo.id}/`, todoItem, config)
```

- `CreateTodo.vue`에서도 위와 같은 작업을 반복한다.

```javascript
// CreateTodo.vue
 getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
```

```javascript
const config = this.getToken()
axios.post(`${SERVER_URL}/todos/`, todoItem, config)
```



### 2.2.7 회원가입 오류 해결하기

- `settings.py`의 `REST_FRAMEWORK`는 주석처리해준다.

```python
# settings.py
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
#     ),
# }
```

- `todos`의 `views.py`에서 decorator를 가져온다.
  - :white_check_mark: 데코레이터 순서가 중요하므로 유의한다!!

```python
# todos/views.py

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def todo_list_create(request):
    pass

@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def todo_update_delete(request, todo_pk):
    pass
```



### 2.2.8 로그아웃

- `App.vue`에 `<script>` 태그를 생성한다.

```javascript
// App.vue

export default {
  name: 'App',
  methods: {
    logout: function () {
      localStorage.removeItem('jwt')
      this.$router.push({ name:'Login' })
    }
  }
}
```

- `App.vue`에 logout 클릭하는 곳 만들어준다.

```vue
<!-- App.vue -->
      <router-link @click.native="logout" to="#">Logout</router-link>  |

```



***Copyright* © 2020 Song_Artish**