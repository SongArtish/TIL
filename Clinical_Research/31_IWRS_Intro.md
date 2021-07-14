# IWRS Intro

2021.07.14

---

[TOC]

---



## Role & Flow

> IP allocation 과정은 다음과 같다.

- 역할을 다음과 같다.

|    Subject     |                        Role                        |
| :------------: | :------------------------------------------------: |
|     **PI**     |     randomization, IP allocation, prescription     |
|    **IPM**     |           IP 보관 및 pharmacy에 delivery           |
| **Pharmacist** | IP receipt & allocation 후 subject에게 IP dispense |
|   **PM/CRA**   |     site에 IP배송 요청 및 pharmacy monitoring      |

- 흐름은 다음과 같다.

|         Stage         |          Subject           |                         Explanation                          |
| :-------------------: | :------------------------: | :----------------------------------------------------------: |
|       배송요청        | PM<br />(Sponsor의 위임자) | - 환자 등록여부에 대한 알람(시스템)이 PM에게 전달된다.<br />- PM은 현황을 파악하여 IPM에게 IP 배송을 요청한다. |
| **Delivery** (IP배송) |            IPM             |       창고(warehouse, stock)의 약을 약사에게 배송한다.       |
|  **Dispense** (불출)  |         Pharmacist         |                약사가 subject에게 약을 준다.                 |
|   **Return** (반납)   |          Subject           |            Subject가 약사에게 남은 약을 반납한다.            |
|     **CRA Sign**      |            CRA             |                  CRA는 문서에 서명을 한다.                   |

- 처방 과정도 존재한다. (의사가 subject에게 약을 처방한다.)
- **trigger**
  - **trigger level**: DRUGID 수량이 trigger level에 도달하면 시스템에서 배송요청이 된다.
  - **maintenance level**(유지수량): pharmacy에서 유지해야할 DRUGID의 수량



## Randomization

### 종류

> randomization에는 2가지가 있다.
>
> - **Group (TRT/CNT)**
> - **IP**

- 아래의 표는 randomization 예시이다.

| RNNO | GROUP | 처방  | IPNO  |      | USED |
| :--: | :---: | :---: | :---: | :--: | :--: |
| R001 |  TRT  | IP001 | IP001 | TRT  |  Y   |
| R002 |  CNT  | IP004 | IP002 | TRT  |  Y   |
| R003 |  TRT  | IP002 | IP003 | TRT  |      |
| R004 |  CNT  | IP005 | IP004 | CNT  |  Y   |
| R005 |  TRT  |       | IP005 | CNT  |  Y   |
| R006 |  CNT  |       | IP006 | CNT  |      |

- Double-blind: neither the subjects nor the investigator are aware of the treatment assignment.

### Random ID & Code

- Random ID: 통계에서 생성한 group 정보를 포함한 코드
- Random Code: random ID를 customization, 즉 다른 형식으로 formatting한 코드

### Stratification

- 다음표는 성별로 층화(stratification)를 한 예시이다.

| SEX  | RNNO  | GROUP |
| :--: | :---: | :---: |
|  M   | RM001 |  TRT  |
|  M   | RM002 |  CNT  |
|  M   | RM003 |  TRT  |
|  M   | RM004 |  CNT  |
|  F   | RF001 |  TRT  |
|  F   | RF002 |  CNT  |
|  F   | RF003 |  TRT  |
|  F   | RF004 |  CNT  |

- 보통 기관별로 층화를 나누는 **기관층화**를 많이 사용한다.

  | 기관 |  RNNO   |
  | :--: | :-----: |
  | SNU  | RSNU001 |
  | SMC  | RSMC001 |
  | AMC  | RAMC001 |
  | SNU  | RSNU002 |
  | SMC  | RSMC002 |
  | AMC  | RAMC002 |

  



## IP

### Drug Category

> IP Delivery 혹은 IP Labeling 시 구분되는 단위

- 임상시험 각 단계(epoch), 약물용량(dose) 처방기간(duration or period), 기타 임상시험약물여부에 따라 결정된다.

|   Category   |                         Explanation                          |
| :----------: | :----------------------------------------------------------: |
|  **Epoch**   |       run-in, treatment와 같이 임상단계에 따라 구분됨        |
|   **Dose**   | Subject/임상시험 특성에 따라 용량을 구분<br />(예를 들어 남자에게는 10mg, 여자에게는 5mg) |
| **Duration** | 임상시험 스케줄에 따라 1주, 4주 등으로 구분될 수 있음 (방문 간격) |
|     기타     |             background therapy or rescue therapy             |

- epoch은 시점에 따라 복용하는 약물을 달리하는 단계를 의미하는데, `run-in`은 예를 들어 본격적인 treatment 전에 조건을 같게 하기 위해서 동일한 성분을 복용하게 하는 screening 과정의 단계를 말한다.

### Drug ID

- 각 Drug Category 내 하위 구분으로, 대부분 random group과 동일하다.
- 즉 대부분이 blind 대상이 된다.

### Count

- Drug Category > Duration과 대비되는 개념으로, 각 방문별 기간이 일정하지 않은 경우 한 종류의 drug category에서 원하는 수량만큼 처방할 수 있다.

### Schedule

- Random Group에 따라 visit schedule별 dose를 반영하여 drug ID를 세팅할 수 있다.
- 즉 특정 subject가 랜덤 이후 각 visit별로 subject의 condition 혹은 protocol 특성(dose)에 따라 durg ID를 배정받을 수 있다.



***Copyright* © 2021 Song_Artish**