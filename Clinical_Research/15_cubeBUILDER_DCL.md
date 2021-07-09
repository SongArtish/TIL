# cubeBUILDER DCL

> Data Control Language

2021.07.09

---

[TOC]

---



## 1. Normal Range

> 여기서는 LB 정상범위를 설정해본다.

### Spec

> `CRF for EDC 문서 > 실험실검사` 페이지를 참고하여 SPEC을 결정한다.

1. `DCL > Noraml Range`에 들어가서 문서를 바탕으로 spec 정보(검사명)를 입력한다.
   - :white_check_mark: 아래 `Template download`를 클릭하여 다운로드한 문서를 다시 일괄 `Upload`하여 입력하는 것도 가능하다.
   - Category 항목은 실험실검사 종류를 입력한다. (예 - 혈액화학적검사, 뇨검사 등)



### Value

> 앞에서 설정한 spec에 따라 각 기관별 검사항목에 따른 나이, 연령 등의 기준으로 정상범위를 등록한다.

:heavy_exclamation_mark: Value 관련 기능은 Builder에서 CDMS로 이관되었기 때문에, CDMS에서 진행한다.

1. CDMS에 SPM role로 접속하여 Admin > Lab 메뉴로 들어간다.

2. `Template download`를 클릭하여 파일을 다운로드 한다.

   - `NEW` 버튼을 클릭하여 생성해도 되나, 보통 과제에서는 여러 개의 정상범위를 적용해야 하므로 template을 사용하는 것이 편리하다.

3. 다운로드한 엑셀 파일을 열어서 `Low, Upper, Low ratio, Upper ratio, Low equal, Upper equal, Deleted` 값을 입력해준다.

   |   Spec Value 항목   |                           설명                            |     return 값      |
   | :-----------------: | :-------------------------------------------------------: | :----------------: |
   |      **Unit**       |                           단위                            |                    |
   |     **Target**      |                  뇨검사 부분관련 text 값                  | Positive, Negative |
   |    **Low/Upper**    |                    정상 하한값/상한값                     |                    |
   | **Low/Upper ratio** |          정상으로 간주할 수 있는 하한/상한 범위           |                    |
   | **Low/Upper equal** |         하한값/상한값을 범위에 넣을 것ㅇ니지 설정         |         YN         |
   |     **Deleted**     | 조건이 바뀌어 필요 없는 항목일 경우 "Y"로 표시하여 업로드 |         YN         |

   - `Upper ratio`의 경우, 10이 정상이고 Upper ratio가 3이라면 30(10*3) 이상 값이 올 경우 Query를 발생하는 로직 구현 시 사용한다.

4. 작성한 엑셀 파일을 CDMS >Admin > Lab에 다시 업로드한다.

5. Builder > CRF Page > LB의 각 행에 `Spec` 옵션이 표시된 것을 확인할 수 있다.

6. LB의 각 행에서 알맞은 Spec 옵션을 선택해준다.

   - 이걸 하기 이전에 LB Page의 type이 `Laboratory Test`인지 확인한다.

7. 완료하면 Entry Search 메뉴에서 ID 검색창에 `LBORRES`을 입력하면 해당 내용을 확인할 수 있게 된다.



## 2. Medical Coding

> `DCL > Medical Coding` 메뉴에서는 **연구자가 입력한 병력/약력에 대해서 DM이 다시 코딩을 하는 기능을 세팅**한다.

- `Create` 버튼을 눌려서 카테고리 및 coder를 입력한다.
  - 예시 - MH(Category ID), Medical History(Category label, Description)
- Categoruy type 및 dictionary에서 적절한 값을 설정해준다.
  - 예시 - Medical Term > MedDRA
- :arrow_forward: 아래의 리스트는 **CMDS 코딩 메뉴에 있는 리스트의 column을 설정**하는 곳이다.
  - :exclamation: 필수로 체크되어 있는 `AE_NAME` column의 우측 item 창을 클릭해서 item을 연결해준다.
    - 예시 - `MHTERM(MH)`
  - relationship이 있는 항목의 경우, `RELATION`에 visible을 체크해주고, 아이템에 `-REL`도 추가해준다.
- 그리고 저장을 해준다.
- 실습에서는 <u>MT, AE, CM</u>을 Medical Coding List에 추가해준다.



## 3. Menu

> **CDMS에서 사용하는 각 메뉴의 column을 정의하는 공간**

- 필요한 column을 추가하거나 필요 없는 column은 보이지 않도록 설정 가능하다.
- 그 밖에 column label 수정이 필요한 경우에는 `Col Alias`을 수정하면 된다.



### 대상자 Status 설정

> 임상시험에서 사용되는 status 값은 5가지로 분류된다.

|     대상자 status     |                          설명                           |
| :-------------------: | :-----------------------------------------------------: |
|     **Screening**     |               대상자를 등록만 해놓은 상태               |
| **Screening Failure** | 선정 제외 기준을 만족하지 못하여 스크리닝 탈락한 대상자 |
|      **Ongoing**      |  선정 제외 기준 만족한 후에 무작위 배정을 받은 대상자   |
|     **Drop out**      |        무작위 배정 받은 후에 중도 탈락한 대상자         |
|     **Complete**      |              모든 임상시험을 완료한 대상자              |

- 모든 `status`의 대상자 수를 합산한 값은 전체 대상자 수의 값과 동일하다.

1. `Builder > DCL > Menu > Menu Tree> Subject > 2번째 Subject 메뉴`를 클릭한다.

   - 1번째 Subject 메뉴 - INV를 제외한 나머지 SPONSER role을 가진 user가 보이게 되는 리스트
   - 2번째 Subject 메뉴 -  INV user들의 리스트

2. `SUBJ_STATUS` column의 `USE code` 버튼을 클릭한다.

3. 나타나는 창에서 위의 5가지 status를 <u>순서대로</u> 입력하고 visible을 체크한 후 저장한다.

   - 여기까지는 단순히 CDMS의 리스트에 나타날 필터 목록을 정의한 것에 불과하다.

4. 다음으로는 `특정 데이터를 입력했을때 해당 status가 반환`될지에 대한 **event를 적용**한다.

   - 조건은 다음과 같다.

     |          status           |                        condition                         |
     | :-----------------------: | :------------------------------------------------------: |
     |     **Screening(00)**     | 별다른 조건 필요 없음<br />(대상자를 등록만 해놓은 상태) |
     | **Screening Failure(01)** |           IEYN item이 `No`으로 선택되었을 경우           |
     |      **Ongoing(02)**      |           RNYN item이 `Yes`로 선택되었을 경우            |
     |     **Drop out(03)**      |         DSDECOD가 `Withdrawal`로 선택되었을 경우         |
     |     **Complete(04)**      |         DSDECOD가 `Completed`로 선택되었을 경우          |

5. 먼저 Screening Failure 조건을 설정하기 위해 `Builder > Entry > CRF Page > IEYN item`으로 이동한다.

6. `EVENT`에서 status 번호에 알맞은 이벤트 `SUBJ_STATUS.L1.01`을 선택하고 `Value Type = Specify`, `Value = 2`로 설정하고 저장한다.

   - 여기서 `Value = 2`는 `No`를 선택했을 경우를 의미한다.
   - `Yes`일 경우에는 해당 item에 맞게 한다. 보통은 `Value = 1`로 세팅하면 된다.

7. 이외의 status도 조건에 맞게 item에 event를 설정해준다.



***Copyright* © 2021 Song_Artish**
