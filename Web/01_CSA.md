# Client Server Architecture

---

[TOC]

---



## Overview

클라이언트와 서버 간의 통신은 **요청**과 **응답**으로 구성된다.

![client&server](img/client&server.png)

`(출처: github pages)`



## Protocol

통신 간에는 메시지를 주고 받는 양식과 규칙의 체계가 존재하는데, 이를 **protocol(통신 규약)**이라고 한다. **웹에서는 HTTP라는 프로토콜**을 사용하며, HTTP를 이용해 주고받는 메시지는 `HTTP 메시지`라고 부른다.



## API

API는 Application Programming Interface의 약자로, 클라이언트가 리소스를 잘 활용할 수 있도록 서버에서 제공하는 인터페이스이다. 보통 인터넷에 있는 데이터를 요청할 때는 HTTP라는 프로토콜을 사용해서 **주소(URL, URI)를 통해 접근**할 수 있게 된다.



## SSR vs CSR

### Rendering

컴퓨터 프로그램을 사용하여 모델 또는 이들을 모아놓은 장면인 scene file로부터 영상을 만들어내는 과정

### SSR: Server Side Rendering

PHP, JSP, ASP, Node.js 등 Server-Side Script 언어 기반의 템플릿 엔진을 이용해 동적인 웹 콘텐츠(html) 문서를 만드는 방식이다. **웹 페이지를 브라우저에서 렌더링하는 대신에 서버에서 렌더링**한다. 브라우저가 서버의 URI로 `GET` 요청을 하면, 서버는 웹 페이지를 완전히 렌더링하고 파일을 브라우저로 전송한다.

- SEO(Search Engine Optimization)가 우선인 경우, 일반적으로 SSR을 사용한다.
- 웹 페이지의 첫 화면 렌더링이 빠르게 필요한 경우에도, 단일 파일의 용량이 작은 SSR이 적합하다.

### CSR: Client Side Rendering

Client(Web Browser) 에 내장된 JavaScript 엔진이 동적으로 html element 를 생성한 뒤, root element 에 추가하여 웹 콘텐츠를 만드는 방식이다. 일반적으로 CRS은 SSR의 반대로 여겨지는데, CSR은 **클라이언트에서 페이지를 렌더링**한다.브라우저가 서버로 요청을 보내면, 서버는 웹 페이지의 골격이 될 단일 페이지와 JavaScript 파일을 전송하고, 클라이언트는 이것을 받아서 페이지를 렌더링한다. 페이지에서 DB에 저장된 데이터가 필요한 경우에는 API를 통해 요청한다.

- 사이트에 풍부한 상호작용이 있는 경우, CSR은 빠른 라우팅, 동적 렌더링 등으로 강력한 사용자 경험을 제공한다.



***Copyright* © 2022 Song_Artish**