# Solidity 이벤트

---

[TOC]

---



## Event

이벤트는 어떤 결과가 발생했을 때 해당 컨트랙트에서 dApp 클라이언트 또는 다른 컨트랙트에게 전달한다.



## Event Handling

컨트랙트는 **`event` 키워드를 사용해 이벤트를 설정**하고, 경우에 따라 **`emit` 키워드를 사용해 이벤트를 실행**한다. 이벤트가 실행된 경우, 트랜잭션에 기록된다.

```solidity
contract coinTransfer {
	// event 이벤트명(파라미터유형1 파라미터1, 파라미터유형2 파라미터2, ...);
	event Transfer(address from, address to, uint256 value);
	
	function transfer(address to, addres samount) {
		// ...
		// emit 이벤트명(인자1, 인자2, ...)
		emit Transfer(msg.sender, to, amount);
	}
}
```



***Copyright* © 2022 Song_Artish**