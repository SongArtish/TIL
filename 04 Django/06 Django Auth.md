# Django Auth

2020.09.16.

> Django Authentication System은 **인증(Authentication)**과 **권한(Authorization)** 부여를 함께 제공하며, 크게 User object, Web request에 대한 인증 시스템이 있다.
>

---

[TOC]

---



**준비하기**

- `accounts`라는 앱 생성 후 기본 세팅을 해준다.

```bash
$ python manage.py startapp accounts
```

오늘 수업은 accounts 앱에서 회원 정보와 관련된 요소들을 다룬다.



## Authentication Built-in Forms

> Django는 기본적으로 인증과 관련된 built-in form들을 제공한다. [Using the Django authentication system](https://docs.djangoproject.com/en/3.1/topics/auth/default/)



|  회원가입   |     로그인     |    로그아웃    |
| :---------: | :------------: | :------------: |
| user create | session create | session delete |



### 회원가입 : `UserCreationForm`

> `UserCreationForm`은 `ModelForm`이며, 회원가입에는 `회원가입 작성 페이지(GET)`와 `회원가입 로직(POST)` 2가지 logic이 필요하다.
>
> - `ModelForm` - ORM을 통해서 데이터베이스를 생성한다! 여기서는 ID생성을 위한 ID, 패스워드, 이메일 등을 생성하는 틀을 가지고 있다. 그리고 이미 form 형태를 취하고 있으므로, 바로 불러와서 유효성 검사도 할 수 있다.



**url 생성**

```python
# accounts/urls.py

path('signup/', views.signup, name='signup'),
```

**view 함수 생성**

- `UserCreationForm`은 `ModelForm`이기 때문에 따로 `forms.py`를 생성하지 않고 바로 form을 사용할 수 있다.

```python
# accounts/views.py

import django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == "POST":
        # POST를 통해서 받은 데이터를 불러와야 한다.
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request,'accounts/signup.html', context)
```

- `UserCreationForm`을 사용한 후에 반드시 `migrate`를 해줘야 한다.

**html 페이지 만들기**

```django
<!-- accounts/signup.html -->
{% extends 'base.html' %}

{% block content %}
<h1>회원가입</h1>
<form action="{% url 'accounts:signup' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
{% endblock  %}
```

**메인 페이지 상단에 회원가입 링크 만들기**

```django
<!-- base.html -->

<a href="{% url 'accounts:singup' %}">Signup</a>
```



### 로그인  :  `AuthenticationForm`

> 로그인에는 `로그인 페이지`와 `로그인 로직` 2가지 logic이 필요하다.

**로그인 로직**

- `login`은 첫번째 인자로 `request`를 받는다.

```
login(request, user, backend=None)
```

**url 작성**

**view 함수 작성**

```python
# accounts/views.py

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login

def login(request):
    # 사용자 인증이 되었다면
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)
```

**html 페이지 만들기**

```django
<!-- accounts/login.html -->

{% extends 'base.html' %}

{% block content %}
<h1>로그인</h1>
<form action="{% url 'accounts:login' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="login">
</form>
{% endblock  %}
```



## Cookie & Session

**Cookie(쿠키)**

> `쿠키(Cookie)`는 클라이언트의 **로컬에 저장**되는 key-value의 작은 데이터 파일로, HTTP의 비연결지향(connectionless)과 무상태(stateless)라는 특성에서 서버와 클라이언트를 연결해주는 역할을 한다.
>
> - Chrome 개발자도구(`F12`) > Application > Storage > Cookies 에서 쿠키 데이터를 확인할 수 있다.

**Session (세션)**

> 사이트와 특정 브라우저 사이의 "state(상태)"를 유지시키는 것으로 주로 로그인 상태 유지에 사용된다.  
>
> - Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 세션을 알아내며, 세션 정보는 django DB의 django_session 테이블에 저장된다.

:ballot_box_with_check: 쿠키 : 클라이언트 로컬에 파일로 저장

:ballot_box_with_check: 세션 : 서버에 저장 (이때 session id는 쿠키의 형태로 클라이언트 로컬에 저장)

:white_check_mark: HTTP **쿠키**는 상태가 있는 **세션**을 만들도록 해준다.



### 로그아웃 : `logout`

**url 등록**

```python
# accounts/urls.py

path('logout/', views.logout, name='logout'),
```
**view 함수 작성**

- 로그아웃은 세션만 지우면 된다.
```python
# accounts/views.py
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```



### 세션 유효기간 변경 : `SESSION_COOKIE_AGE`

```python
# settings.py

# 하루를 sec으로 상수 값 만들기
DAYS_IN_SECONDS = 86400
SESSION_COOKIE_AGE = DAYS_IN_SECONDS

# 활동할 때마다 cooke_age 원래대로 reset
SESSION_SAVE_EVERY_REQUEST = True
```



### 로그인 사용자에 대한 접급 권한 : `is_authenticated`

> Django는 session과 middleware를 통해 인증시스템을 request 객체에 연결하며, User class의 속성(attribute)인 `is_authenticated`를 통해 사용자가 인증되었는지 확인할 수 있다. (User에 항상 True이며, AnonymousUser에 대해서만 항상 False)

**사용자 인증 여부에 따라 다른 템플릿 보여주기**

- html 템플릿에서 사용자 인증 여부에 따라 템플릿을 다르게 표시할 수 있다. `request.user.is_authenticated`

```django
<!-- base.html -->
{% if request.user.is_authenticated %}
	<h3>Hello, {{ user.username }}</h3>
	<a href="{% url 'accounts:logout' %}">Logout</a>
{% else %}
	<a href="{% url 'accounts:signup' %}">Singup</a>
	<a href="{% url 'accounts:login' %}">Login</a>
{% endif %}
```
- view 함수에도 `request.user.is_authenticated`를 활용하여 인증된 사용자가 `signup`과 `login`에 접근하지 못하도록 조작할 수 있다.

```python
# views.py
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    ...
```

**로그인 사용자에게만 글 작성(create) 보여주기**

```django
<!-- articles/index.html -->

<h1 class="text-center">Articles</h1>
{% if request.user.is_authenticated %}
	<a href="{% url 'articles:create' %}">NEW</a>
{% else %}
	<a href="{% url 'articles:create' %}">[새글을 작성하려면 로그인해주세요]</a>
```



### 로그인 사용자에 대한 접근 권한 :  `@login required` 

> 사용자가 로그인 했는지 확인하는 view를 위한 데코레이터로, 로그인 하지 않은 사용자를 `settings.LOGIN_URL`에 설정된 경로로 redirect 시킨다.
>
> - LOGIN_URL의 기본 값은 `/accounts/login/`

- `Create, Update`에 `login_required` 데코레이터 붙이기

```python
# articles/views.py

from django.contrib.auth.decorators import login_required

@login_required
def create(request):
    pass
@login_required
def update(request):
    pass
```

**페이지 삭제(`delete`)에서의 `@login required`**

- `login required` 데코레이터는 GET method 요청을 처리할 수 있는 view함수에서 사용해야 한다.
- `delete` 함수에서는 `@require_POST` 때문에 `405 Error`가 발생하게 된다.

```python
# articles/views.py

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')
```



### 페이지 연결 : `next`

> Login 하지 않은 사용자가 create에 접근하려는 경우, decorator의 기능 중 `next` parameter를 처리해서 사용자 친화적으로 바꿔준다.

- `login.html`의 form의 action을 칸을 비워준다.

```django
<!-- accounts/login.html -->

<form action="" method="POST">
    ...
</form>
```

- login하지 않고 create를 클릭하면 로그인 페이지로 넘어가게 되는데, 다음과 같은 url로 가게된다.

```
.../login/?next=/articles/create/
```

- 로그인 후 바로 create 페이지로 넘어갈 수 있도록 view함수를 수정한다.

```python
# accounts/views.py

def create(request):
    if ... :
         return redirect(request.GET.get('next') or 'articles:index')
  	...
```



## User

> User objects는 User가 Django 인증 시스템에서 표현되는 모델로 오직 하나의 `User` 클래스(Class)만 존재하며, User 클래스는 AbstractUser 클래스의 상속을 받는다.
>
> `AbstractUser` : User model을 구현하는 완전한 기능을 갖춘 기본 클래스



### 회원정보수정 : `UserChangeForm`

> 회원정보를 수정하는 form으로, ModleForm이다.

**url과 view 함수 작성**

```python
# accounts/urls.py
path('update/', views.update, name='update'),

# accounts/views.py
from django.contrib.auth.forms import UserChangeForm
```

**html 템플릿 작성**

- `base.html`에는 인증된 사용자일 경우 index 페이지의 상단에 회원정보 수정 페이지로 갈 수 있는 링크를 만들어준다.

```django
<!-- base.html -->
{% if request.user.is_authenticated %}
	<a href="{% url 'accounts:update' %}">정보수정</a>
```

- `Signup`과 같은 템플릿을 작성하면 회원정보 수정란에서 사용자 권한 등과 같은 모든 필드를 다 제공하기 때문에, **Django 제공 form을 상속** 받아서 **custom**한다.



### UserModel 커스터마이징 : `get_user_model`

>Django에서는 User를 직접 참조하는 대신 django.contrib.auth.get_user_model()을 사용하여 user model을 참조해야 하며, 이는 현재 프로젝트에서 활성화(active)된 user model을 리턴한다.

**새로운 UserModel 정의**

- `forms.py`에서 기존 `UserModel`을 상속받아 와서 커스터마이징을 한다.

```python
# accounts/forms.py

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')
```

- get_user_model에서 `()괄호`를 빼먹지 않도록 주의한다.
- 이를 view 함수에 적용해준다.

```python
# accounts/views.py
from .forms import CustomUserChangeForm

def update(request):
    if request.method == 'POST':
        # ModelForm은 첫 인자로 데이터(request.POSt)가 입력된다.
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```



### 회원탈퇴

**url 생성**

```python
# accounts/urls.py
path('delete/', views.delete, name='delete'),
```

**view 함수 작성**

```python
from django.views.decorators.http import require_POST

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')
```
- `base.html`에 `회원탈퇴` 링크를 넣어준다.

```django
<!-- base.html -->
{% if request.user.is_authenticated %}
      <form action="{% url 'accounts:delete' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
```



### 비밀번호 변경 : `PasswordChangeForm`

**url 등록**

```python
# accounts/urls.py

path('password/', views.password, name='password'),
```
**`base.html`에 링크 생성**

```html
<!-- base.html -->
<a href="{% url 'accounts:password' %}">비밀번호 변경</a>
```
- `PasswordChangeForm`의 입력 인자값은 다음과 같다.
- 첫번째 요소가 `user`이므로 생성시 `instance = user`가 아닌, `request.user`인자를 입력한다.

```python
class PasswordChangeForm():
    def __init__(self, user, *args, **kwargs):
        pass
```

**view 함수 작성**

```python
# accounts/views.py	

from django.contrib.auth.forms import PasswordChangeForm

def password(request):
    # update
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/password.html', context)
```

- 하지만 비밀번호를 변경하면 `session id`가 사라지기 때문에 자동으로 로그아웃이 된다.
- 따라서, form 저장 후 `update_session_auth_hash(request, form.user)`를 입력해서 session이 수정될 수 있도록 해준다.

```python
# accounts/views.py

from django.contrib.auth import update_session_auth_hash

def password(request):
    ...
    if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    ...
```



***Copyright* © Song_Artish**