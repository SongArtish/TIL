# Git Branch

> branch는 나무가지라는 의미로 코드의 분기를 의미한다. 효율적인 협업과 분업을 위한 도구로써 사용한다.

---

[TOC]

---



### `git init`

> `git init`을 통해 해당 repository를 git으로 관리해준다.

```bash
$ git add .
$ git commit -m ""
```

- `git log`를 확인하면 현재 master라는 기본 가지(분기점)에 저장되어 있다는 것을 알 수 있다.

```bash
$ git log --oneline
```



### branch 확인

> 현재 생성한 branch의 목록을 확인할 수 있다.

```bash
$ git branch
```



### branch 생성

```bash
$ git branch <new branch name>
```



### branch 이동

> 해당 branch로 git 파일을 이동시킬 수 있다.

```bash
$ git switch <branch>
```



### branch 삭제

```bash
$ git branch -d <branch name>
```



### `git log`

- 모든 branch의 log를 확인할 수 있다.

```bash
$ git log --all --oneline
```

```bash
$ git log --oneline --all
```

- `--graph` 옵션을 통해서 log를 시각적으로 나타낼 수도 있다.

```bash
$ git log --oneline --all --graph
```





### branch 병합

> 현재 branch와 대상 branch를 병합한다.

```bash
$ git merge <branch name>
```



### <참고> 이상적인 branch name

- master : 제품으로 출시될 수 있는 branch
- develop : 다음 출시 버전을 개발하는 branch
- feature : 기능을 개발하는 branch
- release : 이번 출시 버전을 준비하는 branch
- hotfix : 출시 버전에서 발생한 버그를 수정하는 branch



***Copyright* © Song_Artish**