# Edit Check Specification

> Edit Check에 대한 명세서

2021.07.08

---

[TOC]

---



## Structure

```markdown
### ECS 계층
Main > Instance
```

### Main

> instance의 집합

- CRF Group과 ECS type에 따라 구분한다.

### Instance

> 각각의 ECS 객체

- **instance의 구성**은 다음과 같다.

  |     요소     |              정의              |                    종류                    |
  | :----------: | :----------------------------: | :----------------------------------------: |
  |  **Target**  |    instance가 동작하는 위치    |                                            |
  |   **Node**   | logic tree, 즉 function의 조합 |    source(LF인 경우), condition(LF 외)     |
  | **Relation** | target과 node의 각 item의 관계 | SAME, Previous&Next, No Relation, 특수관계 |

  - :white_check_mark: 관계는 반복되는 것(SV, QST_TB)에서만 나타나므로, relation은 Visit, Table QST에 의해 결정된다.

### Naming Convention

|     요소     |                   Convention                   |
| :----------: | :--------------------------------------------: |
|   **Main**   | `<CRF Group ID No.>.<CRF Group ID>_<ECS Type>` |
| **Instance** |     `<CRF Group ID>_<ECS Type>_<Seq No.>`      |



## ECS Type

| ECS Type |        Full Name        |                             기능                             |
| :------: | :---------------------: | :----------------------------------------------------------: |
|  **SQ**  |      System Query       |    SQ 조건에 맞는 데이터가 입력된 경우 시스템 쿼리를 발행    |
|  **BL**  |     Erase and Blind     | 조건에 맞는 페이지 내 항목(CRF, QST, ITEM)을 지우고 비활성화 |
|  **LF**  |       Link Force        | LF 조건에 맞는 데이터를 완전연동 (자동계산)<br />- 연동된 데이터는 직접 수정할 수 없다. |
|  **NS**  | NA Schedule(Not Commit) |   조건에 맞는 데이터가 입력된 경우 타겟 페이지를 비활성화    |
|  **NV**  |  NA Visit(Not Commit)   |    조건에 맞는 데이터가 입력된 경우 타겟 방문을 비활성화     |

- :ballot_box_with_check: BL만 target이 `CRF, QST, ITEM`이 올 수 있고, 나머지는 모두 ITEM을 target으로 한다.
- `Not Commit`은 저장된 페이지는 비활성화하지 않는 옵션이다.
- ~:white_check_mark: `SQ`는 숫자와 날짜와 관련된 range를~
- 기타 타입
  - **Goto Page(GP)**: RADIO 레이아웃의 아이템에서 특정 code가 선택 된 후에 페이지가 저장이 되면 해당 code 옆에 다른 페이지로 이동할 수 있는 링크가 표시 되도록 하는 기능
  - **Dynamic Comment(DC)**: QST 하단에 고정 코멘트를 지정하고 그 코멘트 내에서 특정 페이지 링크를 설정하여 이동할 수 있도록 하는 기능



## Function

- function의 구조는 다음과 같다.

  ```markdown
  - LEAF
  - Argument(인수)
  - Return Value
  ```

  - `Return Value`는 T/F(True, False, Null), value, count가 될 수 있다.
  - :white_check_mark: 함수에 붙어있는 `ITEM`을 `LEAF`라고 한다.



## Relation

### 대소비교

> 대소비교는 우선 숫자와 날짜만 비교한다.

|    Type     |          함수          |                         설명                         |
| :---------: | :--------------------: | :--------------------------------------------------: |
| **Numeric** |   **GT, LT, GE, LE**   |              Greate/Less Than, or Equal              |
|  **Date**   |   DGT, DLT, DGE, DLE   |                  앞에 D를 붙여준다.                  |
|             | LELE, LELT, LTLE, LTLT |                     양방향 비교                      |
|    Char     |   CGT, CLT, CGE, CLE   | 앞에 C를 붙여준다.<br />(char 대소비교는 거의 사용X) |



### 같다/다르다

|       함수       | **의미**  |                 comment                 |
| :--------------: | :-------: | :-------------------------------------: |
| **EQ**, NEQ, EQ  |   Equal   | Except Empty: 둘 다 값이 있을 경우 비교 |
| **NE**, NNE, NEE | Not Equal |                                         |

- :white_check_mark: `NE` vs `NEE`

  | function |          name          |         description          |         factor         | return value |
  | :------: | :--------------------: | :--------------------------: | :--------------------: | :----------: |
  |  **NE**  |       Not Equal        | 문자열 비동일 비교 결과 반환 | 2개의 인수(문자, 필수) |  true/false  |
  | **NEE**  | Not Equal Except Empty | 문자열 비동일 비교 결과 반환 | 2개의 인수(문자, 필수) |  true/false  |

  - NULL 문자를 포함하여 비교한다.
  - :ballot_box_with_check: **인수 중 NULL 문자가 존재하는 경우**
    - `NE`는 인수가 모두 NULL인 경우 false를 반환
    - `NEE`는 인수 중 하나라도 NULL이 존재하는 경우 NULL문자를 반환

  ```markdown
  ## 요약
  # 공통점
  - 2개의 문자열이 서로 다른지를 체크
  # 차이점
  - NE는 인수가 모두 NULL인 경우 false를 반환하는 반면, NEE는 인수 중 하나라도 NULL이 존재하는 경우 NULL문자를 반환
  ```




### NULL

> Relational.Empty Function (empty)

| function |        name        |                  description                  |      factor       | return value |
| :------: | :----------------: | :-------------------------------------------: | :---------------: | :----------: |
|  **EM**  |       Empty        |         인수값이 NULL문자열인지 점검          | 인수1 (문자,필수) |  true/false  |
| **EMS**  | Empty or not saved | 인수값이 NULL 또는 **INIT 문자열**인지를 점검 | 인수1 (문자,필수) |  true/false  |

```markdown
## 요약
# 공통점
- NULL 값인지 체크한다.
# 차이점
- EMS는 저장되지 않았는지도 검사한다.
```

- :ballot_box_with_check: 헷갈릴 때는 더 강력한 **EMS를 사용**!
- :white_check_mark: **INIT(initialize, 초기 상태상태)**, 즉 page가 저장되어 있지 않으면 ECS logic이 시행되지 않기 때문에 이러한 경우 EMS를 사용
- :small_red_triangle: **참고** - **EMN** (Not Empty)
  - 인수값이 NULL문자열이 아닌지를 점검
  - 인수값이 NULL 인 경우 FALSE가 반환
  - 인수값이 INIT(미저장) 상태인 경우 NULL이 반환 :heavy_check_mark:



### Date & Time

|   함수   |          의미           |            기능            |
| :------: | :---------------------: | :------------------------: |
| **ADDD** |        Add Days         |   특정일 이후 일을 계산    |
| **ADDM** |       Add Months        |  특정월 이후 월 값을 반환  |
| **DFDD** |   Difference of Dates   | 2개 인수의 일수 차이 반환  |
| **DFDM** | Difference of Date&Time | 2개 인수 min(분) 차이 반환 |
| **CMTD** |       Commit Date       | 현재 시간 (page 저장시간)  |



### String & Text

|        함수        |                             기능                             |
| :----------------: | :----------------------------------------------------------: |
|     **SPLIT**      | 구분자를 기준으로 앞/뒤를 split<br />(예시 - CMINDCAE ==> 1^감기) |
|      **CUT**       |                     문자열을 자르는 함수                     |
|  **CCAT,  CLIST**  | CCAT: 그냥 텍스트를 합침<br />CLIST: 구분자를 넣어서 텍스트를 합침 |
| **LOWER, UPPER  ** |                                                              |
|      **LEN**       |                                                              |



### Control & Condition

>  IF를 응용해서 사용한다.

- `DCD`만 Normal Range에서 Library로 사용
- `NVL`은 Library에 부분적으로 빈번하게 사용

|  함수   |              설명              |
| :-----: | :----------------------------: |
| **IF**  |             조건문             |
|   DCD   |                                |
|  CASE   |                                |
| **NVL** | NOT NULL인 첫 인수의 값을 반환 |

- :small_red_triangle: NVL 예시 - NVL(AGE, TRUE)



### Logic

|  함수   | 설명 |
| :-----: | :--: |
| **AND** |      |
| **ANY** |      |
| **NOT** |      |

- OR는 사용하지 않는다! 대신 ANY를 사용한다.



### Aggregate

> Aggregate Function(집계 함수)은 반복이 발생하는 구조(Visit, TB)에만 적용할 수 있다.

**1. Aggregate**

> A는 `aggregate`를 의미한다.

|     Function     |         return         |
| :--------------: | :--------------------: |
|     **AROW**     |     마지막 행 번호     |
|  **AMAX, AMIN**  |        max, min        |
|     **ASUM**     |          sum           |
| **ADMAX, ADMIN** | Aggregate Date Max/Min |

**2. Aggregate Count**

|     Function     |                                      |           return           |
| :--------------: | :----------------------------------: | :------------------------: |
|    **ACCEQ**     |          Aggregate Count -           |   인수와 같은 값의 개수    |
| **ACDBT, ACNBT** | Aggregate Count Date/Numeric Between | 사이에 있는 날짜/숫자 개수 |
|     **ACNT**     |          Aggregate Count -           |      살아있는 행 개수      |



### Normal Range

> return 값은 T/F

**정상범위**

| 정상범위 function |            설명            |
| :---------------: | :------------------------: |
|      **NRR**      |        Normal Range        |
|     **NRLU**      | Normal Level Upper(상한치) |
|     **NRLL**      |  Normal Level Low(하한치)  |

**확장된 정상범위**

- NRE, NREL, NREU 등이 있다. (E - extended)



### Arithmetic

| function | 설명 |
| :------: | :--: |
| **ADD**  |      |
| **SUB**  |      |
| **MUL**  |      |
| **DIV**  |      |

| function  |    설명    |
| :-------: | :--------: |
| **ROUND** |            |
| **FLOOR** | 버림(바닥) |
| **CEIL**  | 올림(천장) |

| function  | 설명 |
| :-------: | :--: |
|  **LOG**  |      |
| **LOG10** |      |
|  **EXP**  |      |
|  **POW**  |      |
| **SQRT**  |      |

- `LOG`는 거의 사용하지 않는다.

| function |      설명      |
| :------: | :------------: |
| **MIN**  |                |
| **MAX**  |                |
| **MOD**  | modulo(나머지) |
| **AVG**  |                |
| **SUM**  |                |

- :white_check_mark: **ADD vs SUM**

  | function |   name    |           description            |        factor         | return value |
  | :------: | :-------: | :------------------------------: | :-------------------: | :----------: |
  | **ADD**  | Addition  | 인수로 입력된 숫자들의 합계 반환 | 1개 이상의 인수(숫자) | 합계 or NULL |
  | **SUM**  | Summation | 인수로 입력된 숫자들의 합계 반환 | 1개 이상의 인수(숫자) | 합계 or NULL |

  - 인수 중 숫자형이 아닌 경우 합계에서 제외된다.
  - :ballot_box_with_check: **인수 중 NULL 문자가 존재하는 경우**
    - `ADD`는 **NULL을 반환**
    - `SUM`은 **NULL을 합계에서 제외**

  ```markdown
  ## 요약
  # 공통점
  - 인수로 입력된 숫자의 총합을 반환
  # 차이점
  - 인수 중 NULL 값이 있는 경우 ADD는 NULL을 return하지만, SUM은 NULL을 합계에서 제외
  ```


| function | 설명 |
| :------: | :--: |
| **ABS**  |      |
| **AGE**  |  ?   |



## ECS 순서

> NV, NS, Blind, Linkforce, System Query 순으로 ECS를 작성/고려해야 한다.

**NV**

subject가 등록되면 V1을 제외하고 모든 방문이 비활셔ㅓㅇ화 되어 있고 순서대로 활성되는 로직 구현

- IEYN이 Yes가 아니면 V2 비활성화
- IEYN이 No이면 V1 비활성화 (미저장 페이지)
- RNNO가 null이면 V3와 종료방문 비활성화
- V4 ~ 종료방문 직전 방문의 경우 이전 방문이 입력되지 않으면 비활성화
- DSCOMPL이 아니면 SVDTC없는 방문 비활성화

**NS**

- AGE, SEX가 입력되지 않으면 IE 페이지 비활성화
- AGE, SEX가 입력되지 않으면 LB 페이지 비활성화
- 가임여부가 Yes가 아니면 PG 페이지 비활성화
- RNNO가 null이면 DS페이지 비활성화
- Option: V2 IPDTC가 null이면 AE페이지 비활성화 등틍
- 참고
  - 남자는 임신검사를 않는다
  - 임상시험용 의약품 처방 & 투여는 default로 NS 처리한다.



**BLIND**

- YN, ND, NONE 체크시 해당 영역(CRF, QST, ITEM) 비활성화
- 가능한 item보다는 QST단위로 설정 (특수한 경우만 item에)

**Linkforce**

- 자동계산/입력 설정

**System Query**

- 저장가능: query 발생
- 저장불가: 저장되지 않음 (100% 확실한 경우에만 설정)
- 참고
  - MH는 BRTHDTC~V1DTC이어야 한다.



***Copyright* © 2021 Song_Artish**