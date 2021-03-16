# Linux 명령어

2021.03.16

---

[TOC]



---



## Linux

> Linux®는 리눅스 커널에 기반을 둔 오픈소스 유닉스 계열 운영체제(OS)이다.



## 간단한 명령어

### 1. File & Directory

**1.1 ls**

- list information about file

- :ballot_box_with_check: cmd에서 `ls` 명령어를 사용하려는 경우 아래의 명령어로 등록할 수 있다.

  ```shell
  doskey ls=dir
  ```

**1.2 cd**

- change directory

**1.3 mkdir**

- 디렉토리 생성

```shell
mkdir <폴더명>
```

**1.4 rmdir**

- 디렉토리 삭제
- 단, 하위 디렉토리나 파일 존재 시에는 실행되지 않는다.

**1,5 rm -r**

- 디렉토리 전부 삭제
- 하위 폴더/파일도 전부 삭제한다.

**1.6 mv**

- 파일 이동

**1.7 cp**

- copy one or more files to another location



### 2. 파일 실행

**2.1 cat**

- 파일 편집 (`concatenate FILE(s), or standard input, to standard output`)

  ```sh
  cat <파일명>
  ```

- **종료할 때**는 `Ctrl + C`

**2.2 vi**

- 파일 편집 (실행모드, 입력모드, 명령모드)

  ```shell
  vi <파일명>
  ```

- 종료할 때는 `Esc` 누르고

  - **저장하고 종료** `:wq` 입력 후 `Enter`
  - **저장하지 않고 종료** `:q!` 입력 후 `Enter`



## PyCharm 사용하기

**설치하기**

> 설치 방법에 대한 내용은 추가가 필요하다.

**실행하기**

- 먼저 설치한 pycharm 내부의 **bin 폴더**에 들어간다.

  - /pycharm/pycharm-community-2020.3.3/bin

- bin 폴더 내에서 아래의 명령어를 입력하면 PyCharm이 실행된다.

  ```shell
  sh pycharm.sh
  ```

  

***Copyright* © 2021 Song_Artish**