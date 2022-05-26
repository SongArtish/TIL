# HTTP 요청

---

[TOC]

---



## Preflight Request

교자 출처 리소스 공유(CORS) Preflight Request(사전 요청)는 **본격적인 교차 출처 HTTP 요청 전에 서버 측에서 그 요청의 메서드와 헤더에 대해 인식하고 있는지를 체크**하는 것이다.

- "Access-Control-Request-Method"
- "Access-Control-Request-Headers"
- "Origin"

위의 총 3가지 HTTP Request Header를 사용하는 HTTP Method(`OPTIONS`)이다. 즉, 본 요청을 보내기 전에 먼저 본 요청에 대한 권한을 확인하는 작업을 통해, 본 요청이 유효한지 체크할 수 있다.

**Access-Control-Max-Age** 헤더를 이용하면, 사전 요청 결과가 얼마 동안 캐시될 지를 나타낼 수 있다. 아래는 10분 동안 사전 요청 결과를 캐시하는 예시이다.

```javascript
Access-Control-Max-Age: 600
```



## Simple Request

반대로, 위와 같은 **CORS Preflight가 트리거 되지 않는 일부 요청이** 있는데, 이를 Simple Request(단 순 요청)라고 한다.단순 요청에 충족되는 요청 조건은 아래와 같다.

1. 다음 중 하나의 Method
   - GET
   - HEAD
   - POST
2. User Agent가 자동으로 설정한 Header외에, 수동으로 설정할 수 있는 헤더는 오직 Fetch 명세에서 "CORS-safelisted request-header"로 정의한 Header 뿐.
   - Accept
   - Accept-Language
   - Content-Language
   - Content-Type (아래 추가 요구 사항에 유의)
   - DPR
   - Downlink
   - Save-Data
   - Viewport-Width
   - Width
3. Content-Type 헤더는 다음의 값들만 허용
   - application/x-www-form-urlencoded
   - multipart/form-data
   - text/plain



***Copyright* © 2022 Song_Artish**