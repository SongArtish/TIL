# SQL Statements

*****

[TOC]

*****



## Overview

데이터베이스에서 하려는 동작은 대부분 SQL문을 통해서 할 수 있다. 여기서는 SQL문 중 CRUD를 제외한 나머지 부분에 대해서 다룬다.



## WHERE

필터 역할을 하는 쿼리문이다. WHERE는 선택적으로 사용할 수 있다.

```sql
SELECT 특성_1, 특성_2 FROM 테이블_이름 WHERE 특성_1 = "특정 값"
```

다음과 같이 사용할 수 있다.

```sql
// 특정 값을 제외한 값 찾기
... WHERE 특성_1 <> "특정 값"
// 크기 비교
... WHERE 특성_2 > "특정 값"
// 문자열에서 특정 값과 비슷한 값들을 필터할 때 LIKE와 \% 혹은 \*를 사용한다.
... WHERE 특성_3 LIKE "%특정 문자열%"
// 리스트의 값과 일치하는 데이터를 필터할 때는 IN을 사용한다.
... WHERE 특성_4 IN ("특정값_1", "특정값_2")
// 값이 없는 경우 NULL을 찾을 때는 IS와 같이 사용한다.
... WHERE 특성_5 IS NULL
// 값이 없는 경우를 제외할 때는 NOT을 추가해 이용한다.
... WHERE 특성_6 IS NOT NULL
```



## ORDER BY

돌려받는 데이터 결과를 어떤 기준으로 정렬할지 결정한다. ORDER BY는 선택적으로 사용할 수 있다.

- **ASC** : 오름차순 (default)
- **DESC** : 내림차순

```sql
SELECT * FROM 테이블_이름 ORDER BY 특성_1
sqlite> SELECT * FROM users ORDER BY age, last_name LIMIT 10;	// 예시
```

기본 정렬은 오름차순이다. 아래와 같이 `DESC`를 사용하여 내림차순으로도 정렬할 수 있다.

```sql
SELECT * FROM 테이블_이름 ORDER BY 특성_1 DESC
```



## JOIN

A `JOIN` clause is used to combine rows from two or more tables, based on a related column between them.

### INNER JOIN

둘 이상의 테이블을 서로 공통된 부분(**교집합**)을 기준으로 연결한다. 앞의 INNER을 생략하고 `JOIN`으로도 실행할 수 있다. (`WHERE A=B`는 대신해서 쓰는 느낌이다~)

```sql
SELECT * FROM 테이블_1 JOIN 테이블_2 ON 테이블_1.특서_A = 테이블_2.특성_B
```

### OUTER JOIN

`OUTER JOIN`은 기준 테이블에서 JOIN 대상 테이블에 일치하는 값이 없을 경우 null로 조회하여 노출된다. 즉, **기준이 되는 테이블의 값들은 모두 노출되며, JOIN대상 테이블의 값이 있을 경우 값이 노출되고 없으면 Null 값이 노출**된다. (**합집합**)

`Outer Join`은 다양한 선택지가 있다. `LEFT (OUTER) JOIN`으로 Left Inclusive를 실행할 수 있다.

```sql
SELECT * FROM 테이블_1 LEFT JOIN 테이블_2 ON 테이블_1.특성_A = 테이블_2.특성_B
```

`RIGHT (OUTER) JOIN`으로 Right Inclusive를 실행할 수도 있다.

```sql
SELECT * FROM 테이블_1 RIGHT JOIN 테이블_2 ON 테이블_1.특성_A = 테이블_2.특성_B
```

아래는 JOIN을 이용한 활용 예시이다.

```sql
-- TODO: Q 5-2-8. category의 name이 soccer인 content의 title, body, created_at, user의 name을 찾기위한 SQL을 작성해주세요.

const PART5_2_8 = `SELECT content.title, content.body, content.created_at, user.name FROM content
    LEFT JOIN user ON content.userId=user.id
    JOIN content_category ON content.id=content_category.contentId
    JOIN category ON category.id=content_category.categoryId
    WHERE category.name = "soccer"
`;
```



## LIKE

정확한 값에 대한 비교가 아닌, 패턴을 확인하여 해당하는 값을 반환한다.

- `_` : 반드시 이 자리에 한 개의 문자가 존재해야 한다.

- `%` : 이 자리에 문자열이 있을 수도 없을 수도 있다.

```sql
SELECT <column> FROM <table> WHERE <condition> LIKE '<condition>';
```

| 와일드 카드 |        예시         |              의미              |
| :---------: | :-----------------: | :----------------------------: |
|      %      |         2%          |        2로 시작하는 값         |
|             |         %2          |         2로 끝나는 값          |
|             |         %2%         |        2가 들어가는 값         |
|      _      |         _2%         |   두 번째가 2로 시작하는 값    |
|             |        1___         |    1로 시작하고 4자리인 값     |
|             | `2_%_%`<br />`2__%` | 2로 시작하고 적어도 3자리인 값 |

- 예시 : users에서 나이가 20대인 사람

```sql
SELECT * FROM users WHERE age LIKE '2_';
```

- 예시 : users 에서 지역번호가 02인 사람

```sql
SELECT * FROM users WHERE phone LIKE '02-%';
```

- 예시 : users에서 이름이 '준'으로 끝나는 사람

```sql
SELECT * FROM users WHERE first_name LIKE'%준';
```



## Select 실행 순서

데이터를 조회하는 SELECT문은 정해진 순서대로 동작한다. SELECT 문의 실행 순서는 다음과 같다.

- FROM
- WHERE
- GROUP BY
- HAVING
- SELECT
- ORDER BY



***Copyright* © 2022 Song_Artish**