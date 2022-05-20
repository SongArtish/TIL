# HTTP Intro

---

[TOC]

---



## Overview

HTTP는 HyperText Transfer Protocol의 줄임말로, HTML과 같은 문서를 전송하기 위한 [Application Layer](https://ko.wikipedia.org/wiki/%EC%9D%91%EC%9A%A9_%EA%B3%84%EC%B8%B5) 프로토콜이다. 웹 브라우저와 웹 서버의 소통을 위해 디자인되었다.



## 특징

### Stateless

Stateless(무상태성)는 말 그대로 상태를 가지지 않는다는 뜻이다. HTTP는 통신 규약일 뿐, HTTP로 클라이언트와 서버가 통신을 주고 받는 과정에서, 클라이언트나 서버의 상태를 추적하거나 저장하지 않는다. 즉, **HTTP는 특정 상태를 담고 있지 않으며, 이전 요청이나 다음 요청을 기억하지 않는다.**  따라서, 필요에 따라 다른 방법(쿠기-세션, API 등)을 통해 상태를 확인해야 한다.



***Copyright* © 2022 Song_Artish**

