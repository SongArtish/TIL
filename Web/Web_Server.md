# Web Server

---

[TOC]

---



## Overview

서버에 접속한 사용자에게 웹 서비스를 제공하기 위해 사용되는 서버의 한 종류이다. HTTP 요청을 받고 HTML, CSS, JavaScript, Image 등의 **정적인 정보**를 반환하는 역할을 한다. 대표적인 웹서버는 `IIS`, `Apache`, `Nginx`, `GWS` 등이 있다.

```markdown
서비 종류
1. FTP 서버
2. 웹 서버
3. 데이터베이스 서버
4. 기타
```



## <참고> WAS

> Web Application Server

**앱서버**는 웹서버와 앱 사이의 동적인 정보를 생성하는 역할을 담당하는 **미들웨어**다. 웹서버와 앱은 서로 간 알지 못하기 때문에, 앱서버가 가운데에서 중간다리 역할을 한다. 대표적인 앱서버로는 `Tomcat`, `uWsgi`, `WebLogic`, `Jboss` 등이 있다. 예를 들어, `uWsgi`는 HTTP 요청을 python으로, 반대로 python 응답을 웹서버로 전달해준다.



***Copyright* © 2022 Song_Artish**