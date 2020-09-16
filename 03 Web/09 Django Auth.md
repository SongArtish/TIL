# Django Auth

2020.09.16.

> Django Authentication System에서는 **인증**과 **권한** 부여를 함께 제공한다. 크게 User object, Web request에 대한 인증 시스템이 있다.
>

---

[TOC]

---



**Authentication** (인증)

- 자신이 누구라고 주장하는 사람의 신원을 확인하는 것

**Authorization** (권한, 허가)

- 가고 싶은 곳으로 가도록 혹은 원하는 정보를 얻도록 허용하는 과정



여기까지 인트로!!



`accounts`라는 앱 생성 후 기본 세팅하기

```bash
$ python manage.py startapp accounts
```



## Authentication Built-in Forms

- django는 기본적으로 인증과 관련된 built-in form들을 제공
- 회원가입(`UserCreationForm`), 로그인(`AuthenticationForm`)

[Using the Django authentication system](https://docs.djangoproject.com/en/3.1/topics/auth/default/)

> *class* `UserCreationForm`[¶](https://docs.djangoproject.com/en/3.1/topics/auth/default/#django.contrib.auth.forms.UserCreationForm)
>
> ​	A [`ModelForm`](https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/#django.forms.ModelForm) for creating a new user.
>
> It has three fields: `username` (from the user model), `password1`, and `password2`. It verifies that `password1` and `password2` match, validates the password using [`validate_password()`](https://docs.djangoproject.com/en/3.1/topics/auth/passwords/#django.contrib.auth.password_validation.validate_password), and sets the user’s password using [`set_password()`](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#django.contrib.auth.models.User.set_password).



### 회원가입

회원자입 작성 페이지 (GET)

회원가입 로직(POST)

2가지 : user, create 2가지

### `UserCreationForm`

- ModelForm이다.



회원가입을 위한 url 생성

```python
# accounts/urls.py

    paht('signup/', views.signup, name='signup'),
```

view함수 생성

- `UserCreationForm`은 `ModelForm`이기 때문에 따로 `forms.py`를 생성하지 않고 바로 form을 사용할 수 있다.

```python
# accounts/views.py

import django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm
    context = {
        'form' : form,
    }
    return render(request,'accounts/signup.html', context)
```



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



Index 페이지 상단에 로그인 표시창 만들기

```django
<!-- base.html -->

<a href="{% url 'accounts:singup' %}">Signup</a>
```



### 로그인 페이지

> 로그인 페이지와 로그인 로직 2가지가 필요하다. (session, create)



### `AuthenticationForm`

- 첫 번째 위치인자로 `request`를 취한다.



## Cookie & Session

HTTP (HyperText Transfer Protocol)

- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜
- 웹에서 이루어지는 모든 데이터 교환의 기초

HTTP 특징

- 비연결지향(connectionless) : 서버는 응답 후 접속을 끊음
- 무상태(stateless) : 접속이 끊어지면 클라이언트와 서버간의 통신이 끝나며 상태를 저장하지 않음



이러한 비연결지향과 무상태 특성에서 서버와 클라이언트를 연결해주는 역할이 쿠키이다!

Cookie(쿠키)

- 클라이언트의 로컬에 저장되는 키-값의 작은 데이터 파일
- 웹 페이지에 접속하면 요청한 웨 페이지를 받으며 쿠키를 로컬에 저장하고, 클라이언트가 재요청시에 웹 페이지 요청과 함께 쿠기 값도 같이 전송

- 예시

  - 아이디 자동완성, 공지 하루 안보기, 팝업 체크, 비로그인 장바구니 담기 등
  - 편의를 위하되 지워지거나 유출 되도 큰 일은 없을 정보들을 저장

  





*Copyright* © Song_Artish