# Git

> Git은 분산버전관리시스템(DVCS, Distributed Version Control System)으로 소스코드의 버전 및 이력을 관리할 수 있다.

---

[TOC]

---



## 기초 사용법

> 기초 사용법에서는 git을 통해서 간단하게 버전을 관리할 수 있는 방법에 대해서 다룬다.

### 준비하기

- 윈도우에서 git을 활용하기 위해서 `git bash`를 설치한다.

> `git-bash`는 CLI(Command-line Interface)이다. git을 활용하기 위해서 GUI(Graphic User Interface) 툴인 `source tree`, `github desktop` 등을 활용할 수도 있다.

- 초기 설치를 완료한 이후에 컴퓨터에 author 정보를 입력한다.

```bash
$ git config --global user.name <user_name>		# 이름 등록
$ git config --global.user.email <user_email>	# 이메일 등록
```

- 예시) `git config --global user.email "bulgen@naver.com"`

  ​		 `git config --global user.name "Song-Artish"`

- 아래의 명령어를 사용하여 현재 등록된 유저 정보를 확인할 수도 있다.

```bash
$ git config --global user.name
$ git config --global.user.email
```



### 로컬 저장소(repository) 활용하기

> ```markdown
> 1. git init
> 2. git add
> 3. git commit
> ```

1. **`init`**

저장소를 초기화하는 과정이다.

```bash
$ git init
```

- `.git`폴더가 생성되며, 여기에 git과 관련된 모든 정보가 저장된다.

- git bash에 `(master)`라고 표시되는데, 이는 현재 폴더가 git으로 관리되고 있다는 뜻이며, `master`라는 branch에 있다는 뜻이다.

- :ballot_box_with_check: git 저장소를 제거할 때는 해당 폴더에서 git bash를 실행하고 다음의 명령어를 입력한다.

  ```bash
  $ rm -rf .git
  ```

---

2. **`add`** 

`working directory`, 즉 작업 공간에서 변경된 사항을 이력으로 저장하기 위해서는 반드시 `staging area`를 거쳐야 한다.

```bash
$ git add {파일/폴더}
```

```bash
# 예시
$ git add markdown.md   # 파일 (확장자명 포함)
$ git add images/       # 폴더 (뒤에 '/'가 붙으면 폴더이다.)
$ git add .			    # 현재 디렉토리에 있는 모든 파일과 폴더
```

- `git status`라는 명령어를 통해 새롭게 작성/수정된 파일이 git으로 관리되고 있는지를 확인할 수 있다.

``` bash
$ git status
```

- git에 등록된 파일/폴더를 삭제하고 싶을 경우, `git rm -r --cached <파일/폴더명>`라는 명령어를 입력한다.

---

3. **`commit`**

commit은 **이력을 확정짓는 명령어**로, 해당 시점의 스냅샷을 기록한다.

커밋시에는 반드시 메시지를 작성해야 하며, <u>메시지는 변경사항을 알 수 있도록 명확하게 작성한다.</u>

```bash
$ git commit -m "마크다운 정리"
[master (root-commit) 6c84015] 마크다운 정리
 1 file changed, 170 insertions(+)
 create mode 100644 markdown.md				# 최초 커밋시의 메시지
```

- 커밋 메시지 변경시, `git commit --amend`라는 명령어를 입력한다. 단, 되도록이면 사용하지 않는 것이 좋다.

커밋 이후에는 아래의 명령어를 통해 지금까지 작성된 커밋 이력을 확인한다. 커밋은 해시값을 바탕으로 구분된다.

```bash
$ git log
commit 1aad18d102376b6b77631d93135c393efcd28b4d (HEAD -> master, origin/master)
								# commit 뒤에는 commit의 기록을 나타내는 `해시값`
Author: Song-Artish <bulgen@naver.com>
Date:   Fri Jul 17 11:49:05 2020 +0900

    마크다운 정리
    
$ git loge --oneline							     # 이력을 간단하게 보기 위한 명령어
1aad18d (HEAD -> master, origin/master) 마크다운 정리	 # 해시값의 7자리까지만 나타냄
```



### 원격 저장소(remote repository) 활용하기

> 원격 저장소 기능을 제공하는 다양한 서비스 중에 Github을 기준으로 설명한다. Github에 respository를 생성한 후에 아래의 절차를 진행한다.
>
> ```markdown
> - git remote add (저장소 초기화)
> - git push (원격 저장소로 업로드)
> - git pull (원격 저장소에서 불러오기)
> ```

1. `remote add`

원격 저장소를 등록한다.

```bash
$ git remote add origin {github url}
```

- 원격저장소(remote)로 origin이라는 이름으로 github url을 등록(add)한다.
- 등록된 원격 저장소를 보기 위해서는 아래의 명령어를 활용한다.

```bash
$ git remote -v
origin  https://github.com/Song-Artish/TIL.git (fetch)
origin  https://github.com/Song-Artish/TIL.git (push)
```

---

2. `push`

원격 저장소로 업로드한다.

```bash
$ git push origin master
```

`origin`이라는 이름의 원격 저장소로 commit 기록들을 업로드한다.

이후 변경사항이 생길 때마다, `add`, `commit`, `push`를 반복한다.

---

3. `pull`

원격 저장소로부터 불러온다.

```bash
$ git pull origin master
$ git clone <주소>		# 최초로 복사할 경우에는 clone 사용
```

`origin`이라는 이름의 원격 저장소로부터 새로운 commit 기록들을 불러온다.



## Git Structure

> Git의 구조는 다음과 같다.

```markdown
## git 공간

- working dir: 실제 작업공간
- staging area: 명령어를 입력했을 때 임시로 저장이 되는 공간
- local repository: 명령어를 입력했을 때 버전이 기록되는 공간
```

![Git Structure](img/git_structure.jfif)

`(출처: https://ndb796.tistory.com/187)`



## Git Flow

> `develop` `release` `master` 등으로 나눠서 하는 형상관리 전략

Git-flow는 총 5가지의 브랜치를 사용해서 운영을 한다.

- **master** : 제품으로 출시될 수 있는 branch
- **develop** : 다음 출시 버전을 개발하는 branch
- **feature** : 기능을 개발하는 branch
- **release** : 이번 출시 버전을 준비하는 branch
- **hotfix** : 출시 버전에서 발생한 버그를 수정하는 branch

> **master**와 **develop**가 중요한 **매인 브랜치**이고 나머지는 필요에 의해서 운영하는 브랜치라고 할 수 있다.

![git_flow](img/git_flow.png)

`(출처: https://uxgjs.tistory.com/183 [UX 공작소])`

- 참고링크: [배달의링크 Git Flow](https://woowabros.github.io/experience/2017/10/30/baemin-mobile-git-branch-strategy.html)



## Git Init

> `git init`을 통해 해당 repository를 git으로 관리해준다.

```bash
$ git add .
$ git commit -m ""
```



## Commit

> `commit`은 Git 저장소에 디렉토리에 있는 모든 파일에 대한 스냅샷을 기록하는 것이다.

```bash
$ git commit -m "<메시지>"
```

### 로그 

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

### 내용 정정

```bash
$ git commit --amend
```





## Git Branch

> branch는 나무가지라는 의미로 코드의 분기를 의미한다. 효율적인 협업과 분업을 위한 도구로써 사용한다.

### 브랜치 생성

```bash
$ git branch <브랜치명>
```

### 브랜치 확인

> 현재 생성한 branch의 목록을 확인할 수 있다.

```bash
$ git branch
```

### 브랜치 이동

> 해당 branch로 git 파일을 이동시킬 수 있다.

```bash
$ git checkout <브랜치명>
```

:ballot_box_with_check: `checkout` 명령어가 현재는 `switch(브랜치 변경)`와 `restore(변경사항 복원)`으로 변경되었다.

### 브랜치 병합

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

### 브랜치 삭제

```bash
$ git branch -d <브랜치명>
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



## HEAD

> 현재 checkout된, 즉 현재 작업중인 commit.

### HEAD 분리하기

```bash
$ git checkout <해당 해시값>
```

### 상대참조 이동

:ballot_box_with_check: **상대참조**

|     기호     |             설명              |          예시           |        예시결과        |
| :----------: | :---------------------------: | :---------------------: | :--------------------: |
|     `^`      |  한 번에 한 commit 위로 이동  | `git checkout master^^` | master의 조부모로 이동 |
| **`~<num>`** | 한 번에 여러 commit 위로 이동 |  `git checkout HEAD~3`  | HEAD의 3단계 위로 이동 |

### 강제 이동

- master를 `HEAD`의 3칸 위로 이동시킬 경우

```bash
$ git branch -f master HEAD~3
```

### 작업 되돌리기

- 현재의 작업을 삭제하고 이전 작업으로 되돌린다.

```bash
$ git reset
```

- 현재의 작업을 남기고 이전 작업을 추가한다.

```bash
$ git revert
```



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



## Git User

### 사용자 등록

- 아래와 같이 git에 기본적인 사용자에 대한 정보를 등록한다.

```bash
$ git config --global user.name <user_name>		# 이름 등록
$ git config --global.user.email <user_email>	# 이메일 등록
```

- 이후 push 요청을 하면 자동으로 로그인 페이지가 나타나서 로그인을 하면 원격저장소를 사용할 수 있다.



### 사용자 변경/제거

> git 등록된 계정 변경/삭제는 다음과 같이 할 수 있다.

**자격 증명**

```markdown
제어판 > 사용자 계정 > Windows 자격 증명 > 일반 자격 증명
```

- 일반 자격 증명에서 git 정보가 저장되어 있으며 `자세히` 버튼을 눌린다.
- 편집을 원하면 `편집` 버튼, 삭제하고 다시 로그인하려면 `제거` 버튼을 누르면 된다.

**기존 사용자 Gitlab 정보 변경하기**

- 기존 사용자 정보를 bash 창에서 확인해본다.

```bash
$ git config --global --list
```

- 새로 입력할 이름을 입력한다.

```bash
$ git config --global user.name <사용자명>
```

- 그리고 `gitlab 아이디`를 이메일로 등록한다.

```bash
$ git config --global user.email <gitlab아이디>
```

- 이후 `git push`를 하면 git의 로그인 페이지가 뜬다.



***Copyright* 2021 © Song_Artish**