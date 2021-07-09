# cubeBUILDER Release

> Builder setup한 beta 사이트를 real 사이트로 release하는 과정

2021.07.09

---

[TOC]

---



## 시작하기 전

**테스트 사이트 설정**

- CDMS에 SPM으로 접속하여 `Admin > User > Site`로 이동한다.
- 리스트 중 release할 사이트는 `테스트 사이트` 체크박스를 해제해준다.
  - :star::star::star: **반드시 테스트 사이트 체크박스를 해제해준다!!**
- 리스트 중 test를 위한 기관은 `테스트 사이트` 체크박스를 클릭한다.



## Release 과정

- `Builder > Admin > Release`로 접속한다.
- `Exclude ECS`에 `No`가 체크된 상태에서 진행한다.
  - :white_check_mark: 최초 release 시에는 `Exclude ECS`를 `Yes`로 체크할 수 없다.
- 오른쪽 아래 `Check` 버튼을 눌려준다.
  - 오른쪽 `Release` 창에서 **실제 사이트와 베타 사이트의 차이점**을 확인할 수 있다.
- 왼쪽에 나타난 `Reason` 창에 release 사유를 작성하고 `Release` 버튼을 눌려준다.
  - 다소 길고 구체적으로 작성하여야 한다.
- 이렇게 release가 완료된 상태에서 다시 `Check` 버튼을 누르면 `Release 창`에서 실제-베타 사이트 간 차이점을 확인할 수 있다.
- `https://edu-beta.cubecdms.com/`에서 중간에 `-beta`를 지우고 [사이트](https://edu.cubecdms.com/)에 접속하면 실제 사이트에서 과제를 진행할 수 있다.



## 참고

- `ADMIN > STUDY(USER)`에서 사용자를 추가해야 해당 사용자가 내가 생성한 builder에 접속할 수 있다.



***Copyright* © 2021 Song_Artish**
