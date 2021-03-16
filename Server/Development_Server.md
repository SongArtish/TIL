# 개발서버 사용하기

> A development server is a type of server that is designed to facilitate the development and testing of programs, websites, software or applications for software programmers.

2021.03.16

---

[TOC]

---



## VPN 접속

- 먼저 VPN에 접속한다.

> - putty 등의 **SSH 클라이언트**를 사용하여 서버에 연결한다.
> - 여기서는 **GPU 개발서버**에 연결하는 과정을 다룬다.



## PuTTY

> PuTTY는 SSH, 텔넷, rlogin, raw TCP를 위한 클라이언트로 동작하는 자유 및 오픈 소스 단말 에뮬레이터 응용 프로그램이다. (출처: 위키피디아)

- 먼저 [PuTTY](https://putty.softonic.kr/)를 설치한다.
- PuTTY를 실행하고 메인화면에서 할당받은 **IP 주소**를 입력하고 `Open` 버튼을 클릭한다.
- 이후 터미널 창이 뜨면 할당받은 **아이디 값**을 입력하고, 다음으로 **비밀번호**를 입력한다.
- 그러면 개발서버가 성공적으로 연결된 것을 확인할 수 있다.



## Powershell

> PowerShell은 명령줄 셸 및 스크립팅 언어로 구성된 플랫폼 간 작업 자동화 및 구성 관리 프레임워크이다. (출처: [공홈](https://docs.microsoft.com/ko-kr/powershell/scripting/overview?view=powershell-7.1_))

- 먼저 **Windows PowerShell**을 실행한다.
- 아래와 같이 명령어를 입력한다.

```powershell
ssh <아이디>@<ip주소> -p 22
```

- 그리고 **비밀번호**를 입력해주면 개발서버를 사용할 수 있다.



## <참고사항>

- :ballot_box_with_check: 반드시 VPN에 접속이 되어 있어야 개발 서버를 사용할 수 있다.
- :ballot_box_with_check: 개발 서버는 **conda** 와 동일한 환경에서 이용할 수 있다.
- :ballot_box_with_check: 서버 연결 후에는 해당 서버 내에서 **git clone**을 받아 코드 작업을 할 수 있다.



***Copyright* © 2021 Song_Artish**

