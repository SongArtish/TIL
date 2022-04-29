# APT

> Ubuntu의 패키지 매니저

---

[TOC]

---



## Overview

- Ubuntu에는 `apt`라는 패키지 매니저가 내장되어 있다.

```shell
$ apt
```



## 주요 명령어

| 명령어                                  | 기능                               | Desc.                |
| --------------------------------------- | ---------------------------------- | -------------------- |
| `apt update`                            | 패키지 목록 갱신                   | **관리자 권한 필요** |
| `apt list --upgradable`                 | 업그레이드 가능한 패키지 목록 출력 |                      |
| `apt upgrade`                           | 전체 패키지 업그레이드             | **관리자 권한 필요** |
| `apt --only-upgrade install <패키지명>` | 특정 패키지만 업그레이드           | **관리자 권한 필요** |
| `apt install <패키지명>`                | 패키지 설치                        | **관리자 권한 필요** |
| `apt list --installed`                  | 설치된 패키지 보기                 |                      |
| `apt search <검색어>`                   | 패키지 검색                        |                      |
| `apt show <패키지명>`                   | 패키지 정보 확인                   |                      |
| `apt remove <패키지명>`                 | 패키지 삭제                        | **관리자 권한 필요** |

- :ballot_box_with_check: `apt update` 명령어는 설치된 프로그램이 새로운 버전으로 변경되는 것이 아니라 **패키지를 다운로드받을 수 있는 여러 저장소의 최신 정보를 업데이트**한다.



## 관리자 권한 사용

관리자 권한을 사용하는 경우, 명령어 앞에 `sudo`를 입력한다.

```shell
$ sudo apt install <패키지명>
$ sudo apt install wget # 예시
```



## 패키지 예시 :pushpin: 

### wget

URL을 통해 파일을 다운로드 받는 프로그램

```shell
$ wget -O <생성할 파일명> <URL 경로>
```

- :ballot_box_with_check: Ubuntu에서 복사&붙여넣기는 다음의 key를 이용한다.
  - 복사: `Ctrl` + `Shift` + `C`
  - 붙여넣기: `Ctrl` + `Shift` + `V`

### zoom

- [Installing Zoom on Linux](https://support.zoom.us/hc/en-us/articles/204206269-Installing-Zoom-on-Linux#h_89c268b4-2a68-4e4c-882f-441e374b87cb)에서 **Using the terminal** 부분을 참고한다.



***Copyright* © 2022 Song_Artish**