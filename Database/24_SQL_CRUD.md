# SQL CRUD

*****

[TOC]

*****



## Overview

|      | 구문   | 예시                                                         |
| ---- | ------ | ------------------------------------------------------------ |
| C    | INSERT | INSERT INTO classmates (name, age, address) VALUES ('이송영', 25, '서울'); |
| R    | SELECT | SELECT * FROM classmates WHERE id=1;                         |
| U    | UPDATE | UPDATE classmates SET name='이송영' WHERE id=1;              |
| D    | DELETE | DELETE FROM classmates WHERE id=1;                           |



## 데이터 추가: INSERT

특정 table에 새로운 행을 추가하여 데이터를 추가할 수 있다.

```sqlite
INSERT INTO <table> (*columns) VALUES (*values);
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);	// 예시
```

다음과 같이 간단하게 data를 추가할 수 있다.

```sqlite
INSERT INTO <table> VALUES (*values);
```

`,`(쉼표)를 사용해서 한 번에 여러 개의 데이터를 추가할 수 있다.

```sqlite
INSERT INTO <table> VALUES (*values), (*values), (*values), (*values), ... ;
```





## 데이터 조회: SELECT

데이터셋에 포함될 특성을 특정한다.

```sql
SELECT 'hello world'
SELECT 5
SELECT 1+20
```

### FROM

테이블과 관련된 작업을 할 경우 반드시 입력해야 한다. FROM 뒤에는 결과를 도출해낼 데이터베이스 테이블을 명시한다.

```sql
SELECT 특성_1, 특성_2 FROM 테이블_이름
SELECT * FROM 테이블_이름
```

> `*`는 와일드카드(wildcard)로 전부 선택할 때 사용된다.

### LIMIT

결과 출력 데이터의 개수를 정할 수 있다. LIMIT는 선택적으로 사용할 수 있으며, 쿼리문에서 사용할 때에는 가장 마지막에 추가한다.

```sqlite
SELECT <*columns> FROM <table> LIMIT <num>;
SELECT rowid, name FROM classmates LIMIT 200	// 예시
```

### OFFSET

특정 위치에서부터 데이터를 가져온다. 앞의 num 만큼의 값을 제외하고 뒤에서부터 데이터를 가져온다.

```sqlite
SELECT <*columns> FROM <table> LIMIT <num> OFFSET <num>;
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;	// 예시
```

### WHERE

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

### DISTINCT

table에서 특정 column 값을 중복없이 가져올 때 사용할 수 있다.

```sql
SELECT DISTINCT 특성_1 FROM 테이블_이름
SELECT DISTINCT age FROM classmates;	// 예시
```

DISTINCT에서 여러 개의 특성을 입력하면, 입력한 특성의 유니크한 **조합** 값들을 선택할 수 있다.

```sql
SELECT DISTINCT 특성_1, 특성_2 FROM 테이블_이름
```



## 데이터 수정: UPDATE

특정 table에 특정한 레코드를 수정할 수 있다.

```sqlite
UPDATE <table> SET <*columns=values> WHERE <condition>;
UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=4;	// 예시
```



## 데이터 삭제: DELETE

특정 table에 특정한 레코드를 삭제할 수 있다.

```sqlite
DELETE FROM <table> WHERE <condition>;
DELETE FROM classmates WHERE rowid=4;	// 예시
```

단, SQLite에서 마지막 행이 삭제된 후 새로운 데이터를 생성하게 되면, 마지막 행의 pk에 이어서 데이터가 생성된다. 그리고 테이블 생성시 `AUTOINCREMENT `속성을 사용해서 이미 사용한 적이 있는 행은 사용하지 않도록 할 수 있다.



***Copyright* © 2022 Song_Artish**