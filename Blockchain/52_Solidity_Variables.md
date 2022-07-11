# Solidity 변수

---

[TOC]

---



## Overview

솔리디티에서 변수는 크게 **상태변수**, **지역변수**, **전역변수**로 나누어진다. 상태변수와 지역변수는 일반적인 프로그래밍 언어에서의 변수와 동일하다.

```solidity
{데이터타입} {변수명};	// 변수명으로 선언
{데이터타입} {변수명} = {초기화할 값};	// 선언 및 초기화
```

전역변수는 솔리디티만의 특수한 변수(함수)로서, 주로 블록체인에 관한 정보를 제공하며, 따로 선언이나 초기화 없이 불러와서 사용한다.



## 1. 상태변수

컨트랙트 저장소(이더리움 블록체인)에 영구적으로 저장되는 변수로, 항상 `스토로지`에 저장된다. 보통 컨트랙트 최상위 단에 선언한다.

```solidity
pragma solidity ^0.8.14;

contract SimpleStorage {
	uint storedData;	// 상태변수 선언
	uint storedData2 = 20	// 상태변수 선언 및 초기화
}
```

### 접근 수준

컨트랙트 내의 상태(state) 변수를 선언할 때는 지정할 수 있는 접근 수준을 함께 표기한다. 접근 수준은 4가지로 나뉜다.

1. `internal` (default)
   - 상태 변수에 기본적으롤 사용
   - **컨트랙트** 및 해당 컨트랙트를 상속받은 컨트랙트만 접근 가능
   - 외부에서 액세스 불가능
2. `public`
   - 컴파일러가 자동으로 getter 함수를 생성해줌
   - 컨트랙트 내에서 직접 퍼블릭 상태 변수를 사용 가능
   - <u>외부 컨트랙트나 클라이언트 코드에서도</u> getter 함수를 통해 퍼블릭 상태 변수에 접근 가능
3. `private`
   - **동일한 컨트랙트 멤버만** 프라이빗 상태 변수에 접근 가능
   - :ballot_box_with_check: private 키워드는 함수명, 함수 인자명 등을 정의할 때 앞에 언더바(`_`)로 시작하는 것이 관례
4. `constant`/`immutable`
   - 선언될 때 값을 할당해야 함
   - 상수화 = **변경 불가능**



## 2. 지역변수

함수가 실행될 때까지만 존재하는 변수를 의미한다. 지역변수 역시 기본값으로는 `스토리지`에 저장된다. (reference type의 경우 재정의 가능) 보통 함수 아래에 선언되는 변수를 말한다.

```solidity
pragma solidity ^0.8.14;

contract SimpleStorage {
	...
	function simpleFunction() public pure returns(uint) {
		uint a;	// 지역변수 선언
		uint b = 1;	// 지역변수 선언 및 초기화
		a = 1
		uint result = a + b
		return result
	}
}
```



## 3. 전역변수

글로벌한 블록체인 안에 있는 특수 변수를 말한다. 블록체인 및 트랜잭션에 대한 속성을 가지고 올 수 있다.

```solidity
function f(uint start, uint daysAfter) public {
	if (block.timestamp >= start + daysAfter * 1 days) {
		// 여기서 block.timestamp는 전역변수
	}
}
```

- **block**: 블록에 대한 정보를 가지고 있다.
- **msg**: 컨트랙트를 시작한 트랜잭션 콜이나 메시지 콜에 대한 정보를 가지고 있다.
- **tx**: 트랜잭션 데이터를 가지고 있다.
- **This**: 현재 컨트랙트를 참조한다. 현재 컨트랙트 주소로 암시적으로 변환된다.

|          전역변수           |   데이터 형식   |                  설명                   |
| :-------------------------: | :-------------: | :-------------------------------------: |
| blockhash(uint blockNumber) |     byte32      |        주어진 블록의 해시를 반환        |
|        block.basefee        |      uint       |         현재 블록의 기본 수수료         |
|        block.chainid        |      uint       |           현재 블록의 체인 ID           |
|       block.coinbase        | address payable |         현재 블록의 채굴자 주소         |
|      block.difficulty       |      uint       |           현재 블록의 난이도            |
|       block.gaslimit        |      uint       |          현재 블록의 가스 한도          |
|        block.number         |      uint       |            현재 블록의 번호             |
|       block.timestamp       |      uint       |      현재 블록의 유닉스 타임스탬프      |
|          gasleft()          |     uint256     |        남아있는 가스의 양을 반환        |
|          msg.data           | bytes calldata  |           전체 콜데이터 본문            |
|         msg.sender          |     address     | 현재 호출을 수행하고 있는 메시지 발신자 |
|           msg.sig           |     bytes4      |  호출 데이터의 첫 4바이트(함수 식별자)  |
|          msg.value          |      uint       |    메시지와 함께 보낸 이더(Wei) 금액    |
|         tx.gasprice         |      uint       |           트랜잭션 가스 비용            |
|          tx.origin          |     address     |             트랜잭션 발신자             |



***Copyright* © 2022 Song_Artish**