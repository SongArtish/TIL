# cubeBUILDER DataSet

> Entry에 연구자가 입력한 Data Set을 추출할 수 있도록 구성하는 작업이다.

2021.07.07

---

[TOC]

---



## 1. Entry Search

> Entry Search를 이용하여 Self QC를 진행한다.

- `BUILDER > Entry > Entry Search`에서 각각의 item 등이 잘 입력되었는지 리스트 형태로 확인할 수 있다.

### Sub Item 확인

>  연구자가 입력한 data를 출력하기 위해서는 반드시 **Sub Item**이 입력되어야 한다.

- :ballot_box_with_check: **출력하지 않아도 되는 item**의 경우에는 **Sub item을 `-`으로** 입력한다.
  - :arrow_forward: Sub item 검색창에 `-`를 입력하고 검색한다.
  - dummy item 외에 `-`로 sub item이 입력된 item이 존재한다면, 올바른 sub item을 입력해준다.



## 2. Main

> `Builder > Dataset > Dataset`으로 접속하면, 경고창과 함께 domain key 값을 입력해야하는 필드들이 나타난다. 해당 필드들을 `Create` 버튼을 눌려 Non CRF를 추가해준다.

- 쉽게 말해 foreign key를 연결해주는 과정인 것 같다.
- :white_check_mark: NonCRF - 사용자가 입력하지 않아도 시스템의 정보를 불러오는 것을 의미
- 입력 데이터 값들을 `DB Spec` 문서를 참조한다.

### Subject ID

> 모든 데이터셋에 Subject ID를 연결해준다.

- NonCRF Label: `Screening No.`
- Variable ID: `SUBJID`
- Domain은 `ALL`을 체크해준다.

> 나머지 항목들도 `DB spec` 문서를 참조하여 동일하게 입력한다.

### 기타 항목 설정

> 기타 설정 항목은 해당 데이터가 필요한 domain을 선택하여 추가하도록 한다.

|         NonCRF         |                             설명                             |
| :--------------------: | :----------------------------------------------------------: |
| **Item Category ID 2** | LB(static table) 등에서 seq 다음의 **검사명**(예 - LB.2.Hemo에서 Hemo)을 가져온다. |
|   **Dataset Domain**   |                 해당 domain의 입력을 붙인다.                 |
|    **ATC & MedDRA**    | 설정한 각각의 도메인에 ATC, MEDDRA의 코딩 변수가 함께 출력된다. |
|   **Team Id & Name**   |                 해당 대상자의 팀 id 및 이름                  |
|          기타          |          CRF 버전, 연구자 성명, 마지막 저장 날짜 등          |

- `ATC - Anatomical Therapeutic Chemical`
- `MedDRA - Medical Dictionary for Regulatory Activities`

### Entry Import

> 설정한 NonCRF 및 CRF를 함께 데이터셋으로 출력하기 위해서

- `Data Set > Data Set > Main`에서 `Entry Import`를 클릭한 후 `CRF`를 체크하고 `Confirm` 버튼을 눌려준다.
- 다음으로 나타나는 화면(`Log`)에서 success 여부를 확인할 수 있다.
- **:ballot_box_with_check: 이후 Entry를 변경한 경우, 반드시 Entry Import를 다시 진행해준다!**



## 3. Domain

> `Data set > Data set > Domian` 탭은 생성한 CRF 및 NonCRF 영역을 확인할 수 있다.

- :ballot_box_with_check: `Domain` 탭 좌측 상단의 파란색 글씨의 `Entry 최종 수정 시간`보다 `Domain` 탭의 최근 `Input time`이 항상 더ㅗ 최신이어야한다!
- :white_check_mark: `Variable, Variable Item` 탭에서도 Domian 탭과 같이 생성한 데이터들을 확인할 수 있다.



## 4. Entry Validation

- `Data set > Data set > Main` 탭에서 `DB Spec.` 파일을 다운로드 한다.
- `Log` 탭으로 이동하여 다운받은 DB Spec 파일을 업로드 해준다.
- 업로드 하면 나타나는 `Upload File` 탭으로 이동하여 log 기록을 클릭한다.
- `Entry Validation Report` 버튼과 `Data Structure Validation Report`를 클릭하고 파일을 다운로드하여 **작성한 데이터가 잘 작성되었는지 비교검사를 한다.**



## 5. CDMS에서의 데이터 출력

> 이렇게 설정하면 CDMS에서 설정한 데이터 내용을 출력할 수 있다.

- CDMS에서 `DM` role로 과제에 접속한다.
- `Data > DataSet > DataSet`으로 접속해서 데이터를 출력할 수 있다.



***Copyright* © 2021 Song_Artish**
