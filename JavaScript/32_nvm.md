# NVM

> Node Version Manager

---

[TOC]

---



## Overview

- `node.js`의 다양한 버전을 관리하는 프로그램
- :warning: Window 환경에서는 nvm을 사용할 수 없다.



## Install

1. nvm 설치

   ```shell
   # ubuntu에서 설치
   $ wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash
   ```

2. 설치 확인

   ```shell
   $ nvm --version
   ```

   - 버전이 잘 나온다면 NVM 설치를 성공한 것이다.

   - :ballot_box_with_check: nvm이 설치되었음에도 `Command 'nvm' not found, did you mean:`과 같은 문구가 발생한다면 아래의 명령어를 입력한다.

     ```shell
     $ source $HOME/.nvm/nvm.sh
     ```

3. node.js 설치

   ```shell
   $ nvm install --lts
   ```

   ```shell
   $ node -v
   ```



## 간단한 사용법

아래의 명령어로 현재 nvm을 통해 설치한 node version을 확인할 수 있다.

```shell
$ nvm ls
```

특정 버전의 node를 설치하고 싶다면 아래 명령어를 사용한다.

```shell
$ nvm install <버전>
# nvm install 12.18.3
```

사용 중인 node version을 다른 버전으로 변경하고 싶을 때는 아래의 명령어를 입력한다.

```shell
$ nvm use <버전>
# nvm use 14.15.5
```



***Copyright* © 2022 Song_Artish**
