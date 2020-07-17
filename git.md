# Git

> Git은 분산버전관리시스템(DVCS, Distributed Version Control System)이다. 소스코드의 버전 및 이력을 관리할 수 있다.



## 준비하기

윈도우에서 git을 활용하기 위해서 git bash를 설치한다.

git을 활용하기 위해서 GUI(Graphic User Interface) 툴인 `source tree`, `github desktop` 등을 활용할 수도 있다. (Git-bash는 CLI[Command-line Interface]이다.)

초기 설치를 완료한 이후에 컴퓨터에 author 정보를 입력한다.

```bash
$ git config --global user.name {user name}
$ git config --global.user.email {user email}
```

- 예시) `git config --global user.email "bulgen@naver.com"`

  ​		 `git config --global user.name "Song-Artish"`



## 로컬 저장소(repository) 활용하기

### 1. 저장소 초기화

```bash
$ git init	# 해당 폴더를 git 저장소로 초기화
Initialized empty Git repository in C:/Users/bulgen/.git/	#예시
```

- `.git`폴더가 생성되며, 여기에 git과 관련된 모든 정보가 저장된다.
- git bash에 `(master)`라고 표시되는데, 이는 현재 폴더가 git으로 관리되고 있다는 뜻이며, `master`라는 branch에 있다는 뜻이다.

### 2. `add` 

`working directory`, 즉 작업 공간에서 변경된 사항을 이력으로 저장하기 위해서는 반드시 `staging area`를 거쳐야 한다.

```bash
$ git add {파일/폴더}    # 특정 파일/폴더를 stage로 올리기
$ git add markdown.md   # 파일 (확장자명 포함)
$ git add images/       # 폴더 (뒤에 '/'가 붙으면 폴더이다.)
$ git add .			    # 현재 디렉토리에 있는 모든 파일과 폴더
```

- markdown.md 파일이 폴더에 새롭게 작성되었으나, 아직 git으로 관리되지 않고, `add` 전 상태

``` bash
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        markdown.md
        
nothing added to commit but untracked files present (use "git add" to track)
```

- markdown.md 파일을 add 후에 staging area로 올라간 상태

```bash
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   markdown.md
```

### 3. `commit`

commit은 **이력을 확정짓는 명령어**로, 해당 시점의 스냅샷을 기록한다.

커밋시에는 반드시 메시지를 작성해야 하며, <u>메시지는 변경사항을 알 수 있도록 명확하게 작성한다.</u>

```bash
$ git commit -m "마크다운 정리"
[master (root-commit) 6c84015] 마크다운 정리
 1 file changed, 170 insertions(+)
 create mode 100644 markdown.md				# 최초 커밋시의 메시지
```

커밋 이후에는 아래의 명령어를 통해 지금까지 작성된 커밋 이력을 확인한다.

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

커밋은 해시값을 바탕으로 구분된다.



## 원격 저장소(remote repository) 활용하기

원격 저장소 기능을 제공하는 다양한 서비스 중에 github을 기준으로 설명한다.

### 0. 준비사항

- Github에 repository 생성



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



### 2. `push` - 원격 저장소로 업로드

```bash
$ git push origin master
```

`origin`이라는 이름의 원격 저장소로 commit 기록들을 업로드한다.

이후 변경사항이 생길 때마다, `add`, `commit`, `push`를 반복한다.