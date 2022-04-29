# Git 브랜치

---

[TOC]

---



## Overview

branch는 나무가지라는 의미로 코드의 분기를 의미한다. 효율적인 협업과 분업을 위한 도구로써 사용한다.



## 브랜치 생성

```bash
$ git branch <브랜치명>
```



## 브랜치 확인

> 현재 생성한 branch의 목록을 확인할 수 있다.

```bash
$ git branch
```



## 브랜치 이동

> 해당 branch로 git 파일을 이동시킬 수 있다.

```bash
$ git checkout <브랜치명>
```

:ballot_box_with_check: `checkout` 명령어가 현재는 `switch(브랜치 변경)`와 `restore(변경사항 복원)`으로 변경되었다.



## 브랜치 병합

> 현재 branch와 대상 branch를 병합한다.

```bash
$ git merge <브랜치명>
```

:white_check_mark: `예시: B 브랜치를 A 브랜치로 병합하는 경우`

- 우선, 병합 브랜치인 A로 이동한다.

```bash
$ git checkout A
```

- 이후, 대상 브랜치인 B에 대한 병합 명령어를 입력한다.

```bash
$ git merge B
```



## 브랜치 삭제

```bash
$ git branch -d <브랜치명>
```



## 브랜치 리스트 업데이트

- 원격 저장소의 branch 리스트를 업데이트 한다.

```bash
$ git remote update origin --prune
```



## 모든 브랜치 리스트 조회

- To show all local and remote branches that (local) Git knows about

```bash
$ git branch -a
```



***Copyright* 2021 © Song_Artish**