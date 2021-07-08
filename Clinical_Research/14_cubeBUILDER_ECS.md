# cubeBUILDER ECS

> Edit Check Specifications. 함수를 이용하여 **조건문을 생성**하는 것

2021.07.07

---

[TOC]

---



:ballot_box_with_check: **ID Naming Rule**

- ECS ID는 다음의 규칙에 따라서 작성하도록 한다.

  ```markdown
  [페이지번호].[Domain명]_[ECS type]
  ```

- 예시) - 03.DM_SQ



## 1. System Query

> **Data가 바르게 입력되지 않은 경우에 Query를 발생**시킴

```markdown
#### 실습
- Alcohol은 반드시 `No`가 입력되어야하나 `Yes`가 입력됨
```

- `Builder > ECS > Main > Create` 버튼을 클릭하고 SQ(System Query)를 생성한다.
- 생성한 ECS 오른쪽 아이콘 중 `Instance Create` 버튼을 클릭하여 Instance Editor 페이지로 이동한다.
- ECS 명세 문서를 참조하여 `ECS ID`를 입력하고, `Message`에는 발행될 Querty 구문(보여줄 텍스트 문구)를 지정한다.
- Description에는 조건문을 설명해준다.
  - 예시 - if DM.Alcohol == Yes: publish Query;
- 아래의 `Node Tree > Target`에는 지정할 item을 연결해준다.
- 그리고 `Node Tree > +` 버튼을 눌려서 function에서 `EQ`(equal 검사)를 검색하고 추가해준다.
  - Item 값은 `DM > Alcohol`을 지정해준다.
  - 아래의 비교값은 data type을 `CONST`로 변경해주고 오른쪽 입력창에 `1`을 입력해준다.
- 저장버튼을 누르고 :star:CDMS에서 확인:star:을 한다.
  - :white_check_mark: `Instance Editor > Log View`를 클릭하면 CDMS에서 ecs 수행 결과를 확인할 수 있다.



## 2. Erase and Blind

> **조건에 따라 ITEM 또는 QST을 비활성화**

### QST Blind

```markdown
#### 실습
- MD에서 `ND`를 체크할 경우, 상세 항목 입력 테이블을 비활성화한다.
```

- 위와 동일하게 Main ECS 및 ECS instance를 생성한다.
- Node Tree의 target은 **비활성화 target**을 의미한다.
  - 따라서 target type을 QST으로 설정하고, item에 `MH_TB`을 입력해준다.
- `Node Tree > +` 버튼을 클릭하고 function으로 `EMN`(Not Empty)으로 설정한다.
- 위 function의 하위 item은 `MHND`로 설정해준다.

### Item Blind

```markdown
#### 실습
- Reason for Unscheduled Visit이 `Others`가 아닐 경우, `Others, specify` 항목 비활성화
```

- 위와 동일하게 명세에 따라 Main ECS와 ECS instance를 생성한다.
- Node Tree target으로 `SVUVRECO`를 입력한다.
- 다음으로 function으로 `NE`(Not Equal)을 추가한다.
  - `NE`은 문자열 비동일 비교 결과를 반환한다.
  - :white_check_mark: `EQ`(Equal)로 function을 사용하게 되면, 아무 것도 클릭하지 않았을 때도 `Others, specify`가 활성화되게 된다.



## 3. Link Force

> **입력된 data를 통해서 값을 연동**

```markdown
#### 실습
- 동의서 서명일과 생년월일을 이용하여 나이 계산
```

- ECS type을 Link Force로 지정하고 위와 동일하게 main, instance를 생성한다.
- target을 `AGE(DM)`으로 설정하고, `AGE`라는 ECS 함수를 추가해준다.
  - `AGE` 함수 설명을 보면 2개의 인수가 필요하다.
    - 인수1 (날짜, 필수): 기준날짜 (서면동의일, 방문일 등)
    - 인수 (날짜, 필수): 생년월일
- 따라서, 인수1에는 `EN > ICDTC`, 인수2에는 `DM > BRTHDTC` 아이템을 입력한다.
- :ballot_box_with_check: 앞의 SQ나 blind는 return 값이 논리값(T/F)였으나, Link Force의 경우 CONST 혹은 VAR을 반환한다.
  - 따라서, function root 값을 `condition`이 아닌 `source`로 반드시 변경해준다!
- 이렇게 `age` 값을 시스템에서 자동 입력해주기 때문에 `Entry > CRF Page > DM > AGE > Property`에서 `autofill`을 추가해주고, `Default Missing Check`를 `No`로 변경해준다.



## 4. NA

> **조건에 따라 VISIT 또는 SCHEDULE을 비활성화**하여 연구자가 CRF를 입력하지 못하다록 한다.

|    ECS Type     |                          설명                          |
| :-------------: | :----------------------------------------------------: |
|  **NA Visit**   |   schedule 화면에서 보이는 세로 열(Visit)을 비활성화   |
| **NA Schedule** | schedule 화면에서 보이는 가로 행(CRF Group)을 비활성화 |

|    NA Type     |                          설명                          |
| :------------: | :----------------------------------------------------: |
| **Initialize** |         저장된 page도 초기화 한 후에 비활성화          |
| **Not Commit** | 미저장된 page만 비활성화 (저장된 페이지는 그대로 유지) |

- NA Schedule 예시 - 남자일 경우, pregnancy test 행 비활성화

> 일반적으로 연구자가 입력한 data를 그대로 유지하며, 혹시 잘못 적용한 logic에 따른 data 초기화를 방지하기 위해 **대부분 `Not commit`으로 사용한다.**

```markdown
#### 실습
- V1에서 적합성 여부가 `아니오`인 경우 V2를 비활성화 (NA Visit)
```

- ECS Type을 `NA Visit(Not Commit)`으로 지정하고 main을 생성한다.
- Node Tree target을 SVDTC(SV)로 지정한다.
  - 그리고 명세에서 V1만 NA로 설정하라고 명시되어 있기 때문에, target의 visit을 `All`에서 `V1(NV`로 변경해준다.)
- :ballot_box_with_check: 보통 SVDTC(방문일)로 target을 지정한다.
- 그리고 `EQ` function을 추가하여 조건문을 완성한다.
- 저장 후 CDMS의 subj schedule표를 확인한다.
  - :ballot_box_with_check: **Not Commit**으로 설정하였기 때문에 저장되지 않은 Page(회색 사각형)만 비활성화(점서표시)되며, 저장된 Page(초록색 사각형)는 비활성화되지 않는다.



## 5. others

> 여기서는 심화된 ECS를 학습한다.

```markdown
#### 실습1
- V1 visit date 와 Date of informed consent의 차이가 0~28일이 아니면 Query 발생
```

- logical 구조를 잘 설계하여 Node Tree를 작성한다.

- 다음의 함수를 사용한다.

  - LELE(Less than or Equal, <= x <\): 숫자형 크기 비교, 인수1 <= 인수2 <= 인수3 의 결과를 반환

  - DFDD(Day Difference): 인수1과 인수2의 날짜차이를 반환

- :small_red_triangle: Node Tree에서 function대신 **Library**를 사용해서 위 로직을 작성할 수 있다.

**달러 표시 사용**

```markdown
Date of Visit 1[[$A$]] is not within 28 days after date of informed consent([[$B$]]).
```

- Message에 위와 같이 `[[Var]]`을 입력하면 변수를 사용할 수 있다.
- 해당 변수는 `Node ID`에서 정의해준다.

```markdown
#### 실습2
- AEND에 체크가 되어있지 않으나 AETERM이 하나도 없을 경우 Query 발생
```

- 명세서를 따라서 위와 동일하게 진행한다.
- `ACNT`(aggregate, count) 함수: Leaf에 지정된 Item값의 수를 반환합니다.
  - :ballot_box_with_check: 해당 function의 item `Row No.`는 `All Row Number`이 아닌, `All Row Aggregation`으로 설정해주어야 한다.
- :white_check_mark: 이 부분도 library에 `SQ_COUNT_02_TABLE(GL)`로 사용할 수 있다.

```markdown
#### 실습3
- Date of informed consent가 IRB Approval Date 이전인 대상자의 저장불가 Query 설정
```

- main과 instance를 생성한다.
- instance의 `Force Save `는 unchecked로 설정하여, 해당 조건을 만족하지 않으면 저장을 할 수 없도록 설정한다.
- functions
  - NVL(Null Value): NULL 또는 INIT이 아닌 첫번째 인수를 반환
    - `INIT` - 아예 저장조차 되지 않는 상태(데이터 X)
  - TIADT: Site IRB Approval Date
    - 과제 사이트를 생성할 때 설정한 IRB 승인일

```markdown
#### 실습4
- 연령에 따른 선정기준 관련 Query 설정
```

```markdown
#### 실습5
- AE에 대한 약물 치료가 있다고 기재되었으나 해당 AETERM이 CM 페이지에서 약물의 투여목적으로 기재되지 안ㅅㅎ았을 때 Query 조건 설정
```

- function

  - `IN`(In): 인수1이 인수2의 구분자로 분리된 token에 존재하는지 판별(존재하면 return `true`)
    - CONST에 2가지 숫자를 기입할 경우 그냥 `2,4` 이렇게 입력하면 된다.
  - `ACCEQ` (Equal Value Count): Leaf에 지정된 item값이 인수 리스트에 동일한 값이 존재하는 경우의 횟수를 반환
  - `CCAT` (Concatenate): 인수로 주어진 문자열을 연결한 결과를 반환

- 메시지를 다음과 같이 입력한다.

  ```markdown
  [Other action taken] is selected [[$A:CODE$]], but there are no prior and concomitant medications for which [Indication] matches the adverse event term [[$B$]]
  ```

  - :ballot_box_with_check: **`[[$A:CODE$]]`는 A에 입력된 값의 UI value를 반환**한다.

- :white_check_mark: 본 실습도 library에서 `SQ_COUNT_03_AECONTRT_TRT(GL)`로 바로 사용할 수 있다.

```markdown
#### 실습6
- CM Page에서 투여목적으로 선택된 AE과 AE page의 AETERM이 다를 경우 Query 발생
```

- CONST에 `EMPTY/DELETD` 입력하여, 가져온 값이 `EMPTY/DELETD`와 동일한지 비교한다.
  - 이외의 경우(수정한 경우 포함)에는 `AETERM`을 가져오게 된다.
- :heavy_exclamation_mark: 여기서 `AETERM`의 `Row Rel.`은 `Table Related Row Number`로 설정해주어야 한다.
  - AETERM에 사용된 term을 가져오게 related 기능이 작동된다.
- :white_check_mark: 본 실습도 library에서 `SQ_RELATED_02_TERM_NEE(GL)`로 바로 사용할 수 있다.

```markdown
#### 실습7
- Is the Subject eligible to participate in this clinical trial due to having satisfied all eligibility criteria?가 [Yes]일 경우에 V2 활성화
```

:white_check_mark: 본 실습도 library에서 `NV_NEXT_01(GL)`로 바로 사용할 수 있다.

```markdown
#### 실습8
- 성별과 연령이 입력되었을 경우에만 Local Laboratory Test 활성화
```

- ECS type을 **NA Schedule**(Not Commit)으로 설정하여 instance를 생성한다.

```markdown
#### 실습9
- 실험실검사 검사결과에 따른 정상/비정상 완전연동
```

> :small_red_triangle: 본 실습을 진행하기 위해서는 `DCL > Normal Range`가 설정되어 있어야 한다!

```markdown
Keyword
#LF #Multi_Instance
```

- ECS Type을 `LF`, `Muilti Inst.`를 `Yes`로 체크하고 Main을 생성한다.

- Multi Instance에서는 instance를 ID를 따로 작성할 필요가 없다.

  - 자동으로 개수에 맞게 생성될 예정이다.

- Target은 `LBNOR`이며, 처음에는 ST(static table) 의 첫 번째 요소를 입력한다.

- node 추가에서 library를 사용하여 `LF_NRR`을 추가한다.

- :ballot_box_with_check: **완전연동에서는 root type을 `condition`이 아닌 `source`로 변경해주어야** 한다!

  - 따라서 DCD node에서 root type을 변경하여 전체 root type을 `Source`로 변경한다.

- function

  - DCD(Decode) - 조건에 맞는 값을 선택하여 반환

    - 쉽게 말해 `DCD(a, b, c, d, e, f)`의 경우 다음과 같은 logic을 가진다.

    ```python
    if a == b:
        return b
    elif a == c:
        return d
    else:
        e
    ```

  - NRR(Normal Range) - Normal Range 이탈 시 TRUE를 반환
  
- CDMS에 가서 첫 번째 행이 잘 작동하는지 확인한다.

- 확인이 되면 Target에서 `+` 버튼을 눌려서 행을 4개 더 추가한다.

- 각 행에 맞는 item을 연결해준다.

- 그리고 Entry에서 Normality 항목에는 `autofill` property를 추가해준다.



## Validation

> `ECS > Main > Download ECS Log`에서 `Edit Check Validation`을 다운로드 받으면 ECS 작동 여부를 체크했는지에 대한 데이터를 확인할 수 있다.



***Copyright* © 2021 Song_Artish**
