# MySQL 명령어

---

[TOC]

---



## 1. Database (Schema)

### 1.1 Schema 생성

```mysql
CREATE DATABASE <스키마 이름>;
```

- 기본 옵셥을 설정할 수도 있다.

  - 예시: `CHARSET=utf8`, `COLLATE=utf8_bin`

    ```mysql
    CREATE DATABASE <스키마 이름> DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    ```

    - `CHARSET`: 데이터 인코딩 방식
    - `COLLATE`: DB에서 문자 데이터 다루는 방식

### 1.2 Schema 조회

```mysql
SHOW DATABASES;
```

### 1.3 Schema 사용

```mysql
USE <스키마 이름>;
```

- 생성한 DB를 MySQL에게 사용하겠다고 명령하는 과정

### 1.4 Schema 삭제

```mysql
DROP DATABASE <스키마 이름>;
```





***Copyright* © 2022 Song_Artish**