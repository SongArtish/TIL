# Klaytn Testnet

---

[TOC]

---



## baobab

baobab(바오밥)은 크레이튼 기반 테스트넷으로, 메인넷에서 새로운 스마트 컨트랙트를 발행하기 전 테스트해볼 수 있는 네트워크이다.

> 스마트 컨트랙트를 생성하는 과정은 클레이튼 기반 블록체인 위에 새로운 프로그램을 등록하는 행위이다.

**지갑 생성하기**

> :pushpin: 테스트용 클레이튼 지급을 요구할 때마다 지갑의 개인키를 이용해야 하기 때문에, **테스트용 지갑은 메인넷 지갑과 별개로 사용**하는 것이 좋다.

카이카스 지갑을 생성하고 테스트넷으로 네트워크를 전환한다.

**테스트 클레이튼 받기**

[Klaytn Wallet](https://baobab.wallet.klaytn.foundation/access?next=faucet) 페이지로 이동한다. 우측 상단의 네트워크가 `Baobab Testnet`인지, 그리고 좌측 선택된 카테고리가 `Klay Faucet`인지 확인한다. 그리소 복사한 개인키를 붙여놓고 `Access` 버튼을 누른다.

이후 private key와 account address(public key)를 입력하면 테스트 클레이튼을 받을 수 있다.



## <실습> Baobab Network에 스마트 컨트랙트 배포하기

### Klaytn IDE 사용

[Klaytn IDE](https://ide.klaytn.foundation
)를 사용하여 Baobab Network에 스마트 컨트랙트를 배포해본다.

1. Klaytn IDE의 contract 폴더에 Count.sol 파일을 만들고, 다음 코드를 입력한다.


```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract Count {
    uint256 public count = 0;

    function setCount(uint256 _count) public {
        count = _count;
    }
}
```

2. KLAY를 받은 계정을 IDE에 import하여 Baobab Network에 배포를 진행한다.
3. 



***Copyright* © 2022 Song_Artish**