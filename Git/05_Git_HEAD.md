# Git HEAD

---

[TOC]

---



## Overview

`HEAD`는 현재 checkout된, 즉 현재 작업중인 commit을 의미한다.



## HEAD 분리하기

```bash
$ git checkout <해당 해시값>
```



## 상대참조 이동

|     기호     |             설명              |          예시           |        예시결과        |
| :----------: | :---------------------------: | :---------------------: | :--------------------: |
|     `^`      |  한 번에 한 commit 위로 이동  | `git checkout master^^` | master의 조부모로 이동 |
| **`~<num>`** | 한 번에 여러 commit 위로 이동 |  `git checkout HEAD~3`  | HEAD의 3단계 위로 이동 |



## 강제 이동

- master를 `HEAD`의 3칸 위로 이동시킬 경우

```bash
$ git branch -f master HEAD~3
```



## 작업 되돌리기

- 현재의 작업을 삭제하고 이전 작업으로 되돌린다.

```bash
$ git reset
```

- 현재의 작업을 남기고 이전 작업을 추가한다.

```bash
$ git revert
```



***Copyright* 2021 © Song_Artish**