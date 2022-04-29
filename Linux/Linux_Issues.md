# Linux 이슈

```
해결한 Linux 이슈를 정리한다.
```

---

[TOC]

---



### natuilus 실행 에러

ubuntu에서 nautilus를 실행하려고 명령어를 입력했다.

```shell
$ nautilus .
Command 'nautilus' not found, but can be installed with:
sudo apt install nautilus
```

그래서 nautilus를 설치하기 위해 명령어를 입력했다.

```shell
$ sudo apt install nautilus
E: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?
```

이를 위해 `apt-get`을 업데이트하고 다시 설치 명령어를 입력하니 정상적으로 `nautilus`가 설치되었다.

```shell
$ sudo apt-get update
$ sudo apt install nautilus
```

하지만, 설치 완료 후 `nautilus`를 실행하니 다시 오류가 발생했다.

```
$ nautilus .
Unable to init server: Could not connect: Connection refused
(nautilus:2371): Gtk-WARNING **: 09:44:13.185: cannot open display:
```

:question::question::question:



***Copyright* © 2022 Song_Artish**