# 블록체인 Intro

---

[TOC]

---



## 배경

블록체인 기술은 비트코인이라는 암호화폐와 함께 등장한 것으로, 이는 기존 금융 시스템과 관련이 있다.

**화폐의 역사**

1. **실물화폐**: 조개 껍데기, 쌀, 담배 등 물물교환을 넘어서 교환의 더 나은 방법으로 사용한 특정한 물건. 내구성, 휴대성, 균질성에 문제점이 존재함

2. **금속화폐**: 금과 같은 귀금속으로 만든 화폐. 산업/기술의 발달로 거대해진 경제 시장에 필요한 화폐를 공급하는 것이 어려워짐

3. **신용화폐**: 국가, 지폐 발권은행 등의 신용으로 보증되는 수표, 어음 등의 화폐. 신용을 매개로 하며 실물이 없는 화폐

**화폐의 특성**

- 휴대성(Portability): 소지하기 편해야 함
- 가분성(Divisibility): 분할에 용이함(ex. 지폐 -> 동전)
- 내구성(Durability): 형태가 쉽게 변하지 않음
- 동질성(Uniformity): 같은 성질이나 특성 (크기, 모양, 가치가 모두 같음)
- 가치의 안정성(Limited Supply): 공급량이 제한됨

**화폐의 3대 기능**

1. 교환의 매개체
2. 가치 척도의 기능
3. 가치 저장 기능

**기존 금융 시스템의 문제점**

- 화폐의 독점적 발행권을 가진 중앙기관의 정책이 자산에 영향을 주는 것에 사람들은 불만을 가지게 되었다.

이러한 맥락에서 사토시 나카모토는 최초의 암호화폐인 비트코인을 개발하게 되었다.



## Blockchain

> 블록체인(block chain)은 관리 대상 데이터를 '**블록**'이라고 하는 소규모 데이터들이 **P2P** 방식을 기반으로 생성된 **체인** 형태의 연결고리 기반 **분산** 데이터 저장 환경에  저장하여 누구라도 임의로 수정할 수 없고 누구나 변경의 결과를 열람할 수 있는 분산 컴퓨팅 기술 기반의 **원장** 관리 기술이다. (출처: 위키백과)

블록체인의 핵심은 **인터넷 상에 있는 사람들과 동일한 데이터를 가지는 것**이다. 블록체인은 다음과 같은 방식으로 데이터를 저장하고 공유한다.

- 누구나 데이터를 추가할 수 있다.
- 데이터는 한 번 추가되면, 수정/삭제할 수 없다.
- 개인/단체가 데이터를 관리하는 것이 아닌, 블록체인 네트워크에 있는 모든 사람들이 함께 관리한다.

### Block

> 트랜잭션을 담은 거래 기록의 집합

블록은 **데이터를 저장하는 공간**이다. 블록에는 자산에 대한 정보를 담거나, 개인 정보를 암호화해서 담는 등 다양한 유형의 정보를 담을 수 있다. 따라서 블록의 구성은 어떤 종류의 데이터를 저장하느냐에 따라 결정되는데, 일반적인 암호화폐에서는 블록에 **거래기록**(transaction)을 저장한다.

### Chain

> 블록을 만들어진 순서대로 연결한 블록의 집합

네트워크에 참여한 사용자가 하나의 블록에 일정한 갯수의 트랜잭션을 넣어 네트워크에 공유하면, 새로운 블록을 만들어 새롭게 생긴 트랜잭션들을 담는다. 그리고 이 새로운 블록에는 이전 블록을 지칭하는 데이터를 함께 넣어, 직전 블록이 어떤 블록인지 저장한다.

블록체인은 본질적으로 특정한 구조를 지닌 데이터베이스일 뿐이며 순서가 지정된 링크드 리스트이다.

### Distributed Ledger

**원장**은 거래 내역의 집합이며, 블록체인은 원장을 저장하는 데이터베이스 유형 중 하나이다.

**분산원장(Distributed Ledger)**은 중앙 집중식 DB와 달리 분산되어 있으며, 데이터를 여러 위치에 두거나, 여러 사용자들이 나눠서 가지고 있는 데이터베이스 유형이다. 분산 원장 시스템에서 데이터를 저장하기 위해서는 데이터를 공유하고 있는 당사자들이 합의해야 하며, 당사자들의 합의를 통해 분산되어 있는 데이터베이스들이 하나의 일관된 데이터를 가질 수 있다.

블록체인은 특정 기술이 추가된 분산 원장의 한 종류이다. 네트워크 내 모든 노드들이 새로운 블록에 대한 유효성을 검증하고 난 후에, 블록을 체인에 추가할 수 있다. 일반적인 분산 원장과 비교한 블록체인의 특징은 다음과 같다.

1. **블록 구조**: 일반적으로 블록 형태로 데이터가 저장된다.
2. **순서**: 모든 블록이 직전 블록을 가리킴으로써 순서대로 배열되어 있다.
3. **블록 생성 메커니즘**: 블록을 생성할 노드를 정하기 위해 PoW, PoS와 같은 메커니즘을 사용한다. 이는 경쟁적이며, 자원을 소모한다.
4. **토큰**: 블록을 생성하기 위해 자원을 소모한 노드에게 보상으로 코인을 제공하며, 이 코인은 화폐 역할을 한다.

만약 자원을 소모해 블록을 생성했는데 아무런 보상도 주어지지 않는다면 아무도 블록을 만들려 하지 않을 것이기 때문에, 블록체인에는 코인이 필수적이다.

### Node

노드는 네트워크에 장치 또는 데이터 지점을 의미한다. 쉽게 말해 네트워크에 접속해 있어서 연결될 수 있는 컴퓨터를 지칭한다.



## Cryptography

- 복호화 가능
  - 대칭키 암호화
    - AES, DES...
    - ARIA, SEED
  - 비대칭키 암호화(공개키 암호화)
    - RSA, ECC
    - ECDSA
    - DS(전자서명)
- 복호화 불가능(단방향 암호화, 해시함수)
  -  SHA256, keccak256, RIPEMD-16



## Hash Function

임의의 길이의 데이터를 **고정된 길이의 데이터**로 매핑하는 함수(블록해시)

- {해시, 해시 값, 해시 코드} = 해시 함수에 의해 얻어지는 값

$$
해시: H(x)
(여기서 x는 데이터, H는 해시함수)
$$

- 산업에서 가장 널리 쓰이는 해시 함수는 SHA-2 (e.g., SHA-256), SHA-3 (e.g., Keccak)

- 각 블록이 이전 해시 값을 가지고 다른 블록과 연결되어 있다. (체인)
- Genesis 블록의 경우, empty 값(null과는 다른) 혹은 random 값을 넣어주면 된다.

**해시의 활용**

- 비밀번호 저장시, DB에서는 해시함수로 암호화하여 저장

- 버전관리 혹은 문서 복제 등을 검사하기 위해 사용

  - 해시함수는 문자열로 축소하기 때문에 문서의 모든 단어를 비교하는 것보다 속도가 빠르다.

- 문자를 숫자나 저장되는 주소로 치환하여 검색에 사용

  ```markdown
  # 블록체인 활용 분야
  
  - 음식의 유통 경로 추적
  - 소프트웨어 개발에 보안 더하기
  - 디지털 콘텐츠 관리
  - 의료 기록 추적
  - 대출 승인
  - 보험금 청구
  - 감사 추적
  - 투표
  - 스마트 계약
  - 암호화폐
  ```



## Nonce

> 암호화 임시값

nonce를 사용하여 정해진 규칙에 부합하는 hash 값을 생성할 수 있다.

- Proof of Work(Pow) : nounce를 변경해가면서 최종 해시를 구하는 작업
- 마이닝(채굴) : 작업증명(Pow)을 통해 최종 블록을 생성하는 것



## 블록 생성

블록체인 네트워크에서 거래가 발생하여 새로운 트랜잭션이 생기면, 이 트랜잭션은 네트워크 내에 있는 모든 노드들에게 공유된다. 따라서 블록체인에서는 다양한 검증(Verification) 절차를 수행한다.

트랜잭션에 대한 유효성 검사 뿐만이 아니라, 트랜잭션이 블록에 블록에 담기고, 해당 블록이 체인에 추가되어 블록체인의 일부가 될 때 트랜잭션에 대한 처리가 완료된다. 여기서 트랜잭션을 모아서 하나의 블록으로 만드는 과정을 **채굴(Mining)**이라고 한다.

채굴은 암호화폐 송금 서비스를 운영하는 핵심 역할을 하기 때문에, 채굴 노드에게는 보상이 주어지게 되며, 이 보상을 얻기 위해 채굴은 경쟁적으로 이루어진다. 경쟁에 참여한 노드들은 각각 블록을 만들어 네트워크에 전파하며, 이 경쟁에서 승리한 노드가 생성한 블록이 채택된다. 채굴 노드는 블록 생성에 대한 보상으로 코인을 받으며, 발행된 코인은 블록체인 네트워크 내에서 화폐의 역할을 하게 된다.



## 기술적 해결 과제

블록체인이 금융 서비스에 적용되기 위해서는 몇 가지 기술적 과제가 아직 남아있다.

1. **거래 비밀성**: 블록체인에 저장되는 정보는 소유자와 합의된 관리자만 거래 내역에 접근가능해야한다.
2. **신뢰 및 보안 유지**: 신뢰와 보안 유지를 위해서는 퍼블릭 블록체인을 도입하는 것도 고려해야 한다.
3. **속도**: 실제 사용이 가능하기 위해서는 적어도 초당 3,000건 이상 처리할 수 있는 성능을 보유한 블록체인이 필요하다.
3. **확장성 확보**: 갑자기 많은 트래픽이 발생했을 경우 다운이나 지연 없이 서비스 연속성이 보장되어야 한다.
4. 분산원장기술이 금융에 적용될 경우 발생할 수 있는 검증되지 않은 요소들(보안 상의 위험, 법적인 위험성 증가)도 있다.



***Copyright* © 2022 Song_Artish**