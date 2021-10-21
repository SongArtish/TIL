# Relational Database

> 관계형 데이터베이스

2021.10.19

---

[TOC]

---



## 데이터베이스

> 기업이나 조직 또는 개인이 필요에 의해 **데이터를 일정한 형태로 저장**해 놓은 것

- **DBMS**
  - Database Management System
  - 데이터베이스를 관리하는 소프트웨어



## 관계형 데이터베이스

> 많은 사용자들이 **동시에 데이터를 공유 및 조작**할 수 있는 기능을 제공

1. 정규화를 통해 이상(ANOMLY) 현상을 제거하고 데이터 중복을 피할 수 있다.
   - 삽입 이상(Insertion anomaly) : 데이터를 삽입할 때 의도와는 상관없이 원하지 않는 값들도 함께 삽입하는 현상
   - 삭제 이상(Deleting anomaly) : 데이터를 삭제할 때 의도와는 상관없는 값들도 함께 삭제되는 연쇄 삭제 현상
   - 갱신 이상(Modification anomaly) : 반복되는 데이터 중 일부를 갱신 할 때 데이터 불일치가 발생하는 현상
2. 동시성 관리, 병행 제어를 통해 데이터를 공유
3. 데이터 무결성을 보장
4. 데이터를 복구하는 기능



## SubQuery

- 하나의 SQL 문장 내부에 존재하는 또 다른 SELECT 문장
- 서브쿼리의 위치에 따라 구분된다.
  - SELECT 절 : Scala Subquery
  - FROM 절 : Inline view
  - WHERE 절 : Subquery



***Copyright* © 2021 Song_Artish**