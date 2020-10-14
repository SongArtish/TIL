# SQL

2020.09.22

*****

[TOC]

*****



**Database**

> 체계화된 데이터의 모임. 몇 개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 집합체라고 할 수 있다.



## 1. SQL 개념

> SQL(Structured Query Language)는 관계형 데이터베이스 관리시스템([^RDBMS])의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어이다.
>
> [^RDBMS]: Relational Database Management System



### 기본용어

**스키마 (schema)**

> 데이터베이스의 구조와 제약 조건(자료의 구조, 표현 방법, 관계)에 관련한 전반적인 명세를 기술한 것

| Column | Datatype |
| :----: | :------: |
|   id   |   INT    |
|  age   |   INT    |
| phone  |   TEXT   |
| email  |   TEXT   |



**테이블 (table)**

> 열(**컬럼**/필드)과 행(**레코드**/값)의 모델을 사용해 조직된 데이터 요소들의 집합
>
> - pk (Primary Key, 기본키)
> - 열 (Column)
> - 행 (Row), 레코드



### SQL 문법 

SQL 문법은 다음과 같이 세가지 종류로 구분될 수 있다.

|          분류          |    뜻  |                         개념                             |                            예시                            |
| :--------------------: | :----------------------------------------------------------: | :--------------------------------------------------------: | ---------------------------------------------------------- |
| **DDL** | 데이터 정의 언어 | 데이터를 정의하기 위한 언어<br />관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 |**CREATE**<br />**DROP**<br />**ALTER**|
| **DML** |              데이터 조작 언어      | 데이터를 CRUD 등을 하기 위한 언어 |**INSERT**<br />**UPDATE**<br />**DELETE**<br />**SELECT**|
| **DCL** | 데이터 제어 언어 | 데이터베이스 사용자의 권한 제어를 위해 사용되는 언어이다. |**GRANT**<br />**REVOKE**<br />COMMIT<br />ROLLBACK|

> - DDL: Data Definition Language
> - DML: Data Manipulation Language
> - DCL: Data Control Language



### Datatype

> SQLite는 동적 데이터 타입으로, 기본적으로 유연하게 데이터가 들어간다.
>
> - `INTEGER`, `TEXT`, `REAL`, `NUMERIC`, `BLOB`
> - Boolean은 없다



## 2. SQLite

> [SQLite](https://www.sqlitetutorial.net/)는 서버가 아닌 응용 프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스이다.
>
> - 장점 : 구글 안드로이드 운영체제 기본 탑재된 데이터베이스, 임베디드 소프트웨어 활용, 오픈소스 프로젝트



### 설치

**INSTALL**

1. [사이트](https://www.sqlite.org/download.html)에서 dll, tools 2가지 파일 설치
2. 압축풀어서 폴더에 담기
3. 환경변수 PATH 설정

- 처음에 설치하면 bash에서 다음의 명령어로 sqlite를 실행할 수 있다.

```bash
$ winpty sqlite3
```

**SETTINGS**

git-bash에서 기본적인 세팅을 해준다.

```bash
$ vi ~/.bashrc
```

- 이후 불러온 창에서 다음을 입력한다.

```
alias jp="jupyter notebook"
alias sqlite3="winpty sqlite3"
```

- 그 후 `Esc` 키를 누르고 해당 창의 제일 밑에 부분에서 `:wq`를 입력하여 설정을 저장하고 종료한다.

```
:wq
```

- 다음으로 bash창에서 다음을 입력한다.

```bash
$ source ~/.bashrc
```

- 이 과정을 마치면 `sqlite3`라는 명령어로 SQLite를 실행할 수 있다.

```bash
$ sqlite3
```



### SQLite 실행

```bash
$ sqlite3
```



### SQLite 종료

`Ctrl` + `C` * 2번



### 외부 csv파일 불러오기

**Database 생성**

```bash
$ sqlite3 <Database Name>.sqlite3
```

- 예시

```bash
$ sqlite3 tutorial.sqlite3
```

- 다음의 명령어로 `mode`를 csv 파일을 읽어오는 상태로 변경한다.

```sqlite
sqlite> .mode csv
```

- `.mode`를 입력해 보면 현재 output mode가 csv인 것을 확인할 수 있다.

```sqlite
sqlite> .mode
current output mode: csv
```

- hellodb.csv라는 파일을 가져와서 examples라는 테이블에 넣어준다.

```sqlite
sqlite> .import hellodb.csv examples
```



### 데이터 조회

> **`SELECT문`**은 데이터베이스에서 특정한 테이블을 반환한다.
>
> - `SELECT` : 조회 (READ)
> - `*` : 모든 column 지정

```sqlite
sqlite> SELECT * FROM examples;
```

- `rowid` 컬럼까지 조회하려면 다음의 명령어를 사용한다.

```sqlite
sqlite> SELECT rowid, * FROM classmates;
```

- 다음의 옵션을 사용하면 테이블을 조금 더 보기 좋게 출력할 수 있다.

```sqlite
sqlite> .headers on
sqlite> .mode column
```





## 3. SQLite 테이블

|   명령어    |       기능       |          사용법           |
| :---------: | :--------------: | :-----------------------: |
|   CREATE    |   테이블 생성    |    CREATE TABLE _ ();     |
| ALTER TABLE | 테이블 이름 수정 | ALTER TABEL _ RENAME TO _ |
|    DROP     |   테이블 삭제    |       DROP TABLE _        |



### Table 생성

```sqlite
sqlite> CREATE TABLE <table> (
	<column> <DATATYPE> <(option)>,
    ...
)
```

- 예시 : id가 정수이며 pk인 classmates라는 이름의 테이블을 생성

```sqlite
sqlite> CREATE TABLE classmates (
	id INTEGER PRIMARY KEY,
    name TEXT
);
```



**AUTOINCREMENT**

테이블 생성시 `AUTOINCREMENT` 속성을 사용하면, 데이터를 삭제하고 생성할 때 Django와 같이 이미 사용된 적이 있는 행은 사용되지 않는다.

```sqlite
sqlite> CREATE TABLE <table> (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    ...
);
```

- 예시 : 필드가 name만 있는 경우 예시

```sqlite
sqlite> INSERT INTO tests (name) VALUES ('홍길동'), ('김철수');
```

- **하지만** SQLite는 특정한 요구사항이 없다면 AUTOINCREMENT 속성을 사용하지 않아야 한다!



### Table 목록 조회

```sqlite
sqlite> .tables
```



### Table 이름 수정

```sql
ALTER TABLE <table_name> RENAME TO <new_table_name>;
```

- 자세한 것은 [5.7 테이블 변경 : ALTER](### 5.7 테이블 변경 : ALTER) 참조!



### Schema 조회

```sqlite
sqlite> .schema <table>
```



### Table 삭제(DROP)

```sqlite
sqlite> DROP TABLE <table>;
```



## 4. SQLite CRUD

|      | 구문   | 예시                                                         |
| ---- | ------ | ------------------------------------------------------------ |
| C    | INSERT | INSERT INTO classmates (name, age, address) VALUES ('이송영', 25, '서울'); |
| R    | SELECT | SELECT * FROM classmates WHERE id=1;                         |
| U    | UPDATE | UPDATE classmates SET name='이송영' WHERE id=1;              |
| D    | DELETE | DELETE FROM classmates WHERE id=1;                           |



### 데이터 추가 (INSERT)

- 특정 table에 새로운 행을 추가하여 데이터를 추가할 수 있다.

```sqlite
sqlite> INSERT INTO <table> (*columns) VALUES (*values);
```

- 예시

```sqlite
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
```

- 다음과 같이 간단하게 data를 추가할 수 있다.

```sqlite
sqlite> INSERT INTO <table> VALUES (*values);
```

- `,`(쉼표)를 사용해서 한 번에 여러 개의 데이터를 추가할 수 있다.

```sqlite
sqlite> INSERT INTO <table> VALUES (*values), (*values), (*values), (*values), ... ;
```



**테이블 다시 만들기**

- 이번에는 `id`를 직접 정의하고 `NOT NULL`을 추가해준다.

```sqlite
sqlite> CREATE TABLE classmates (
	id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);
```

- 위와 같이 작성하면 데이터 입력시 `id`를 포함해서 모든 필드의 값들을 필수적으로 입력해줘야 한다. 
- SQLite가 만들어주는 `rowid`를 사용하는 것이 좋다 !



### 데이터 조회 (SELECT)

**`LIMIT num`**

> 특정한 table에서 원하는 개수만큼 Column을 가져온다

```sqlite
sqlite> SELECT <*columns> FROM <table> LIMIT <num>;
```

```sqlite
sqlite> SELECT rowid, name FROM classmates LIMIT 1
```



**`OFFSET num`**

> 특정 위치에서부터 데이터를 가져온다

- OFFSET은 앞의 <num> 만큼의 값을 제외하고 뒤에서부터 데이터를 가져온다.

```sqlite
sqlite> SELECT <*columns> FROM <table> LIMIT <num> OFFSET <num>;
```

- 예시

```sqlite
sqlite> SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
```



**`WHERE column=value`**

> 특정 조건에 해당하는 데이터를 가져온다

```sqlite
sqlite> SELECT <*columns> FROM <table> WHERE <condition>;
```

- 예시

```sqlite
sqlite> SELECT rowid, name FROM classmates WHERE address='서울';
```



**`DISTINCT`**

> table에서 특정 column 값을 중복없이 가져오기

```sqlite
sqlite> SELECT DISTINCT <column> FROM <table>;
```

- 예시

```sqlite
sqlite> SELECT DISTINCT age FROM classmates;
```



### 데이터 수정 (UPDATE)

> 특정 table에 특정한 레코드를 수정할 수 있다.

```sqlite
sqlite> UPDATE <table> SET <*columns=values> WHERE <condition>;
```

- 예시

```sqlite
sqlite> UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=4;
```



### 데이터 삭제 (DELETE)

> 특정 table에 특정한 레코드를 삭제할 수 있다.

```sqlite
sqlite> DELETE FROM <table> WHERE <condition>;
```

- 중복이 불가능한(UNIQUE) 값인 `rowid`를 기준으로 한다.

```sqlite
sqlite> DELETE FROM classmates WHERE rowid=4;
```

- 단, SQLite에서 마지막 행이 삭제된 후 새로운 데이터를 생성하게 되면, 마지막 행의 pk에 이어서 데이터가 생성된다.
- 테이블 생성시 [AUTOINCREMENT](###Table 생성) 속성을 사용해서 이미 사용한 적이 있는 행은 사용하지 않도록 할 수 있다.



## 5. SQL 활용하기



**시작하기**

- 해당 폴더에서 `git-bash`를 실행 후 sqlite로 파일을 실행한다.

```bash
$ sqlite3 tutorial.sqlite3
```

- 테이블 리스트를 확인해본다.

```sqlite
sqlite> .table
```

- 테이블 모드를 확인하고 `csv`로 변경해준다.

```sqlite
sqlite> .mode
sqlite> .mode csv
sqlite> .mode
```

**외부데이터 가져오기**

```sqlite
sqlite> .import users.csv users
```



### 5.1 WHERE 조건문

```sql
sqlite> SELECT <*columns> FROM <table> WHERE <condition>;
```

- 예시 : 나이가 30 이상인 조건에 해당하는 데이터의 모든 정보를 가져온다.

```sqlite
sqlite> SELECT * FROM users WHERE age >= 30;
```

- 예시 : 나이가 30 이상인 조건에 해당하는 데이터의 성을 가져온다.

```sqlite
sqlite> SELECT last_name, age FROM users WHERE age>=30;
```



### 5.2 COUNT

다음의 표현식은 레코드의 개수를 반환한다.

```sqlite
sqlite> SELECT COUNT(<column>) FROM <table>
```

- column을 모두 지정할 때는 `*`을 사용하면 된다.



### 5.3 AVG(), SUM(), MIN(), MAX()

다음의 표현식은 기본적으로 숫자(INTEGER)일때만 가능하다. (`AVG(), SUM(), MIN(), MAX()`)

```sqlite
sqlite> SELECT AVG(<column>) FROM <table>; 
```

- 예시

```sqlite
sqlite> SELECT AVG(age) from users WHERE age>=30;
```

```sqlite
sqlite> SELECT first_name, MAX(balance) FROM users;
```

```sqlite
sqlite> SELECT AVG(balance) FROM users WHERE age>=30;
```



### 5.4 Wild Cards : `LIKE`

> 정확한 값에 대한 비교가 아닌, 패턴을 확인하여 해당하는 값을 반환한다.
>
> - `_` : 반드시 이 자리에 한 개의 문자가 존재해야 한다.
>
> - `%` : 이 자리에 문자열이 있을 수도 없을 수도 있다.

```sqlite
sqlite> SELECT <column> FROM <table> WHERE <condition> LIKE '<condition>';
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

```sqlite
sqlite> SELECT * FROM users WHERE age LIKE '2_';
```

- 예시 : users 에서 지역번호가 02인 사람

```sqlite
sqlite> SELECT * FROM users WHERE phone LIKE '02-%';
```

- 예시 : users에서 이름이 '준'으로 끝나는 사람

```sqlite
sqlite> SELECT * FROM users WHERE first_name LIKE'%준';
```



### 5.5 정렬 : `ORDER BY`

> `ORDER BY`를 활용해서 해서 해당 필드를 기준으로 정렬할 수 있다.
>
> - **ASC** : 오름차순 (default)
> - **DESC** : 내림차순

```sql
sqlite> SELECT <*columns> FROM <table> ORDER BY <*columns> <ASC/DESC>;
```

- 예시 : users에서 나이순으로 오름차순 정렬하여 상위 10개만 뽑으면

```sqlite
sqlite> SELECT * FROM users ORDER BY age ASC LIMIT 10;
```

- 예시 : users에서 나이순, 성 순으로 오름차순 정렬하여 상위 10개만 뽑으면

```sql
sqlite> SELECT * FROM users ORDER BY age, last_name LIMIT 10;
```

- ASC는 default 값이기 때문에 생략가능하다.
- ORDER BY 이후 나열된 column의 순서대로 정렬 우선순위가 결정된다.



### 5.6 Group By

> 지정된 기준에 따라 행 세트를 그룹으로 결합한다. 데이터를 요약하는 상황에 주로 사용한다.
>
> - SELECT 문의 옵션 절(optional clause)이다.

```sql
sqlite> SELECT <*columns> FROM <table> GROUP BY <*columns>;
```

- 예시 : users에서 각 성(last_name)씨가 몇 명씩 있는지 조회

```sqlite
sqlite> SELECT last_name, COUNT(*)
	FROM users
	GROUP BY last_name;
```



### 5.7 테이블 변경 : ALTER

> 테이블 자체를 변경한다.

**테이블 생성**

```sql
sqlite> CREATE TABLE articles (
   ...> title TEXT NOT NULL,
   ...> content TEXT NOT NULL
   ...> );
```

**데이터입력**

```sql
sqlite> INSERT INTO articles VALUES('1번제목', '1번내용');
```

**테이블명 변경**

```sql
sqlite> ALTER TABLE articles RENAME TO news;
```

**새로운 컬럼 추가**

- 새로운 필드에 `NOT NULL` 옵션을 입력하면 기존의 데이터와 충돌하면서 오류가 일어난다.

```sql
sqlite> ALTER TABLE news
   ...> ADD COLUMN created_at TEXT;
```

- 따라서, 이러한 경우 DEFAULT 값을 넣어서 새로운 컬럼을 추가한다.

```sql
sqlite> ALTER TABLE news
   ...> ADD COLUMN subtitle TExt NOT NULL DEFAULT 1;
```



***Copyright* © 2020 Song_Artish**