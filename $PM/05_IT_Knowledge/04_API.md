# API

---

[TOC]

---



## Overview

> Application Programming Interface (응용 프로그램 프로그래밍 인터페이스)

- 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 **인터페이스**를 뜻한다.
  - **인터페이스(interface)**는 컴퓨팅에서 컴퓨터 시스템끼리 **정보를 교환하는 공유 경계**이다.
- 클라이언트 프로그램과 서버 프로그램 사이에 있는 체계
- cf. UI(User Interface)



## Request

| Request | Method                |
| ------- | --------------------- |
| Create  | POST                  |
| Read    | GET                   |
| Update  | PUT(전체)/PATCH(일부) |
| Delete  | DELETE                |



## Response

| HTTP Status Code |                     | Desc.                                            |
| ---------------- | ------------------- | ------------------------------------------------ |
| 1xx              | 정보                | 요청을 받았으며 프로세스를 계속한다              |
| **2xx**          | **성공**            | 요청을 성공적으로 받았으며 인식했고 수용하였다   |
| 3xx              | 리다이렉션          | 요청 완료를 위해 추가 작업 조치가 필요하다       |
| **4xx**          | **클라이언트 오류** | 요청의 문법이 잘못되었거나 요청을 처리할 수 없다 |
| **5xx**          | **서버 오류**       | 서버가 명백히 유효한 요청에 대해 충족을 실패했다 |



## JSON

- API에서 전달하는 정보 형식 중 하나

```json
{
    key1: value1,
    key2: value2,
    key3: [value3, value4, value5]
}
```

```json
{
    "category": "beverage",
    "sort": "desc",
    "items": ["cafe mocha, cafe latte, americano"]
}
```



***Copyright* © 2022 Song_Artish**
