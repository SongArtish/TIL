# git 이슈

> git 관련 이슈를 정리한다.

---

[TOC]

---

## git push stuck @initial setting

> 최초 깃 등록시, git push 명령어를 입력하면 작업이 멈추는 현상이 계속해서 반복되었다.

- 눈에 보이는 점은 git bash에서 github에 로그인이 되지 않은 상태에서, clone이 되며
- `git push` 명령어를 입력해도 github 로그인 창이 나타나지 않았다.
- `자격 증명 관리자`에서도 github 관련 정보가 등록되어 있지 않았다.

**해결 방안**

- `자격 증명 관리자`에 들어가서 직접 github credentials를 직접 입력하였다.
- `인터넷 또는 네트워크 주소`
  - `git:https://github.com`
- 사용자 이름(아이디) 및 암호 입력



***Copyright* 2021 © Song_Artish**