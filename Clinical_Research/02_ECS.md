# Edit Check Specification

> Edit Check에 대한 명세서

2021.07.08

---

[TOC]

---



## Structure

### Main & Instance

> **Main은 instance의 집합**이다.

- CRF Group과 ECS type에 따라 구분한다.

> **Instance는 각각의 ECS 객체**이다.

### ECS Type



| ECS Type |                                                    |
| :------: | :------------------------------------------------: |
|  **SQ**  |                                                    |
|  **BL**  | 페이지 내에 있는 항목(CRF, QST, ITEM)을 blind한다. |
|  **LF**  |                      자동계산                      |
|  **NA**  |                   NV, NS로 구성                    |

- ECS ID는 다음과 같이 구성하면 좋다.
  - `<CRF Group ID 순서>.<CRF Group ID>_<ECS ID>`



- :ballot_box_with_check: blind만 target이 `CRF, QST, ITEM`이 올 수 있고, 나머지는 모두 ITEM을 target으로 한다.



\#Instance 구성

- **Target:** Instance가 동작하는 위치

- Node:

   

  Logic Tree, 즉 Function의 조합

  - Source(LF일 경우)
  - Condition(LF 외)

- Relation:

   

  Target과 Node의 각 Item의 관계

  - Visit, Table QST에 의해 결정됨
  - Type
    - SAME
    - Previous, Next
    - No Relation
    - 기타 특수 관계
  - 기타: 외부에서는 Single page, Cross page 쿼리와 같이 구분하기도 하나 cubeBUILDER내에서는 무의미 함

- 관계는 반복되는 것(SV, QST_TB)에서만 나타난다



## ID Naming Convention

- 

## ECS Type



## Function 구조



## Relation

### 대소비교

우선 숫자와 날짜만 비교한다.

- Numeric: GT, LT, GE, LE
- Date: DGT, DLT, DGE, DLE
- LELE, LELT, LTLE, LTLT도 위와 같이 Numeric, Character, Date type이 있음
  - range를 비교할 때
  - LE+LE, LE+LT -> 100 <= A <= 200
- Character의 대소비교는 속성상 거의 사용되지 않음
  - 참고로 이런게 있다
  - Character: CGT, CLT, CGE, CLE

### 같다다르다

- EQ, **N**EQ, EQ**E**(Except Empty: 둘 다 값이 있을 경우 비교)
  - equal.
- NE, **N**NE, NE**E**
  - not equal?
- 속성상 NEQ, NNE는 거의 상용되지 않음

### null

- EM: NULL을 체크
- EMS: NULL or INIT을 체크
  - INIT: initialize, 초기 상태
- :white_check_mark: INIT상태, 즉 page가 저장되어 있지 않으면 ECS logic이 시행되지 않기 때문에 이러한 경우 EMS를 사용



Date, Time

- ADDD(ADD Days): 28일 후, 3일 전
- ADDM(ADD months): 3개월 이내
- DFDD(Difference of Dates): 2개 날짜의 차이
- DFDM(Difference of Date & Time): 투약후 30분, 48시간
  - return 값이 min(분)
- CMTD(Commit Date): 현재 시간(저장시간)
  - page 저장시간



String, text

- SPLIT
  - 구분자를 기준으로 앞/뒤를 split
  - 예시) CMINDCAE ==> 1^감기
- CUT
- CCAT,  CLIST
  - concatenate(`&)
  - CCAT: 그냥 텍스트를 합침
  - CLIST: 구분자를 넣어서 텍스트를 합침
- LOWER, UPPER  
- LEN



Control, Condition

 IF를 응용해서 사용함, DCD만 Normal Range에서 Library로 사용. , NVL은 Library에 부분 적으로 빈번하게 사용됨

- IF
- DCD
- CASE
- NVL: NOT NULL인 첫 인수의 값을 반환

:small_red_triangle: NVL(AGE, TRUE)

- 인수 중 값이 있는 첫번째 인수의 값을 반환



Logic

 AND, OR==>ANY, NOTOR는 사용하지 않는다! 대신 ANY를 사용한다.

***Copyright* © 2021 Song_Artish**