# solc

---

[TOC]

---



## Overview

solc는 솔리디티 컴파이러이다.



## 시작하기

### 설치

> 우분투OS 기준으로 작성되었다.

1. solc를 설치한다.

   ```shell
   sudo add-apt-repository ppa:ethereum/ethereum
   sudo apt update
   sudo apt install solc
   ```

2. 버전을 확인한다.

   ```shell
   solc --version
   ```

   위 명령어를 입력했을 때, 다음과 같은 출력값이 나와야 한다. (버전별로 사이할 수는 있다.)

   ```
   solc, the solidity compiler commandline interface
   Version: 0.8.15+commit.e14f2714.Linux.g++
   ```

3. 예제 코드를 작성해본다.

   `solc_practice`라는 폴더 생성 후 폴더 안에 `simpleStorage.sol` 파일을 만들고 아래 코드를 입력한다.

   ```solidity
   // SPDX-License-Identifier: GPL-3.0
   pragma solidity >=0.4.16 <0.9.0;
   
   contract SimpleStorage {
       uint storedData;
   
       function set(uint x) public {
           storedData = x;
       }
   
       function get() public view returns (uint) {
           return storedData;
       }
   }
   ```

   위 코드는 `set` 함수를 이용해 데이터를 저장하고, `get` 함수를 이용해 저장한 데이터를 반환하는 아주 간단한 컨트랙트이다.

### 솔리디티 코드 컴파일

솔리디티 코드 배포를 위해 `solc`를 사용해 컴파일을 한다. 위에서 생성한 `solc_practice` 디렉토리로 가서 다음 명령어를 입력한다.

```shell
solc --optimize --bin simpleStorage.sol
```

- `solc --bin {컴파일할 sol파일 이름}`: 솔리디티 파일을 이진 형식으로 컴파일하는 명령어
- `--optimize` 옵션: 컴파일 전 작성한 솔리디티 코드가 약 200회 실행된다고 가정했을 때를 기준으로 컨트랙트를 최적화

명령어를 실행하고 나면 16진수 이진코드가 출력된다. 이 이진코드는 작성한 솔리디티 코드를 컴파일한 결과값이며, EVM은 이 코드를 실행한다.

### ABI 생성

> **ABI(Application Binary Interface)**
>
> **스마트 컨트랙트 코드에 대한 설명**이 담긴 JSON 형식의 인터페이스이다. 이더리움 네트워크에 있는 각 노드들은 지갑을 통해 상호작용하는데, 이 때 JSON-RPC 형식의 데이터로 상호작용을 한다. 이 상호작용을 위한 데이터가 바로 ABI이다.
>
> ABI는 스마트 컨트랙트 코드에 있는 함수에 대해 정의하고, 컨트랙트에 있는 함수에 어떤 인자를 넣어야 하는지, 어떤 데이터가 반환되는지 등을 가지고 있으며, 노드가 컨트랙트를 실행하기 위해 어떤 작업을 수행해야 하는지 알려준다.

solc의 `--abi` 옵션을 사용해서 컨트랙트의 ABI를 생성한다. 아래의 명령어를 입력한다.

```shell
solc --abi simpleStorage.sol
```

명령어가 정상적으로 실행되면 배열이 출력된다. 배열에는 컨트랙트 내 함수에 대한 정보가 객체 형태로 들어가 있다.

```solidity
// ABI 예시
[
    {
        "inputs":[],
        "name":"get",
        "outputs":[{"internalType":"uint256","name":"","type":"uint256"}],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[{"internalType":"uint256","name":"x","type":"uint256"}],
        "name":"set",
        "outputs":[],
        "stateMutability":"nonpayable",
        "type":"function"
    }
]
```



***Copyright* © 2022 Song_Artish**