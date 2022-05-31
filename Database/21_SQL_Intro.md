# SQL Intro

*****

[TOC]

*****



## Overview

SQL(Structured Query Language)는 관계형 데이터베이스 관리시스템([^RDBMS])의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어이다. MySQL, Oracle, SQLite, PostgreSQL 등 다양한 데이터베이스에서 SQL 구문을 사용할 수 있다.

> RDMS: Relational Database Management System



## 기본용어

### 스키마 (schema)

데이터베이스의 구조와 제약 조건(자료의 구조, 표현 방법, 관계)에 관련한 전반적인 명세를 기술한 것

| Column | Datatype |
| :----: | :------: |
|   id   |   INT    |
|  age   |   INT    |
| phone  |   TEXT   |
| email  |   TEXT   |

### 테이블 (table)

열(**컬럼**/필드)과 행(**레코드**/값)의 모델을 사용해 조직된 데이터 요소들의 집합

- pk (Primary Key, 기본키)
- 열 (Column)
- 행 (Row), 레코드



## Datatype

SQLite는 동적 데이터 타입으로, 기본적으로 유연하게 데이터가 들어간다.

- `INTEGER`, `TEXT`, `REAL`, `NUMERIC`, `BLOB`
- Boolean은 없다



***Copyright* © 2020 Song_Artish**