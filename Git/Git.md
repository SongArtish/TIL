# Git



---

[TOC]

---



## Git 구조

![Git Structure](img/git_structure.jfif)

(출처: https://ndb796.tistory.com/187)



git flow

develop release master 나눠서 하는 형상관리 전략?0?



- commit
- branch
- checkout
- cherry-pick
- reset
- revert
- rebase
- merge



트리공유

export tree 

import tree



학습자료

build level

import level



## Main

## 1. Commit

### 1.1 Git Commit

> `commit`은 Git 저장소에 디렉토리에 있는 몯ㄴ 파일에 대한 스냅샷을 기록하는 것이다.

```bash
$ git commit
```



### 2. Git Branch

**브랜치 생성**

```bash
$ git branch <브랜치명>
```

**브랜치 이동**

```bash
$ git checkout <브랜치명>
```

**브랜치 병합**

- 병합할 브랜치로 이동한다.

```bash
$ git merge <브랜치명>
```



### 3. Git Rebase

> branch를 베이스(Base)로 commit을 재정렬하는 과정

- rebase를 할 브랜치로 이동한다.
- master로 rebase를 할 경우 아래와 같이 입력한다.

```bash
$ git rebase master
```

- 아래의 코드로 A 브랜치를 B 브랜치 위치로 진행 시킬 수도 있다.

```bash
$ git rebase <A> <B>
```





## Commit 트리 이동하기

`HEAD`

> 현재 checkout된 commit (현재 작업중인 commit)

**HEAD 분리하기**

```bash
$ git checkout <해당 해시값>
```





**상대참조**

- 한번에 한 커밋 위로 움직이는 `^`
- 한번에 여러 커밋 위로 올라가는 `~<num>`

- master의 부모로 이동하기

```bash
$ git checkout master^
```

- HEAD의 부모로 이동하기

```bash
$ git checkout HEAD^
```

- 아래와 같이 조부모로 이동할 수도 있다.

```bash
$ git checkout HEAD^^
```



강제로 이동

- master를 `HEAD`의 3칸 위로 이동시킬 경우

```bash
$ git branch -f master HEAD~3
```



작업 되돌리기

- 현재의 작업을 삭제하고 이전 작업으로 되돌린다.

```bash
$ git reset
```

- 현재의 작업을 남기고 이전 작업을 추가한다.

```bash
$ git revert
```



Git Cherry-pick

> 현재 위치(`HEAD`) 아래에 있는 일련의 commit에 대한 복사본을 만든다.

```bash
$ git cherry-pick <Commit1> <Commit2> <...>
```

- :ballot_box_with_check: 여기서 각각의 commit 사이에는 `,`(쉼표)가 아닌 공백으로 구분해준다!



Git Interactive Rebase

리베이스 UI 열기

- 현재 위치에서 4단계 위까지 우선 복사한다.

```bash
$ git rebase -i HEAD~4
```

- 열린 UI 창에서 복사할 commit 기록과 순서를 선택한다.



commit 내용 정정하기

```bash
$ git commit --amend
```



Git Tag

> 태그란, 커밋을 참조하기 쉽도록 알기 쉬운 이름을 붙이는 것

```bash
$ git tag <태그명> <위치>
```



Git Describe

> 태그와 커밋 횟수, 축약된 커밋 이름으로 사람이 읽고 구분할 수 있는 버전 정보를 알려준다.

- 실제로 해보니 작동하지는 않는다.

```bash
$ git describe
$ git describe <브랜치명>
```

