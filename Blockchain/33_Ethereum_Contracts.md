# Ethereum Contracts

---

[TOC]

---



## 스마트 컨트랙트 동작 방식

### Coding

솔리디티의 경우 대표적으로 Remix라는 웹 IDE에서 작성 및 테스트를 할 수 있다.

아래 예시 코드는 컨트랙트에 storedData라는 했다. set 메서드는 고, ㅎget 메서드는 공한다.

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract SimpleStorage {
	// 숫자 타입 공용 변수를 설정
	uint storedData;
	// set 함수: storedData를 받아옴
	function set(uint x) public {
		storedData = x;
	}
	// get 함수: 공용 변수 storedData를 조회하여 반환
	function get() public view returns (uint) {
		return storedData;
	}
}
```

### Compile

작성한 스마트 컨트랙트 소스는 바로 사용할 수 없으며, 컴파일을 해야한다. 컴파일을 하게 되면, ABI code와 Byte code가 생성된다.

Remix에서 솔리디티 언어의 컴파일이 가능하다. Remix 이외, 각 IDE마다 컴파일하는 방법은 다양하다.

```solidity
// ABI code
[
	{
		"inputs": [],
		"name": "get",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": {
			{
				"internalType": "uint256",
				"name": "x",
				"type": "uint256"
			}
		},
		"name": "set",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
```

```solidity
// Byte code
{
	"functionDebugData": {},
	"generatedSources": [],
	"linkReferences": {},
	"object": "60806040523...",
	"opcodes": "PUSH1 0x80 PUSH1 0x40 MSTORE CALLVALUE DUP1 ...",
	"sourceMap": "101:194:0:-:0;;;;;;;;;;;;;;;;;"
}
```

### Deploy

1. bytecode와 abi를 사용해 컨트랙트 객체를 생성한다. 이 객체는 블록체인에 컨트랙트를 배포할 때 사용된다.
2. 배포 트랜잭션을 생성한다. 트랜잭션을 생성할 때, 계정, gas limit, 컨트랙트 객체 등이 포함되어야 한다.
3. 트랜잭션을 네트워크에 올린다.
4. 이후 채굴 노드가 이 배포 트랜잭션을 포함한 블록을 채굴하고 브로드캐스팅 하게 되면, 우리가 작성한 스마트 컨트랙트의 CA(컨트랙트 계정)가 생성된다.

배포는 언어/환경에 따라 다르다. 만약, Remix를 사용한다면 컴파일 버튼을 누르고 배포 칸으로 들어와 설정(Account, gas, value 등) 후 버튼 클릭만으로 배포는 자동으로 이루어져, 컨트랙트 주소가 생성된다.

이렇게 생성된 주소가 바로 스마트 컨트랙트 계정 주소 값이 되며, 이 주소 값으로 스마트 컨트랙트를 활용할 수 있다. (트랜잭션 해시와 스마트 컨트랙트의 주소값은 전혀 다르다)

### Access & Use

스마트 컨트랙트 주소를 이용하여 정보를 활용할 수 있다. 트랜잭션을 생성할 때 스마트 컨트랙트 주소를 사용하게 되면, 스마트 컨트랙트가 가지고 있는 메서드를 사용할 수 있다. 이더리움 블록체인에 있는 상태를 변경/조회할 수 있다.

송금이나 스마트 컨트랙트 등 상태를 변경하는 경우에는 함수를 실행하겠다는 메시지를 담은 트랜잭션을 보내야 한다. 블록체인에 기록을 하는 것이기 때문이다. 반면, 블로게인으로부터 스마트 컨트랙트의 변수값 등을 단순히 `조회`만 하는 경우, 블록체인에 기록하지 않기 때문에 별도로 비용이 들지 않는다. 따라서, 일반적인 트랜잭션과는 다르게 자신의 노드에 동기화된 블록 내 데이터를 읽어주는 `트랜잭션 call`을 한다. 트랜잭션 call은 데이터를 읽기만 하기 때문에 비용이 들지 않는다. 물론, 메인넷에서 이루어지는 모든 트랜잭션에는 가스비가 부과되기 때문에 테스트넷에서 충분한 테스트를 거쳐야 한다.



***Copyright* © 2022 Song_Artish**