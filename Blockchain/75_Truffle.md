# Ganache

---

[TOC]

---



## Overview
truffle 프레임워크는 스마트 컨트랙트(solidity) 개발 시 개발, 배포 및 테스트 환경을 제공한다. 이 프레임워크는 node.js에서 동작하며 npm으로 설치할 수 있다.
**요구사항**
- NodeJS 5.0 이상
- Windows, Linux, Mac OS X
- JSON RPC API를 지원하는 이더리움 프로토콜

```bash
npm install -g truffle
```
설치 후 truffle을 실행하면 명령어를 확인할 수 있다.
- 공식 문서: https://trufflesuite.com/docs/truffle/overview



## Truffle 프로젝트 생성

다음 명령어를 통해 Truffle Sample Project를 만들어본다.

```bash
mkdir sample
cd sample
truffle init
```

sample 폴더에서 `truffle init`을 통해 트러플 프로젝트를 초기화한다. 정상적으로 수행이되면 폴더 구조가 생긴다.

- **contracts**: solidity로 개발된 스마트 컨트랙트 소스 파일 폴더
- **contracts/Migrations.sol**: 배포를 도와주는 solidity 파일(삭제하면 안 됨)
- **migrations**: 배포를 위한 스크립트 파일 폴더
- **migrations/1_initial_migration.js**: Migration.sol을 배포하는 스크립트
- **test**: 개발된 컨트랙트를 테스트하기 위한 폴더
- **truffle-config.js**: truffle 설정 파일

Migrations.sol 파일을 삭제하면 배포 시 오류가 발생한다. 배포 시 내부적으로 이 컨트랙트를 사용한다.

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

## Truffle Develop

TRUFFLE DEVELOP은 truffle에서 기본으로 제공하는 이더리움 클라이언트이다.

### 이더리움 클라이언트 실행

```bash
truffle develop
```

위 명령어를 프로젝트 루트폴더(여기서는 sample 폴더)에서 실행하면 10개의 Accounts와 Private Keys가 리스트업되면서 `truffle(develop)>` 프롬프트가 나타나게 된다. 또한 JSON-RPC용(http://127.0.0.1:9545/) 서비스가 제공된다.
명령어 실행과 동시에 truffle console로 입장하게 되는데, `.exit`을 입력하면 콘솔이 종료된다.

이전에 배웠던 Ganache와 같은 역할을 하는 이더리움 클라이언트이다.Ganache에서 배웠던 방법과 마찬가지로 MetaMask에 계졍을 연동하여 사용할 수 있따.

### 스마트 컨트랙트 컴파일

다음 명령어를 실행하면 프로젝트 루트 폴더에 `/build` 폴더가 생성이 되며, contracts 폴더 아래에 있는 solidity 파일이 json 형태로 변경되어 생성된다.

```shell
truffle(develop)> compile
```

### 스마트 컨트랙트 배포

아래 명령어 실행 시 `/build` 폴더에 생성된 파일이 서버에 배포된다.

```shell
truffle(develop)> migrate
```

### 스마트 컨트랙트 테스트

아래 명령어 실행 시 `/test` 폴더에 있는 `.js`, `.sol` 파일을 실행하여 테스트를 수행한다.

> 주의: solidity 파일로 테스트 파일을 생성 시 파일명은 contract 명과 일치하게 하며, contract name은 Test~로 시작하고, 함수명도 test~로 시작해야 한다.

```shell
truffle(develop)> test
```



## <실습> 스마트 컨트랙트 생성하기

### 샘플 코드 작성

`contracts/Sample.sol` 파일을 생성하고, 아래 코드를 스마트 컨트랙트 내용으로 저장한다.

```solidity
pragma solidity ^0.8.10;
contract SimpleStorage {
   uint val;

   function set(uint x) public {
      val = x;
   }

   function get() public view returns (uint) {
      return val;
   }
}
```

### 배포 스크립트 작성

`migrations/2_deploy_sample.js` 파일을 생성한다.

```javascript
var SimpleStorage = artifacts.require("SimpleStorage");

module.exports = function(deployer) {
   deployer.deploy(SimpleStorage);
}
```

컨트랙트를 호출할 때는 파일명이 아닌 컨트랙트명으로 불러온다. 배포 파일을 확인하면 파일명 앞에 숫자가 붙어 있다. migrations 폴더 아래에 포함된 모든 파일을 실행하기 때문에 배포 시 우선순위를 주기 위해 앞에 숫자를 붙여준다.

### 테스트 컨트랙트 작성

`test/TestSimpleStorage.sol` 파일을 생성한다.

```solidity
pragma solidity ^0.8.10;

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/Sample.sol";

contract TestSimpleStorage {
   function testSimpleStorage() public {
      SimpleStorage ss = new SimpleStorage();

      uint expected = 4;
      ss.set(expected);
      Assert.equal(ss.get(), expected, "value equal test");
   }
}
```

위 코드를 준비하면 테스트 과정이 모두 준비되었다. 이제 컴파일 후 Ethereum Client(Truffle Develop)에 배포하고 테스트까지 과정을 진행한다.

### 컴파일

생성한 스마트 컨트랙트를 컴파일한다.

```shell
truffle(develop) > compile
```

### 배포

```shell
truffle(develop) > migrate
```

### 테스트

아래 명령어를 통해 truffle develop에 배포, 테스트까지 완료한다.

```shell
truffle(develop) > test
```



## Truffle과 Ganache 연동

Truffle은 설정 파일만 간단히 수정하여 Ganache와 연동이 가능하다. Ganache 연동을 위해 네트워크 설정을 해야한다. `truffle-config.js` 파일을 간단히 수정한다.

```javascript
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

수정 후 truffle networks를 확인한다.

```shell
truffle(develop) > truffle networks
```

development 네트워크가 기본으로 등록된 것을 확인할 수 있다. 이전에 개발을 진행했던 파일을 그대로 Ganache 네트워크에 업데이트 해본다.

> Ganache에 블록이 추가되지 않으면, Truffle을 재시작해본다.

```shell
truffle(develop)> truffle migrate
```

Ganache > TRNASACTIONS 탭에서 Ganache 네트워크에 파일이 올라간 것을 확인할 수 있다.


***Copyright* © 2022 Song_Artish**