# Solidity 함수

---

[TOC]

---

## 함수 선언

솔리디티에서 함수는 다음과 같이 선언한다.

```solidity
function 함수이름(파라미터형식1 마라미터1, 파라미터형식2 파라미터2, ...) {...}
```

함수가 값을 반환하는 경우, 다음과 같이 선언한다.

```solidity
function 함수이름(파라미터, ...) returns (반환 형식) {...}
```

## 접근 수준

> 여기 내용은 **함수 접근 수준**으로, **상태 변수 접근 수준**과는 다른 내용이다.

```markdown
1. public: contract의 내부/외부 모두에서 해당 함수 호출 가능
2. private: contract 내부에서만 호출 가능
3. internal: cotract 내부 혹은 상속된 contract에서 호출 가능
4. external: contract의 외부에서만 호출 가능 (contract 내부 호출 불가)
```

- `public` (default)
  - 외부에서도 접근 가능
  - 컨트랙트 내부, 외부, 클라이언트 코드에서 모두 호출 가능
- `external`
  - public과 비슷함
  - 외부(external) 컨트랙트나 클라이언트 코드에서 호출 가능
  - 컨트랙트 내부에서는 호출 불가능, `f()`로 호출 불가능
  - **컨트랙트 내부에서 호출**하는 경우, `this.f()`와 같이 **`this`를 활용한 호출** 가능
- `internal`
  - 컨트랙트 멤버와 상속된 컨트랙트에서 호출 가능
- `private`
  - 컨트랙트 멤버만 호출 가능

> 무언가를 `internal` 혹은 `private`로 만드는 것은 다른 계약이 정보를 읽거나 수정하는 것을 방지할 뿐이다. 퍼블릭 블록체인 특성상 데이터는 공개되어 있다.

```solidity
contract exampleC {
    function changeName(address account, string newName) internal {...}
    function checkGas(uint256 amount) private returns (bool) {...}
}
```

## Qualifier

함수가 컨트랙트 내부 상태를 변경할 수 있는 능력을 선언하는 것이다.

### view, pure

- `view`로 표시된 함수는 상태를 변경하지 않는 읽기 전용 함수이다. 
- `pure`는 스토리지에서 변수를 읽거나 쓰지 않는 함수이다.

```solidity
proagma solidity ^0.8.14;
contract exampleC {
    uint256 public constant maxLimit = 1000;
    mapping(address => bool) public frozenAccount;

    function checkGas(uint256 amount) private pure returns (bool) {
        if (amount < maxLimit) return true;
        return false;
    }
    function validateAccount(address account) internal view returns (bool) {
        if (frozenAccount[account]) return true;
        return false;
    }
}
```

### payable

- `payable`을 선언하면 함수에서 이더를 받을 수 있다.

```solidity
proagma solidity ^0.8.14;
contract exampleC {
    function getEther() payable returns (bool) {
        if (msg.value === quoteFee) {
            // ...
        }
    }
}
```

## 생성자 함수(constructor)

생성자 함수를 선언하면, 컨트랙트가 생성될 때 생성자 함수가 실행되며 컨트랙트의 상태를 초기화할 수 있다. `constructor` 키워드를 사용해 생성자 함수를 선언할 수 있다.

```solidity
proagma solidity ^0.8.14;
contract exampleC {
    address public account;
    constructor(address _account) internal {
        account = _account
    }
}
```

## selfdestruct

`selfdestruct` 함수를 사용하여 컨트랙트를 소명할 수 있다.

```solidity
selfdestruct(컨트랙트 생성자의 주소);
```

## 함수 제어자(modifier)

비슷한 역할을 하는 코드를 모아서 만든 특별한 형태의 함수이다. 함수 선언에 `modifier`를 추가하여 함수에 변경자를 적용할 수 있다.

> 변경자: 함수를 실행하기 전, 요구 조건을 만족하는지 확인하는 작업

변경자를 작성할 때는 `_;`를 사용한다. `_;`는 함수를 실행하는 시점을 나타내며, 변경자 코드는 `_;` 코드를 기준으로 실행 시점이 달라진다. `_;` 이전의 코드는 함수가 실행되기 전에 실행되고, `_;` 이후의 코드는 함수 실행이 종료되고 실행된다.

```solidity
int public num = 0;
modifier changeNum {
    num++;    // 함수 실행 전 실행됨
    _;    // 함수 실행
    num--;    // 함수 실행 후 실행됨
}
```

위 예시 코드에서 선언한 `chnageNum` 변경자는 다음과 같이 사용할 수 있다.

```solidity
function func() public changeNum {
    if (num == 1) {
        // do something
    }
}
```

함수 변경자를 사용하면 함수를 **선언적**으로 사용할 수 있다는 특징이 있다.

## Function Overloading

A contract can have multiple functions of the same name but with different parameter types. This process is called “overloading” and also applies to inherited functions. The following example shows overloading of the function `f` in the scope of contract `A`.

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract A {
    function f(uint value) public pure returns (uint out) {
        out = value;
    }

    function f(uint value, bool really) public pure returns (uint out) {
        if (really)
            out = value;
    }
}
```

- [참고 자료](https://docs.soliditylang.org/en/v0.8.14/contracts.html?highlight=constant#function-overloading)

***Copyright* © 2022 Song_Artish**