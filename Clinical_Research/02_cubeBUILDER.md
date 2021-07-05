# cubeBUILDER

> CDMS를 setup하는 곳

2021.07.05

---

[TOC]

---



## 1. 계정 생성

- [builder 사이트](https://edu-builder.cubecdms.com/login)에 접속하여 계정을 생성한다.
- 이후 로그인한다.



## 2. 과제 생성

### 2.0 List of Studies

> 로그인을 하면 user가 설정 가능한 과제를 확인할 수 있는 리스트가 있다.

- 해당 리스트에서 원하는 과제를 검색/생성할 수 있다.
- :white_check_mark: organization이 `씨알에스큐브`인 과제는 샘플 과제로, review(참고) 목적으로 생성되어 있다.



### 2.1 Study Information

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



### 2.2 PROPERTY

#### Property Import

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

#### EDC 스크리닝 번호 설정

- :ballot_box_with_check: `기관코드 자릿 수 설정`: 임상시험 진행 기관의 코드
- 스크리닝 번호의 구성은 다음과 같다.
  - **S + SC(사이트 코드) 2자리 + 일련번호 3자리**
  - 예시) S02003

- **설정 방법**
  - `Identifier`에 S를 입력한 후, `Number format > Identifier`를 오른쪽으로 추가해준다.
  - 앞에서 사이트코드(기관코드)를 입력했기 때문에, `Number format > Site Codwe`를 바로 오른쪽으로 추가해준다.
  - 마지막으로 `Seq no.` 설정 후, `Number format > Seq no.`를 오른쪽으로 추가해준다.
  - `Confirm` 버튼을 누른 후, 마지막으로 `Save` 버튼을 눌려서 저장해준다.

**Enrollment number부터 학습!!!!!!!!!!!!!**



#### EDC 기타

`Log-in Page Settings`

- 과제 ID가 포함된 과제의 웹사이트 주소를 생성하며 해당 주소로 접속할 수 있다.
- 예시)` www.cubecdms.com/**cubedemo_2021**/login`

`Image`

- 설정된 웹사이트 주소로 접속했을 때 표시되는 그림을 지정
- 지정하지 않으면 기본 설정

`e-Training`

- 과제에서 사용할 트레이닝 방법 선택
- 기본적으로 `cubeCDMS training(System)`이 지정됨



### 2.3 LANGUAGE

> CDMS에서 사용할 언어를 설정한다.

- 한국어, 영어, 중국어, 일본어를 지원한다.
- 사용할 언어를 선택한 후, `Default` 언어를 반드시 하나 설정해준다.



### 2.4 ROLE & PRIV.

> CDMS에서 사용할 역할 & 권한

- :ballot_box_with_check: 사이트에서 **ROLE**과 **Privilege**의 리스트를 확인할 수 있다.
  - 자세한건 `Basic_Training_Role&Priv_IWRS_FULL.xlsx` 파일을 참고한다.
- 가급적이면 **Library Import 기능**을 이용하여 Role과 Privilege를 설정한다.
  - `Import` 방법은 앞선 [Property Import](####Property Import)와 동일하다.
  - 앞선 `PROPERTY` 부분과 동일하게 과제 scope별 라이브러리를 사용한다.
- 설정된 내용에 대한 Excel파일을 다운로드 할 수 있다.
- 추후 과제를 오픈 한 후에 R&P에서 설정한 내용을 단독으로 `Check` 버튼을 통해 release 할 수 있다.



## 3. Entry

> 연구자가 입력하는 **화면을 구성하는 메뉴**

- :heavy_exclamation_mark: 본 실습은 실제 study 진행 시 반드시 아래의 2개의 문서를 토대로 진행하여야 한다.
  - 기본 문서로  `CRF for EDC` 문서를 준비한다.
  - `DB specification` 문서는 참고용으로 확인한다.

### 3.1 CYCLE & VISIT

> 해당 과제에서 사용할 :cactus:**방문 구조** 결정하는 메뉴

- :star: `e-CRF schedule` 표에서 작성되어 있는 방문 구조(일정)를 바탕으로 `CYCLE & VISIT`에 입력한다.

#### 3.1.1 CYCLE 설정

| Cycle 종류 |     full name     |                       설명                        |
| :--------: | :---------------: | :-----------------------------------------------: |
|   **NV**   |   Normal Visit    |                     정규방문                      |
|   **UV**   | Unscheduled Visit |                예정되지 않은 방문                 |
|   **AV**   |     All Visit     | 특정 방문에 속하지 않고 언제든지 입력 가능한 방문 |

- `CYCLE ID`에는 NV, UV, AV를 입력한다.
- `TYPE`에는 Normal Visit, Unscheduled Visit, All Visit으로 설정한다.
- :white_check_mark: UV는 반복되기 때문에, 자동으로 `Repeat` 체크박스가 선택된다.

#### 3.1.2 VISIT 설정

> - `EN(Enrollment) ~ V5`까지가 정규방문(NV)에 속한다.
> - `Code`: 해당 데이터가 어떤 방문에 속하는지 표시하기 위한 코드 (중복 입력X)
>   - :ballot_box_with_check: 코드번호는 `DB spec > Visitinfo`에서 확인할 수 있다. 
> - :white_check_mark: UV `Code`의 `#:+2000#`은 2000번부터 auto_increment가 된다는 의미이다.

- NV에 EN ~ V5를 입력한다.
- AV에 `Adverse Event`, `Prior and Concomitant Medications`, `Disposition`, `Principal Investigator's Signature` 등을 추가한다.
- 기타 코드 등은 `DB spec > Visitinfo` 문서를 참고한다.
- 이후 `Save` 버튼을 눌려 입력한 값들을 저장한다.



### 3.2 CRF GROUP

> `e-CRF schedule` 표를 참고하여​ :cactus:**CRF 그룹**을 생성하는 과정

- ID 값과 Label 값은 `DB spec > TableList` 문서를 참고한다.
  - DOMAIN -> Group ID
  - Description -> Label
- Type은 현재 EDC에 대한 페이지만을 생성하기 때문에, 모두 `Crfgroup for EDC`를 선택해준다.
- review, freezing, lock, sign, save 등의 체크박스는 각 그룹을 해당 옵션에 포함할 것인지를 결정한다.
  - 일반적으로는 모든 옵션을 체크하고 진행한다.
- 순서가 잘못 지정된 경우, drag&drop으로 순서를 변경할 수 있다.
- 작성이 완료되면 `Save` 버튼을 눌려서 설정을 저장한다.



### 3.3 SCHEDULE

> 앞에서 [Cycle&Visit](####3.1 CYCLE & VISIT)과 [CRF Group](####3.2 CRF GROUP)에서 설정한 내용 및 `e-CRF Schedule`표를 바탕으로 스케줄을 지정한다.

- `e-CRF Schedule`표를 바탕으로 스케줄을 입력한다.
  - :white_check_mark: `Quck Add`를 활성화하면 빠르게 스케줄을 입력할 수 있다.
- :ballot_box_with_check: AV(All Visit)의 경우, AE, CM, DS, SN이 각각에 맞도록(모양 - 대각선으로) 입력해준다.
- :white_check_mark: [참고] `Label hide`를 클릭하여 표시화면 Size를 줄일 수 있다.



## 4. Data Set



## 5. ECS

> Edit Check Specifications. 함수를 이용하여 조건문을 생성하는 것.



## 6. DCL

> Entry와 ECS에 포함되지 않는 **기타 기능**을 집합



## 7. User 등록

> `ADMIN > STUDY(USER)`에서 사용자를 추가해야 해당 사용자가 내가 생성한 builder에 접속할 수 있다.

ADMIN 메뉴

- `ADMIN > STUDY(USER)`의 Privilege는 **Builder의 권한** 설정을 의미한다.
- `ADMIN > RELEASE`
  - **release**: 연구자들이 사용할 수 있는 real 사이트를 오픈하는 것



***Copyright* © 2021 Song_Artish**
