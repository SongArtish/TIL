# DB Relationship (1 : N)

2020.09.21

> **Relationship Fields**는 모델 간 관계를 나타내는 필드이다.

|    관계    |        필드         |
| :--------: | :-----------------: |
| 1 : N 관계 |   `ForeignKey()`    |
| M : N 관계 | `ManyToManyField()` |
| 1 : 1 관계 |  `OneToOneField()`  |



*****

[TOC]

*****



## 1 : N 관계

### `Foreign Key`

> **외래 키**는 참조하는 테이블에서 1개의 키에 해당하고 참조하는 측의 관계 변수는 참조되는 측의 테이블의 키를 가리킨다.
>
> - 참조하는 테이블과 참조되는 테이블이 동일할 수도 있다. (**재귀적 외래 키**)
> - 댓글 등에 사용된다 !



## 1 : N 관계 in Django

`ForeignKey()`

> Django의 `ForeignKey()`필드에는 2개의 위치 인자가 필요하다. [Django Model Field](https://docs.djangoproject.com/en/3.1/ref/models/fields/)
>
> - 참조하는 모델
> - `on_delete` 옵션
>
> ---
>
> [`on_delete`](https://docs.djangoproject.com/en/3.0/ref/models/fields/#arguments)
>
> > 참조하는 클래스가 삭제되는 경우, 해당 DB를 어떻게 처리할지에 대한 옵션
>
> - **`CASCADE`** : 부모 객체(참조된 객체)가 삭제됐을 때 이를 참조하는 객체도 삭제
> - **`PROTECT`** : 참조가 되어 있는 경우 오류 발생
> - SET_NULL : 부모 객체가 삭제 됐을 때 모든 값을 NULL로 치환. (NOT NULL 조건 시 불가능)
> - SET_DEFAULT : 모든 값이 DEFAULT 값으로 치환
> - SET() : 특정 함수 호출
> - DO_NOTHING : 아무것도 하지 않음. 다만, 데이터베이스 필드에 대한 SQL ON DELETE 제한 조건을 설정해야 한다.
> - **`RESTRICT`** (new in 3.1) : RestrictedError를 발생시켜 참조된 객체의 삭제를 방지



### 모델 만들기

- 외래 키를 생성할 때, 참조하는 모델과 `on_delete` 인자를 넣어준다.

```python
# articles/models.py

class Comment(models.Model):
    # 외래키 - 참조하는 class 이름의 소문자로 작성하는게 보통 
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
```



### <참고> `shell_plus`로 인스턴스 생성

```bash
$ python manage.py shell_plus
```

- 인스턴스를 생성한다.

```shell
In [1]: comment = Comment()

In [2]: comment.content = 'first comment'

In [3]: comment.content
Out[3]: 'first comment'
```

- 참조할 클래스 필드의 값을 입력해야 인스턴스가 저장이 된다.

```shell
In [11]: comment.article = article

In [12]: comment.save()
```

- 다음과 같은 방법으로도 저장할 수 있다.

```shell
In [16]: comment = Comment(content = 'second comment', article = article)
```



### admin 페이지에 모델 등록

```python
# articles/admin.py

admin.site.register(Comment)
```



### :star: 참조 & 역참조

**참조** : Comment가 Article을 참조하는 것

- **`article`**

**역참조** : Article이 Comment를 참조하는 것

- **`comment_set`**
- :star: Django에서는 역참조 시, `<모델>.<역참조모델>_set`을 이용한다.

```shell
In [4]: article.comment_set.all()
Out[4]: <QuerySet []>
```

- 역참조된 모델의 set은 다음과 같이 불러올 수 있다.

```shell
In [5]: comments = article.comment_set.all()
# 
In [6]: comments.first().content
# 리스트 형식으로 접근
In [7]: comments[0].content
```

- :small_red_triangle:주의!  DTL에서는 all 뒤의 괄호(`all()`)를 생략한다.



### :star: related_name

- `related_name`을 설정해서 역참조 시 이름을 지정한다.

```python
# articles/models.py

article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name = 'comment')
```

- 단, 이렇게 설정하면 defalut 값인 `_set`은 사용할 수 없다.



### ModelForm 생성

```python
# articles/forms.py

from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ['article',]
```

- 댓글 작성 때, 게시글을 편집하면 안 되므로, `article`은 제외시킨다.
- exclude의 리스트 뒤에는 항상 `,`(콤마)를 붙여준다.

```python
# articles/views.py

from .forms import ArticleForm, CommentForm

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)
```



## :star: get_object_or_404

> 조회하고자 하는 객체가 없는 경우, 기본적으로 `505 ServerError` 페이지를 표시하는데 이러한 경우 `404 NotFound` 페이지를 표시하도록 하는 Shortcut 함수이다.

- 인스턴스를 불러올 때의 코드를 `get_object_or_404(모델, pk)`로 수정해준다.

```python
# articles/views.py

from django.shortcuts import get_object_or_404

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # article = Article.objects.get(pk=pk)
    
def comments_delete(request, article_pk, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    
def update(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    
def comments_create(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
```



## <실습> 댓글 만들기

### Create

**url 생성**

```python
# articles/urls.py

path('<int:pk>/comments/', views.comments_create, name='comments_create'),
```

**view 함수 작성**

- 외래 키의 정보는 save의 :arrow_right: `commit = False` 옵션을 활용해서 저장한다.

```python
# articles/views.py

@require_POST
def comments_create(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # commit 기본값은 T이지만, F로 설정하면 바로 저장되지 않는다.
        comment = comment_form.save(commit = False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'comment_form' : comment_form,
        # detail로 다시 오기 위해 필요하다.
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)
```

**템플릿 작성**

```html
<!-- detail.html -->

<form action="{% url 'articles:comments_create' article.pk %}" method = 'POST'>
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
</form>
```



### Read

> :star: `article.comment_set.all()`을 사용하여 모든 댓글을 불러온다.

**view 함수 작성**

```python
# articles/views.py

def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    # 해당 게시글의 모든 댓글을 출력하는 것이다.
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)

```

**템플릿 작성**

```html
<!-- detail.html -->

...
  <hr>
  <h4>댓글 목록</h4>
  {% for comment in comments %}
    <li>{{ comment.content }}</li>
  {% endfor %}
  <hr>
...
```



### Update

- 댓글 update는 다른 페이지를 거치지 않고 보통 해당 페이지에서 바로 업데이트를 한다.
- 해당 부분은  JavaScript가 필요하므로 넘어간다.



### Delete

**url 작성**

- pk 값이 article과 comment 2개가 필요하므로 구분해준다.

```python
# articles/urls.py

path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
```

**view 함수 작성**

```python
# articles/views.py

from .models import Comment

@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

**삭제 버튼 만들기**

```html
<!-- detail.html -->

<h4>댓글 목록</h4>
{% for comment in comments %}
<li>
    {{ comment.content }}
    <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" class="d-inline">
    	{% csrf_token %}
        <input type="submit" value="DELETE">
    </form>
</li>
{% endfor %}
```



### 기타

**댓글 개수 출력하기**

1. filter 이용 

- Query를 덜 보내기 때문에 count에 비해 빠르다.

```django
<h4>댓글 목록</h4>
{{ comments|length }} 개
```

2. count 메서드 사용

```django
<h4>댓글 목록</h4>  
{{ comments.count }} 개
```

**댓글 존재유무에 따라 다르게 출력하기**

- `{% if %} {% endif%}`, `{% for %} {% empty %} {% endfor %} ` 구문을 활용한다.

```html
<!-- 댓글출력 예시 -->
<h4>댓글 목록</h4>
	<!-- 댓글 개수 -->
    {% if comments|length %}
      <p>{{ comments.count }} 개의 댓글이 있습니다.</p>
    {% endif %}
	
	<!-- 댓글 유무에 따라-->
    {% for comment in comments %}
      <li>
        {{ comment.content }}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" class="d-inline">
          {% csrf_token %}
          <input type="submit" value="DELETE">
        </form>
      </li>
    {% empty %}
      <p>댓글이 아직 없습니다.</p>
    {% endfor %}
```



## <참고> Lookup 필드

> [Lookup 필드](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#field-lookups)는 `__<lookpup>`의 형태로 사용된다.
>
> - `gt`(greater than, 초과), `gte`, `lt`, `lte` 및 다른 것들이 있다.

```shell
Model.objects.filter(pk__gt=4)
Model.objects.get()
```

**filter 와 get**

- filter : query_set으로 조건에 해당하는 모든 것을 가져온다.
- get : 단 하나의 값만 가져온다.



*Copyright* © Song_Artish