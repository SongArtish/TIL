# Linux 명령어

2021.03.16

---

[TOC]

---



### pwd: 현재 위치 확인

print working directory

```shell
$ pwd
```

### mkrid: 새로운 폴더 생성

make directions

```shell
$ mkdir <폴더명>
```

### ls: 특정 폴더에 포함된 파일/폴더 확인

list

```shell
$ ls
```

| 자주 사용하는 옵션     | desc.                                       |
| ---------------------- | ------------------------------------------- |
| `ls -l`                | 폴더/파일의 포맷을 표현                     |
| `ls -a`                | list all (숨어있는 폴더/파일 포함하여 출력) |
| `ls -al` 또는 `ls -la` |                                             |

- `ls -l` 명령어를 입력하면 아래와 같이 표시된다. (예시)

  ```
  drwxr-xr-x #생략
  -rw-r--r-- # 생략
  ```

  - 여기서 `d`로 시작하는 것은 폴더를, `-`로 시작하는 것을 파일을 나타낸다.

- :pushpin: cmd에서 `ls` 명령어를 사용하려는 경우 아래의 명령어로 등록할 수 있다.

  ```shell
  $ doskey ls=dir
  ```

### nautilus: GUI 탐색기 실행

```shell
$ nautilus .
```

### explorer.exe: GUI 디렉토리 열기

```shell
$ explorer.exe .
```

- 별다른 패키지를 설치하지 않고 사용할 수 있다.

### cd: 폴더 이동

change directory

```shell
$ cd <폴더명>
```

### touch: 파일 생성

```shell
$ touch <파일명>
$ touch hi.txt
```

- 현재 디렉토리에 `hi`라는 이름의 텍스트 파일이 생성된다.

  - Ubuntu에서는 `gedit`이라는 텍스트 편집기가 사용된다.

- :ballot_box_with_check: 텍스트 파일에 데이터를 입력하기 위해서는 아래의 명령어를 사용한다.

  ```shell
  $ echo '<데이터>' > <파일명>
  $ echo 'this is an sample text.' > hi.txt
  ```

### vi: 파일 편집

```shell
$ vi <파일명>
```

- 3가지의 모드로 파일을 편집한다.
  1. 실행모드
  2. 입력모드
  3. 명령모드
- 아래의 명령어로 **종료**할 수 있다.
  - 저장 후 종료: `Esc` 를 누르고 `:wq` 입력 후 `Enter`
  - 저장하지 않고 종료: `Esc`를 누르고 `:q!` 입력 후 `Enter`

### cat: 파일의 내용을 터미널에 출력

concatenate FILE(s), or standard input, to standard output

```shell
$ cat <파일명>
$ cat hi.txt
```

- 종료할 때는 `Ctrl + C`를 사용한다.

### rm: 폴더/파일 삭제

remove

```shell
$ rm <파일명>
$ rm -rf <폴더>
```

- 옵션 `r`: recursive. 디렉토리를 전부 삭제. 하위 폴더/파일도 모두 삭제.
- 옵션 `f`: force. 질문을 받지 않고 지울 때 사용.

### rmdir: 디렉토리 삭제

```shell
$ rmdir <폴더>
```

- 단, <u>하위 디렉토리나 파일 존재 시</u>에는 실행되지 않는다.

### mv: 폴더/파일 이름 변경 혹은 위치 이동

move

```shell
$ mv <폴더/파일명> <이동 폴더>/
$ mv bye.txt bye/
```

```shell
$ mv <폴더/파일명> <변경 폴더/파일명>
```

### cp: 폴더/파일 복사

```shell
$ cp <원본 파일명> <복사할 파일명>
$ cp bye.txt hello.txt
```

```shell
$ cp -rf <원본 폴더> <복사할 폴더>
```



## 도움말

각 명령어에 포함된 옵션은 `명령어 이름만 입력`하거나 `-h` 또는 `--help`와 같은 옵션을 통해 확인할 수 있다.



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