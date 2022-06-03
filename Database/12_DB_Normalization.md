# 데이터베이스 정규화

---

[TOC]

---



## Overview

데이터베이스 정규화는 데이터베이스 설계를 재구성하는 테크닉이다.정규화를 통해 불필요한 데이터(redundancy)를 없앨 수 있고, 삽입/갱신/삭제 시 발생할 수 있는 각종 이상현상(anamolies)들을 방지할 수 있다.



## Data Redundancy

데이터 중복(data redundancy은 실제 데이터의 동일한 복사본이나, 부분적인 복사본을 뜻한다. 데이터 중복은 데이터베이스 내에서 몇 가지 문제점을 지닌다.

- 일관된 자료 처리의 어려움
- 저장 공간 낭비
- 데이터 효율성 감소



## Data Integrity

데이터 정규화는 데이터 무결성을 강화하는 목적도 가진다. 데이터 무결성(data integrity)은 데이터의 수명 주기 동안 정확성과 일관성을 유지하는 것을 의미한다.



## Anomaly

데이터 이상 현상(anomaly)은 기대한 데이터와 다른, 이상 현상을 의미한다. 다음과 같은 3가지 현상이 있다.

### Update Anomaly

갱신 이상(update anomaly)은 여러 행(레코드)에 걸쳐 동일한 데이터가 있을 때, 어떤 행을 갱신해야 하는지 논리적인 일관성이 없는 경우에 발생한다.

### Insertion Anomaly

삽입 이상(insertion anomaly)은 데이터를 삽입하지 못하는 경우를 가리킨다. 예를 들어, 특정 데이터가 들어왔지만, `NOT NULL`인 항목이 비어있는 경우, 삽입 이상에 해당한다.

### Deletion Anomaly

삭제 이상(deletion anomaly)은 데이터의 특정 부분을 지울 때 의도치 않게 다른 부분도 함께 지우는 이상 현상이다.



***Copyright* © 2022 Song_Artish**