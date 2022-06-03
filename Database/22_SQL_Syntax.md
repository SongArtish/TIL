# SQL 문법 종류

*****

[TOC]

*****



## Overview

SQL에서는 역할에 따라 문법이 다양하게 존재하며, 일반적으로는 다음과 같이 분류한다.

- Data Definition Language
- Data Manipulation Language
- Data Control Language
- Data Query Language
- Transaction Control Language



## DDL: Data Definition Language

데이터 정의 언어(DDL)는 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 언어이다.

- CREATE
- DROP
- ALTER



## DML: Data Manipulation Language

데이터 조작 언어(DML)는 데이터베이스에 데이터를 저장할 때 사용하는 언어이다. 이를 이용하면 CRUD를 할 수 있다.

- INSERT
- UPDATE
- DELETE
- SELECT



## DCL: Data Control Language

데이터 제어 언어(DCL)는 데이터베이스에 대한 접근 권한과 관련된 문법이다. 권한을 주는 `GRANT`나, 권한을 가져가는 `REVOKE` 등이 있다.

- GRANT
- REVOKE
- COMMIT
- ROLLBACK



## DQL: Data Query Language

DQL은 정해진 스키마 내에서 쿼리할 수 있는 언어이다. `SELECT`가 DQL에 해당한다. 이렇게 언어를 분류했지만, DQL은 DML의 일부분으로 취급하기도 한다.

- SELECT



## TCL: Transaction Control Language

TCL은 DML을 거친 데이터의 변경사항을 수정할 수 있다. `COMMIT`처럼 DML이 작업한 내용을 데이터베이스에 커밋하거나, `ROLLBACK`처럼 커밋했던 내용을 다시 롤백하는 문법이 있다.

- COMMIT
- ROLLBACK



***Copyright* © 2022 Song_Artish**