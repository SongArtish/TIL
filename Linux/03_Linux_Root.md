# Ubuntu 관리자 권한

---

[TOC]

---



## 경로

### 절대 경로

- 루트폴더(`/`)로부터의 절대적인 위치
- `\home\[username]\helloWorld\hello\`

### 상대 경로

- 현재 위치로부터의 상대적인 위치
- 현재 위치한 폴더는 점(`.`)으로 표현
- 상위 폴더는 두개의 점(`..`)으로 표현



## 관리자(root) 권한

### whoami: 현재 사용자 확인

```shell
$ whoami
```

### sudo: 관리자 권한 획득

superuser do, substitute user do

```shell
$ sudo <명령어>
```

> `sudo` 명령어는 유닉스 및 유닉스 계열 운영 체제에서, 다른 사용자의 보안 권한, 보통 superuser로서 프로그램을 구동할 수 있도록 하는 프로그램이다



***Copyright* © 2022 Song_Artish**