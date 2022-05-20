# HTTP 요청 메서드

---

[TOC]

---



## Overview

HTTP 요청 메서드는 **주어진 리소스에 수행하길 원하는 행동을 나타내며**, `HTTP 동사`라고 부르기도 한다.



## 종류

- **GET**: 특정 리소스의 표시를 요청한다. `GET`으 사용하는 요청은 오직 데이터를 받기만 한다.
- **HEAD**: `GET` 메서드의 요청과 동일한 응답을 요구하지만, <u>응답 본문을 포함하지 않는다.</u>
- **POST**: 특정 리소스에 entity를 제출할 때 쓰인다. 이는 종종 서버 상태의 변화나 부작용을 일으킨다.
- **PUT**: 목적 리소스 모든 현재 표시를 요청 payload로 바꾼다. (교체)
- **DELETE**: 특정 리소스를 삭제한다.
- **CONNECT**: 목적 리소스로 식별되는 서버로의 터널을 맺는다.
- **OPTIONS**: 목적 리소스의 통신을 설정하는 데 사용된다.
- **TRACE**: 목적 리소스의 경로를 따라 메시지 loop-back 테스트를 한다.
- **PATCH**: 리소스의 부분만을 수정하는데 사용된다. (수정)

HTTP 메소드는 CRUD 행동에 따라 목적에 맞게 사용해야 한다.

| Request |    Method    |
| :-----: | :----------: |
|  Read   |     GET      |
| Create  |     POST     |
| Update  | PUT or PATCH |
| Delete  |    DELETE    |



## HTTP API 디자인

HTTP API 디자인에는 Best Practice가 존재한다.

| 요청                 | URL 디자인 | Method |
| -------------------- | ---------- | ------ |
| 모든 사용자 조회     | /users     | GET    |
| 새 사용자 추가       | /users     | POST   |
| 1번 사용자 정보 갱신 | /users/1   | PUT    |
| 1번 사용자 정보 삭제 | /users/1   | DELETE |
| 1번 사용자 정보 조회 | /users/1   | GET    |



***Copyright* © 2022 Song_Artish**