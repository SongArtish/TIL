# HTTP 메시지

---

[TOC]

---



## Overview

**HTTP 메시지**는 클라이언트와 서버 사이에서 데이터가 교환되는 방식이며, **요청(requests)**과 **응답(response)**이라는 2가지 유형이 있다. HTTP 메시지는 몇 줄의 텍스트 정보로 구성되며, 이러한 정보는 구성 파일, API, 기타 인터페이스에서 자동으로 완성한다. 아래는 HTTP 메시지의 예시이다.

![HTTP_messages](img/HTTP_messages.png)

`(출처: MDN)`

요청과 응답은 다음과 같은 유사한 구조를 가진다.

1. **start line**: start line에는 요청이나 응답의 상태를 나타낸다. 항상 첫 번째 줄에 위치하며, 응답에서는 status line이라고 부른다.
2. **HTTP headers**: 요청을 지정하거나, 메시지에 포함된 본문을 설명하는 헤더의 집합이다.
3. **empty line**: 헤더와 본문을 구분하는 빈 줄
4. **body**: 요청과 관련된 데이터나 응답과 관련된 데이터 또는 문서를 포함한다. 요청과 응답의 유형에 따라 선택적으로 사용한다.



## Request

HTTP 요청은 클라이언트가 서버에 보내는 메시지이다.

### Start line

Start line에는 3가지 요소가 있다.

1. 수행할 작업(GET, PUT ,POST 등)이나 방식(HEAD or OPTIONS)을 설명하는 **HTTP method**를 나타낸다.

2. 요청 대상(일반적으로 URL 혹은 URI) 또는 프로토콜, 포트, 도메인의 절대 경로는 **요청 컨텍스트**에 작성된다. 이 요청 형식은 HTTP method마다 다르다.

   - origin 형식: `?`와 쿼리 문자열이 붙는 절대 경로이다. POST, GET, HEAD, OPTIONS 등의 method와 함께 사용한다.

     ```
     POST / HTTP 1.1
     GET /background.png HTTP/1.0
     HEAD /test.html?query=alibaba HTTP/1.1
     OPTIONS /anypage.html HTTP/1.0
     ```

   - absolute 형식: 완전한 URL 형식으로, 프록시에 연결하는 경우 대부분 GET method와 함께 사용한다.

     ```
     GET http://developer.mozilla.org/en-US/docs/Web/HTTP/Messages HTTP/1.1
     ```

   - authority 형식: 도메인 이름과 포트 번호로 이루어진 URL의 authority component이다. HTTP 터널을 구축하는 경우, `CONNECT`와 함께 사용할 수 있다

     ```
     CONNECT developer.mozilla.org:80 HTTP/1.1
     ```

   - asterisk 형식: `OPTIONS`와 함꼐 별표(`*`) 하나로 서버 전체를 표현한다.

     ```
     OPTIONS * HTTP/1.1
     ```

3. **HTTP 버전**은 메시지의 다른 구조를 결정한다. 이를 위해 HTTP 버전을 함께 입력한다.

### Headers

요청의 Headers는 기본 구조를 따른다. 대소문자 구분 없는 문자열과 콜론(`:`) 값을 입력한다. 값은 헤더에 따라 다르다. 여러 종류의 헤더가 있고, 다음과 같이 그룹을 나눌 수 있다.

- General headers: 메시지 전체에 적용된다.
- Request headers: User-Agent, Accept-Type, Accept-Language와 같은 헤더는 요청을 보다 구체화한다. Referer처럼 컨텍스트를 제공하거나 If-None과 같이 조건에 따라 제약을 추가할 수 있다.
- Entity headers: Content-Length와 같은 헤더는 body에 적용된다. body가 비어있는 경우, entity headers는 전송되지 않는다.

![Request_headers](img/Request_headers.png)

`(출처: MDN)`

### Body

요청의 본문은 HTTP 메시지 구조의 마지막에 위치한다. 모든 요청에 body가 필요하지는 않다. GET, HEAD, DELETE, OPTIONS처럼 서버에 리소스를 요청하는 경우에는 본문이 필요하지 않다. POST나 PUT과 같은 일부 요청은 데이터를 업데이트하기 위해 사용한다. body는 다음과 같이 두 종류로 구분된다.

- Single-resource bodies(단일-리소스 본문): 헤더 2개(Content-Type과 Content-Length)로 정의된 단일 파일로 구성된다.
- Multiple-resource bodies(다중-리소스 본문): 여러 파트로 구성된 본문에서는 각 파트마다 다른 정보를 지닌다. 보통 HTML form과 관련이 있다.



## Response

### Status line

응답의 첫 줄은 Status lien이라고 부르며, 다음과 같은 정보를 포함한다.

1. 현재 프로토콜의 버전(HTTP/1.1)
2. 상태 코드: 요청의 결과를 나타낸다. (200, 302, 404 등)
3. 상태 텍스트: 상태 코드에 대한 설명

예를 들면 `HTTP/1.1 404 Not Found.`와 같이 표시된다.

### Headers

응답에 들어가는 HTTP headers는 요청 헤더와 동일한 구조를 가지고 있다. 대소문자 구분 없는 문자열과 콜론(`:`) 값을 입력한다. 값은 헤더에 따라 다르다. 요청의 헤더와 마찬가지로 몇 그룹으로 나눌 수 있다.

- General headers: 메시지 전체에 적용된다.
- Response headers: Vary, Accept-Rangers와 같이 상태 줄에 넣기에는 공간이 부족했던 추가 정보를 제공한다.
- Entity headers: Content-Length와 같은 헤더는 body에 적용된다. body가 비어있는 경우, entity headers는 전송되지 않는다.

![Response_headers](img/Response_headers.png)

`(출처: MDN)`

### Body

요청의 본문은 HTTP 메시지 구조의 마지막에 위치한다. 모든 요청에 body가 필요하지는 않다. 201, 204와 같은 상태 코드를 가지는 응답에는 본문이 필요하지 않다. 응답의 body는 다음과 같이 두 종류로 구분된다.

- Single-resource bodies(단일-리소스 본문):
  - 길이가 알려진 단일-리소스 본문은 2개의 헤더(Content-Type과 Content-Length)로 정의한다.
  - 길이를 모르는 단일 파일로 구성된 단일-리소스 본문은 Transfer-Encoding이 `chunked`로 설정되어 있으며, 파일은 chunk로 나뉘어 인코딩되어 있다.
- Multiple-resource bodies(다중-리소스 본문): 서로 다른 정보를 담고 있는 body이다.



***Copyright* © 2022 Song_Artish**

