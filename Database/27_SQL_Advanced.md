# SQL Advanced

---

[TOC]

---



## CASE

프로그래밍 언어의 if문과 같은 기능으로 사용할 수 있는 SQL의 문법이다. CASE를 사용하면 특정 조건에 따라 다른 결과를 받을 수 있다.

```sql
SELECT CASE
			WHEN CustomerId <= 25 THEN 'GROUP 1'
			WHEN CustomerId <= 50 THEN 'GROUP 2'
			ELSE 'GROUP 3'
		END
	FROM customers
```



## SUBQUERY

쿼리문을 작성할 때, 다른 쿼리문을 포함할 수 있다. 이 때 포함되는 다른 쿼리문을 SUBQUERY라고 한다. 서브쿼리는 실행되는 쿼리에 중첩으로 위치해 정보를 전달하며, 소괄호로 감싸야 한다.

```sql
SELECT CustomerId, CustomerId = (SELECT CustomerId FROM customers WHERE CustomerId = 2)
FROM customers
WHERE CustomerId < 6
```

또한, 서브쿼리의 위치에 따라 다음과 같이 구분될 수 있다.

- SELECT 절 : Scala Subquery
- FROM 절 : Inline view
- WHERE 절 : Subquery

이어지는 내용에서는 서브쿼리를 어떻게 사용할 수 있을지 알아본다.

### IN

`IN`은 특정한 값이 서브쿼리에 있는지 확인할 수 있다. `NOT IN`은 이와 반대되는 개념으로 사용된다.

```sql
SELECT *
FROM customers
WHERE CustomerId In (SELECT CustomerId FROM customers WHERE CustomerId < 10)
```

### EXISTS

`EXISTS` 또는 `NOT EXISTS`는 돌려받은 서브쿼리에 존재하는 레코드를 확인한다. 만약 조회하려는 레코드가 존재한다면 TRUE를, 그렇지 않은 경우에는 FALSE를 리턴한다.

```sql
SELECT EmployeeId
FROM employees e	# e로 축약
WHERE EXISTS (
	SELECT 1
    FROM customers c	# c로 축약
    WHERE c.SupportRepId = e.EmployeeId
	)
ORDER BY EmployeeId
```

### FROM

FROM에도 서브쿼리를 사용할 수 있다. 다음과 같이 쿼리문과 서브쿼리를 사용해 조회된 결과를 하나의 테이블이나 조회할 대상으로 지정해 사용할 수 있다.

```sql
SELECT *
FROM (
	SELECT CusomterId
    FROM customers
    WHERE CusomterId < 10
	)
```



***Copyright* © 2022 Song_Artish**