# OpenZeppelin

---

[TOC]

---



## Overview

오픈제플린(OpenZeppelin)은 2015년 데미안 브리너와 마누엘 아라오스가 공동설립한 개발 회사이다. 오픈제플린은 솔리디티 기반의 스마트 컨트랙트를 개발하는 프레임워크인 오픈제플린(OpenZeppelin)과, 스마트 컨트랙트를 관리하고 운영하는 플랫폼인 제플린OS를 제공하고 있다.

데미안 브리너와 마누엘 아라오스는 2015년부터 스마트 컨트랙트 개발을 위해 가장 인기 있는 라이브러리를 구축하고, 보안 감사 분야에서 최고의 회사들과 협력하고, 분산된 애플리케이션을 위한 개발 플랫폼을 개발하기 시작했다. 그들의 프로젝트는 회사를 설립하게 되며, Smart Contract Solutions에서 Zeppelin Solutions로, 그리고 나중에 제플린(Zeppelin)으로 이름이 바뀌었다.



## OpenZeppelin 라이브러리 사용 방법

Remix와 Truffle을 이용하여 오픈제플린 라이브러리를 사용한다.

### Truffle을 이용한 openzeppelin-solidity Library 활용

openZeppelinSample 폴더를 만들고 `truffle init`을 통해 트러플 기반 프로젝트 초기화를 진행한다.

```bash
mkdir openZeppelinSample
cd openZeppelinSample
truffle init
```

솔리디티 사용을 위한 openzeppelin solidity 라이브러리를 설치해준다.

```bash
npm install -E openzeppelin-solidity
```

VS Code에서 확인하면 `node_modules`에서 openzeppelin-solidity 내부 구조를 확인할 수 있다.

Ganache에 업로드하기 위해 Ganache - Truffle 연동을 진행한다.

```javascript
// truffle-config.js
module.exports = {
   networks: {
      development: {
         host: "127.0.0.1",
         port: 7545,
         network_id: "5777",
      },
   },
}
```

> **Migrations.sol이 아닌 `Migrations.ligo` 파일이 생성되는 경우**

`Migrations.sol` 파일을 생성 후 아래 코드를 넣어준다.

```solidity
pragma solidity ^0.5.16;

contract Migrations {
  address public owner;
  uint256 public last_completed_migration;

  modifier restricted() {
    if (msg.sender == owner) _;
  }

  constructor() public {
    owner = msg.sender;
  }

  function setCompleted(uint completed) public restricted {
    last_completed_migration = completed;
  }

  function upgrade(address new_address) public restricted {
    Migrations upgraded = Migrations(new_address);
    upgraded.setCompleted(last_completed_migration);
  }
}
```

`migrations > 1_initial_migration.js` 파일은 다음과 같이 변경해준다.

```javascript
const Migrations = artifacts.require("Migrations");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
};
```

만약 솔리디티 버전이 openzeppelin 버전과 다르다면 `truffle-config.js`를 수정한다.

```javascript
   compilers : {
      solc : {
         version: "0.8.10",
      },
   }
```



## ERC-20 스마트 컨트랙트 작성

OpenZeppelin 라이브러리를 활용해 간단한 ERC-20 컨트랙트를 작성 후 배포해본다. `ZeppelinTestToken.sol` 파일을 작성한다.

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.10;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract ZeppelinTestToken is ERC20 {
   constructor() ERC20("ZeppelinTestToken", "ZTT") {
      _mint(msg.sender, 100000000e18);
   }
}
```

이전에 작성했던 ERC-20 코드에 비해 많은 부분이 없어지고 간편해졌다.

migrations 폴더 안에 `2_deploy_ZeppelinTestToken.js`를 작성한다.

```javascript
var ZeppelinTestToken = artifacts.require("ZeppelinTestToken");

module.exports = function(deployer) {
   deployer.deploy(ZeppelinTestToken);
};
```

배포를 하기 전 사용할 openzeppelin/contract 경로를 추가한다.

```bash
npm install @openzeppelin/contracts
```

이후 배포를 진행하여 Ganache에서 블록 생성과 MetaMask를 활용한 테스트를 실시한다.

```bash
truffle migrate
```

contracts/ZeppelinTestToken의 코드를 살펴보면 import를 통해 라이브러리에 존재하는 `ERC20.sol` 파일을 가져와서 사용할 수 있다.

```javascript
import "@openzeppelin/contracts/token/ERC20/ERC20.sol
```

- [OpenZeppelin ERC-20 Library](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#ERC20)



## Remix에서 OpenZeppelin Library 사용하기

### Remix에서는 자동으로 npm 패키지를 제공한다.

1. `ZeppelinTestToken.sol` 파일을 만들어 위에서 사용한 코드를 사용하면 확인할 수 있다. 
2. 왼쪽 `FILE EXPLORERS`에서 `.deops/npm` 아래로 `@openzeppelin`을 확인할 수 있다.
3. MetaMask를 이용해 배포 후 토큰이 잘 들어왔는지 테스트를 진행한다.

### Remix에서는 Github를 import할 수 있다.

1. Home에서 하단의 GitHub를 누른다.
2. 나타나는 팝업창에서 openzeppelin의 github 주소를 추가한다. 최종 파일의 엔드포인트 URI를 입력한다.
   다음은 GitHub 주소를 추가할 때 사용하는 리스트의 예시이다.
   - ERC20.sol: https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v2.5.1/contracts/token/ERC20/ERC20.sol
   - IERC20.sol: https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v2.5.1/contracts/token/ERC20/IERC20.sol
   - Context.sol: https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v2.5.1/contracts/GSN/Context.sol
   - SafeMath.sol: https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v2.5.1/contracts/math/SafeMath.sol
   - SimpleToken.sol: https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v2.5.1/contracts/examples/SimpleToken.sol
   - ERC20Detailed.sol: https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v2.5.1/contracts/token/ERC20/ERC20Detailed.sol
3. 추가를 완료하면 FILE EXPLORERES에서 `github > OpenZeppelin > ...` 하위에 파일(ex. `ERC20.sol`)이 생성된 것을 확인할 수 있다.


***Copyright* © 2022 Song_Artish**