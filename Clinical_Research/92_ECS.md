# ECS 로직

---

[TOC]

---



## DA

### Blind

> 유해찬마루님 자료를 참고하였다.

1. 타겟 - DAENDTC, 최종방문일과 임상시험종료일이 작성되지 않았으면 블라인드.
2. 타겟 - QST DA01, v2 ip처방이 없거나 예가 아니면 트루를 반환하여 블라인드처리, 그리고 v3방문일, 최종방문일, 임상시험종료일이 작성되지 않으면 트루를 반환하여 블라인드처리
3. 타겟 - QST DA02, v3 ip처방이 없거나 예가 아니면 트루를 반환하여 블라인드처리, 그리고 v4방문일, 최종방문일, 임상시험종료일이 작성되지 않으면 트루를 반환하여 블라인드처리
4. 타겟 - QST DA02, v4 ip처방이 없거나 예가 아니면 트루를 반환하여 블라인드처리, 그리고 최종방문일, 임상시험종료일이 작성되지 않으면 트루를 반환하여 블라인드처리
5. ns는 v2의 ip처방이 없거나, 이후 방문기록이 작성되지 않으면 비활성화 시키는 것



## 기타

> 김홍원님 자료를 참고하였다.

|      |           | 유효 범위                                  | 쿼리조건                                                     | ECS                                  |
| ---- | --------- | ------------------------------------------ | ------------------------------------------------------------ | ------------------------------------ |
|      | ICDTC     | IRB부터(포함)                              | IRB 이전이면 쿼리발행                                        | NVL (DLT, TRUE)                      |
|      | SVDTC(V1) | ICDTC 28일 이내                            | 0~28일 이내가 아니면 쿼리발행                                | NOT, LELE (0 ,DFDD ,28)              |
|      | SVDTC(V2) | V1과 14일 이내                             | 0~14일 이내가 아니면 쿼리발행                                | NOT, LELE (0 ,DFDD ,14)              |
| 14   | SVDTC(V3) | V2와 11~17일 이내                          | 11~17일 이내가 아니면 쿼리발행                               | NOT, LELE (11 ,DFDD ,17)             |
| 28   | SVDTC(V4) | V2와 25~31일 이내                          | 25~31일 이내가 아니면 쿼리발행                               | NOT, LELE (25 ,DFDD ,31)             |
| 42   | SVDTC(V5) | V2와 39~45일 이내                          | 39~45일 이내가 아니면 쿼리발행                               | NOT, LELE (39 ,DFDD ,45)             |
|      | EOS       | 이전 최대 방문일 이후 (비포함)             | ADMAX(SVDTC)와 작거나 같으면 쿼리발행                        | DLE                                  |
|      | UV        | V2 이후 EOS 이전 (비포함)                  | V2와 작거나 같고 혹은 ADMAX(SVDTC)와 크거나 같으면 쿼리발행  | ANY(DLE,DGE)                         |
|      | UV        | 이전 최대 방문일 이후 (비포함)             | ADMAX(SVDTC)와 작거나 같으면 쿼리발행                        | DLE                                  |
|      | MHSTDTC   | 생년월일 부터 V1 까지 (포함)               | 생년월일 보다 작거나 V1보다 크면 쿼리발행                    | ANY(DLT,DGT)                         |
|      | MHENDTC   | V1 이전 6개월 까지의 병력 종료 기록 (포함) | (V1-6개월) 보다 작으면 쿼리발행                              | DLT(ADMM,-6)                         |
|      | MHENDTC   | MHSTDTC 부터 V1 까지 (포함)                | MHSTDTC 보다 작거나 V1 보다 크면 쿼리발행                    | ANY(DLT,DGT)                         |
|      | LB,EG     | V1 : V1 4주 이내 (포함)                    | 4주 이내가 아니면 쿼리발행                                   | AND(IN(SHVID), NOT(LELE,-28,DFDD,0)) |
|      | LB,EG     | V2 이후 : 해당 방문일과 동일 (포함)        | 동일하지않으면 쿼리발행                                      | AND(INN(SHVID), NEE)                 |
|      | PE,PG     | 해당 방문일과 동일 (포함)                  | 동일하지않으면 쿼리발행                                      | NEE                                  |
|      | DASTDTC   | V2 3일 이내 (포함)                         | 당일 보다 작거나 3일 이후일 때 쿼리발행                      | ANY(DLT, DGT(ADDD,3))                |
|      | DAENDTC   | DASTDTC부터 (DSDTC OR 최대 방문일) 까지    | DASTDTC보다 작거나 최종방문보다 크면 쿼리발행                | ANY(DLT,DGT(NVL(DSDTC,SVDTC))        |
|      | AESTDTC   | DASTDC부터 (DSDTC OR 최대 방문일) 까지     | DASTDTC보다 작거나 최종방문보다 크면 쿼리발행                | ANY(DLT,DGT(NVL(DSDTC,SVDTC))        |
|      | AEENDTC   | AESTDTC부터 (DSDTC OR 최대 방문일) 까지    | DASTDTC보다 작거나 최종방문보다 크면 쿼리발행                | ANY(DLT,DGT(NVL(DSDTC,SVDTC))        |
|      | CMSTDTC   | (DSDTC OR 최대 방문일) 까지                | 최종방문보다 크면 쿼리발행                                   | DGT(NVL(DSDTC,SVDTC))                |
|      | CMENDTC   | CMSTDTC부터 (DSDTC OR 최대 방문일) 까지    | CMSTDTC보다 작거나 최종방문보다 크면 쿼리발행                | ANY(DLT,DGT(NVL(DSDTC,SVDTC))        |
|      | DSDTC     | 최종방문일부터 (포함)                      | 최종방문일보다 작으면 쿼리발행                               | DLT                                  |
|      |           |                                            |                                                              |                                      |
|      |           |                                            | 마지막방문일                                                 |                                      |
|      |           |                                            | NVL(DSDTC.ADMAX(SVDTC))를 이용해서 DSDTC가  없을 때 SVDTC의 마지막 방문을 이용할 수 있게 |                                      |



***Copyright* © 2021 Song_Artish**