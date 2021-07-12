# cubeBUILDER 시작하기

> cubeBUILDER는 CDMS를 setup하는 프로그램이다.

2021.07.05

---

[TOC]

---



## 시작하기 전

> 시작하기 전, **계정을 생성**한다.

- [builder 사이트](https://edu-builder.cubecdms.com/login)에 접속하여 계정을 생성한다.
- 이후 로그인한다.



## 빠른 셋업하기

> BUILDER 라이브러리를 사용하면 과제를 빠르게 셋업할 수 있다.

**Study Copy**

- `BUILDER > Copy 버튼` 클릭후 Library Study에서 `CLONE_IWRSFULL` 선택하고 과제를 copy해서 진행한다.
- `Study > Info`에서 `Protocol, Aliasm, Title`을 입력하고 `Save`한다.

**Entry Copy**

`Entry > CRF GROUP > Group Copy`에서 `CRF_FOR_EDC_GL`  검색 후 필요한 Group 선택



## List of Studies

> 로그인을 하면 user가 설정 가능한 과제를 확인할 수 있는 리스트가 있다.

- 해당 리스트에서 원하는 과제를 검색/생성할 수 있다.
- :white_check_mark: organization이 `씨알에스큐브`인 과제는 샘플 과제로, review(참고) 목적으로 생성되어 있다.



## Study Information

- 첫 화면 리스트에서 `Create` 버튼을 눌려 과제를 생성한다.

|    필드값    |                             설명                             |                             예시                             |
| :----------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|    **ID**    |                  해당 study의 id값 (고유값)                  |                HM_AS_201 (한미약품 아스피린)                 |
| **Protocol** | **임상시험 계획서 제목 혹은 과제명**<br />(보통 ID와 Protocol명을 동일하게 설정) |                                                              |
|  **Alias**   |                     과제를 지칭하는 별칭                     |                                                              |
|  **Title**   |          임상시험 계획서의 첫 페이지에 나오는 제목           | 고혈압 환자를 대상으로 A약물이 효과가 있는지를 검증하는 임상시험 |
|  **Phase**   |                     임상시험 단계를 설정                     |                                                              |
|  **Active**  |                  (`No`는 과제 삭제를 의미)                   |                         `Yes`로 선택                         |
|  **System**  | CRScube에서 제공하는 솔루션<br />(실습에서는 CDMS와 IWRS를 사용) |                                                              |

- **System**에 대한 간단한 설명

> CRScube에서 제공하는 솔루션은 아래와 같다.

|  Solution   |                             Role                             |
| :---------: | :----------------------------------------------------------: |
|  **CDMS**   |                       데이터 수집공간                        |
|  **IWRS**   |               약품 재고 관리 등 행정절차 제공                |
|   **PRO**   | 환자가 직접 앱으로 데이터를 입력하는 것<br />(EDC로 데이터 입력됨) |
|   **PR**    |                                                              |
| **CONSENT** |                  Tablet을 통한 동의서 서명                   |
|   **DDC**   |                          (초기단계)                          |

- `[Create]`를 누르면 과제가 생성되며, 과제 리스트에서 확인할 수 있다.
  - :ballot_box_with_check: Create 완료 후 CDMS에서 접속이 가능하다!
- 생성한 과제의 ID를 클릭하여 과제에 접속한다.
- `STUDY > INFO` 메뉴에서 앞에서 설정한 정보 확인 가능



## PROPERTY

### Property Import

- `STUDY > PROPERTY > PROPERTY`에서 `Import`를 한다.

  |         Type         |                            설명                             |
  | :------------------: | :---------------------------------------------------------: |
  |   **DOUBLE_ENTRY**   | Paper로 진행된 과제를 Double Entry로 QC하기 위한 라이브러리 |
  |     **IWRSFULL**     |  EDC + 무작위배정 +임상시험 모든절차 등 모든 scope의 과제   |
  |     **IWRSSUB**      |        EDC + 무작위배정<br />(IP 배송관리 및 배정 X)        |
  |      **PHASE**       |                  일반 EDC만 사용하는 과제                   |
  | **PMS**(시판후 조사) |             PMS나 OS 과제에 사용되는 라이브러리             |

  - :arrow_forward: `DOUBLE_ENTRY`: 종이로 작성된 데이터를 디지털로 옮기기 위한 라이브러리 (2명이 입력하기 때문에 `double entry`이다.)
  - :ballot_box_with_check: ​ `IWRSFULL, IWRSSUB, PHASE, PMS`가 주로 쓰인다.

- 여기서 `IWRSFULL`을 import 한다.

  - :white_check_mark: 상단의 `saved` 버튼은 이 과제에 저장된 property 표시 유뮤이다.

- ::ballot_box_with_check: `Import`를 클릭하면 `Save`를 누르지 않아도 자동으로 설정된다.

### EDC 스크리닝 번호 설정

- :ballot_box_with_check: `기관코드 자릿 수 설정`: 임상시험 진행 기관의 코드
- 스크리닝 번호의 구성은 다음과 같다.
  - **S + SC(사이트 코드) 2자리 + 일련번호 3자리**
  - 예시) S02003

- **설정 방법**
  - `Identifier`에 S를 입력한 후, `Number format > Identifier`를 오른쪽으로 추가해준다.
  - 앞에서 사이트코드(기관코드)를 입력했기 때문에, `Number format > Site Codwe`를 바로 오른쪽으로 추가해준다.
  - 마지막으로 `Seq no.` 설정 후, `Number format > Seq no.`를 오른쪽으로 추가해준다.
  - `Confirm` 버튼을 누른 후, 마지막으로 `Save` 버튼을 눌려서 저장해준다.

### EDC 기타

`Log-in Page Settings`

- 과제 ID가 포함된 과제의 웹사이트 주소를 생성하며 해당 주소로 접속할 수 있다.
- 예시)` www.cubecdms.com/**cubedemo_2021**/login`

`Image`

- 설정된 웹사이트 주소로 접속했을 때 표시되는 그림을 지정
- 지정하지 않으면 기본 설정

`e-Training`

- 과제에서 사용할 트레이닝 방법 선택
- 기본적으로 `cubeCDMS training(System)`이 지정됨



## LANGUAGE

> CDMS에서 사용할 언어를 설정한다.

- 한국어, 영어, 중국어, 일본어를 지원한다.
- 사용할 언어를 선택한 후, `Default` 언어를 반드시 하나 설정해준다.



## ROLE & PRIV.

> CDMS에서 사용할 역할 & 권한

- :ballot_box_with_check: 사이트에서 **ROLE**과 **Privilege**의 리스트를 확인할 수 있다.
  - 자세한건 `Basic_Training_Role&Priv_IWRS_FULL.xlsx` 파일을 참고한다.
- 가급적이면 **Library Import 기능**을 이용하여 Role과 Privilege를 설정한다.
  - `Import` 방법은 앞선 [Property Import](####Property Import)와 동일하다.
  - 앞선 `PROPERTY` 부분과 동일하게 과제 scope별 라이브러리를 사용한다.
- 설정된 내용에 대한 Excel파일을 다운로드 할 수 있다.
- 추후 과제를 오픈 한 후에 R&P에서 설정한 내용을 단독으로 `Check` 버튼을 통해 release 할 수 있다.



***Copyright* © 2021 Song_Artish**
