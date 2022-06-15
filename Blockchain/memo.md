# memo

---

[TOC]

---



## 블록체인의 상태

블록체인은 트랜잭션으로 변화하는 상태 기계(State Machine)

### 상태 기계

- 블록체인은 **초기 상태**에서 **변경사항**을 적용하여 **최종 상태**로 변화하는 상태 기계
  - 이전 블록의 최종 상태(final state)는 현재 블록의 초기 상태(initial state)
  - Gen Block의 경우 임의의 초기 값들이 설정되어 있는데, 이것이 Gen Block의 초기 상태이자 최종상태
- (어카운트 기반) 블록체인의 상태
  - TX는 어카운트를 생성하거나 변경
  - 항상 같은 결과를 보장하기 위해 하나의 TX가 반영되는 과정에서 다른 TX의 개입은 제한됨



## Ethereum 어카운트 종류

1. External Account: 사용자(end user)가 사용하는 어카운트 (**EOA**)
2. Contract Account: 스마트 컨트랙트를 표현하는 어카운트

- Ethereum은 EOA와 스마트 컨트랙트의 상태를 기록 및 유지
  - 스마트 컨트랙트는 특정 주소에 존재하는 **실행 가능한 프로그램**
  - 프로그램은 상태를 가지기 때문에 Ethereum/Klaytn은 스마트 컨트랙트를 어카운트로 표현
- EOA는 블록에 기록되는 TX를 생성
  - 블록에 기록되는 TX든은 명시적인 변경을 일으킴(ex. 토큰 전송, 스마트 컨트랙트 배포/실행)



## Transactions

- TX의 목적은 블록체인의 상태를 변경하는 것
  - TX는 보내는 사람(sneder, from)과 받는 사람(recipient, to)이 지정되어 있음
  - to가 누구냐에 따라 TX의 목적이 세분화됨
- Gas: TX를 처리하는데 발생하는 비용
  - TX를 처리하는데 필요한 자원(computing power, storage)을 비용으로 전환한 것이 가스(gas)
  - Sender는 TX의 처리를 위해 필요한 가스의 총량과 같은 가치의 **플랫폼 토큰**을 제공해야함
  - 이때 지출되는 플랫폼 토큰을 가스비(Gas Fee)라 정의
  - 가스비는 블록을 생성한 노드가 수집



## 트랜잭션과 서명

- 플랫폼은 sender가 TX 처리에 필요한 가스비를 가지고 있는지 확인
  - 가스비 확인은 구현에 따라 상이
  - Ethereum/Klaytn은 노드가 TX를 수신함과 동시에 가스비 이상의 balance가 있는지 확인
  - TX의 체결과 동시에 sender의 balance에서 가스비를 차감
- TX는 sender의 서명(v, r, s)이 필요
  - 어카운트의 balance를 사용하기 때문
  - 서명의 증명은 구현마다 상이
    - Ethererum: 서명 -> 공개키 도출 -> 어카운트 주소 도출 -> 어카운트 존재유무 확인
    - Klaytn: from 주소 확인 -> 저장된 공개키 불러오기 -> 서명 직접 검증



## 블록체인 별 트랜잭션

account 기반의 블록체인에는 `nonce` 값이 있다.

```solidity
{
	nonce: 1,
	from: '0xd0ea3e0eabaea095ea3ba231c043dbf8c0feb40a',
	to: '0x5e47b195eeb11d72f5e1c26aebb6d341f1a9bedb',
	value: 10,
	// omitted other fields for brevity
	// platform specific fields are required
}
```



```solidity
// Ethereum 트랜잭션 예시
{
	nonce: '0x01',
	gasPrice: '0x4a817c800',	// 20,000,000,000
	gas: '0x5208',	// 21,000
	value: '0xde0b6b3a7640000',	// 1,000,000,000,000,000,000 = 1 ETH
	
	to: '0x3535353535353535353535353535353535353535',
	v: '0x25',
	r: '0xf4...88d',
	s: '0x7e...fd0',
	// some fields are omitted for brevity
}
```

```solidity
// Klaytn 트랜잭션 예시
{
	type: 'VALUE_TRANSFER',
	nonce: '0x01',
	gasPrice: '0x05d21dba00',
	gas: '0x0493e0',
	value: '0x01',
	to: '0xef...a01',
	from: '0xd0...4fa',
	v: '0x07f6'
	r: '0x5...3f3',
	s: '0x7...70e'
}
```





***Copyright* © 2022 Song_Artish**