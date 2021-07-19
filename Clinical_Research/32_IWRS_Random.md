# IWRS Random

2021.07.13

---

[TOC]

---



## 과제 개요

> IP 배송/배정/불출 등의 과정을 제외한 random(무작위배정)을 진행하는 과제

- 본 과제의 층화예시는 **기관층화**만 설정한다.
- 배정군은 시험군, 대조군 2가지이다.



## 과제 진행과정

### Study 설정

1. `Builder > Study > Property > Property`에서 `Import`버튼을 클릭하고 `IWRSSUB_GL` 라이브러리를 import 한다.
2. `Study > Property > EDC > Enrollment number`에 `{RC}`, `Auto input`으로 설정되어 있음을 확인한다.
   - Enrollment number에는 통계팀에서 전달하는 random code를 업로드하여 사용할 예정이기 때문

### Entry > CRF Page 설정

1. `Entry > CRF Page > RN` page의 type이 `Enroll/Random Page`로 설정되어 있는 것을 확인한다.
2. `RNYN` item에서 `RANDOM.CRITERIA` 이벤트를 추가해준다.
   - value는 `specify, 1`로 지정한다.
3. RNYN이 설정되었을 때의 DTC를 자동으로 입력하기 위해서 `RNDTC`에 `RANDOM.DATE, SUPP_SUBJ.ENR_DATE` 이벤트를 추가한다.
   - value 타입은 `ALL`로 한다.
   - 또한 property에 `AUTOFILL`을 추가해주고 default missing check `No`로 설정한다.
4. 그리고 RNNO에 아래의 4가지 event를 추가해준다.
   - INITIALIZE.RAND_CODE : 무작위 배정번호를 받은 후에는 초기화 불가능
   - IWRS_CODE.RANDOM : IWRS를 통해서 업로드 된 무작위배정번호가 연동
   - SEND_MAIL.ENR_CODE : 무작위 배정번호가 입력 되면 알람 메일 발송
     - :ballot_box_with_check: Value Type이 "Not Empty"일때만 적용 되도록 설정한다.
   - SUBJECT.ENR_CODE : 무작위 배정번호가 필요한 곳에 해당 Data 연동
   - 마찬가지로 `AUTOFILL`과 default missing check `No`로 설정해준다.

### IWRS 설정

1. `Builder > IWRS > Property > Random`로 이동한다.
2. 여기서는 기관층화 및 랜덤번호 업로드를 사용할 것이기 때문에 `Stratified Block(Upload)`를 체크해준다.
3. No. of randomization은 무작위배정을 하는 횟수이며, `1`입력
4. Site는 기관(site)별로 진행하기 때문에 `Team`입력
5. No. of stratification은 층화 정보이며, 층화정보는 없기 때문에 `1` 입력
6. 배정군은 시험군, 배정군 2가지기 때문에 group = 2를 입력한다.
7. Stratification label에는 `RANDOM`이라고 입력한다.
8. Group Label에서 Random group은 `TRT, CTR`로 입력하고 저장한다.
   - 시험군, 대조군
9. `IWRS > RANDOM` 메뉴로 이동하여 `Template download > Test code`를 클릭하여 문서를 다운로드 한다.
10. Excel 문서의 Data 시트를 참고하여 code 시트를 작성한 후에 upload 버튼을 클릭하여 업로드한다.
    - sample 과제에서 업로드된 파일은 교재 사이트에서 다운로드하여 업로드하였다.
      - :white_check_mark: 다른 파일을 업로드 할 떄는 `Team ID`는 내가 설정한 site ID로 변경한 후 업로드한다! (아니면 업로드가 되지 않는다.)
    - :ballot_box_with_check: Code시트 작성시 반드시 층화별로 squence가 구분되어야 한다.
11. 업로드가 완료되면 `IWRS > RANDOM > GENERATION`에서 schema를 `Test code`로 선택해주면 업로드한 데이터를 확인할 수 있다.

- :ballot_box_with_check: Release할 때는 IWRS shcema를 Test code가 아닌 `Real code`로 업로드해야만 release가 된다.



***Copyright* © 2021 Song_Artish**
