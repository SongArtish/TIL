# SegWit

---

[TOC]

---



## 배경

| 속도                                                     | 확장성                                                       |
| :------------------------------------------------------- | :----------------------------------------------------------- |
| 합의에 도달하여 거래기록이 장부에 기록되는데 걸리는 시간 | 갑자기 많은 트래픽이 발생했을 경우 다운이나 지연 없이 서비스 연속성이 보장되는 성질 |

현재 블록체인의 속도와 확장성을 개선하기 위한 여러 방법은 크게 4가지로 정리할 수 있다.

1. 블록의 용량 증대
2. 블록체인 내 기술 도입: 샤딩 등
3. 블록체인 외부와 연계
4. 합의 알고리즘 재설계

여기서 세그윗(SegWit)은 **`1. 블록의 용량 증대`를 통한 개선 방법** 중 하나이다.



## SegWit

세그윗(Segwit)d리나 Segregated Witness의 약자로, **비트코인의 블록에서 디지털 서명 부분을 분리함으로써 블록 당 저장 용량을 늘리는 소프트웨어 업그레이드**를 의미한다. 즉, 고정된 블록의 가용 공간을 늘려서 속도를 개선하는 것이다.

기존 비트코인의 블록 구조는 다음과 같았다. (비트코인 블록은 약 1MB이다.)

|    데이터 종류     | 비율 |
| :----------------: | :--: |
| 디지털 서명 데이터 | 75%  |
|    그 외 데이터    | 25%  |

우지한을 비롯한 채굴 세력들을 주축으로 비트코인 시스템에서 블록의 크기 자체를 늘리자는 **하드포크 방식**도 제안되었지만, 비트코인 커뮤니티는 보다 안정적인 개선이 가능한 세그윗, 즉 **소프트포크 방식**을 택하게 되었고, 2017년 8월 1일 기준 세그윗을 적용하였다. 디지털 서명 데이터 부분만 별도로 Off-Chain에서 작동하게 분리함으로써 기존 시스템에는 영향을 주지 않으면서 처리 속도를 개선할 수 있게 되었다.



## 특징

1. **거래 속도의 확장성(Scalability)**

   세그윗은 서명 부분을 따로 Witness라는 데이터 영역으로 분리해 더 많은 거래를 처리할 수 있도록 업데이트하며, 거래 속도를 높인다.

2. **거래 가변성 문제(Transaction Malleability)**

   모든 비트코인 거래는 해당 거래를 식별할 수 있는 거래의 ID(Transaction ID, TXID)를 포함한다. **TXID가 ID**라면 **전자서명은 비밀번호**라고 할 수 있다. 거래 가변성은 실질적인 거래 내용에는 변화가 없지만, 거래 ID(TXID)만 변경하여 새로운 거래를 만들어 낼 수 있는 일종의 버그이다. 세그윗은 서명과 거래(TXID)를 분리하여 이러한 문제를 막을 수 있다.

3. **버전 호환**

   세그윗은 하드포크가 아닌 소프트포크이다. 비트코인 소프트웨어 업그레이드를 하지 않아도 세그윗 이전과 세그윗 적용 버전을 모든 노드에서 사용할 수 있다.

| 블록 용량 증가                     | 트랜잭션 속도 증가                                    | 트랜잭션 가변성 해결                                         |
| ---------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------ |
| 디지털 서명 데이터 분리            | 더 많이 저장할 수 있는 블록을 통해 트래낵션 속도 증가 | 서명이 더 이상 트랜잭션 데이터의 일부가 아니기 때문에 해당 데이터 변경 불가 |
| 실질 블록 크기 1MB -> 4MB까지 증가 | 하나의 트랜잭션에 30달러 이상에서 1달러 미만으로 절감 | 서명 조작 불가                                               |



## Segwit 2x

세그윗과 비교했을 때 세그윗2x의 주된 차이점은 단지 트랜잭션을 일괄 처리하는 방식을 변화시킬 뿐만 아니라, 블록 크기를 1MB -> 2MB로 증가시킨다는 것이다. 또한, 세그윗2x는 비트코인 거버넌스의 기본 규칙 중 하나에 실질적인 변화를 제안했다. 하지만 이는 결국 합의를 달성하지 못해 <u>중단</u>되었다.



***Copyright* © 2022 Song_Artish**