# Sample Study EDC

---

[TOC]

---



## Group과 Check box

**1.하나의 QST내에 2개 이상의 Check box layout을 설정해야 하는 경우**

- QST 내에 첫번째 Item으로 Layout이 `GROUP`인 item으로 생성한다.
- 그리고 GROUP item의 child로 `check box layout`을 설정한다.

**2. 하나의 QST내에 2개 이상의 Group을 설정하는 경우**

- QST 내에 첫번째 ITEM으로 Layout이 `GROUP`인 item을 생성한다.
- GROUP item의 child로 또 다시 layout이 `GROUP`인 item을 두개 추가한 후에 각 item에 `Check` layout을 설정한다.
- `Parent GROUP ITEM`에는 `CHILD_PLACEMENT` Property를 설정한다.



## Innter Table

> 행 추가가 가능한 Table Question 내에서 다시 하위 행을 추가할 수 있는 구조이다.

- 기본적인 Table Question 하위에 layout이 `INNERTABLE`인 item을 생성한다.
  - 이 item은 INNTERTABLE내 `+` 버튼을 추가하기 위해서이다.
- layout이 `INNTERTABLE`인 item이 생성되면 Table QST에서 하위 QST을 생성할 수 있는 버튼이 보이게 된다; `Add Question` 버튼
- 기존에 생성한 Table QST에서 하위 Table QST을 추가한다.
- 추가한 Table QST에 하위 행 추가가 필요한 `항암제명, 투여경로, 1일투여량, 단위, 투여일` ITEM을 생성한다.
- Table QST의 `LAYOUT_WIDTH`라는 propert로 Innter table 내 행 추가 버튼 컬럼도 포함하여 %비율을 맞춰준다.



## ATC

1. `Entry > CRF PAGE`에서 약물을 입력해야하는 page의 item으로 이동한다.
   - 보통 CMTRT이다.
2. layout을 `Medication`으로 선택하고 code에 사전과 `Direct Input`을 지정해준다.
3. `DCL > Medical Coding`에서 `New`버튼을 누르고 아래와 같이 항목을 작성한다.
   - Category ID - `CM`
   - Category label - `Concomitant Medications`
   - Category type - `Medication`
   - Code dictionary `ATC INDEX 2021` 체크
   - Description - `Concoitant Medications`
4. 그리고 하위 항목 중 `DRUG, UNIT, PATH, PURPOSE`에 visible 체크를 해주고 `CMTRT, CMDOSU, CMROUTE< CMINDC`를 각각 item 입력란에 입력하고 저장한다.
5. `Data Set > Main`에서 Create 버튼을 클릭하고 `Anatomical Therapeutic Chemical`을 선택하고 confirm한다.
6. 다음으로 우측 아래의 `Entry Import` 버튼을 클릭한다.
7. `Data Set > Variable`로 이동하여 Domain Id가 `CM`인 `ATC`로 name이 시작하는 항목들이 잘 추가되었는지 확인한다.



## Cycle Repeat

> 동일한 Cycle방문 구조를 여러번 반복 하여 진행할때 설정

- 주로 항암과제에서 사용된다.

1. `BUILDER > Entry > CYCLE & VISIT`에서 각 cycle visit이 어떤 방식으로 진행될지 먼저 정하여 설정한다.
   - cycle repeat여부에 체크한다.
2. CODE와 LABEL을 표기하는 규칙은 ##사이의 숫자에서 1씩 증가하는 형태이다.
   - 예를 들어 Code의 `#:+100#01`는 Data set 상에서 Visit code가 10101, 10201 형태로 기재된다.
   - Label의 `C#:+1#D1`은 EDC화면 상의 label이 C2D1, C3D1 형태로 표시된다.
   - C##D1으로 설정하게 되면 C1D1부터 시작하게 된다.



## SAE

> CRScube에서 제공하는 기본 SAE report form인 77-2호 양식, CIOMS 양식을 CRF Group copy를 통하여 설정하고 SAE발생에 따른 Report 작성 및 제출 방법에 대해 학습한다.]

### Builder에서 세팅하기

1. `BUILDER > Entry > Cycle & Visit`에서 SAE에 대한 cycle & visit을 생성하고, type을 `Report(SAE, ...)`으로 설정한다.

2. `Entry > CRF Group`에서 Group Copy버튼을 클릭하고 창이 열리면 과제 검색란에 `SAE_CIOMS`를 검색한다.

   - 77-2호 양식은 `SAE_77_2`이다.

3. "SAE" GROUP ID를 체크 하고 Save 한다.

4. `Entry > Schedule`에서 SAE의 스케줄을 등록한다. (visible - `No`)

5. `Entry > CRF Page`에서 AE 페이지의 페이지 타입이 `AE page`로 설정되어 있는지 확인한다.

6. AETERM Item에 `REPORT_ITEM.0.NAME` 이벤트를 지정한다.

7. AESER item에서 SAE Report를 발생시키고 알람을 줄 항목을 확인하고 그에 맞는 이벤트를 적용한다. 

   - `REPORT_ITEM.0.AECHECK`, `REPORT_ITEM.0.CHECK`
   - 이벤트 ID 중간에 숫자(0)는 CRF GROUP에서 확인한 Report Id에 숫자와 일치해야한다.
   - 예시) `REPORT_ITEM.**0**.NAME`, `REPORT_ITEM.**0**.AECHECK`, `REPORT_ITEM.**0**.CHECK`

8. `Entry > Report`에서 CRF GROUP을 COPY함에 따라 해당 정보도 복사되므로 확인한다.

   - Name : 사용할 Report의 이름을 지정한다.
   - Cycle : Report의 Cycle을 설정한다.
   - All Team : 소속 된 기관의 Report만 확인할지 전체 기관의 Report를 모두 확인할지를 결정한다.
     - Y인 경우 소속 된 기관 뿐만 아니라 모든 기관의 Report 열람 가능
   - Step : Report 작성 및 제출 절차를 설정한다.

   - Type : PDF출력 화면을 지정한다.
     - Type1 : Entry 화면을 Report form으로 사용하고 여기에 머릿글과 바닥글을 적용하여 PDF로 출력할 수 있는 타입 (새로 개발 된 형태)
     - Type2 : 제약사, CRO form과 동일하게 html 작업 된 PDF로 출력하는 타입 (현재까지 가장 많이 사용 됨), (기존에 생성 된 CIOMS나 77-2호 양식은 값이 보이지 않음) 
     - Type3 : Blank eCRF와 동일한 PDF로 출력할 수 있는 타입 (Entry만 설정하여 사용 가능함)
     - Type이 비어 있는 것은 본 기능이 생기기 전에 적용 된 report form이다. 위에서 복사한 CIOMS form을 포함하여 77-2호 양식 등은 이 전에 만들어진 form이며, 비어있는 것이 맞다.

### CDMS에서 작성하기

- `CDMS > AE`에서 아이템을 저장하면 `SAE Report`를 작성할 수 있는 아이콘에 오른쪽에 생긴다.

  > 24시간 안에 제약사에 보고할 의무가 있기 때문에

- 아이콘 클릭 후 SAE Report를 작성한다.

- 보고서 작성을 완료하면 등록된 이메일로 SAE 보고서가 전송된다.

  - :white_check_mark: 메일 전송 관련 사항은 `BUILDER > ROL&PRIV> > PRIVILEGE`에서 `MAIL` privilege 검색해서 참고한다.



## Version Control

|                       |                             설명                             |
| :-------------------: | :----------------------------------------------------------: |
| **Version 일괄 변경** | 등록된 모든 대상자의 버전 변경<br />(한 과제 내에 1개의 version만 존재) |
|  **Version Control**  | 이미 등록된 대상자는 제외하고 버전 변경<br />(한 과제 내에 여러 개의 version 존재) |

- Version 일괄 변경은 기존에 설정된 EDC화면을 재수정하여 변경을 진행

**Version 일괄 변경**

- `BUILDER > Entry Version`에서 수정 버튼을 눌려서 version을 수정한다.
- `ID`는 EDC의 버전을, `Version`은 CRF의 버전을 의미한다.
- (기존 item을 삭제하고 새로 release하면 변경된다.)
- :white_check_mark: version 일괄변경 작업을 하기 전, 이전 버전의 Blank eCRF와 Annotated eCRF을 꼭 다운로드 받아서 보관할 수 있도록 한다!

**Version Control**

> 일반적으로 기관별 IRB 승인일을 기준으로 버전을 관리한다.

- :ballot_box_with_check: 등록(EN)페이지는 버전 관리 기준이 되므로 version control할 수 없다.

1. `Entry > CRF Page > ICDTC`에서 item에 `SUBJECT.BEGIN_DATE` event를 설정한다.

   - 해당 이벤트를 적용하지 않으면 subject 등록 시점으로 버전 관리가 진행된다.

2. ECS에서 인스턴스를 추가해준다.

   - EN_SQ_02 (ECS ID), Informed consent date is the date on which version management is based and cannot be modified (Message)를 입력해준다.

   - `Force save` 항목은 체크를 해지한다.

     - ICDTC가 한번 입력된 후에는 수정이 불가능하도록 하기 위해서

   - target은 `ICDTC`로 설정한다.

   - 로직은 다음과 같다.

     ```markdown
     NE(ITEM(ICDTC), ITEMP(ICDTC))
     ```

     - ITEMP: Previous Item Answer Data

3. `ECS > Version`으로 이동하여 새로운 ECS version을 추가한다.

   - Version에 `2.00`을 입력하고 Description은 적절하게 작성한다.

4. 다음으로 `Entry > Version`으로 이동하여 새로운 버전을 추가한다.

   - Version은 앞에서 입력한 `2.00` 버전을 입력
   - Descrpition은 적절하게 입력
   - Effective Date는 현재 날짜보다 이전에 CRF 변경에 대한 결정이되므로 과거날짜로 기록
   - ECS Version ID도 ECS Version과 동일하게 입력

5. `CDMS > Admin > User > Site`로 이동하여 version control 적용 기준일을 설정한다.

   - Version 2.00의 적용일(effective date)를 앞에서 설정한 날짜를 등록한다.
   - 보통 IRB 승인일로 한다.

- :ballot_box_with_check: 방금 설정한 적용일에서 Version 2.00의 적용일 이전에 ICDTC가 작성되었다면 Version1로 CRF가 설정되고, 이후에 ICDTC가 작성되었다면 Version2로 CRF가 설정된다.

6. `Builder > Entry > Schedule`에서 version을 지정하고 각각 다른 스케줄을 추가하여 사용할 수 있다.
   - 삭제를 하는 경우에는, 해당 version에서 `deleted`를 yes로 설정하는 것이 아닌 `visible`을 no로 설정해준다.
7. CDMS에서 Version 2.00 기준일에 따라 ICDTC가 다른 subject를 입력하고, version에 따라 설정한 schedule이 알맞게 표시되는 것을 확인한다.

> 다음으로는 2.00버전에서 선정기준 4번을 삭제해본다.

1. `Entry > CRF Page > IE` 페이지를 클릭하고 `Version Up` 버튼을 클릭한다.
2. 2.00 버전을 선택하고 save 버튼을 클릭한다.
3. 새로 생긴 2.00 버전에서 `IN04` QST을 삭제한다.

> 이제 2.00 버전에서 제외기준 5번을 추가해본다.

- 2.00 버전에서 `EX05` QST를 추가한다.
  - 이 경우, 1.00 버전에서도 동일한 `EX05` QST가 추가되는 것을 확인할 수 있다.
  - :white_check_mark: 추가/삭제하였어도 `show deleted`를 포함하여 1.00버전과 2.00버전의 page, crf, qst, item의 개수가 동일하여야 한다.

> **ECS version control**

- ECS instane를 생성하는 시점에서 version을 `2.00`으로 선택하면 된다.
- 기존에 존재하는 instance의 경우 리스트에서 오른쪽의 `Version up` 버튼을 클릭하면 된다.
- 그리고 1.00세는 동작하고 2.00에서는 동작하지 않도록 하기 위해서는 instance의 version은 `2.00`으로 설정하고, expired는 `Yes`로 설정하면 된다.



***Copyright* © 2021 Song_Artish**