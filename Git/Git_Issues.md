# git 이슈

> git 관련 이슈를 정리한다.

---

[TOC]

---



## 최초 등록시의 git push stuck 현상

> 최초 깃 등록시, git push 명령어를 입력하면 작업이 멈추는 현상이 계속해서 반복되었다.

- 눈에 보이는 점은 git bash에서 github에 로그인이 되지 않은 상태에서, clone이 되며
- `git push` 명령어를 입력해도 github 로그인 창이 나타나지 않았다.
- `자격 증명 관리자`에서도 github 관련 정보가 등록되어 있지 않았다.

**해결 방안**

- `자격 증명 관리자`에 들어가서 직접 github credentials를 직접 입력하였다.
- `인터넷 또는 네트워크 주소`
  - `git:https://github.com`
- 사용자 이름(아이디) 및 암호 입력



## Permission denied (publickey)

> [블로그](https://lasdri.tistory.com/809)를 참고하였다.

- 내 git repository를 clone하려고 하는데 아래의 오류가 발생하였다.

  ```markdown
  Warning: Permanently added the RSA host key for IP address '15.164.81.167' to the list of known hosts.
  git@github.com: Permission denied (publickey).
  fatal: Could not read from remote repository.
  
  Please make sure you have the correct access rights
  and the repository exists.
  ```

**github 접속**

- `github > setting > SSH and GPG keys`에 들어가서 `New SSH key` 버튼을 클릭한다.

**SSH 키 생성**

- git bash를 실행하여 아래의 명령어를 작성한다.

  ```bash
  ssh-keygen -t rsa -b 4096 -C "email@email.com"
  ```

- 아래의 query에서 `Enter`를 누른다.

  ```bash
  Enter file in which to save the key (/c/Users/사용자/.ssh/id_rsa):
  ```

- 아래 query가 나타나면 임의의 비밀번호를 입력하고 엔터를 누른다. 다음으로 비밀번호 재입력을 한다.

  ```bash
  Enter passphrase (empty for no passphrase):
  ```

- 완료가 되면 콘솔에 파일이 생성된 경로가 표시되며 해당 폴더로 이동하여 `id_rsa.pub` 파일을 메모장으로 연다.

  ```
  C:\Users\사용자\.sshid_rsa.pub
  ```

- 해당 내용을 복사한다.

**SSH 키 등록**

- 다시 github 사이트 창으로 이동하여 `SSH keys > Add new` 페이지에서 title에 적당한 제목을 입력하고 복사한 key를 붙여넣고 `Add SSH key` 버튼을 누른다.
- 문제가 해결된 것을 확인할 수 있다.



***Copyright* 2021 © Song_Artish**