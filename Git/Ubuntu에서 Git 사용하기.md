# Ubuntu에서 Git 사용하기

---

[TOC]

---



## Git 설치

터미널을 열고 아래 명령어를 입력한다.

```shell
$ sudo apt install git
```

정상적으로 설치되었는지 확인한다.

```shell
$ git --version
```



## Git 환경설정

사용자 이름과 이메일 주소를 설정한다.

```shell
$ git config --global user.name "<사용자명>"
$ git config --global user.email "<이메일 주소>"
```

Git에서 commit 메시지를 기록할 때, 특히 merge commit 확인 메시지가 나올 때 텍스트 에디터가 열린다. 기본 값으로는 `vi` 텍스트 에디터가 열리는데, 아래의 명령어로 변경할 수 있다. (nano로 변경)

```shell
$ git config --global core.editore nano
```



## SSH 등록

github에서 ssh 공개키(비대칭키 중 하나)를 등록한다.

### 1. SSH 키 생성

```shell
$ ssh-keygen
```

- 3번의 Enter를 누르면 성공적으로 키가 생성된다.

위 명령어는 `~/.ssh./`에 2개의 파일 `id_rsa`와 `id_rsa.pub`를 생성한다. 이 2개의 파일은 ssh 키 페어라고 하며, 이 중 `id_rsa.pub`는 누구에게나 공개해도 되는 **공개키(Public Key)**라고 한다. 그리고 `id_rsa`는 **개인키(Private Key)** 또는 **비밀키(Secret Key)**라고 한다.

### 2. Public Key 복사

아래의 명령어를 프로프트에 입력하고, 표시되는 공개키를 복사한다.

```shell
cat ~/.ssh/id_rsa.pub
```

### 3. Github에 등록

Github로 이동하여 Settings > SSH and GPG keys > SSH keys > New SSH key에서 복사한 key를 추가한다.



***Copyright* © 2022 Song_Artish**