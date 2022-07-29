# Solidity 상속

---

[TOC]

---



## 상속

솔리디티의 `contract` 객체는 상속을 지원한다. 상속을 통해 컨트랙트에 기능들을 추가하고, 확장할 수 있다. 상속을 사용하려면 부모 컨트랙트에 `is` 키워드를 지정해준다.

```solidity
contract ChildContract is ParentContract {
	// ...
}
```

솔리디티는 **다중 상속**도 지원한다.

```solidity
contract ChildContract is ParentContract1, ParentContract2, ParentContract3 {
	// ...
}
```



## Function Overriding

Base functions can be overridden by inheriting contracts to change their behavior if they are marked as `virtual`. The overriding function must then use the `override` keyword in the function header. The overriding function may only change the visibility of the overridden function from `external` to `public`. The mutability may be changed to a more strict one following the order: `nonpayable` can be overridden by `view` and `pure`. `view` can be overridden by `pure`. `payable` is an exception and cannot be changed to any other mutability.

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Base
{
    function foo() virtual external view {}
}

contract Middle is Base {}

contract Inherited is Middle
{
    function foo() override public pure {}
}
```

- [참고 자료](https://docs.soliditylang.org/en/v0.8.14/contracts.html#function-overriding)



***Copyright* © 2022 Song_Artish**