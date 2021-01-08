# Git 기초

> Git은 분산버전관리시스템(DVCS, Distributed Version Control System)으로 소스코드의 버전 및 이력을 관리할 수 있다.

```한국어
git 공간
- working dir: 실제 작업공간
- staging area: 명령어를 입력했을 때 임시로 저장이 되는 공간
- local repository: 명령어를 입력했을 때 버전이 기록되는 공간
```

---

[TOC]

---



## 준비하기

윈도우에서 git을 활용하기 위해서 git bash를 설치한다.

 git-bash는 CLI(Command-line Interface)이다. git을 활용하기 위해서 GUI(Graphic User Interface) 툴인 `source tree`, `github desktop` 등을 활용할 수도 있다.

초기 설치를 완료한 이후에 컴퓨터에 author 정보를 입력한다.

```bash
$ git config --global user.name {user name}		# 이름 등록
$ git config --global.user.email {user email}	# 이메일 등록
```

- 예시) `git config --global user.email "bulgen@naver.com"`

  ​		 `git config --global user.name "Song-Artish"`

- 뒤에 `{}` 항목을 빼고 입력하면 현재 등록 정보를 확인할 수 있다.



## 로컬 저장소(repository) 활용하기

### 1. 저장소 초기화

```bash
$ git init
```

- `.git`폴더가 생성되며, 여기에 git과 관련된 모든 정보가 저장된다.
- git bash에 `(master)`라고 표시되는데, 이는 현재 폴더가 git으로 관리되고 있다는 뜻이며, `master`라는 branch에 있다는 뜻이다.

> git 저장소를 제거할 때는 해당 폴더에서 git bash를 실행하고 다음의 명령어를 입력한다.
>
> ```bash
> $ rm -rf .git
> ```

---

### 2. `add` 

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

### 3. `commit`

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



## 원격 저장소(remote repository) 활용하기

원격 저장소 기능을 제공하는 다양한 서비스 중에 Github을 기준으로 설명한다. Github에 respository를 생성한 후에 아래의 절차를 진행한다.



### 1. 원격 저장소 등록

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

**원격 저장소**

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

---

### 2. `push` - 원격 저장소로 업로드

```bash
$ git push origin master
```

`origin`이라는 이름의 원격 저장소로 commit 기록들을 업로드한다.

이후 변경사항이 생길 때마다, `add`, `commit`, `push`를 반복한다.

---

### 3. `pull` - 원격 저장소로부터 불러오기

```bash
$ git pull origin master
$ git clone <주소>		# 최초로 복사할 경우에는 clone 사용
```

`origin`이라는 이름의 원격 저장소로부터 새로운 commit 기록들을 불러온다.



***Copyright* © Song_Artish**