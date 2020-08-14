# Django Template & View

2020.08.14.

*****

[toc]

*****



## 1. 코드 작성 순서

```python
1. urls.py
2. views.py
3. templates
```

### 1.1 `urls.py`

> 위치: `<프로젝트 폴더>/<프로젝트 폴더>/url.py`

```python
path('<url 이름>/', views.<url 이름>),
```

- `path('', views.<url 이름>)`을 입력하면, 메인페이지 주소가 할당된다.
- `url`에서는 `_`(언더바) 보다는 `-`(하이픈)이 더 권장된다.

```python
# 예시
from articles import views

urlpatterns = [
    path('<url 이름>/', views.<url 이름>),
    path('admin/', admin.site.urls),	# 관리자 페이지 (default)
]
```
**Django imports style guide**

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

### 1.2 `view.py`

> 위치: `<프로젝트 폴더>/<프로젝트 폴더>/view.py`

```python
def index(request):
    return render(request, '<템플릿 파일명>.html')
```

- view함수는 반드시 첫번째 인자로 `request`가 입력되어야 한다.
- `render()`를 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨준다.

```python
# context 예시
import random
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    # context는 딕셔너리 형태로 정의해야 한다.
    context = {	
        'pick':pick,
        'menu': menu
    }
return render(request, 'dinner.html', context)
```

### 1.3 `templates > .html`

> 위치: `<앱 폴더>/templates` 안에 html 파일 생성

```html
<!-- context를 받은 경우 html 입력 예시-->
<body>
    <h2>오늘 저녁은 {{pick}}입니다.</h2>
</body>
```



## 2. DTL (Django Template Language)

>  Django Template System에서 사용하는 built-in template system으로 `조건`, `반복`, `치환`, `필터`, `변수` 등의 기능을 제공(html에서는 불가)한다. 프로그래밍적 logic이 아니라, 프레젠테이션을 표현하기 위한 것이다.
>
> [Django 공식문서](https://docs.djangoproject.com/en/3.0/topics/templates/) 참고

### 2.1 Variable

```html
{{variable}}
```
#### Variable Routing

> 주소 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것

```python
# urls.py 예시
path('hello/<name>/', views.hello)
path('hello/<str: name>/', views.hello)		# str : '/(slash)'를 제외한 문자열, 숫자
path('hello/<int: numbers/'), views.hello)	# int : 정수 값만 입력 가능
```
- default는 `str`이기 때문에 생략 가능하다.

```python
# views.py 예시
def hello(request, name):
    context = {
        'name': name,
    }
return render(request,'hello.html',context)
```

```html
<!-- .html 예시 -->
<body>
    <h1>안녕하세요, {{name}}</h1>
</body>
```

### 2.2 Filter

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

**length**

> Returns the length of the value. This works for both strings and lists.

```html
{{ value|length }}
```
If `value` is `['a', 'b', 'c', 'd']` or `"abcd"`, the output will be `4`. The filter returns `0` for an undefined variable.

*****

**capfirst**

```html
<!-- capfirst -->
{{ value|capfirst }}
```

If `value` is `"django"`, the output will be `"Django"`.

*****

**time**

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
{{ value|time:"TIME_FORMAT" }}
```

the output will be the string `"01:23"` (The `"TIME_FORMAT"` format specifier for the `de` locale as shipped with Django is `"H:i"`).

*****



### 2.3 Tags

>  [Built-in template tags and filters](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#ref-templates-builtins-tags)

```html
{% tag %}
```

#### `for`

> `{% endfor %}`를 통해 반드시 종료를 선언해야한다.

```html
{% for _ in variable %}
	<p>내용</p>
{% endfor %}
```
```html
<!-- for 예시 -->
<body>
    {% for menu in menus %}
     	{{ forloop.counter }} : {{ menu }}
	{% endfor %}
</body>
<!-- forloop.counter은 넘버링이 필요한 경우 사용한다. -->
```

```html
<!-- for...empty 구문 -->
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% empty %}
    <li>Sorry, no athletes in this list.</li>
{% endfor %}
</ul>
<!-- 비어 있는 경우 출력할 내용을 선언한다. -->
```

#### `if`, `elif`, `else`

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



## 3. Form

> 웹에서 사용자 정보를 입력하는 여러(text, button, checkbox, file, hidden, image, password, radio, reset, submit) 방식을 제공하고, **사용자로부터 할당된 데이터를 서버로 전송하는 역할**을 담당하는 HTML 태그. 한 페이지에서 다른 페이지로 데이터를 전달하기 위해 사용한다.

**3.1 `url`의 구조**

> url은 `프로토콜://호스트주소/경로(path)` 이하 `key:value`로 구성된다.
>
> `https://search.naver.com/search.naver?` 에서 `?`는 query string이라고 하며, 이하 `query=검색어`와 같이 `key:value`의 형태를 가진다.

query=헤이즈

- query string
- key=value

**3.2 절차**

```python
1. throw.html에서 <form>태그 사용
2. catch로 요청을 보냄
3. catch가 view 함수 실행하고 데이터를 받음
4. catch.html 실행
```

**3.3 throw & catch**

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
    message = request.GET.get('name')	# 없으면 none을 반환하기 때문에 get 메서드 사용
    context = {
        'message' : message
    }
    return render(request, 'catch.html',context)
```

- throw에서 보낸 `<form>` 데이터는 **request** 안에 딕셔너리의 형태로 담겨있다.

*Copyright* © Song_Artish