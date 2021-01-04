# Web Crawler

> Notes of Python Web Crawler

---

[TOC]

---



## 개요

- 크롤러는 크롤링 소프트웨어를 말한다.
- Python 웹 크롤러로는 `Selenium`, `BeautifulSoup`, `Scrapy` 등이 있다.

|                   도구                    |     속도     | 리소스 | 문서화 | 커뮤니티 | 기능 | 난이도 |
| :---------------------------------------: | :----------: | :----: | :----: | :------: | :--: | :----: |
| **[BeautifulSoup](###1.1 BeautifulSoup)** | 빠름(조건부) | 가벼움 |  보통  |   보통   | 적음 |  쉬움  |
|      **[Selenium](###1.2 Selenium)**      |     느림     | 무거움 |  좋음  |   좋음   | 보통 |  쉬움  |
|        **[Scrapy](###1.3 Scrapy)**        |     빠름     | 가벼움 |  좋음  |   좋음   | 많음 |  보통  |



## BeautifulSoup

> [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)는 HTML, XML 파일의 정보를 추출해내는 python 라이브러리이다.
>
> -  python 내장 모듈인 `requests` 혹은 `urllib`을 이용해 HTML를 다운로드 받고, `BeautifulSoup`로 데이터를 추출하는 방식이다.

|          | 장/단점                                                      |
| -------- | ------------------------------------------------------------ |
| **장점** | 쉬움, 심플함, 빠름 (멀티프로세스, 멀티 스레드 적용시 해당)   |
| **단점** | javascript 렌더링이 필요한 사이트들을 크롤링하기 어려움. 병렬처리 로직을 별도로 작성하지 않으면 느린편 |

- *`BeatifulSoup`을 활용한 웹 크롤링 기초는 [블로그](http://hleecaster.com/python-web-crawling-with-beautifulsoup/)를 참조하였다.*

### 1) 웹 요청보내기: `requests` 라이브러리

> 파이썬에서는 `requests`라는 라이브러리를 활용하여 편리하게 웹 페이지에 요청을 보낼 수 있다.
>
> - 만약 `requests` 라이브러리가 설치되어 있지 않다면 pip를 통해 설치한다.

아래의 코드는 네이버 홈 화면의 `HTML 문서 전체`를 긁어서 출력해준다.

```python
import requests

webpage = requests.get("http://www.naver.com/")
print(webpage.text)
```



### 2) 파싱하기: `BeautifulSoup` 라이브러리

> [BeautifulSoup 라이브러리](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)는 HTML 문서를 탐색해서 원하는 부분만 쉽게 가져올 수 있도록 한다.
>
> ```python
> soup = BeautifulSoup(html_doc, 'html.parser')
> ```

아래의 코드는 네이버 홈 화면을 `BeautifulSoup`를 활용해 가져온다.

```python
import requests
from bs4 import BeautifulSoup

webpage = requests.get("http://www.naver.com/")
soup = BeautifulSoup(webpage.content, "html.parser")	# 1

print(soup)
```

- `#1`에서 `BeautifulSoup`의 첫 번째 인자로는 webpage의 content라는 html 문서를 넣어준다.

- `#1`에서 `BeautifulSoup`의 두 번째 인자로는 사용할 parser를 넣어주는데, 여기서는 `html.parser`를 사용한다.

  | Parser                 | 선언방법                                                     | 장점                                                         | 단점                                   |
  | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------------- |
  | **파이썬 html.parser** | `BeautifulSoup(html_doc, 'html.parser')`                     | 설치 필요X<br />적당한 속도                                  |                                        |
  | **lxml HTML parser**   | `BeautifulSoup(html_doc, 'lxml')`                            | 매우 빠름                                                    | lxml 추가 설치 필요                    |
  | **lxml XML parser**    | `BeautifulSoup(html_doc, 'lxml-xml')`<br />`BeautifulSoup(html_doc, 'xml')` | 매우 빠름<br />유일하게 지원되는 xml parser                  | lxml 추가 설치 필요                    |
  | **html5lib**           | `BeautifulSoup(html_doc, 'html5lib')`                        | 웹 브라우저와 같은 방식으로 페이지를 파싱<br />유효한 HTML5 생성 | html5lib 추가 설치 필요<br />매우 느림 |

  - `lxml` 모듈을 사용하기 위해서는 다음과 같이 pip로 설치할 수 있다.

    ```bash
    $ pip install lxml
    ```

  - :heavy_exclamation_mark: 실제로 `lxml` parser를 사용하려고 하면 PyCharm 다음과 같은 오류가 발생한다.

    ```
    bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: xml. Do you need to install a parser library?
    ```

    - 해결방안: PyCharm에서는 오류가 발생하지만, VSCode로 실행하면 정상적으로 작동한다.



### 3) 태그(Tag) 탐색하기

**특정 태그 탐색**

> 아래의 방법은 특정 태그의 최상위 하나만을 반환한다.

- 위에서 파싱한 데이터에서 `<p>` 태그만 가져올 경우, 아래와 같이 코드를 작성할 수 있다.

  ```python
  print(soup.p)
  ```

- 다른 태그들도 위와 같은 방법으로 가져올 수 있다.

**태그 내용 탐색**

- 만약 태그 속성들은 빼고 그 안에 있는 텍스트만 가져오는 경우, 아래와 같이 코드를 작성할 수 있다.

  ```python
  print(soup.p.string)
  ```

**태그 트리구조 탐색**

- 태그는 보통 트리구조로 위계가 있기 때문에 하위 항목을 모두 탐색하고 싶다면, `.children`을 사용할 수 있다.

  ```python
  for child in soup.ul.children:
      print(child)
  ```

- 반대로, 지정된 태그의 상위 항목을 가져올 경우 `.parents`를 사용한다.

  ```python
  for parent in soup.ul.parents:
      print(parent)
  ```



### 4) 웹사이트 구조 분석하기: 개발자 도구

- 거의 모든 웹 브라우저에서 개발자 도구를 사용할 수 있으며, 개발자 도구를 통해서  편리하게 HTML 문서 구조를 확인할 수 있다.
- Google Chrome의 경우 `F12`키를 누르면 개발자 도구를 사용할 수 있다.



### 5) 원하는 부분 가져오기 1: `find_all`

> `.find_all()`을 사용하여 원하는 태그를 모두 가져올 수 있다.
>
> - *`.find_all()`은 **[정규식](#####(1) 정규식 활용하기), [html 속성](#####(3) html 속성 활용하기), [함수](#####(4) 함수 활용하기)** 등을 사용해서 편리하게 원하는 부분을 추출할 수 있다.*

- 아래의 코드는 html 문서의 모든 `<h2>` 태그를 가져온다.

```python
print(soup.find_all("h2"))
```

- 아래와 같이 결과 값이 리스트 형태로 출력된다.

  ```
  [<h2 class="blind">뉴스스탠드</h2>, <h2 class="blind">주제별 캐스트</h2>, <h2 class="blind">Sign in</h2>, <h2 class="blind"> 
  타임스퀘어</h2>]
  ```

  - 결과 값의 type을 출력해 보면 `<class 'bs4.element.ResultSet'>`라고 나온다.

  ```python
  print(type(soup.find_all("h2")))
  ```

  ```
  <class 'bs4.element.ResultSet'>
  ```

#### (1) 정규식 활용하기

- `<ol>` 및 `<ul>`이 포함된 리스트를 가져오는 경우 아래와 같이 코드를 작성한다.

  ```python
  import re
  soup.find_all(re.compile("[ou]l"))
  ```

- `<h1>` ~ `<h9>`까지의 모든 헤딩 태그를 가져오는 경우 아래와 같이 코드를 작성한다.

  ```python
  import re
  soup.find_all(re.compile("h[1-9]"))
  ```

  - :heavy_exclamation_mark: 어째서인지 VSCode로 네이버 홈 페이지를 가져오는 경우 잘 작동하지 않는다.
    - 해결방안: 앞에 `print()`를 붙여주면 해결된다!!

#### (2) 리스트 활용하기

- 리스트로 원하는 태그들을 지정해서 가져올 수도 있다.

- 예를 들어, `<h1>`과 `<p>` 태그만을 가져오는 경우

  ```python
  soup.find_all(['h1', 'p'])
  ```

#### (3) html 속성 활용하기

- html 속성을 지정해서 가져올 수도 있다.

- 이 때 `.find_all()`에서 **`attrs`**라는 parameter를 <u>딕셔너리 형태</u> 지정한다.

  ```python
  print(soup.find_all(attrs={'class':'column_left'}))
  ```

- 아래와 같이 여러개의 속성을 한 번에 지정하는 것도 가능하다.

  ```python
  soup.find_all(attrs={'class':'footer-list', 'id':'footer-address-list'})
  ```

#### (4) 함수 활용하기

- 원하는 부분을 지정하기가 어려운 경우, 함수를 활용해서 가져올 수 있다.

  ```python
  # 예시
  def search_function(tag):
      return tag.attr('class') == "card-title" and tag.string == "Hello World"
  
  soup.find_all(search_function)
  ```



### 6) 원하는 부분 가져오기 2: `select()`

> `select()`라는 메서드를 통해 CSS 선택자를 활용하여 원하는 부분을 가져올 수도 있다.

**class 앞에는 `.`(점)을 찍어준다.**

- 예를 들어 card-region-name이라는 클래스를 가진 요소들만 가져오고 싶은 경우 아래와 같이 코드를 작성한다.

  ```python
  soup.select(".card-region-name")
  ```

**id 앞에는 `#`(샵)을 찍어준다.**

- 예를 들어 hot-articles-go-download라는 id를 가진 요소들만 가죠오고 싶은 경우 아래와 같이 코드를 작성한다.

  ```python
  soup.select("#hot-articles-go-download")
  ```

  

### 7) 텍스트만 읽어오기: `get_text()`

> 태그의 텍스트 부분만 가져오는 경우 `.get_text()`라는 메서드를 사용한다.

```python
# 예시
for x in range(0,10):
    print(soup.select(".card-title")[x].get_text())
```



## Selenium

> [Selenium](https://selenium-python.readthedocs.io/)은 웹 자동화 테스트 (버튼 클릭, 스크롤 조작 등등)에 사용되는 프레임워크이다.
>
> - `Selenium`을 이용한 크롤러는 웹 페이지에서 javascript 렌더링을 통해 생성되는 데이터들을 손쉽게 가져올 수 있다.
> - :white_check_mark: `Selenium` 사용을 때에는 [Docker](https://github.com/SeleniumHQ/docker-selenium)를 사용하면 편리하다. 특히 headless 모드로 크롤링할 때 리소스 정리가 매우 쉽다.

|          | 장/단점                                                      |
| -------- | ------------------------------------------------------------ |
| **장점** | 사용자가 보는 웹 페이지의 모든 정보를 가져올 수 있음, javascript rendering 기능 지원, 사용방법이 직관적이고 쉬움 |
| **단점** | 느림, 메모리를 많이 차지                                     |



## Scrapy

> [Scrapy](https://github.com/scrapy/scrapy)는 크롤링을 위해 개발된 유료 프레임워크이다.

- 미들웨어, 파이프라인, javascript renderer(splash), proxy, xpath, CLI 등 다양한 기능들과 플러그인들을 사용할 수 있다.
- 병렬처리, robots.txt 준수 여부, 다운로드 속도 제어등도 설정할 수 있다.
- Django 와 같은 백엔드 서비스와 연동하기도 좋고, 플러그인도 다양해서 여러모로 만능인 프레임워크이다. [참고 사이트](https://blog.theodo.com/2019/01/data-scraping-scrapy-django-integration/)

|          | 장/단점                                                      |
| -------- | ------------------------------------------------------------ |
| **장점** | 다양한 플러그인 보유, 훌륭한 커뮤니티와 문서화, 크롤링에 필요한 다양한 기능 |
| **단점** | 플러그인들끼리 서로 호환이 안되는 경우가 있을 수 있음        |





https://aonee.tistory.com/40 참고하기

***Copyright* © 2020 Song_Artish**