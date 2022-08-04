# Git 명령어

---

[TOC]

---



## Git Init

> `git init`을 통해 해당 repository를 git으로 관리해준다.

```bash
$ git add .
$ git commit -m ""
```



## Git Commit

> `commit`은 Git 저장소에 디렉토리에 있는 모든 파일에 대한 스냅샷을 기록하는 것이다.

```bash
$ git commit -m "<메시지>"
```

- commit 메시지 내용을 수정하는 경우 아래의 명령어를 사용한다.

```bash
$ git commit --amend
```



## Git Log

> `git log`를 확인하면 현재 master라는 기본 가지(분기점)에 저장되어 있다는 것을 알 수 있다.

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



## Git Rebase

> 해당 branch를 기준(`Base`)으로 commit을 재정렬하는 과정

- rebase를 할 브랜치로 이동한다.
- master로 rebase를 할 경우 아래와 같이 입력한다.

```bash
$ git rebase master
```

- 아래의 코드로 A 브랜치를 B 브랜치 위치로 진행 시킬 수도 있다.

```bash
$ git rebase <A> <B>
```

:ballot_box_with_check: **Rebase UI 열기**

- 현재 위치에서 4단계 위까지 우선 복사한다.

```bash
$ git rebase -i HEAD~4
```

- 열린 UI 창에서 복사할 commit 기록과 순서를 선택한다.



## Git Cherry-Pick

> 현재 위치(`HEAD`) 아래에 있는 일련의 commit에 대한 복사본을 만든다.

```bash
$ git cherry-pick <Commit1> <Commit2> <...>
```

- :ballot_box_with_check: 여기서 각각의 commit 사이에는 `,`(쉼표)가 아닌 공백으로 구분해준다!



## Git Tag

> 태그란, commit을 참조하기 쉽도록 알기 쉬운 이름을 붙이는 것

```bash
$ git tag <태그명> <위치>
```



## Git Remote

> 원격 저장소와 관련된 다양한 명령어에 대해 다룬다.

- 원격 저장소 확인

```bash
$ git remote show
```

- 특정 원격 저장소 정보 확인

```bash
$ git remote show <저장소 이름>
```

- 원격저장소 제거

```bash
$ git remote rm <저장소 이름>
```



## Git Stash

아직 commit하지 않은 작업을 스택에 임시로 저장한다.

```bash
git stash
```



***Copyright* 2021 © Song_Artish**