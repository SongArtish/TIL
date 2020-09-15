# Django TV

2020.08.14.



*****

[toc]

*****



**코드 작성 순서**

```python
1. urls.py
2. views.py
3. templates
```



## 1. `urls.py`

> Django 서버에 요청(request)이 들어오면, 그 요청이 어디로 가야하는지 인식하고 관련된 함수(view)로 넘겨준다.
>
> 위치: `<프로젝트 폴더>/<프로젝트 폴더>/url.py`

```python
urlpatterns = [
    path('<url 이름>/', views.<함수 이름>),
]
```

- `url`에서는 `_`(언더바) 보다는 `-`(하이픈)이 더 권장된다.

```python
# urls.py 예시
from articles import view

urlpatterns = [
    # 메인페이지 주소 할당
    path('', views.index),
    # 관리자 페이지 (default)
    path('admin/', admin.site.urls),
]
```

### URL 분리

- app이 2개 이상일 경우 `urls.py`를 다음과 같이 작성한다.

```python
# <프로젝트 폴더> / urls.py

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<앱 폴더>/', include('<앱 폴더>.urls')),
]
```
- `include()`는 다른 URLconf(<앱>/urls.py)들을 참조할 수 있도록 도와준다.

### URL Namespace

> 여러 개의 app이 존재할 때, `app_name`을 지정한다.

```python
# <앱 폴더> / urls.py

from django.urls import path
from . import views

app_name = '<앱 이름>'
urlpatterns = [
    path('<템플릿 이름>/', views.<템플릿 이름>, name='이름 값'),
]
```

### Variable Routing

> 주소 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것

```python
# urls.py 예시

path('hello/<name>/', views.hello)
# str : '/(slash)'를 제외한 문자열, 숫자
path('hello/<str: name>/', views.hello)
# int : 정수 값만 입력 가능
path('hello/<int: numbers/'), views.hello)
```

- default는 `str`이기 때문에 생략 가능하다.



## 2. `views.py`

> `views.py`에서는 함수를 정의하는데, view함수는 첫번째 인자로 `request`가 반드시 입력되어야 한며, `render()`를 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨준다.
>
> 위치: `<프로젝트 폴더>/<프로젝트 폴더>/view.py`

```python
def index(request):
    return render(request, '<템플릿 파일명>.html')
	# render함수를 ㅌㅇ해 
```

- 앱이 여러 개이며, model이 있는 경우는 다음과 같이 사용할 수도 있다.

```python
# views.py 예시
from django.shortcuts import render, redirect
from .models import <모델 이름>

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    # 앱이 여러개인 경우에는 '<앱 이름>/<템플릿>html'로 입력
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    # redirect를 하는 경우 '<앱 이름>:<함수명>'을 입력
    return redirect('articles:detail', pk)
```

- 위에서 모델명은 Article, 앱 이름은 articles이다.
- `request`는 요청 간의 모든 정보를 담고 있는 변수이다.

### Render vs. Redirect

**render**
템플릿을 불러올 때 사용

```python
render(request, template_name, context=None, content_type=None, status=None, using=None)
```

**redirect**
URL로 이동

```python
redirect(to, permanent=False, *args, **kwargs)
```



### Django Namespace

```python
# articles/views.py 

return render(request, 'articles/index.html')
```



## 3 `templates`

> 위치: `<앱 폴더>/templates` 안에 html 파일 생성

- 앱이 여러개인 경우는 `<앱 폴더>/<templates>/<앱 폴더이름>`의 경로에서 template을 관리한다.

**Template Variable**

- `views.py`에서 context를 통해 넘겨준 변수를 template에서는 다음과 같이 사용한다.

```html
<!-- context에서 pick 변수를 받은 경우-->
<body>
    <h2>오늘 저녁은 {{pick}}입니다.</h2>
</body>
```

### URL Name

> path() 함수의 name value를 작성해 `{% url %}`를 통해 template tag로 호출

```html
<!-- throw.html -->

<body>
  <h1>Throw 페이지</h1>
   <!-- 다음과 같이 호출 -->
  <form action="{% url 'catch' %}" method="GET">
    <label for="name">데이터 입력 : </label>
    <input type="text" id="name" name="name">
    <input type="submit">
  </form>
</body>
```

```html
<a href="/pages/"></a>

<!-- 실제 해당 url로 이동 -->
<a href="/pages/index/"></a>
<!-- pages라는 이름의 앱에 있는 index라는 이름의 url로 이동
따라서, 어떠한 경로로 바뀌더라도 잘 따라간다. -->
<a href="{% url 'pages:index'}"></a>
```

### DTL 

>  Django Template Language는 Django 템플릿 시스템에서 사용하는 built-in template system으로 `조건`, `반복`, `치환`, `필터`, `변수` 등의 기능을 제공(html에서는 불가)한다. 프로그래밍적 logic이 아니라, 프레젠테이션을 표현하기 위한 것이다.
>
>  [Django 공식문서](https://docs.djangoproject.com/en/3.0/topics/templates/) 참고
>
>  - `{{ __(a)__ }}` : 사용자가 설정한 것.
>  - `{% __(a)__ %}` : Django에서 제공하는 것. (자세한건 문서 참조)

**2.1 Variables**

```html
{{variable}}
```
```html
<!-- lorem 예시 -->
<p>{% lorem %}</p>	<!-- 전체 입력 -->
<p>{% lorem 3 w %}</p>	<!-- 3개 단어만 출력 (word)-->
<p>{% lorem 3 w random %}</p>	<!-- 랜덤 출력 -->
<p> {% lorem 2 p%} </p>	<!-- 2개 문단 출력 (paragraph) -->
```

**2.2 Filter**

```html
{{variable|filter}}
```

```html
<!-- 예시 -->
<body>
    {% if messages|length >= 100 %}
   		You have lots of messages today!
	{% endif %}
</body>
```
*****

length vs. wordcount

> `length`는 문자열이나 리스트의 길이를 반환하며, `wordcount`는 단어 수를 반환한다.

```html
{{ value|length }}
```
```html
{{ value|wordcount }}
```

*****

title vs. capfirst

> `title`은 각 단어의 첫 문자를 대문자로 변환하는 반면, `capfirst`는 전체의 첫 글자만 대문자로 변환한다.

```html
{{ value|capfirst }}
```

```html
{{ value|title }}
```

*****

time

```html
{{ value|time:"H:i" }}
```

If `value` is equivalent to `datetime.datetime.now()`, the output will be the string `"01:23"`.

```html
{% value|time:"H\h i\m" %}
```

This would display as “01h 23m”.

```html
{{ value|time }}
{{ value|time:"[TIME_FORMAT]" }}
```

the output will be the string `"01:23"` (The `"TIME_FORMAT"` format specifier for the `de` locale as shipped with Django is `"H:i"`).

```html
<!-- 예시 -->
<!-- 2020년 02월 02일 (Sun) PM 02:02 -->
{{today|date:Y년 m월 d일 (D) A h:i}}
```

*****

truncatewords vs. truncatechars

> 글자 수를 제한한다.

```html
  <p> {{ my_sentence|truncatewords:3 }} </p>
  <p> {{ my_sentence|truncatechars:3 }} </p>
  <p> {{ my_sentence|truncatechars:10 }} </p> 
  <!-- 빈칸도 글자수로 count하며, 중간에 잘린 단어는 ... 으로 표시된다.-->>
```

*****

add

> 숫자를 더한다.

```html
{{ number|add:3 }}
```



**2.3 Tags**

>  [Built-in template tags and filters](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#ref-templates-builtins-tags)

```html
{% tag %}
```

---

**`for`**

> `{% endfor %}`를 통해 반드시 종료를 선언해야한다.

```html
{% for _ in variable %}
	<p>내용</p>
{% endfor %}
```
```html
<!-- for...empty 구문 -->
<ul>
{% for athlete in athlete_list %}
    <li>{{ forloop.counter }} : {{ athlete.name }}</li>
{% empty %}
    <li>Sorry, no athletes in this list.</li>
{% endfor %}
</ul>
<!-- 비어 있는 경우 출력할 내용을 선언한다. -->
<!-- forloop.counter은 넘버링이 필요한 경우 사용한다. -->
```

---

`if`, `elif`, `else`

> `{% endif %}`를 통해 반드시 종료를 선언해야한다.

```html
{% if _ in variable %}
    <p>내용</p>
{% endif %}
```

- `and`, `if not`, `if or `, `if not or`, `if and not` 구문과 boolean 연산자도 사용할 수 있다.

```html
<!-- 예시 -->
{% if forloop.first %}	<!-- 첫 번째 반복문일 경우 -->
	<p>첫 번째 반복문 입니다.</p>
{% else %}
	<p>현재 가입한 유저가 없습니다.</p>
{% endif %}
```

### 템플릿 상속

> 다음의 폴더에 `base.html`이라는 모든 템플릿의 기본틀이 되는 base 템플릿을 작성한다.
>
> 위치: `<프로젝트 폴더>/<templates>/base.html`

- `base.html` 파일에는 기본 html 세팅에 기본틀을 짜고 이후 다른 템플릿에서 수정할 수 있는 `blcok` 공간을 만든다.

```html
{% block <블럭 이름> %}
{% endblock %}
```

- block enter로 생성가능

```html
<!-- blcok 예시 -->
<body>
    <div class="container">
        {% block content %}
        {% endblock %}
    </div>
</body>
```

- 다음으로는 `settings.py`에는 `base.html`을 찾을 수 있도록 값을 설정한다.

```python
TEMPLATES = [
    ...
    'DIRS' : [BASE_DIR/'<프로젝트 이름'/'templates'],
    'APP_DIRS' :True,
    ...
]
```

- 템플릿을 가져올 때 DIRS의 폴더를 장 먼저 조사하고 후에 앱폴더의 템플릿을 조사한다.
- 설정한 base 템플릿은 각 앱 템플릿에서 다음과 같이 사용할 수 있다.

```html
{% extends 'base.html' %}
{% block content %}
	<h2> 여기에 내용을 입력합니다. </h2>
{% endblock %}
```

- `{% extends '' %}`태그를 통해 base 템플릿을 불러온다.

## HTML Form

> 웹에서 사용자 정보를 입력하는 여러(text, button, checkbox, file, hidden, image, password, radio, reset, submit) 방식을 제공하고, **사용자로부터 할당된 데이터를 서버로 전송하는 역할**을 담당하는 HTML 태그. 한 페이지에서 다른 페이지로 데이터를 전달하기 위해 사용한다.
>
> 핵심 속성 2가지
>
> - **action** : 입력 데이터가 전송될 URL 지정
> - **method** : 입력 데이터 전달 방식 지정 (GET, POST)

**4.1 `url`의 구조**

> url은 `프로토콜://호스트주소/경로(path)` 이하 `key:value`로 구성된다.

- `https://search.naver.com/search.naver?` 에서 `?`는 query string이라고 하며, 이하 `query=검색어`와 같이 `key:value`의 형태를 가진다.

**4.2 HTTP mehod `GET`**

> 서버로부터 정보를 조회하는데 사용한다. 

- 데이터를 서버로 전송할 때 `query string`을 통해 전송한다.
- 서버의 데이터나 상태를 변경시키지 않아야하기 때문에 조회(html)를 할 때 사용한다.

**4.3 throw & catch**

```python
# 절차

1. throw.html에서 <form>태그 사용
2. catch로 요청을 보냄
3. catch가 view 함수 실행하고 데이터를 받음
4. catch.html 실행
```

**throw**

```html
<form action="/catch/" method="GET">
    <label for="input의 id">라벨</label>
    <input type="text" id="id명" name="이름명">
    <input type="submit">
</form>
```

- `method="GET"`은 서버로부터 정보를 조회하는 데 사용한다. (`query string`을 통해 전송)

**catch**

```python
def catch(request):
    # 없으면 none을 반환하기 때문에 get 메서드 사용
    message = request.GET.get('name')
    context = {
        'message' : message
    }
    return render(request, 'catch.html',context)
```

- throw에서 보낸 `<form>` 데이터는 **request** 안에 딕셔너리의 형태로 담겨있다



**<참고> Django imports style guide**

```python
# standard library
import json

# third-party
import bcrypt

# Django
from django.http import Http404

# local Django
from .models import LogEntry
```



*Copyright* © Song_Artish