# NoSQL

> Not Only SQL

---

[TOC]

---



## Overview

데이터베이스는 크게 **관계형 데이터베이스**와 **비관계형 데이터베이스**로 구분한다. 관계형 데이터베이스는 SQL(구조화 쿼리 언어)을 기반으로 하고, 비관계형 데이터베이스는 NoSQL(비구조화 쿼리 언어)로 데이터를 다룬다.

관계형 데이터베이스(RDB)에서는 테이블의 구조와 데이터 타입 등을 사전에 정의하고, 테이블에 정의된 내용에 알맞는 형태의 데이터만 삽입할 수 있다. RDB는 행(row)과 열(column)로 구성된 테이블에 데이터를 저장한다. 각 열은 하나의 속성에 대한 정보를 저장하고, 행에는 각 열의 데이터 형식에 맞는 데이터가 저장된다. 특정한 형식을 지키기 때문에, 데이터를 정확히 입력했다면 데이터를 사용할 때는 편리하다. RDB에서는 SQL을 활용해 원하는 정보를 쿼리할 수 있으며, 테이블 간의 관계를 직관적으로 파악할 수 있다.

> 대표적인 RDB는 MySQL, Oracle, SQLite, PostgreSQL, MariaDB 등이 있다.

NoSQL은 **데이터가 고정되어 있지 않은 데이터베이스**를 지칭한다. 그러나 NoSQL에 스키마가 반드시 없는 것은 아니다. RDB에서는 데이터를 입력할 때 스키마에 맞게 입력해야 하는 반면, NoSQL에서는 데이터를 읽어올 때만 스키마에 따라 데이터를 읽어온다. 이를 `schema on read`라고도 한다.

> 대표적인 NoSQL은 MongoDB, Casandra 등이 있다.



## 사용되는 경우

1. 비구조적인 대용량의 데이터를 저장하는 경우

   NoSQL 데이터베이스는 관계에 중점을 둔 SQL 데이터베이스보다 자유로운 형태로 데이터를 저장할 수 있으므로 필요에 따라서 새로운 데이터 유형을 추가할 수 있다. 소프트웨어 개발에 정형화되지 않은 많은 양의 데이터가 필요한 경우, NoSQL이 효율적일 수 있다.

2. 클라우드 컴퓨팅 및 저장공간을 최대한 활용하는 경우

   NoSQL 데이터베이스는 데이터베이스를 클라우드 기반으로 쉽게 분리할 수 있도록 지원하며, 저장 공간을 효율적으로 사용한다. 시스템이 커지면서 DB를 증설해야 하는 시점이 오면, SQL 데이터베이스에서는 수직적 확장의 형태로 DB를 증설한다. 수직적으로 확장된 데이터베이스는 관리가 어려워질 수 있는데에 반해, NoSQL은 수평적 확장의 형태로 증설하므로, 이론 상 무한대로 서버를 계속 분산시켜 DB를 증설할 수 있다.

3. 빠르게 서비스를 구축하고 데이터 구조를 자주 업데이트 하는 경우

   NoSQL 데이터베이스의 경우 스키마를 미리 준비할 필요가 없어서, 개발을 빠르게 해야하는 경우에 매우 적합하다. 시장에 빠르게 프로토타입을 출시해야 하는 경우나, 소프트웨어 버전 별로 많은 다운타임(데이터베이스의 서버를 오프라인으로 전환하여 작업하는 시간) 없이 데이터 구조를 자주 업데이트 해야하는 경우에는 일일이 스키마를 수정해주어야 하는 관계형 데이터베이스보다 NoSQL 기반의 비관계형 데이터베이스가 더 효율적이다.



## Type

NoSQL 기반의 비관계형 데이터베이스는 보통 다음과 같이 구성된다.

### KVS (Key-Value Store)

속성을 `key-value`의 쌍으로 나타내며 데이터를 배열의 형태로 저장한다. 여기서는 key는 속성 이름을 뜻하고, value는 속성에 연결된 데이터 값을 의미한다. Redis, Dynamo 등이 대표적인 key-value 형식의 데이터베이스이다.

### Document(문서형) 데이터베이스

데이터를 테이블이 아닌 문서처럼 저장한다. 많은 문서형 데이터베이스에서 JSON과 유사한 형식의 데이터를 문서화하여 저장한다. 각각의 문서는 하나의 속성에 대한 데이터를 가지고 있고, 컬렉션이라고 하는 그룹으로 묶어서 관리한다. 대표적인 문서형 데이터베이스에는 MongoDB가 있다.

### Wide-Column 데이터베이스

데이터베이스의 열(column)에 대한 데이터를 집중적으로 관리하는 데이터베이스이다. 각 열에는 key-value 형식으로 데이터가 저장되고, Column Families라고 하는 열의 집합체 단위로 데이터를 처리할 수 있다. 하나의 행에 많은 열을 포함할 수 있어서 유연성이 높다. 데이터 처리에 필요한 열을 유연하게 선택할 수 있다는 점에서 규모가 큰 데이터 분석에 주로 사용되는 데이터베이스 형식이다. 대표적인 wide-column 데이터베이스에는 Cassandra, HBase가 있다.

### Graph 데이터베이스

자료구조의 그래프와 비슷한 형식으로 데이터 간의 관계를 구성하는 데이터이다. 노드(nodes)에 속성별(entities)로 데이터를 저장한다. 각 노드 간 관계는 선(edge)으로 표현한다. 대표적인 그래프 데이터베이스에는 Neo4J, InfiniteGraph가 있다.



## SQL vs NoSQL

SQL 기반의 데이터 베이스와 NoSQL 데이터베이스 간에는 다음과 같은 차이점이 있다.

- **Storage**: NoSQL은 key-value, document, wide-column, graph 등의 방식으로 데이터를 저장하는 반면, RDB는 SQL을 이용해서 데이터를 테이블에 저장한다.
- **Schema**: SQL을 사용하려면 고정된 형식의 스키마가 필요하나, NoSQL은 RDB보다 동적으로 스키마 형태를 관리할 수 있다. NoSQL은 행을 추가할 때 즉시 새로운 열을 추가할 수 있고, 개별 속성에 대해서 모든 열에 대한 데이터를 반드시 입력하지 않아도 된다.
- **Querying**: RDB는 테이블의 형식과 테이블 간의 관계에 맞춰 데이터를 요청해야 하기 때문에 SQL과 같이 구조ㅘ된 쿼리 언어를 사용한다. 비관계형DB의 쿼리는 **데이터 그룹 자체**를 조회하는 것에 조첨을 두고 있으며, 구조화되지 않은 쿼리 언어인 UnQL(UnStructured Query Language)로도 데이터 요청이 가능하다.
- **Scalability**: 일반적으로 SQL 기반의 RDB는 수직적으로 확장하기 때문에, 성능을 많이 이용하며 복잡하고 시간이 많이 소모된다. 반면 NoSQL로 구성된 DB는 수평적으로 확장하기 때문에, 상대적으로 비용이 저렴하다.

SQL 기반의 관계형 데이터베이스를 사용하는 케이스는 다음과 같다.

1. 데이터베이스의 ACID 성질을 준수해야 하는 경우 (전자 상거래를 비롯한 모든 금융 서비스를 위한 소프트웨어 개발 등)
2. 소프트웨어에 사용되는 데이터가 구조적이고 일관적인 경우

NoSQL 기반의 관계형 데이터베이스를 사용하는 케이스는 다음과 같다.

1. 데이터 구조가 거의 또는 전혀 없는 대용량의 데이터를 저장하는 경우
2. 클라우드 컴퓨팅 및 저장공간을 최대한 활용하는 경우
3. 빠르게 서비스를 구축하는 과정에서 데이터 구조를 자주 업데이트 하는 경우



***Copyright* © 2022 Song_Artish**