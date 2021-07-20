# IWRS Validation

> `TD2518 V1.0_IWRS Validation Report_20200101` 문서를 참고하였다.

2021.07.20

---

[TOC]

---



## Validation

### Resource & Scope

- IWRS Validation process에 필요한 resource와 validation scope에 대한 내용은 아래 표와 같다.

| Validation Items |             Resource              |                            Scope                             |
| :--------------: | :-------------------------------: | :----------------------------------------------------------: |
|  Scenario test   | Study Manager \| DM / Team Leader |              IWRS의 각 기능에 대한 정의 및 검증              |
|  Random Code QC  | Study Manager \| DM / Team Leader | 실제 site에서 사용한 Random Code의 DB upload 적절성에 대한 Quality Check |

### Validation Criteria

- IWRS validation item 및 각 item에 대한 검증 적합기준, 검증 방법은 아래와 같다.

| Criteria for IWRS Deployment |                            Method                            |
| :--------------------------: | :----------------------------------------------------------: |
|        Scenario test         | IWRS의 User(role)별 각 기능을 업무 flow(Development Check List의 내용을 포함함)에 따라 정의 하고 각 기능에 대한 test data를 입력하고 scenario상 예측되는 결과(expected result)와 실제 결과(actual result)의 일치 여부를 확인하고 test data를 적절성의 근거로 한다. |
|    Random Code Upload QC     | 실제 site에서 사용할 Random Code를 DB에 upload하고 이를 다시 출력하여 원본의 data와 비교하여 일치함을 확인 한다. |



## Test Scenario

|  SN  |            Category            |                           Scenario                           |                      Expected   Result                       |
| :--: | :----------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|  0   |       Role &  Privilege        | Role별  권한을 설정하고, cubeIWRS에 SITE와 TEST에 필요한 User를 등록함 |      Role별 권한 설정됨[Role  & Privilege검증에서 확인]      |
|  1   |      IP Delivery Request       |               Manual Delivery로 배송을 요청함                | -Delivery메뉴에 해당 배송 요청 기록이 생성됨     -Drug Stock메뉴의 IP 재고 현황 조회 tab에서 요청한 수량이 배송요청에 표시됨     -IP배송 요청 메일이 (IPM)에게 발송됨 |
|  2   |          IP Delivery           |      IP Manager는 배송요청을 클릭하여 배송확인을 진행함      | -배송확인  화면이 생성되고 자료가 입력 됨     -Delivery메뉴에서 배송상태가 배송요청에서 배송중으로 변경되고 요청자와 IP manager의 서명이  포함된 출하요청서가 생성됨 (Pharmacy  정보 없을 경우에 출하요청서에 약사 정보 출력 되지 않음을 확인)     -Drug Stock 메뉴의 IP 재고 현황 조회 tab에서 해당 수량이  배송요청에서 감소하고 배송중에 증가하여 표시됨     -IP배송중  메일이 (Pharmacist)에게 발송됨 |
|  3   |           IP Receipt           |       Pharmacist는 배송중을 클릭하여 인수확인을 시행함       | -인수확인  화면이 생성되고 해당 자료가 입력됨     - Delivery 메뉴에서 배송상태가 배송중에서 배송완료로 변경되고  IP manager와 Pharmacist의 서명이 포함된 인수인계서가 생성됨(Pharmacy  정보 없을 경우에 인수인계서에 약사 정보 출력 되지 않음을 확인)     -Drug Stock 메뉴의 IP 재고 현황 조회 tab에서 해당 수량이  배송중에서 감소하고 가용재고에 증가하여 표시됨     -Drug Stock 메뉴의 IP 약국 재고 조회 tab에서 해당  IP가 사용대기로 표시됨     -IP배송  완료 메일이 발송됨 |
|  4   |        IP Error Record         |                                                              |                                                              |
| 4.1  |       IP Delivery Error        | IP Error: 인수 확인 시 Pharmacist는 IP error를 체크할 수 있음 | - IP manager와 Pharmacist의 서명이 포함된 인수인계서에 누락, 파손 및 분실로 인한 배송오류 내용이 기재됨     -Drug Stock 메뉴 – IP 재고 현황 조회 tab의 가용재고 수량에서 error에 해당하는 IP의 개수가 제외됨     -IP error log에서 해당 오류 IP기록을 확인할 수 있음     -IP 배송 오류 등록 메일이 발송됨 |
| 4.2  |    Pharmacy Stock IP Error     | 배송 완료 후 약국에  재고로 남아 있는 IP에 대하여    [분실],  [파손] 처리를 할 수 있음 | -Drug Stock 메뉴의 IP 약국 재고 조회 tab에서 상태가 “사용대기”인 임상약은 분실, 파손으로 오류 처리가  가능함     -Drug Stock 메뉴의 IP 오류로그 조회 tab에서 해당 오류 IP  기록을 확인할 수 있으며, 오류 처리된 IP의 상태값을 변경할 수 있음     -[사용대기]  상태의 IP를 오류 처리하면 가용재고에서 해당 개수가 제외됨     -기관별 임상시험용의약품  수불기록 문서의 오류 처리 IP에 대한 기록과 IP 오류로그 조회  tab에서 조회되는 오류 IP 기록이 일치함 |
| 4.3  |        Unused IP Return        | 배송 완료 후 약국에  사용대기, 배송파손,  파손 상태로 보관중인 IP에 대하여 [미사용반납]  처리를 할 수 있음 | -Drug Stock 메뉴의 Unused IP Return tab에서 상태가 “사용대기”, “배송파손” 및 “파손”인 임상약이 list로 출력됨     -Unused IP 반납 요청메일이 IPM에게 발송됨     -미사용 반납이 요청되면 요청 건에  대하여 인수 확인 혹은 취소할 수 있음     -Unused  IP 반납 완료 시 완료 메일이 IPM에게 발송됨     -Unused IP 반납 취소 시 취소 메일이 IPM에게 발송됨     -미사용 반납이  완료되면 Pharmacist와 IP manager의 서명이 포함된  IP 반납확인증이 생성됨     -[사용대기] 상태의 IP를 미사용 반납으로 처리하면 가용재고 및 약국재고에서 해당 개수가 제외되고, [배송파손] 상태의 IP를 미사용 반납으로 처리하면 약국재고에서 해당 개수가 제외되며, [파손] 상태의 IP를 미사용 반납으로 처리하면 약국재고에서 해당 개수가 제외됨     -기관별 임상시험용의약품  수불기록 문서의 미사용 반납 IP에 대한 기록과 IP 오류로그 조회  tab에서 조회되는 미사용 반납 IP 기록이 일치함 |
|  5   | Randomization &  IP Allocation | EDC에서    Subject등록하고,  Random No.와 IP를 allocation 할 수 있음 | -무작위 배정이 계획된 순서대로 배정됨  [별도의 검증 프로그램으로  Random순서 및 Random군에 적합한 IP 배정 여부를 확인함]     [Open Label 과제만 기재]  -Open Label의 경우,  EDC 상의 군정보와 Random code, IP code 군정보가 일치함을 확인함     과제별 IP 배정 방법에 따라 작성  [Run-in/구제약/병용약 등 개수만 count하는 IP가 추가적으로 있는 과제만 기재]  -구제약 처방시  Drug Stock 메뉴에서 구제약 재고 수가 감소함     [기본 배정 과제]  -IP가 allocation 되면 Drug Stock메뉴 - IP 재고 현황 조회  tab의 가용재고가 감소함     [개수 배정 과제]  -IP가  allocation되면 계획된 개수 만큼 Drug Stock메뉴 - IP 재고 현황 조회 tab의 가용재고가 감소함     -Drug Stock 메뉴의 IP 약국재고 조회 tab에 해당 IP의 상태가 사용대기에서  불출대기로 변경됨     -IP 재배정을 진행하여 오류 처리된 IP는 Drug Stock 메뉴의 IP 오류로그 조회  tab에서 확인할 수 있음     -불출오류로 재배정을 할 경우, 해당 대상자의 무작위 배정군과 같지 않은 IP 또는 이미 다른 대상자에게 배정된 IP를 재배정하면 에러 메시지가 나타남     -Drug Stock 메뉴의 IP 오류로그 조회 tab에서 배정되었던 IP와 불출오류로  새롭게 배정된 IP 기록을 확인할 수 있음.     무작위 배정 \| IP 배정 메일이 발송됨 |
|  6   |          IP Dispense           |        IP배정 후  해당 방문의 [불출]페이지가 활성화됨        | -Dispense 메뉴의 List에 해당 방문이 표시되고 불출상태가 미불출로 표기됨     -미불출을 클릭하여 불출내용을 기록할 수 있음     -기록하고 저장\|서명하면 상태가 불출완료로 변경됨     -Drug Stock 메뉴의 IP 약국 재고 조회 tab에 해당 IP가 표시되지 않음     -Drug Stock메뉴 - IP 재고 현황 조회 tab의 약국재고 수가 감소함     -[필요시]불출완료 메일 발송됨 |
|  7   |           IP Return            |               IP불출 후  [반납]페이지를 입력함               | -반납상태 미반납으로 표기됨     -미반납을 클릭하면 반납내용을 기록할 수 있음     -기록하고 저장\|서명하면 상태가 반납완료로 변경됨     -하단의 내려받기를 클릭하면 불출/반납기록을 엑셀로 download 받을 수 있음     -[필요시]반납완료 메일 발송됨 |
| 7.1  |         Used IP Return         |                    Used IP를 최종 반납함                     | -약국으로 반납이 완료된 IP는  Drug Stock 메뉴의 Used IP return tab에서  list로 출력됨     -Used IP 반납 요청메일이 IPM에게 발송됨     -반납 요청된 임상약을 확인 후 인수확인 및  반납취소 할 수 있음     -Used IP 반납 완료 시 완료 메일이 IPM에게 발송됨     -Used IP 반납 취소 시 취소 메일이 IPM에게 발송됨     -Warehouse로 반납이 완료되면 Pharmacist와 IP manager의 서명이 포함된 IP 반납확인증이  생성됨 |
|  8   |        CRA Verification        |           IP불출과  반납을 확인 후 [서명]을 진행함           | -서명상태가 미서명으로 표기됨     -미서명을 클릭하면 확인기록을 할 수 있음     -기록하고 저장\|서명하면 상태가 서명완료로 변경됨     -서명완료 후 Pharmacist가 불출\|반납기록을 수정하면 미서명으로 서명 상태가 변경됨     -CRA 서명해제 알람 메일이 발송됨 |
|  9   | Subject IP  Accountability Log |       IP수불현황에서  해당 Subject의 수불문서를 출력함       | -출력된 문서의 내용과 입력된 불출/반납/CRA서명기록이 일치함  |
|  10  |  Site IP  Accountability Log   |        IP수불현황에서  해당 Site의 수불문서를 출력함         | -출력된 문서와 해당 기관의 입고 및 불출된  IP 기록이 일치함     -출력된 문서에 전자서명이 가능하고,  전자서명을 시행하면 문서 하단에 서명인, 서명일이 입력 됨을 확인함 |
|  11  |        IP System Expire        |                                                              |                                                              |
| 11.1 |  IP System Expire(Warehouse)   | Warehouse에서 Expire  Date(System)에 의하여 사용기간 만료 처리된 IP를 제외하고 배송 진행되는지  확인 | -System expire date가 적용된 Lot  No. 정보 등록     -기관에 배송되지 않은 IP 중  Expire Date(System)에 의하여 일부 IP가 사용기간  만료” 상태로 변경됨을 확인함     -이 후 배송요청 진행 시 사용기간 만료 처리된 IP는 제외되어 배송됨을 확인함 |
| 11.2 |     IP System Expire(Site)     | Site에서 사용대기 상태의 IP  중 Expire Date(System)에 의하여 사용기간 만료 처리된 IP를 제외하고 배정됨을 확인 | -System expire date가 적용된 Lot  No. 정보 등록     -기관에 배송되어 사용대기 상태의 IP 중 Expire Date(System)에 의하여 “사용기간 만료” 상태로 변경됨을 확인함     -사용기간 만료 처리된 IP는 배정되지않고,  사용대기 상태의 IP가 배정됨을 확인함 |
|  12  |            Trigger             | 가용재고가 Trigger Level이 되면  trigger가 발생함  (트리거 타입  설정 확인하고 설정 내용 입력) | -가용재고가  trigger level 이하가 되면 Delivery메뉴에 시스템배송요청 배송기록이  생성됨   (트리거 타입이 5인 경우에는 전체 카테고리의  임상약이 개수에 맞게 생성됨을 확인함) 설정한 트리거 타입에 맞춰서 내용 수정하기     -시스템배송요청을  승인하면 배송상태가 배송요청으로 변경됨     -시스템배송요청  메일이 생성됨 |
|  13  |           Code Break           | 눈가림 해제 방법을 확인한다.     1.직접 눈가림  해제일 경우에는 EDC의 Drug 메뉴에서 연구자가 바로 임상약 확인 가능     2.직접 눈가림  해제가 아닌 스폰서 승인에 의한 눈가림 해제일 경우에는 EDC의 Drug 메뉴에서 시행되며 PI의 승인요청에 따라 승인코드를 입력하면 눈가림이 해제됨 | 과제별 눈가림 해제 방법에 따라 작성  1. 연구자 직접 눈가림 해제  -Drug 메뉴에 IP가 배정된 Subject List가 생성되고 눈가림 상태가 [유지]로 설정됨     -PI에서만 임상약 column이 생성됨     -눈가림 상태 [유지]를 클릭하면 “즉시 눈가림 해제”  팝업창이 생성됨. 연구자가 전송을 눌러 승인번호를 이메일 또는 문자로 수령함     -연구자가 이메일 또는 문자로 수령한 눈가림 해제  승인번호를 입력하면 눈가림 상태가 [해제]로 변경되며 임상약 종류가  표시됨     -즉시 눈가림 해제 등록 메일이 발송됨        2. 스폰서 승인에 의한 눈가림 해제  -Drug 메뉴에 IP가 배정된 Subject List가 생성되고 눈가림 상태가 [유지]로 설정됨     -PI에서만 임상약 column이 생성됨     -연구자가 눈가림 상태 [유지]를 클릭하여 눈가림 해제를 요청하면 [요청]으로 변경됨     -눈가림 해제 요청 등록 메일이 생성됨     -눈가림 해제 승인자가 [요청]을 [승인] 상태로 변경하면 연구자에게 눈가림 승인 메일이 발송됨      -연구자가 눈가림 해제 승인번호를 입력하면 눈가림  상태가 [해제]로 변경되고 임상약 종류가 표시됨     -눈가림 해제 완료 등록 메일이 생성됨 |
|  14  |            Document            |     해당 메뉴에서 IWRS문서를 일괄  download받을 수 있음      | -Admin의 Document 메뉴에서 IWRS 관련 리포트의 출력 버튼을 확인 할 수 있음     -각 버튼 클릭 시 전체 문서가 출력됨 |



***Copyright* © 2021 Song_Artish**

