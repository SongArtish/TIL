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

- :heavy_exclamation_mark: Entry 진행 시 **반드시 아래의 2개의 문서를 토대로 진행**하여야 한다.

  ```markdown
  - CRF for EDC
  - DB specification
  ```

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



### 3.4 CRF Page

#### Entry 트리구조

BUILDER에서 사용하는 CRF 구조

> 1. Page
> 2. CRF
> 3. Question
> 4. Item - 연구자들이 데이터를 입력하는 필드

- 즉, 가장 큰 범위에서부터 **PAGE > CRF > QST > ITEM**이다.

#### 생성 및 삭제

**생성**

- 각 단계에서 생성을 위해서는 상위 단계에서 `ADD CRF`, `ADD Question`, `ADD Item`을 눌려서 생성한다.

**삭제**

- item을 삭제할 때는 `CRF PAGE `에서 item을 선택하고 `Deleted` 체크박스를 활성화해준다.
- 다만, 삭제한 항목의 <u>id 값은 변경</u>해주면 좋다. 다른 item에서 사용될 수 있기 때문에
  - 예시) `MH01` -> `MH01_DEL` 

#### 3.4.1 Enrollment (EN)

- :heavy_exclamation_mark: (스크리닝 번호가 포함된 페이지)는 반드시 page `TYPE`을 **Registration Page**로 설정한다. (one and unique)
- `CRF for EDC`, `DB Spec` 문서에 따라 QST, ITEM을 등록하고 설정한다.
  - `QST > Type`은 Normal Question으로 설정
  - `Item > Layout`은 각각, DATE와 SYSDEFINED로 설정
  - :white_check_mark: `ITEM > Default Missing Check`는 (누가?) **연구자가 반드시 입력해야하는 항목에 대해 누락** Query를 발행할지 설정하는 부분이다.
    - :exclamation: 별도의 지시사항이 없으면, `YES`로 처리한다.
- :ballot_box_with_check: `ITEM > Sub item`에 `Domain Name`, 즉 EN을 입력한다.
  - 이하도 동일하다.
- :ballot_box_with_check: `ITEM > EVENT`는 해당 아이템 값들에 이벤트를 걸어준다.
  - 각각 `SUPP_SUBJ.IC_DATE`와 `SUBJECT.SCR_CODE` 이벤틀르 설정한다.

#### 3.4.2 대상자 등록 -CDMS

- 대상자를 등록하면, CDMS에서 BUILDER Page 작성 내용을 확인할 수 있다.

[CDMS 문서](03_cubeCDMS.md) 참고

#### 3.4.3 Subject Visit (SV)

> 전반적인 내용은 CRF for EDC와 DB spec 문서를 참고하여 위와 동일하게 진행한다.

**Radio 설정**

> Radio는 선택 항목 중 단 하나만 선택할 수 있는 레이아웃이다.

- `ITEM > Layout`에서 RADIO를 선택하면 `Code` 항목이 생겨난다.

- `Code > [Add]` 버튼을 눌려 내용을 입력한다.

  - 보통 Code Id와 Name은 해당 아이템의 ID, Label과 동일하게 대응되게 입력한다.

  - 아래의 VALUES에 원하는만큼 값을 추가하고 각각의 Val.들을 입력해준다.

    |           Value           |                             설명                             |
    | :-----------------------: | :----------------------------------------------------------: |
    |       **DB Value**        |                          DB 상의 값                          |
    |       **UI Value**        |                      화면에 표시되는 값                      |
    | **Rpt.(Reporting) Value** | Dataset 추출시 출력되는 값<br />**(보통 DB Val.과 동일하게 입력)** |

  - :white_check_mark: Rpt. Val.는 데이터를 전달하기 위하여 엑셀로 데이터를 추출시에 출력되는 값을 의미한다.

**기타 상세 입력**

- radio에서 `others`를 선택한 경우, 상세 내용을 입력할 수 있는 창(`specify below`)을 만들어준다.
- :ballot_box_with_check:**​ Property는 item을 꾸며주는 역할을 한다.**
  - `NOTICE_APPEND`라는 property를 사용하면 radio element 뒤에 표시될 문자열을 입력할 수 있다.
  - NOTICE_APPEND-$$에서 `$$`자리에 연결할 값의 DB value를 입력해준다.
    - 여기서는 NOTICE_APPEND-2라고 입력하면 된다.
    - 그리고 value에 `Specify below`라고 입력해준다.

**특정 조건일 때만 표시**

- UV일 경우에만 표시해주어야 하는 QST은 **Variant을 활용**한다. :ballot_box_with_check:
- 각 아이템의 Variant에서 다음과 같이 조건문을 걸어준다.
  - ALL일 경우, exclude
  - UV일 경우, include

#### 3.4.4 Demographics (DM)

**뒤에 특정 문자열 표시하기**

> Age 항목 옆에 Years라는 단위를 표시하기 위해 `ITEM > Property`에서 **UNIT_APPEND**를 설정한다.

**나이 및 성별 연동**

> Subject List 혹은 나이가 필요한 곳에 **해당 ITEM 값을 연동**하기 위해, `[AGE] ITEM > EVENT`에서 **SUPP_SUBJ.AGE**를 설정한다.

- 성별도 마찬가지로 진행하여 값을 연동한다.

#### 3.5.5 Medical History (MH)

> :exclamation: MH의 QST들은 **Domain name이 `MH`가 아닌 `MY`**인 것에 주의한다!

- 먼저 `QST_NORMAL`과 `QST_TABLE`을 각각 만들어준다.
- :ballot_box_with_check: seq number의 `item > layout`은 sysdefined가 아닌, rownum으로 해야한다!
- :white_check_mark: **MEDCODE**: 연구자가 병력을 검색해서 입력하는 형태

**Radio 아이템의 좌우정렬**

- `ITEM > Property`에서 CODE_WIDTHS_ARR를 지정 후, value에 `50%,50%`의 값을 지정해준다.
  - `CODE_WIDTHS_ARR`는 radio element들의 폭배열을 설정하는 property이다.
  - value는 radio 개수에 맞춰서 해야하며, 합이 반드시 100%가 되어야한다.

**Date Unknown 값 배정**

- `End date`를 설정할 때 UK도 지정할 수 있게 해야한다.
- `ITEM > Property`에서 JSDATA_DDUK, JSDATA_MMUK, JSDATA_ YYUK를 설정해주면, 각각 일, 월, 년 별로 UK 값을 지정할 수 있게 된다.

**Table 항목 폭**

- `Table QST > Property`에서 `LAYOUT_WIDTH`를 설정해주고, 위에서 radio 아이템 좌우정렬을 한 것과 같이 원하는 비율을 지정해준다.

#### 3.4.6 Vital Signs (VS)

> `QST_CATEGORY`를 활용하여, 위에서 ND 옵션을 선택하게 되면 카테고리의 값을 입력하지 않아도 되도록 설정하는 구조를 만든다.

- `QST_CATEGORY`의 ID 값은 **VS_CT**로 설정하며, Label은 필수가 아니다.
  - Label 값을 입력하면 실제 페이지에서 category위에 label 값이 표시된다.
- `QST_CATEGORY` 하위에는 ITEM이 아닌 `QST_NORMAL`을 child로 넣어준다.



#### 3.4.7 Local Laboratory Test



#### 3.4.8 Pregnancy Test



#### 3.4.9 Inclusion/Exclusion Criteria



#### 3.4.10 Randomization



#### 3.4.11 IP Prescription



#### 3.4.12 Adverse Event



#### 3.4.13 Prior and Concomitant...



#### 3.4.14 Disposition



#### 3.4.15 Principal Investigator's ...



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
