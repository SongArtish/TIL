# AWS

> 공통프로젝트 팀원 박종원의 필기를 많이 참고하였다.

2021.02.19

---

[TOC]

---



## 과정 요약

1. AWS 서비스 가입
2. 도메인 얻기
   - 도메인은 구매하거나 무료 도메인을 사용할 수 있다.
   - `우동` 프로젝트의 경우 [가비아](https://www.gabia.com/)에서 구매했다
3. `https`를 사용하기 위하여 도메인에 대한 `SSL인증` 받기
   - aws에서 인증
4. `Amazon Route 53 콘솔(호스트영역)`을 통해 구입한 도메인과 aws 인스턴스 연결
5. https를 사용하는 경우, `로드밸런서` 생성
   - `우동` 프로젝트의 경우 `geolocation`이라는 위치인증 기능을 사용하기 위해서 https 사용
6. Route 53 콘솔(호스트영역)을 통해 도메인을 `ELB`와 연결
   - `ELB: Elastic Load Balancing`
7. 도메인 접속 성공



## 1. AWS  가입

- 해외결제가 가능한 카드를 이용하여 AWS에 가입한다.
- 보안에 유의하도록 한다.



## 2. 도메인 얻기

> 여기서는 [가비아](https://www.gabia.com/)에서 도메인을 구입하였다.

- [가비아](https://www.gabia.com/) 홈페이지에서 회원가입을 한다.
- 도메인 검색창에 원하는 도메인 주소의 키워드를 입력하고 선택한 후 결제한다.
- :white_check_mark: `https`를 사용하는 경우
  - 가비아 네임서버(NS)가 아닌 외부 네임서버(NS)를 선택한다.



## 3. SSL 인증받기

> 보안 소켓 계층(Secure Sockets Layer, *SSL*)

- AWS 사이트에서 로그인 후, Certificate Manager Console로 이동한다.
- AWS 지역을 확인하고, 서비스가 제공될 지역에서 인증을 받는다.
- `인증서 요청` 버튼을 클릭한다.
- 이전 단계에서 얻은 도메인 이름을 넣고 `다음`을 클릭한다.
  - 예시: `udong.shop`
- `이 인증서에 다른 이름 추가` 버튼을 누른후 `*.udong.shop`을 추가한다.
  - 여기서, `*`을 앞에 붙이는 이유는 SSL인증서의 유효범위가 `udong.shop`, `www.udong.shop` 등 모든 URL에 적용하기 위해서이다.
- 

***Copyright* © 2021 Song_Artish**