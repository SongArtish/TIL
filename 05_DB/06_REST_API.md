# REST API

2020.10.05

> 프로그래밍을 통해 요청에 **RESTful한 방식**으로 **JSON을 응답하는 서버**를 만들자!

---

[TOC]

---



## API

|         |            인터페이스             |                목적                |
| :-----: | :-------------------------------: | :--------------------------------: |
| **API** | Application Programming Interface |   프로그래밍으로 특정 작업 수행    |
|   CLI   |      Command Line Interface       | 명령어로 작업을 수행하기 위한 과정 |
|   GUI   |      Graphic User Interface       |       그래픽으로 작업을 수행       |



### API Server

> 사용자의 요청에 대해서 서버가 응답을 해주는 것



### RESTful API

> **`Representational State Transfer`**(상태전송표현) 는 자원과 주소의 지정 방법이다. (개발자들 간의 약속!!:crossed_fingers:) 
>
> ```
> # REST의 구성
> - 자원 : URI
> - 행위 : HTTP Method
> - 표현 : Representations
> ```

예시 

- `GET/article/1/read/`는 불필요한 정보를 제거하여 다음과 같이 만들어야 한다.

```http
GET/articles/1/
```

- `artice/2/create/`는 다음과 같이 만들어야 한다.

```http
POST/artcles/2/
```



#### 구성요소 1 : URI

> URI(Uniform Resource Identifier, 통합 자원 식별자)는 하나의 리소스를 가리키는 문자열이며, 인터넷에 있는 자원을 나타내는 유일한 주소이다. 가장 흔한 URI는 URL로 웹 상에서의 위치로 리소스를 식별한다.
>
> - 통칭, URI는 URL로 인식되지만, 엄밀하게는 URI는 URL과 URN으로 구분할 수 있다.

```http
http://localhost:3000/posts/3
```

- `http` : scheme/프로토콜
- `localhost` : 호스트
- `3000` : 포트
- `posts/3` : path

```http
http://google.com/search?q=http
```

- `q=http` : 쿼리(query). GET요청을 할 때의 query string parameter

```http
http://getbootstrap.com/docs/4.1/layout/overview#containers
```

- `#containers` : 프래그먼트(Fragment). html 문서가 길 때, 북마크와 같은 역할을 수행하는 것으로 브라우저에서 편의를 위해 제공.



#### 구성요소 2 : HTTP

> Hyper Text Transfer Protocol은 컨텐츠를 전송하기 위한 프로토콜(규약)이다.

**HTTP 기본 속성**

|             |                       비고                        |
| :---------: | :-----------------------------------------------: |
|  Stateless  |             상태 정보가 저장되지 않음             |
| Connectless | 서버에 요청을 하고 응답을 한 이후에 연결은 끊어짐 |

**HTTP Method** :eight_pointed_black_star:

|     구분      |                           비고                            |
| :-----------: | :-------------------------------------------------------: |
|    **GET**    |  지정 리소스의 표시를 요청하며, 오직 데이터를 받기만 함   |
|   **POST**    |              클라이언트 데이터를 서버로 보냄              |
| **PUT**/PATCH | 서버로 보낸 데이터를 저장/지정 리소스의 부분만을 **수정** |
|  **DELETE**   |                    지정 리소스를 삭제                     |

- `PUT`은 리소스의 전부, `PATCH`는 일부를 수정한다.
- 이것들은 각각 CRUD에 대응된다고 볼 수 있다.



#### 구성요소 3 : Representations (`JSON`)

**JSON**

`{"Key" : "Value"}`

> JavaScript Object Notation, 즉 JavaScript 객체 표기법으로 파이썬의 딕셔너리의 형태를 보인다. 가벼운 데이터 교환 형식으로 언어 독립적이다.



## :star:Django REST Framework :star:

### Serialization

> **직렬화**는 데이터 구조나 오브젝트 상태를 동일하거나 다른 컴퓨터 환경에 저장하고 나중에 재구성할 수 있는 포맷으로 변환하는 과정이다.

- 앞으로는 http 대신 JSON으로 페이지를 출력한다.

|          |  Django   |       DRF       |
| :------: | :-------: | :-------------: |
| Response |   HTML    |      JSON       |
|  Model   | ModelForm | ModelSerializer |



#### <참고> `django-seed`

> faker와 같이 랜덤한 dummy 데이터를 만들어준다. [Github문서](https://github.com/Brobin/django-seed)

- 아래의 명령어를 통해 15개의 랜덤한 데이터를 생성할 수 있다.

```bash
$ python manage.py seed <api> --number=15
```

- 예시

```bash
$ python manage.py seed articles --number=20
```



### JSON Response 1 : 임시적인 방법

- Article의 모든 객체를 불러와 딕셔너리 형태로 저장한 후, `JsonResponse`를 통해 응답한다.

```python
# articles/views.py

from django.http.response import JsonResponse

def article_list_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append({
            'id': article.id,
            'title': article.title,
            'content': article.content,
            'created_at': article.created_at,
            'updated_at': article.updated_at,
        })
    return JsonResponse(articles_json, safe=False)
```

- :heavy_check_mark:`JsonResponse`에 `safe=False`라는 옵션을 반드시 넣어줘야한다! 
- 기본적인 JSON 형태를 나타내고 있지만, 정상적인 방법이라고는 할 수 없다. 따라서 임시적인 방법으로만 사용한다.



### JSON Response 2 : ModelForm을 안 쓸 때

**기본 틀**

```python
from django.core import serializers
data = serializers.serialize("xml", SomeModel.objects.all())
```

- 위의 코드를 실제로 작성해보면 다음과 같다.

```python
# articles/urls.py
path('json_2/', views.article_list_json_2),

# articles/views.py

from django.core import serializers
from django.http import HttpResponse

def article_list_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize("json", articles)
    return HttpResponse(data, content_type='application/json')
```

- :heavy_check_mark: `content_type`은 문자열이며 **`MIME type`**을 확인해서 사용한다.
- article의 모든 필드를 가져오기 되며, 이때문에 customize가 쉽지 않다.



### JSON Response 3 : DRF :ballot_box_with_check:

> Django REST Framework를 통해 ModelForm을 활용해서 쉽게 customize를 할 수 있다. [공식문서](https://www.django-rest-framework.org/)

#### <참고> `djangorestframework`

**pip 설치**

```bash
$ pip install djangorestframework
```

**앱 등록**

```python
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

**앱 폴더에 `serializers.py`라는 파일 생성**

**Serializer 생성**

```python
# articles/serializers.py

from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at', 'updated_at',]
        # fields = '__all__'
```

- Model을 상속 받는 ModelForm을 작성하는 방식과 동일하다.

**url 및 view 함수 생성**

- :heavy_check_mark:drf에서는 **`@api_view()`**가 없으면 동작하지 않는다. :star::star:
- api_view()에는 리스트 형태로 응답할 HTTP method를 입력하며, default 값은 'GET'이다.

```python
# articles/urls.py

path('json_3/', views.article_list_json_3),

# articles/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer

@api_view(['GET'])
def article_list_json_3(request):
    article = Article.objects.get(pk=1)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
```

- 객체 전체를 불러올 때는 view함수를 다음과 같이 작성한다.

```python
# articles/views.py - 객체 전체 불러오기

@api_view(['GET'])
def article_list_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```

- 위와 같이 articles 가 전체 QuerySet을 가져올 경우, **`many=True`** 옵션을 반드시 넣어줘야 한다. :star::star:



## <실습> Model Serializer CRUD

**Model Serializer 만들기**

```python
# articles/serializers.py

from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title',)
```

**seed 데이터 만들기**

```bash
$ python manage.py seed articles --number=20
```

- seed 명령어는 해당 app의 각각의 모델에 dummy 데이터를 만들어준다.



### READ

**프로젝트 폴더 url**

```python
# api/urls.py

urlpatterns = [
    # ...
    path('api/v1/articles/', include('articles.urls')),
]
```

- `api/version1/app_name/`으로 작성한다. api에서는 이러한 url을 사용하여 버전을 관리한다.

**List 페이지 url 및 view 함수 작성** : serializing 하기

```python
# articles/urls.py
urlpatterns = [
    path('', views.article_list),
]
# articles/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer

# 그냥 괄호만 넣으면 default는 GET요청만 받는다.
@api_view(['GET'])
def article_list(request):
    # 1. 모델에서 데이터를 가져온다.
    articles = Article.objects.all()
    
    # 2. 모델에서 가져온 데이터를 Serializing한다.
    serializer = ArticleSerializer(articles, many=True)

    # 3. 응답해준다.
    return Response(serializer.data)
```

- `Response()`는 다음과 같은 인자를 받는데, `data`는 필수인자이다.

```python
Response(data, status=None, template_name=None, headers=None, content_type=None)
```



**detail 페이지 만들기**

- detail 페이지에서는 모든 데이터를 표시해야하므로, 필드를 추가한 모델을 새로 선언한다.

```python
# articles/serializers.py

class ArticleDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title','content','created_at','updated_at')
```

```python
# articles/urls.py
path('<int:article_pk>/', views.article_detail),

# articles/views.py
from django.shortcuts import get_object_or_404
from .serializers import ArticleDetailSerializer

@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleDetailSerializer(article)
    return Response(serializer.data)
```



### CREATE

**url 및 view함수 생성**

```python
# articles/urls.py
path('create/', views.create_article),

# articles/views.py
from rest_framework import status

@api_view(['POST'])
def create_article(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```



### DELETE

**url 및 view 함수 생성**

```python
# articles/urls.py
path('<int:article_pk>/delete/', views.delete_article),

# aritcles/views.py

@api_view(['DELETE'])
def delete_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return Response({'id' : article_pk}, status=status.HTTP_204_NO_CONTENT)
```



### UPDATE

**url 및 view 함수 생성**

```python
# articles/urls.py
path('<int:article_pk>/update/', views.update_article),

# aritcles/views.py
@api_view(['PUT'])
def update_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```



### RESTful API

> API를 더욱 RESTful하게 만들기 위해서 아래의 기존 로직들을 통합한다.

**list & create**

```python
# articles/urls.py

path('', views.article_list_create),

# articles/views.py
from rest_framework import status

@api_view(['GET', 'POST'])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    else:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

**detail, update, delete**

```python
# articles/urls.py

path('<int:article_pk>/', views.article_detail_update_delete),

# articles/views.py
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(instance = article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        article.delete()
        return Response({'id' : article_pk}, status=status.HTTP_204_NO_CONTENT)
```

- PUT 로직에서 serializer 작성시 반드시 `ArticleSerializer(instance = article, data=request.data)`를 입력한다. `instance=article`을 넣기 않고 그냥 article을 넣으면 create와 같이새로운 인스턴스가 생성되기 때문이다.



#### <참고> `Postman`

> `Postman`은 API 개발을 위한 협업 플랫폼이다. create 버튼이 없는 상황에서 해당 로직이 제대로 동작하는지를 테스트할 수 있는 툴이다.

- request에서 body> `x-www-form-unlencoded` 지정 후 HTTP Method에 대한 응답을 테스트할 수 있다.
- 단, 서버가 실행되고 있어야 동작한다.



#### <참고> HTTP Status Code

- 200 : OK. 요청이 **성공**적으로 되었습니다. 성공의 의미는 HTTP 메서드에 따라 달라집니다.
- 400 : 이 응답은 **잘못된 문법**으로 인하여 서버가 요청을 이해할 수 없음을 의미합니다.
- 401 : 이 응답은 "**비인증**(unauthenticated)"을 의미합니다.
- 403 : 클라이언트는 콘텐츠에 **접근할 권리**를 가지고 있지 않습니다.
  - ex) POST 요청에서 csrf token을 빼먹었을 때
- 404 : 서버는 요청받은 리소스를 **찾을 수 없습**니다.
- 500 : 서버가 처리 방법을 모르는 상황이 발생했습니다.



### 참조모델 작성하기 : Comment

**모델 생성**

```python
# articles/models.py
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**Serializer 생성** : 참조 serializer

```python
# articles/serializers.py

from .models import Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'article',)
        read_only_fields = ('article',)
```

- :white_check_mark:`read_only_field`를 추가해주어야 한다!!

**url 및 view 함수 생성**

```python
# articles/urls.py
path('<int:article_pk>/comments/', views.create_comment),

# articles/views.py
from .serializers import CommentSerializer

@api_view(['POST'])
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

- article의 값이 null이 되면 안되므로 `serializer.save(article=article)`로 저장할 때 article의 값을 지정해주어야 한다!!

**역참조하는 serializer**

- serializer의 모델이 역참조하는 경우 다음과 같이 작성할 수 있다.

```python
# music/serializers.py

# 상세 가수 정보 생성/반환
class ArtistSerializer(serializers.ModelSerializer):
    music_set = MusicListSerializer(
        many=True,
        # 직접작성하는 부분이 아니기 때문에 read_only옵션 넣기
        read_only=True
    )
    music_count = serializers.IntegerField(
        source='music_set.count',
        read_only=True
    )

    class Meta:
        model = Artist
        # 사용자에게 보여주기 위한 필드
        fields = ('id', 'name', 'music_set', 'music_count',)
```





## <참고> DRF 문서화 : `drf-yasg`

> DRF를 정의한 API를 문서화할 수 있는 패키지.
>
> drf-yasg를 단순히 적용만 해도 정의한 모델, API 목록을 볼 수 있는 문서를 생성할 수 있으며, 필요에 따라 개발자가 내용을 추가하거나 수정할 수 있다. [drf-yasg Github](https://github.com/axnsan12/drf-yasg)

**`djangorestframework` 다운그레이드**

- `drf-yasg`는 현재의 `djangorestframework` 3.12버전을 지원하지 않으므로, 3.11 버전으로 다운그레이드를 진행한다.

```bash
$ pip uninstall djangorestframework
$ pip install djangorestframework==3.11
```

- 이외, 현재의 과정을 진행하기 위해서 `django`, `django-seed`, `django-extensions`가 필요하다.

**pip설치**

```bash
$ pip install -U drf-yasg
```

**pip 앱 등록**

```python
# settings.py

INSTALLED_APPS = [
    'drf_yasg',
]
```

**url 생성**

- :white_check_mark:`redocs`, `swagger`에서 문서화된 DRF를 확인할 수 있다!

```python
# music/urls.py

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,
))
    
urlpatterns = [
    path('redocs/', schema_view.with_ui('redoc'), name='api_docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger'),
]
```



***Copyright* © Song_Artish**