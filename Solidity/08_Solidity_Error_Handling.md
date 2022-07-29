# Solidity 에러 핸들링

---

[TOC]

---



## Overview

솔리디티에서 에러를 처리할 때는 `assert`, `require`, `revert` 함수를 사용한다.

- `revert`: 해당 함수를 종료하고 에러를 리턴한다.
- `require`, `assert`: 설정한 조건이 참인지 확인하고, 조건이 거짓이면 에러를 리턴한다.



## revert

`revert`는 다음과 같이 사용할 수 있다.

```solidity
pragma solidity ^0.8.14;

contract VendingMachie {
	address owner;
	function buy(uint amount) public payable {
        if (amount > msg.value / 2 ehter)
            revert("Not engouh Ether provided.");	// 에러를 리턴하면서 에러 메시지를 지정
        // 송금 진행
	}
}
```



## require

`require`는 그 자체로 `if...revert`처럼 사용되는 **게이트키퍼** 역할을 한다.

> 게이트키퍼(gatekeeper): 조건을 만족하면 특정 동작을 실행하고, 조건을 만족하지 않으면 실행하지 못하도록 하는 역할

예를 들어, 위의 `VendingMachine` 컨트랙트의 `buy` 함수는 아래의 코드와 완전히 동일하게 작동한다.

```solidity
pragma solidity ^0.8.14;

contract VendingMachie {
	address owner;
	function buy(uint amount) public payable {
		require(
			amount <= msg.value / 2 ether,	// 주어진 조건이 참이면 넘어가고, 거짓이면 에러 리턴
			"Not enough Ether provided."	// 에러 메시지를 지정할 수 있다.
		)
	}
}
```



## assert

`assert`는 `require`와 사용법이 동일하나, 사용하지 않은 가스를 호출자에게 반환하지 않고, 공급된 가스를 모두 소모하며 상태를 원래대로 되돌린다.



***Copyright* © 2022 Song_Artish**