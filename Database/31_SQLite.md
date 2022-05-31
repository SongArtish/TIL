# SQLite

*****

[TOC]

*****



## Overview

[SQLite](https://www.sqlitetutorial.net/)는 서버가 아닌 응용 프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스이다. 구글 안드로이드 운영체제에 기본 탑재된 데이터베이스이며, 임베디드 소프트웨어로 활용하거나 오픈소스 프로젝트에서 사용할 수 있다.



## 시작하기

먼저 SQLite를 설치한다.

1. [사이트](https://www.sqlite.org/download.html)에서 dll, tools 2가지 파일 설치
2. 압축풀어서 폴더에 담기
3. 환경변수 PATH 설정

처음에 설치하면 bash에서 다음의 명령어로 sqlite를 실행할 수 있다.

```bash
$ winpty sqlite3
```

다음으로 git-bash에서 기본적인 세팅을 해준다.

```bash
$ vi ~/.bashrc
```

이후 불러온 창에서 다음을 입력한다.

```
alias jp="jupyter notebook"
alias sqlite3="winpty sqlite3"
```

그 후 `Esc` 키를 누르고 해당 창의 제일 밑에 부분에서 `:wq`를 입력하여 설정을 저장하고 종료한다.

```
:wq
```

다음으로 bash창에서 다음을 입력한다.

```bash
$ source ~/.bashrc
```

이 과정을 마치면 `sqlite3`라는 명령어로 SQLite를 실행할 수 있다.

```bash
$ sqlite3
```



## 실행하기

```bash
$ sqlite3
```



## 종료하기

`Ctrl` + `C` * 2번



## <실습> 외부 파일 불러오기

먼저 데이터베이스를 생성한다.

```bash
$ sqlite3 <Database Name>.sqlite3
$ sqlite3 tutorial.sqlite3	// 예시
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

:ballot_box_with_check: 불러온 데이터를 저장할 경우 아래의 명령어를 입력한다.

```sqlite
sqlite> .save data.db data
```

- `data`라는 테이블로 불러온 데이터를 `data.db`라는 파일로 저장한다.



***Copyright* © 2020 Song_Artish**