# SQL 데이터베이스

*****

[TOC]

*****



## Overview

SQL의 데이터베이스 및 테이블 관련 명령어에 대해서 알아본다. 데이터베이스는 한 개 이상의 테이블을 포함하며, 테이블은 데이터 기록을 포함하고 있다.



## Database (Schema)

### Schema 생성: CREATE DATABASE

```sql
CREATE DATABASE 데이터베이스_이름;
```

기본 옵션을 설정할 수도 있다. 예를 들어 데이터 인코딩 방식(`CHARSET`)과 DB에서 문자 데이터를 다루는 방식(`COLLATE`)를 설정해본다.

```mysql
CREATE DATABASE <스키마 이름> DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
```

### Schema 조회: SHOW

```sql
SHOW DATABASES;
```

### Schema 사용: USE

데이터베이스를 이용해 테이블을 만들거나 수정/삭제 등의 작업을 하려면, 먼저 데이터베이스를 사용하겠다는 명령을 전달해야 한다.

```sql
USE 데이터베이스_이름;
```

### Schema 삭제: DROP

```sql
DROP DATABASE <스키마 이름>;
```



## Table

|   명령어    |       기능       |          사용법           |
| :---------: | :--------------: | :-----------------------: |
|   CREATE    |   테이블 생성    |    CREATE TABLE _ ();     |
| ALTER TABLE | 테이블 이름 수정 | ALTER TABEL _ RENAME TO _ |
|    DROP     |   테이블 삭제    |       DROP TABLE _        |

### Table 생성: CREATE TABLE

`USE`를 이용해 데이터베이스를 선택했다면, 테이블을 만들 수 있다.

```sql
CREATE TABLE <table> (
	<column> <DATATYPE> <(option)>,
    ...
)
```

예를 들어, id가 정수이며 pk인 user라는 이름의 테이블을 생성하는 경우 다음과 같다. `NOT NULL`을 사용하면 해당 필드의 값을 필수적으로 입력해야 하도록 설정할 수 있다.

```sql
CREATE TABLE user (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL,
    email varchar(255)
);
```

| 필드 이름 |     필드 타입     |       기타 속성        |
| :-------: | :---------------: | :--------------------: |
|    id     |       숫자        | Primary Key, 자동 증가 |
|   name    | 문자열 (최대 255) |                        |
|   email   | 문자열 (최대 255) |                        |

### Table 수정: ALTER TABLE

> 테이블명 변경

`RENAME TO`를 사용하면, 테이블명을 변경할 수 있다.

```sql
ALTER TABLE <table_name> RENAME TO <new_table_name>;
ALTER TABLE articles RENAME TO news;	// 예시
```

> 새로운 컬럼 추가

`ADD COLUMN`을 사용하면, 새로운 컬럼을 추가할 수 있다. 

```sql
ALTER TABLE news ADD COLUMN created_at TEXT;
```

단, 새로운 필드에 `NOT NULL` 옵션을 입력하면 기존의 데이터와 충돌하면서 오류가 일어나기 때문에, 이런 경우 DEFAULT 값을 넣어서 새로운 컬럼을 추가해야 한다.

```sql
ALTER TABLE news ADD COLUMN subtitle TExt NOT NULL DEFAULT 1;
```

### Table 삭제: DROP TABLE

```sqlite
sqlite> DROP TABLE <table>;
```

### Table 정보 확인

```sql
DESCRIBE user;
```

sqlite에서는 다음과 같이 사용할 수 있다.

```sqlite
sqlite> .schema <table>;
sqlite> .tables;	# table 조회
```





## <실습> 외부 csv파일 불러오기

먼저 데이터베이스를 생성한다.

```bash
$ sqlite3 tutorial.sqlite3
```

다음의 명령어로 `mode`를 csv 파일을 읽어오는 상태로 변경한다.

```sqlite
sqlite> .mode csv
```

`.mode`를 입력해 보면 현재 output mode가 csv인 것을 확인할 수 있다.

```sqlite
sqlite> .mode
current output mode: csv
```

hellodb.csv라는 파일을 가져와서 examples라는 테이블에 넣어준다.

```sqlite
sqlite> .import hellodb.csv examples
```

불러온 데이터를 저장할 경우 아래의 명령어를 입력한다. `data`라는 테이블로 불러온 데이터를 `data.db`라는 파일로 저장된다.

```sqlite
sqlite> .save data.db data
```



***Copyright* © 2022 Song_Artish**