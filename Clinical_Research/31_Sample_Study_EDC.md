# Sample Study EDC

2021.07.12

---

[TOC]

---



## Various EDC page

### 1. Item Group을 이용한 Check box 설정

**1.1 하나의 QST내에 2개 이상의 Check box layout을 설정해야 하는 경우**

- QST 내에 첫번째 Item으로 Layout이 `GROUP`인 item으로 생성한다.
- 그리고 GROUP item의 child로 `check box layout`을 설정한다.

**1.2 하나의 QST내에 2개 이상의 Group을 설정하는 경우**

- QST 내에 첫번째 ITEM으로 Layout이 `GROUP`인 item을 생성한다.
- GROUP item의 child로 또 다시 layout이 `GROUP`인 item을 두개 추가한 후에 각 item에 `Check` layout을 설정한다.
- `Parent GROUP ITEM`에는 `CHILD_PLACEMENT` Property를 설정한다.



### Innter Table

> 행 추가가 가능한 Table Question 내에서 다시 하위 행을 추가할 수 있는 구조이다.

- 기본적인 Table Question 하위에 layout이 `INNERTABLE`인 item을 생성한다.
  - 이 item은 INNTERTABLE내 `+` 버튼을 추가하기 위해서이다.
- layout이 `INNTERTABLE`인 item이 생성되면 Table QST에서 하위 QST을 생성할 수 있는 버튼이 보이게 된다; `Add Question` 버튼
- 기존에 생성한 Table QST에서 하위 Table QST을 추가한다.
- 추가한 Table QST에 하위 행 추가가 필요한 `항암제명, 투여경로, 1일투여량, 단위, 투여일` ITEM을 생성한다.
- Table QST의 `LAYOUT_WIDTH`라는 propert로 Innter table 내 행 추가 버튼 컬럼도 포함하여 %비율을 맞춰준다.

## Central&Local Lab



## ATC



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

- 보고서 작성을 완료하면 mail report privilege가 있는 모든 사용자의 이메일로 SAE 보고서가 전송된다.

  - :white_check_mark: 메일 전송 관련 사항은 `BUILDER > ROL&PRIV> > PRIVILEGE`에서 `MAIL` privilege 검색해서 참고한다.



***Copyright* © 2021 Song_Artish**

