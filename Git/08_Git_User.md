# Git 사용자

---

[TOC]

---



## 사용자 등록

- 아래와 같이 git에 기본적인 사용자에 대한 정보를 등록한다.

```bash
$ git config --global user.name <user_name>		# 이름 등록
$ git config --global.user.email <user_email>	# 이메일 등록
```

- 이후 push 요청을 하면 자동으로 로그인 페이지가 나타나서 로그인을 하면 원격저장소를 사용할 수 있다.



## 사용자 변경/제거

> git 등록된 계정 변경/삭제는 다음과 같이 할 수 있다.

### 자격 증명

```markdown
제어판 > 사용자 계정 > Windows 자격 증명 > 일반 자격 증명
```

- 일반 자격 증명에서 git 정보가 저장되어 있으며 `자세히` 버튼을 눌린다.
- 편집을 원하면 `편집` 버튼, 삭제하고 다시 로그인하려면 `제거` 버튼을 누르면 된다.

### 기존 사용자 Gitlab 정보 변경하기

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