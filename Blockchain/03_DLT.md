# DLT

---

[TOC]

---



## 중앙집중원장

기존의 여러 서비스는 중앙집중원장(Centralized Ledger)의 형태를 띄고 있으며, 우리는 기관/기업에게 신뢰비용(수수료 등)을 지불하고, 그들은 서비스를 제공하며 데이터를 보관하고 활용했다. 하지만, 기존 중앙집중형 데이터베이스 관리시스템에는 다음과 같은 취약점이 있다.

- 비용문제: 거래자들 사이에서 과도한 관리, 중개수수료를 청구함
- 시간문제: 상호 거래 프로세스에 중간다리(middleman)가 포함되어 있어 시간/비용 측면에서 비효율적
- 보안문제: 해커들의 공격 대상이 중앙 데이터베이스 하나로 집중되어 있음(단일 실패점, Single Point of Failure)



## 분산원장

분산원장(Distributed Ledger)은 거래 정보를 기록한 원장을 특정 기관의 중앙화된 서버가 아닌 분산화된 네트워크(P2P 네트워크)에서 참여자들이 공동으로 기록 및 관리하는 기술로, 공유원장이라고도 한다. 분산원장은 다음과 같은 <u>장점</u>이 있다.

- **효율성(Efficiency)**: 신뢰할 수 있는 제3의 기관을 설립/운영하기 위한 인력 및 자원 투입이 불필요하다. 시스템 오류 등을 예방하고 해킹 등 보안 사고를 방지하기 위한 인프라 투자 비용도 절감할 수 있다.
- **보안성(Security)**: 중앙 서버가 없기 때문에 해킹 등의 공격으로부터 안전하며, 원장이 모든 참가자에게 공개되기 때문에 원천적으로 정보 유출 소지가 없다.
- **시스템 안정성(Resilience)**: 단일 실패점(Single Point of Failure)이 존재하지 않기 때문에 일부 참가 시스템에 오류 또는 성능 저하가 발생하더라도 전체 네트워크에 미치는 영향이 미미하다.
- **투명성(Transparency)**: 분산원장 기술은 모든 거래 기록을 공개하기 때문에 높은 투명성을 가진다. 거래 추적이 용이하고 규제(고객확인의무: Know Your Customer 등) 준수 비용도 낮다.

하지만 <u>단점</u>도 존재한다. 분산원장 기술에서는 **신뢰를 담보해줄 기관이 존재하지 않기 때문에 시스템 자체에서 신뢰를 형성하는 메커니즘을 설계해야**한다.

> 모든 블록체인은 분산원장이지만, 모든 분산원장이 블록체인은 아니다.
>
> - 합의 알고리즘
> - 거버넌스



## 분산원장기술(DLT)

분산원장기술(Distributed Ledger Technology)은 여러 위치, 여러 사람에 의해 복제, 공유 또는 동기화된 데이터베이스를 어떻게 합의할 것이냐에 대한 기술로, 블록체인 기술의 핵심이다. 이를 위해 **P2P(Peer-to-Peer) 네트워크**와 각 노드가 가지는 데이터 사본을 위한 **합의 알고리즘**이 필요하다.



***Copyright* © 2022 Song_Artish**