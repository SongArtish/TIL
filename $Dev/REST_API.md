# Rest API

> Representational State Transfer

---

[TOC]

---



## Rule

> API를 위한 URL을 만들 때

### 1. URL에 동사를 사용하지 않는다.

- `/getMovieList`, `/findMovie/getInception` 등과 같이 URL에 동사를 사용하지 않는다.
- `/movieList`, /`movie/inception`과 같이 명사만 남긴다.

### 2. HTTP Method를 사용한다.

- GET, POST, PUT, DELETE의 HTTP Method를 사용한다.
- 그러면 `/movieList`라는 하나의 URL로도 4개의 요청을 모두 할 수 있다.

### 3. Query Parameters를 사용한다.

- 검색 등을 할 경우, query parameter를 사용하면 매번 새로운 URL을 만들지 않아도 된다.
- `/movies?release_date=2021`와 같이 사용할 수 있다.
- `/movies?page=5`와 같이 pagination으로도 사용할 수 있다.



***Copyright* © 2021 Song_Artish**