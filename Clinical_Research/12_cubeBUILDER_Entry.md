# cubeBUILDER Entry

> Entry는 연구자들이 데이터를 입력하는 공간을 만드는 작업이다.

2021.07.06

---

[TOC]

---



- :heavy_exclamation_mark: Entry 진행 시 **반드시 아래의 2개의 문서를 토대로 진행**하여야 한다.

  ```markdown
  - CRF for EDC
  - DB specification
  ```



## 1. CYCLE & VISIT

> 해당 과제에서 사용할 :cactus:**방문 구조** 결정하는 메뉴

- :star: `e-CRF schedule` 표에서 작성되어 있는 방문 구조(일정)를 바탕으로 `CYCLE & VISIT`에 입력한다.

### 1.1 CYCLE 설정

| Cycle 종류 |     full name     |                       설명                        |
| :--------: | :---------------: | :-----------------------------------------------: |
|   **NV**   |   Normal Visit    |                     정규방문                      |
|   **UV**   | Unscheduled Visit |                예정되지 않은 방문                 |
|   **AV**   |     All Visit     | 특정 방문에 속하지 않고 언제든지 입력 가능한 방문 |

- `CYCLE ID`에는 NV, UV, AV를 입력한다.
- `TYPE`에는 Normal Visit, Unscheduled Visit, All Visit으로 설정한다.
- :white_check_mark: UV는 반복되기 때문에, 자동으로 `Repeat` 체크박스가 선택된다.

### 1.2 VISIT 설정

> - `EN(Enrollment) ~ V5`까지가 정규방문(NV)에 속한다.
> - `Code`: 해당 데이터가 어떤 방문에 속하는지 표시하기 위한 코드 (중복 입력X)
>   - :ballot_box_with_check: 코드번호는 `DB spec > Visitinfo`에서 확인할 수 있다. 
> - :white_check_mark: UV `Code`의 `#:+2000#`은 2000번부터 auto_increment가 된다는 의미이다.

- NV에 EN ~ V5를 입력한다.
- AV에 `Adverse Event`, `Prior and Concomitant Medications`, `Disposition`, `Principal Investigator's Signature` 등을 추가한다.
- 기타 코드 등은 `DB spec > Visitinfo` 문서를 참고한다.
- 이후 `Save` 버튼을 눌려 입력한 값들을 저장한다.



## 2. CRF GROUP

> `e-CRF schedule` 표를 참고하여​ :cactus:**CRF 그룹**을 생성하는 과정

- ID 값과 Label 값은 `DB spec > TableList` 문서를 참고한다.
  - DOMAIN -> Group ID
  - Description -> Label
- Type은 현재 EDC에 대한 페이지만을 생성하기 때문에, 모두 `Crfgroup for EDC`를 선택해준다.
- review, freezing, lock, sign, save 등의 체크박스는 각 그룹을 해당 옵션에 포함할 것인지를 결정한다.
  - 일반적으로는 모든 옵션을 체크하고 진행한다.
- 순서가 잘못 지정된 경우, drag&drop으로 순서를 변경할 수 있다.
- 작성이 완료되면 `Save` 버튼을 눌려서 설정을 저장한다.



## 3. SCHEDULE

> 앞에서 [Cycle&Visit](####3.1 CYCLE & VISIT)과 [CRF Group](####3.2 CRF GROUP)에서 설정한 내용 및 `e-CRF Schedule`표를 바탕으로 스케줄을 지정한다.

- `e-CRF Schedule`표를 바탕으로 스케줄을 입력한다.
  - :white_check_mark: `Quck Add`를 활성화하면 빠르게 스케줄을 입력할 수 있다.
- :ballot_box_with_check: AV(All Visit)의 경우, AE, CM, DS, SN이 각각에 맞도록(모양 - 대각선으로) 입력해준다.
- :white_check_mark: [참고] `Label hide`를 클릭하여 표시화면 Size를 줄일 수 있다.



## 4. CRF Page

### Entry 트리구조

BUILDER에서 사용하는 CRF 구조

> 1. Page
> 2. CRF
> 3. Question
> 4. Item - 연구자들이 데이터를 입력하는 필드

- 즉, 가장 큰 범위에서부터 **PAGE > CRF > QST > ITEM**이다.

### 생성 및 삭제

**생성**

- 각 단계에서 생성을 위해서는 상위 단계에서 `ADD CRF`, `ADD Question`, `ADD Item`을 눌려서 생성한다.

**삭제**

- item을 삭제할 때는 `CRF PAGE `에서 item을 선택하고 `Deleted` 체크박스를 활성화해준다.
- 다만, 삭제한 항목의 <u>id 값은 변경</u>해주면 좋다. 다른 item에서 사용될 수 있기 때문에
  - 예시) `MH01` -> `MH01_DEL` 

### 4.1 Enrollment (EN)

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

### 4.2 대상자 등록 -CDMS

- 대상자를 등록하면, CDMS에서 BUILDER Page 작성 내용을 확인할 수 있다.

[CDMS 문서](03_cubeCDMS.md) 참고

### 4.3 Subject Visit (SV)

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

### 4.4 Demographics (DM)

**뒤에 특정 문자열 표시하기**

> Age 항목 옆에 Years라는 단위를 표시하기 위해 `ITEM > Property`에서 **UNIT_APPEND**를 설정한다.

**나이 및 성별 연동**

> Subject List 혹은 나이가 필요한 곳에 **해당 ITEM 값을 연동**하기 위해, `[AGE] ITEM > EVENT`에서 **SUPP_SUBJ.AGE**를 설정한다.

- 성별도 마찬가지로 진행하여 값을 연동한다.

### 4.5 Medical History (MH)

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

### 4.6 Vital Signs (VS)

> `QST_CATEGORY`를 활용하여, 위에서 ND 옵션을 선택하게 되면 카테고리의 값을 입력하지 않아도 되도록 설정하는 구조를 만든다.

- `QST_CATEGORY`의 ID 값은 **VS_CT**로 설정하며, Label은 필수가 아니다.
  - Label 값을 입력하면 실제 페이지에서 category위에 label 값이 표시된다.
- `QST_CATEGORY` 하위에는 ITEM이 아닌 `QST_NORMAL`을 child로 넣어준다.

**소수점 TYPE_LENGTH**

- TYPE_LENGTH에서 `N3.1`은 정수 3자리, 소수점 1자리까지 입력하라는 의미이다.
- `ITEM > Layout`에서 TEXT_INPUT > Number를 선택하고 `ITEM > Data Type Length`에서도 `3.1`이라고 입력하면 된다.

**Comment 창 만들기**

- comment 바로 앞의 `QST > Property`에서 COMMENT_APPEND를 설정하고, value에 comment를 입력하면 된다.

### 4.7 Local Laboratory Test (LB)

여기서는 2개의 CRF를 생성해야 한다.

**QST > Property의 Variant**

- QST에서 Property를 입력하고, 해당 property의 가장 우측 아이콘을 클릭하면 각 property의 variant를 설정할 수 있다.

  ```markdown
  V1: *If there are any clinically significant abnormal result, please specify the details on the [Adverse Event] page.
  Except V1: *If there are any newly noted abnormal result since the last Visit, please specify the details on the [Adverse Event] page
  ```

  - 위와 같은 경우, `else 구문`에 해당하는 아래의 문구를 property의 value에 입력한다.
  - 그리고 `if 구문`에 해당하는 위의 문구를 property variant에서 조건문에 맞게 추가해준다.

**Static Rownum Table**

- 테이블 ID를 `LB01_ST`를 입력한다.

- 이후 아래에 새로운 하위 QST들을 생성한다.

- :ballot_box_with_check: `Static Rownum Table > QST > ITEM`에서는 **Sub Item이 매우매우 중요**하다:exclamation:

  - Sub Item에서 해당 열의 번호를 알 수 있어야 한다!

    > QST copy 기능을 통해, 하나의 QST만 생성해서 나머지를 copy할 예정이기 때문에!

  - **LB.1.Erythroctytes**과 같이 Sub Item을 입력한다.

  - 그리고 해당 `ITEM > Property`에서 `DEFAULT_VALUE`를 선택하고 `Erythrocytes`를 값으로 입력해준다.

**copy 기능**

> 하나만 만들어서 나머지를 copy하는 기능

- `상단의 static table QST > Copy Question` 버튼을 클릭하고, `Question List`에서 dropdown을 통해 copy할 target QST을 찾는다.
- target QST를 지정하고 copy 개수를 입력한다.
- :ballot_box_with_check: 생성된 QST에서 `Sub Item`이라는 버튼을 클릭하면 `Sub Item`을 이름을 일괄적으로 변경할 수 있다.
- 기타 변경해야 하는 것들을 직접 입력하여 변경해준다.

### 4.8 Pregnancy Test

> 위에서 실습한 내용을 토대로 작성한다.

### 4.9 Inclusion/Exclusion Criteria

- :ballot_box_with_check: 텍스트만 입력하는 QST는 **Dummy**라는 레이아웃을 사용한다
  - :white_check_mark: `ITEM Property > LABEL_WRATE`를 활용해서 item label의 폭 비율을 100으로 맞춰준다.
- :ballot_box_with_check: :star: **부동호의 경우** `<, >`을 입력하면 시스템에서 태그로 인식하여 오류가 발생할 수 있으므로, 반드시 **`ㄷ + 한자`를 사용하여 입력**한다.

### 4.10 Randomization

> 위에서 실습한 내용을 토대로 작성한다.

- IWRS와 관련된 세팅은 차후에 학습한다.

### 4.11 IP Prescription

> 위에서 실습한 내용을 토대로 작성한다.

### 4.12 Adverse Event

- QST_TABLE을 생성한다.
- Line Number의 경우, ITEM Layout을 **ROWNUM**으로 설정한다.

**DD(Dropdown)**

- Dropdown을 생성하려는 경우, Layout에서 `Dropdown`을 선택하고 Radio와 동일하게 작업을 한다.

**ITEM 2줄로 표시하기**

:ballot_box_with_check: `ROWSPAN_ITEMS`

- Table QST의 **`QST property > ROWSPAN_ITEMS`를 활용**하여 특정 항목의 순서 번호를 지정한다.
- 전체 폭을 차지할 항목의 idx 값을 입력해준다.
  - 예시) 1, 2번째 열은 전체 폭 차지 -> **[0, 1]**

:ballot_box_with_check: `LAYOUT_WIDTH`

> QST Property로 각 항목의 비율을 지정한다.

- 한 줄당 100%가 되어야 한다.
- 예시) 5%,15%,20%,20%,20%,20%,20%,20%,20%,20%
  - 1~6번째가 한 줄
  - 1,2, 7~10번째가 한 줄

### 4.13 Prior and Concomitant...

**Dropdown 하위에 item 생성하기**

- :ballot_box_with_check: `Dropdown > CODE`에서 모든 values의 `Type Text`를 체크해주어야만 사용할 수 있다!
- Dropdown 하위에 ITEM을 생성한뒤, PARENT 옵션과 연결해준다.

### 4.14 Disposition

> 위에서 실습한 내용을 토대로 작성한다.

### 4.15 Principal Investigator's Signature

**전자서명**

- `ITEM > EVENT`에서 **SUPP_SUBJ.ESIGN_STATUS**를 활용하여 입력할 수 있다.
- :ballot_box_with_check: `ITEM > Property > AUTOFILL`을 활용하면 연구자가 입력할 수 없도록 막을 수 있다.
- `ITEM > EVENT > SUPP_SUBJ.ESIGN_TIME`을 활용하면 전자서명 날짜/시간과 자동으로 연동할 수 있다.
- :white_check_mark: 전자서명 관련 ITEM들은 `Default Missing Chekc`를 NO로 체크해주어야한다.



***Copyright* © 2021 Song_Artish**
