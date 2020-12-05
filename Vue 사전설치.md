# Vue 사전설치

2020.12.04

---

[TOC]

---



## 1. Open JDK

**파일 다운로드**

- [사이트](https://kr.azul.com/downloads/zulu-community/)에서 OS에 맞는 버전의 JDK 설치파일 다운로드

  > Java 8 (LTS) - Windosws - x86 64bit - JDK - `.msi`파일

**환경 세팅**

- `환경변수` > `시스템변수` 새로 만들기
  - 변수이름 : `JAVA_HOME`
  - 값 : `<JDK 설치경로>` (예시 : `C:\Program Files\Zulu\zulu-8`)
- `환경변수` > `Path` 선택 후 편집
  - 새로 만들기 : `%JAGA_HOME%\bin`
- :white_check_mark: 여기서 `\`는 실제로는 원화 마크가 표시된다.

**java 버전 확인**

- `cmd`에서 아래 명령어로 자바 버전 확인

```cmd
java -version
```

```cmd
javac -version
```



## 2. STS

**파일 다운로드**

- [사이트](https://github.com/spring-projects/toolsuite-distribution/wiki/Spring-Tool-Suite-3)에서 OS에 맞는 버전의 STS 설치파일 다운로드

  > ##### full distribution on Eclipse 4.15 > `.zip`파일

- 설치 후 압축 풀기



## 3. MySQL

**파일 다운로드**

- [사이트](https://dev.mysql.com/downloads/mysql/)에서  OS에 맞는 버전의 MySQL 설치파일 다운로드

  > | **Windows (x86, 32-bit), MSI Installer** | 8.0.22 | 405.2M | [Download](https://dev.mysql.com/downloads/file/?id=499590) |
  > | ---------------------------------------- | ------ | ------ | ----------------------------------------------------------- |
  > | (mysql-installer-community-8.0.22.0.msi) |        |        |                                                             |

- 사이트 가입 절차가 다소 번거로운데, 사이트 가입을 차근차근 완료한 후 파일을 다운로드한다.
  - `Developer Default` 선택 후 `Next`
  - `Execute` 클릭해서 `Visual C++` 설치 후 `Next`
  - `Execute` 클릭해서 following products 설치 후 `Next`
  - `Next`
  - `Standalone MySQL Server` 선택 후 `Next`
  - 다음의 설정 확인 후 `Next`
    - Config Type : `Development Computer`
    - TCP/IP : 체크
      - Port : `3306`
      - `Open Windows Firewall ports for network access` : 체크
  - `Use Legacy Authentication Method` 선택 후 `Next` (기존 프로그램과의 호환성)
  - root 계정 비번 설정 후 Add User를 이용하여 계정 추가 후 `Next`
    - :heavy_check_mark:계정 추가는 나중에 해도 된다!
  - `Window Service name = MySQL80` 확인 후 `Next`
  - `Exectue` 클릭해서 configuration completed 확인 후 `Finish`
  - `Next`
  - `Finish`
  - `Next`
  - 계정 입력 후 연결 성공 여부 확인 후 `Next`
  - `Execute` 클릭해서 configuration completed 확인 후 `Finish`
  - `Next`
  - Installation Complete 확인 후 `Finish`



## MySQL Workbench

- `MySQL Connections > `root 계정으로 접속

**로그인**

- `Database > Connect to Database` (`Ctrl + U`)에서 설치 시 생성한 계정으로 로그인
  - Username : admin (혹은 ssafy)
  - Password > `Store in Valut ...` : <비밀번호 입력>

**Schema 생성**

- `스키마 생성` 아이콘을 클릭한다.
- `스키마 이름`을 입력하고, `utf8`, `utf8_bin`을 설정한후 `Apply`한다.
- 왼쪽 창에 해당 스키마가 생선된 것을 확인한다.

**Script 실행**

1. `Open a script SQL file` 아이콘 클릭 후, 제공된 `.sql` 파일 선택
2. `Execute the selected portion ...` 아이콘을 클릭하여 script file 실행
3. Schemas Navigator(왼쪽 창)에서 table 생성 확인

**Script 파일 정상 실행 확인**

1. SQL Editor 창에서 `. select * from employees;`이라는 Query 작성
2. `Execute the statement under ...` 아이콘 클릭하여 Query문 실행
3. Resultset Grid에 출력 결과 확인



## MySQL 참고

### MySQL 계정 생성

```
create user '<아이디>'@'<외부접속정보>' identified by '비밀번호';
```

- 예시

```
create user 'ssafy'@'211.183.1.152' identified by 'ssafy';
```

- `<외부접속정보>` : 모든 아이피 접속이 가능하게 하려면 `%`를 입력하면 된다.

### MySQL 권한 설정

```
grant <권한목록> on <데이터베이스.객체> to '<아이디>'@'<외부접속정보>';
```

- `with grant option`

  > 권한을 부여 받은 사용자도 부여 받은 권한을 다른 사용자/role로 부여할 수 있게 된다.

- 예시

```
grant select, insert, delete, update on ssafydb.emp to 'ssafy'@'%';
```

- 모든 DB에 대해서 root와 동일 권한 부여하는 경우

```
grant all privileges on *.* to 'ssafy'@'%' with grant option;
```

- 설정한 권한이 바로 적용되도록 실행 (적용이 안되는 경우)

```
flush privileges;
```

### MySQL 권한 확인 및 해제

- 권한 확인

```
show grants;
```

- 권한 해제

```
revoke <권한목록> on <데이터베이스.객체> from '<아이디>';
```

- 예시

```
revoke select, insert, delete, update on 'ssafyDB'.'emp' from 'ssafy';
```

- 모든 DB의 부여된 권한을 모두 회수하는 경우

```
revoke all on *.* from 'ssafy';
```

### MySQL 계정 삭제

```
drop user '<아이디>'
```

- 예시

```
drop user 'ssafy'
```



**참고**

설치한 툴에서 `unable to load authentication plugin 'caching_sha2_password'` 라는 에러가 발생하는 경우

- MySQL 8.0.4부터 MySQL 서버의 기본 인증 플러그인이 `mysql_native_password`에서 `caching_sha2_password`로 변경되었기 때문이다.

- 해결방법

  ```
  ALTER USER 'ssafy'@'%' IDENTIFIED WITH mysql_native_password BY 'ssafy';
  ```

  



## 4. Node JS

**설치하기**

- [사이트](https://nodejs.org/ko/)에서 LTS 버전 다운로드

- 설치 확인을 해본다.

  ```bash
  node -v
  node --version
  ```

  ```bash
  npm -v
  ```



## 5. @VUE/CLI

- [npmjs 사이트](https://www.npmjs.com/)에서 검색창에 `@vue/cli` 검색 후 설치 명령어 확인

**설치하기**

```bash
npm install -g @vue/cli
```

- 설치 확인을 해본다.

```bash
vue -V
vue --version
```



***Copyright* © 2020 Song_Artish**