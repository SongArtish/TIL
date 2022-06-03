# SQL 내장함수

*****

[TOC]

*****



## Overview

SQL의 내장함수는 2가지로 분류할 수 있다.

- 단일 행 함수(Single Row Function): 문자형, 숫자형, 날짜형, 변환형
- 다중 행 함수(Multi Row Function): 그룹함수



## 문자형 함수



## 숫자형 함수



## 날짜형 함수



## 변환형 함수



## 집합연산

레코드를 조회하고 분류한 뒤, 특정 작업을 하는 연산이다.

### GROUP BY

지정된 기준에 따라 행 세트를 그룹으로 결합하며, 데이터를 요약하는 상황에 주로 사용한다. SELECT 문의 옵션 절(optional clause)이다.

```sql
SELECT <*columns> FROM <table> GROUP BY <*columns>;
```

예를 들어, users에서 각 성(last_name)씨가 몇 명씩 있는지 조회하는 경우 아래와 같이 사용할 수 있다.

```sql
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
```

### HAVING

GROUP BY로 조회된 결과를 필터링할 수 있다.

```sql
SELECT CustomerId, AVG(Total) FROM invoices GROUP BY CustomerID HAVING AVG(Total) > 6.00;
```

### COUNT

다음의 표현식은 레코드의 개수를 반환한다.

```sql
SELECT COUNT(<column>) FROM <table>
```

column을 모두 지정할 때는 `*`을 사용하면 된다. (정확하게 count를 하는 경우에는 id 값을 column에 넣는 것이 좋은 것 같다~)

### SUM()

SUM 함수는 레코드의 합을 리턴하며, 기본적으로 숫자(INTEGER)일 때만 사용할 수 있다.

```sql
SELECT InvoiceId, SUM(UnitPrice) FROM invoice_items GROUP BY InvoiceId;
```

### AVG()

AVG 함수는 레코드의 평균값을 계산하는 함수이며, 기본적으로 숫자(INTEGER)일 때만 사용할 수 있다.

```sql
SELECT AVG(age) from users WHERE age>=30;
```

### MAX(), MIN()

MAX 함수와 MIN 함수는 각각 레코드의 최대값과 최소값을 리턴하며, 기본적으로 숫자(INTEGER)일 때만 사용할 수 있다.

```sql
SELECT first_name, MAX(balance) FROM users;
```



***Copyright* © 2022 Song_Artish**