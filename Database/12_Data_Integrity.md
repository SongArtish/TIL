# 데이터 무결성

2021.09.29

---

[TOC]

---



## 개념

> Data Integrity

- 데이터베이스에 저장되는 데이터의 **정확성**과 **일관성**을 유지하는 것
- 데이터에 **정확성**과 **일관성**을 부여하기 위해 제약 사항을 설정한다.



## 종류

```
:pushpin: 여기서 relation은 DB 테이블을 의미한다.
- PK: Primary Key
- FK: Foreign Key
```



### Domain Integrity

> relation에서 입력되는 데이터가 그 속성의 도메인 영역에서 포함되어야 한다는 규정

- 예시
  - '성별' 속성에 입력될 수 있는 값을 `남`과 `여`로 한정시킨다. 이외의 값은 입력되지 않도록 한다.

### Entity Integrity

> relation에서 각각의 tuple은 유일하게 식별되어야 한다는 규정

- 전후 관계가 의미적으로 이상이 없는가를 규정, 즉 중복된 tuple이 존재하면 안 된다.
- :ballot_box_with_check: PK는 Null값이나 중복된 값을 가질 수 없다.
- 예시
  - PK가 Null 값이나 중복된 값이 없으면 개체 무결성(Entity Integrity)을 충족한다.

### Referential Integrity

> 어떤 relation에 있는 tuple 데이터가 다른 relation에 있는 tuple 데이터와 관계성이 있어야 한다는 규정

- 예시
  - A relation의 PK를 B relation에서 FK로 설정했을 때, B relation의 해당 키들이 모두 A relation PK에 존재하면 참조 무결성(Referential Integrity)을 만족한다.

### Business Integrity

> 기업에서 업무를 수행하는 방법이나 데이터를 처리하는 규칙을 의미

- 넓게 보면 Domain, Entity, Referential Integrity도 업무 무결성(Business Integrity)에 포함될 수 있음
- 업무 무결성은 범위가 넓어 주로 프로그램에서 체크
- 업무 무결성을 물리적으로 강제하는 대표적인 방법으로는 `Trigger`가 존재
- 예시
  - 주문 금액이 3만원 이상이면 배송비 무료
  - 첫 회 보험료를 입금하지 않은 보험계약은 효력 없음



## <참고> 데이터 정합성

> 어떤 데이터들이 값이 서로 일치함

- 중복 데이터를 많이 사용하면 데이터끼리 정합성을 맞추기 어렵다.
- 비정규형을 사용해 Anomaly(이상현상)가 발생하면 정합성이 깨진다.
- 정합성은 데이터가 서로 모순 없이 일관되게 일치해야 함을 의미한다.



***Copyright* © 2021 Song_Artish**