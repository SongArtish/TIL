# Django Test

---

[TOC]

---



## 시작하기

**프로젝트 생성 및 작성**

**User 모델 기본 커스터마이징**

```python
# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

- User 기능 사용을 위해서 `settings.py`에 커스터마이즈 한 User 모델을 반드시 등록해준다.

```python
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```

**마이그레이션**

- 이외 테스트를 하기 위해서 프로젝트 및 앱의 기본적인 코드를 작성해준다.



## Django Test

> Django에서는 다음의 3가지를 테스트한다.
>
> - models
> - forms
> - views - 기능에 대한 테스트



### 0. 구조

**`tests.py` 코드**

- 테스트를 위한 코드는 아래와 같이 작성한다.

```python
# accounts/tests.py

from django.test import TestCase

class AccountTest(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(False)
```

- :white_check_mark:`test_something_that_will_fail`의 값을 변경해준다.

```python
def test_something_that_will_fail(self):
        self.assertTrue(True)
```

**test를 위한 명령어**

```bash
$ python manage.py test
```

**테스트셋업**

- 매 테스트마다 사용하는 코드는 `setUp` 함수에 작성하여 효율성을 제고할 수 있다.

```python
# accounts/tests.py

def setUp(self):
    # Setup run before every test method.
    User.objects.create_user(username='testuser', password='password')
```



### 1. Model 테스트

**생성한 User 모델 테스트**

```python
# accounts/tests.py

from .models import User

def test_user_model_create(self):
    User.objects.create_user(username='testuser', password='password') # setUp 함수에 넣기
    user = User.objects.get(pk=1)
    self.assertEqual(user.username, 'testuser')
```

**User 모델 str method 테스트**

- 테스트를 위해 User 모델에 새로운 column을 추가해본다.

```python
# accounts/models.py

class User(AbstractUser):
    phone = models.CharField(max_length=11)

    def __str__(self):
        # Article object (1) / username
        return f'User object ({self.pk})'
```

```python
# accounts/tests.py

def test_user_str_method(self):
    User.objects.create_user(username='testuser', password='password') # setUp 함수에 넣기
    user = User.objects.get(pk=1)
    self.assertEqual(str(user), 'User object (1)')
```

**User 모델 phone 필드 테스트**

- 생성한 인스턴스의 `_meta` 정보 중 phone 필드의 max_length를 가져온다.
- :white_check_mark:`_meta`에서의 `_(언더바)`를 주의한다.

```python
# accounts/tests.py

def test_user_phone_field_max_length(self):
    User.objects.create_user(username='testuser', password='password') # setUp 함수에 넣기
    user = User.objects.get(pk=1)
    max_length = user._meta.get_field('phone').max_length
    self.assertEqual(max_length, 11)
```



- base 템플릿을 작성한다.

```django
<!-- base.html -->
{% if user.is_authenticated %}
	<a href="">logout</a>
{% else %}
	<a href="">login</a>
{% endif %}
```

- 간단하게 url만 작성한다.

```python
# accounts/urls.py

path('', views.index, name='index'),
```

- 그리고 테스트 함수를 작성한다.

```python
# accounts/tests.py

def test_base_template(self):

    # 1. 로그인 안 했을 때의 테스트
    # 서버를 켜고 /accounts/라는 url로 접속한다는 의미
    response = self.client.get('/accounts/')
    self.assertContains(response, '<a href="">login</a>')
    self.assertNotContains(response, '<a href="">logout</a>')

    # 2. 로그인 했을 때의 테스트
    self.client.login(username='testuser', password='password')
    response = self.client.get('/accounts/')
    self.assertContains(response, '<a href="">login</a>')
    self.assertNotContains(response, '<a href="">logout</a>')
```



### 2. Form 테스트





### 3. View 테스트

- `Todos`라는 앱의 index, create을 간단하게 작성하고 다음과 같이 테스트 할 수 있다.

```python
# todos/tests.py

from django.test import TestCase
from accounts.models import User
from todos.models import Todo

# Create your tests here.
class TodoTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='password')

    def test_todo_index(self):
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/todos/')

        self.client.login(username='testuser', password='password')
        response = self.client.get('/todos/')
        self.assertTemplateUsed(response, 'todos/index.html')        

    # create는 GET, POST 방식 나누기

    def test_todo_create_get(self):
        self.client.login(username='testuser', password='password')        # todos 경로로 요청한다.
        response = self.client.get('/todos/create/')
        # todos/form.html이 렌더링 되었는지 확인
        self.assertTemplateUsed(response, 'todos/form.html')
        self.assertEqual(response.status_code, 200)


    def test_doto_create_post(self):
        self.client.login(username='testuser', password='password')        # todos 경로로 요청한다.
        
        # 1. 유효하지 않은 데이터
        invalid_data = {
            # 'content' :  None
        }
        response = self.client.post('/todos/create/', invalid_data)
        self.assertEqual(response.status_code, 200)

        # 2. 유효한 데이터
        valid_data = {
            'content' : 'test-content'
        }
        response = self.client.post('/todos/create/', valid_data)
        todos = Todo.objects.all()
        self.assertEqual(len(todos), 1)
```



***Copyright* ©  2020 Song_Artish**