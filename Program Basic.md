# 프로그램 기본 사용법

2020.07.17.



## 1. Python



## 2. VS Code

### 1)  기본 shell을 Git Bash로 변경하기

​	(1) `Ctrl+Shift+P`를 입력하면 `>`로 시작하는 입력창이 나타난다.

​	(2) 검색창에서 `Select Default Shell`을 검색하여 클릭한다.

​	(3) 선택옵션 창에서 `Git Bash`를 클릭한다.

​	(4) `Ctrl + J` 혹은 `Ctrl+backtick`을 누르고 terminal에서 기본값이 `bash`로 바뀐 것을 확인한다.



## 3. Git

### 1) 나의 정보를 git에 등록하기 (git-bash 환경설정)

​	(1)  이메일 등록

- `git config --global user.email "bulgen@naver.com"`입력하고 `Enter`

- `git config --global user.email`를 입력하고 `Enter`로 확인

​	(2) 이름 등록

- `git config --global user.name "Song-Artish"` 입력하고 `Enter`

- `git config --global user.name`을 입력하고 `Enter`로 확인

### 2) github 업로드하기

​	<1> add	

​	(1) github에서 repository의 Code 주소 복사

​	(2) git-bash에서 `mkdir TIL` 명령어로 TIL이라는 이름의 폴더 생성

​	(3) `pwd`라는 명령어로 현재 위치 확인      *# print working directory*

​	(4) `cd TIL`이라는 명령어로 TIL의 위치로 이동

​	(5) `git init`이라는 명령어로 현재 위치를 'master'로 설정

​	(6) `git remote add origin 주소`입력. paste는 마우스롤 붙이기

​	*(7) `ctrl+L` 혹은 `clear`라는 명령어로 창 clear 가능 :)*

​	*(8) `ls`라는 명령어로 현재 7위치의 리스트 확인하기*

​	(9) 파일 1개만 add하기: `git add 파일명` 입력

​	(10) `git status`로 상태 확인

​	<2> commit

​	(11) `git commit -m "메시지 입력"`으로 git commit 하기

​	(12) `git log`로 현재까지의 버전 확인하기

​	(13) `Esc`누르고 `:q!` 입력하고 `Enter`하면 

​	<3> push

​	(14) `git push origin master` + `Enter`

### 3) 

