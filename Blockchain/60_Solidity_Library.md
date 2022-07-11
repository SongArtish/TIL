# Solidity 라이브러리

---

[TOC]

---



## 라이브러리

라이브러리의 목적은 "코드를 공유"하기 위함이다. 컨트랙트 간에 코드를 공유하거나, 공통적인 기능을 재사용하고자 할 때 우리는 라이브러리를 활용한다.

- 참고: https://www.openzeppelin.com/



## 라이브러리 호출

외부 라이브러리를 호출할 때는 기존 컨트랙트 호출과는 다른 방식으로 진행한다.

- contract 키워드 대신 `library` 키워드 사용
- 상태 변수, 상속 관계, fallback 함수, payable 함수 지원 안 됨
- 파라미터 받는 것 가능
- 호출 방법
  - `라이브러리 이름.메소드이름()`
  - `using 라이브러리 이름 for 데이터타입`

```solidity
import "./UIntFunctions.sol";
contract Example {
	function isEven(uint x) public pure returns(bool) {
		return UIntFunctions.isEven(x);
	}
}
```

```solidity
import "./UIntFunctions.sol";
contract Example {
	using UIntFunctions for uint;
	function isEven(uint x) public pure returns(bool) {
		return x.isEven()
	}
}
```



***Copyright* © 2022 Song_Artish**