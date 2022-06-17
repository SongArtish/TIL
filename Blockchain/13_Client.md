# Client

---

[TOC]

---



|        구분        |               비트코인                |                    이더리움                     |
| :----------------: | :-----------------------------------: | :---------------------------------------------: |
|    **암호화폐**    |                 1세대                 |                      2세대                      |
|      **기능**      | 비트코인의 거래기록만 블록체인에 적용 | 계약을 기록할 수 있는 스마트 컨트랙트 기술 추가 |
|   **채굴 방식**    |                  PoW                  |              PoW(PoS로 변경 예정)               |
| **상한 채굴 개수** |           약 2,100만 개까지           |                 상한 없이 생산                  |



## Bitcoint Core

비트코인 코어는 비트코인의 레퍼런스 클라이언트으로, 사토시 클라이언트(Satoshi Client)로도 알려져 있다.

```markdown
명칭의 변화
Bitcoin -> Bitcoint-Qt -> Bitcoint Core
```

개발자들은 비트코인 코어의 변경 사항을 통해 기반이 되는 비트코인 프로토콜을 변경하게 되고, 비트코인 코어는 풀노드를 돌리는 것을 전제로 한 소프트웨어이므로 100GB가 넘는 블록체인 데이터를 다운로드 받아야 제대로 사용할 수 있다.

> [Bitcoin Github Repository](https://github.com/bitcoin/bitcoin)

비트코인은 다양한 언어로 개발되었고, C++이 주 언어이다.



## Ethereum Client

이더리움 클라이언트는 이더리움 블록체인 네트워크를 구성하는 개별 클라이언트 노드(node)이기 때문에 중앙집중형 서버 프로그램이 따로 존재하지 않으며, 오로지 클라이언트 프로그램만 존재하게 된다. 이더리움 블록체인에서 응용 프로그램을 빌드하는 것에 사용할 수 있는 도구는 아래 내용과 같다.

### Geth

이더리움 재단(Ethereum Foundation)이 제공하는 고식 클라이언트 소프트웨어로, Go언어로 개발되었다.
Geth를 처음 시작하면 네트워크 내의 다른 이더리움 클라이언트(node)에 연결하는 작업을 먼저 시작하고, 블록체인의 전체 사본을 내려받게 된다. 그리고 블록체인의 복사본을 최신 상태로 유지하기 위해 끊임 없이 다른 노드와 통신한다.또한, Geth를 이용해 블록을 채굴하고, 블록체인에 트랜잭션을 추가하고 블록의 트랜잭션을 검증하며 특랜잭션을 실행할 수도 있으며, RPC를 통해 상호작용할 수 있는 API를 노출하여 서버 역할을 하기도 한다.

> 블록체인에 연결할 수 있는 자바스크립트 클라이언트(Geth Console)도 있다.

### Parity

이더리움 프로토콜의 또 다른 구현체로, Rust 언어로 개발되었다.
이더리움 네트워크에 접속할 수 있는 클라이언트 소프트웨어는 누구나 개발할 수 있으며, [ETHEREUM: A SECURE DECENTRALISED GENERALISED TRANSACTION LEDGER](http://paper.gavwood.com/) 문서를 참고하면 된다.



***Copyright* © 2022 Song_Artish**