# cubeCDMS User

2021.07.09

---

[TOC]

---



## 1. 기관 추가

### 1.1 SPONSER 기관 추가

1. 과제를 생성한 사용자가 CDMS에 SPM으로 접속하여 `Admin > User > site`로 이동한다.
2. 왼쪽 아래 `Add` 버튼을 클릭하여 기관을 등록한다.
3. `SPONSER` type으로 설정하고 필수 항목을 모두 입력한다.
   - `site명`을 클릭하면 sponsor, CRO 기관을 검색할 수 있다.



### 1.2 연구기관 추가

**사이트 추가**

- 진행하는 과제로 이동하여 `Admin > User > Site`에 들어간다.
- 연구기관이므로 `Investigator`를 선택하고, 기타 설정을 완료하여 사이트를 추가한다.

**권한 부여**

- `Admin > User > User`에 들어가서 권한을 부여하고자 하는 사용자를 ID를 클릭한다.
- 제일 밑에 역할 추가 `+` 버튼을 누르고 해당하는 사이트를 연결한다.
- 실습에서는 제일 권한이 많은 `PI`로 권한을 부여한다.

**대상자 등록**

- 다시 첫 화면으로 돌아가 과제를 클릭하고, 역할을 선택한다.
- `Subject > Subject 추가` 버튼을 추가하면 사이트를 선택할 수 있고 대상자를 등록할 수 있다.



## 2. 사용자 등록

1. `Admin > User > User`에서 사용자를 등록한다.
2. 필수 항목을 입력하고 저장한다.
   - 시작일과 완료일은 자동으로 입력되며, 추후 수정이 가능한다.
3. `Organization`(소속 site)에는 실제로 User가 소속된 기관을 선택한다.
   - 제약사, CRO, DEV 등의 스폰서 기관 소속인 User는 **PI, Sub-I, CRC** 외 role을 설정할 수 있다.
   - `INV(병원) 기관 소속인 user는 `**PI, Sub-I, CRC**만 선택할 수 있다.
4. `Role, Site` 부분에는 해당 User가 담당할 기관을 선택한다.

- :small_red_triangle: **Organization은 반드시 해당 user가  소속된 기관을 선택해야**한다. 스폰서 user의 계정을 테스트하기 위해 Organization에 test 기관을 선택하는 경우가 빈번하게 발생하기 때문에 유의해서 적용한다.



***Copyright* © 2021 Song_Artish**
