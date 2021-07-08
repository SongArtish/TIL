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



## Function

- function의 구조는 다음과 같다.

  ```markdown
  - LEAF
  - Argument(인수)
  - Return Value
  ```

  - `Return Value`는 T/F(True, False, Null), value, count가 될 수 있다.



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



### NULL

> empty

|  함수   |        기능         |
| :-----: | :-----------------: |
| **EM**  |     null을 체크     |
| **EMS** | NULL or INIT을 체크 |

- :white_check_mark: **INIT(initialize, 초기 상태상태)**, 즉 page가 저장되어 있지 않으면 ECS logic이 시행되지 않기 때문에 이러한 경우 EMS를 사용



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
|      **CUT**       |                                                              |
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
| **OR**  |      |
| **ANY** |      |
|  NOTOR  |      |

- ANY, NOTOR는 사용하지 않는다! 대신 ANY를 사용한다?



***Copyright* © 2021 Song_Artish**