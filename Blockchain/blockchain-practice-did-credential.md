# <실습> DID를 활용한 졸업증명서 개발

---

[TOC]

---



## Overview

여기서는 간단하게 부트캠프 졸업을 증명하는 졸업증명서를 개발해본다.

먼저 **검증 가능한 크리덴셜과 크리덴셜이 저장될 공간**을 고려해야 한다. [vc-data-model 페이지](https://ssimeetupkorea.github.io/vc-data-model/#basic-concepts)에서 정의하는 크리덴셜은 다음과 같다.


## 1단계: 졸업증명서 개발하기

### 전체 코드

이 코드는 Issuer와 Credential을 포함하는 Solidity 코드이다. `claimCredential` 함수로 Credential을 발행하고, `getCredential` 함수를 통해 Credential을 발행한 주소에서 VC를 확인하는 간단한 구조이다.

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.15;

contract CredentialBox {
    address private issuerAddress;
    uint256 private idCount;
    mapping(uint8 => string) private alumniEnum;

    // VC 구현을 위한 구조체
    struct Credential {
        uint256 id; // index 순서를 표기하는 idCount
        address issuer; // 발급자
        uint8 alumniType;   // 졸업증명서 타입
        string value;   // credential에 포함되어야 하는 암호화된 정보 (JSON 형태)
    }

    mapping(address => Credential) private credentials;

    constructor () {
        issuerAddress = msg.sender;
        idCount = 1;
        alumniEnum[0]= "SEB";
        alumniEnum[1]= "BEB";
        alumniEnum[2]= "AIB";
    }

    function claimCredential(address _alumniAddress, uint8 _alumniType, string calldata _value) public returns (bool) {
        require(issuerAddress == msg.sender, "Not Issuer");
            Credential storage credential = credentials[_alumniAddress];
        require(credential.id == 0);    // 초기값(비어있는 값)인지 확인 - solidty는 uint, int의 초기값이 null이 아닌 0이다.
        credential.id = idCount;
        credential.issuer = msg.sender;
        credential.alumniType = _alumniType;
        credential.value = _value;

        idCount += 1;

        return true;
    }

    function getCredential(address _alumniAddress) public view returns (Credential memory) {
        return credentials[_alumniAddress];
    }

}
```

### 1. Credential 구조제

```solidity
    // VC 구현을 위한 구조체
    struct Credential {
        uint256 id; // index 순서를 표기하는 idCount
        address issuer; // 발급자
        uint8 alumniType;   // 졸업증명서 타입
        string value;   // credential에 포함되어야 하는 암호화된 정보 (JSON 형태)
    }
```

### 2. `claimCredential` 함수

```solidity
    function claimCredential(address _alumniAddress, uint8 _alumniType, string calldata _value) public returns (bool) {
        require(issuerAddress == msg.sender, "Not Issuer");
            Credential storage credential = credentials[_alumniAddress];
        require(credential.id == 0);    // 초기값(비어있는 값)인지 확인 - solidty는 uint, int의 초기값이 null이 아닌 0이다.
        credential.id = idCount;
        credential.issuer = msg.sender;
        credential.alumniType = _alumniType;
        credential.value = _value;

        idCount += 1;

        return true;
    }
```

`claimCredential` 함수를 통해 발급자(issuer)는 어떠한 주체(_alumniAddress)에게 크리덴셜(Credential)을 발행(claim)할 수 있게 된다.

### 3. `getCredential` 함수

```solidity
    function getCredential(address _alumniAddress) public view returns (Credential memory) {
        return credentials[_alumniAddress];
    }
```

이 함수를 통해 어떠한 주체(_alumniAddress)를 통해 발행(claim)한 크리덴셜(Credential)을 확인할 수 있다.

### 4. Remix를 이용하여 스마트 컨트랙트 배포 & 사용

1. Remix에서 `CredentialBox.sol`이라는 파일을 만들고, 전체 코드를 입력한다.
2. 컨트랙트 코드를 컴파일한다.
3. 컨트랙트 코드를 배포한다. (Ropsten 테스트넷)
4. 배포가 완료되면, `claimCredential` 함수를 실행한다.
    - _alumniAddress: Credential을 발행받을 테스트넷 주소
    - _alumniType: 졸업증명서 타입 (BEB이라면 1)
    - _value: 아래의 예시 코드를 붙여넣는다. (JWT으로 암호화된 토큰이다.)
        ```
        eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWRwIjoiY29kZSBzdGF0ZXMiLCJ0eXBlIjoiYmViIiwidG9rZW4iOiJ0ZXN0IiwidmFsdWUiOiLsvZTrk5zsiqTthYzsnbTsuKAgRElEIOyImOujjOymnSDrsJzquInsnYQg7JyE7ZWcIO2BrOumrOuNtOyFnCDthYzsiqTtirgifQ.82P54qXYP-dY1_dKSv9RGISg_NhzEfILioFYRfCe5B0
        ```
        > 해당 내용은 [jwt 페이지](https://jwt.io/)에서 decode하여 확인할 수 있다.
5. Credential 컴펌이 완료되었다면, `getCredential` 함수를 실행한다.
    - _alumniAddress: Credential을 발행받은 주소
    `getCredential` 함수를 통해 해당 주소에게 저장되어있던 검증가능한 크리덴셜이 발행되었음을 확인할 수 있다.
    ```
    tuple(uint256,address,uint8,string): 1,0xB5dD06311DeD26053c00E4dc8d96f3003ba3CbE2,2,eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWRwIjoiY29kZSBzdGF0ZXMiLCJ0eXBlIjoiYmViIiwidG9rZW4iOiJ0ZXN0IiwidmFsdWUiOiLsvZTrk5zsiqTthYzsnbTsuKAgRElEIOyImOujjOymnSDrsJzquInsnYQg7JyE7ZWcIO2BrOumrOuNtOyFnCDthYzsiqTtirgifQ.82P54qXYP-dY1_dKSv9RGISg_NhzEfILioFYRfCe5B0
    ```



## 2단계: 다양한 기능을 추가한 크리덴셜 실습

이번에는 기존에 개발했던 졸업증명서 코드에 이전에 배웠던 솔리디티 문법을 활용하여 다양한 기능을 추가한 것이다.

### 전체 코드

단순히 발급하는 형태의 스마트 컨트랙트에서 issuer를 컨트롤하고, 발급 시간에 대한 정보를 크리덴셜에 추가하고, 상태를 변경하는 함수도 추가하였다.

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.15;

abstract contract OwnerHelper {
    address private owner;

    event OwnerTransferPropose(address indexed _from, address indexed _to);

    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function transferOwnership(address _to) onlyOwner public {
        require(_to != owner);
        require(_to != address(0x0));
        owner =_to;
        emit OwnerTransferPropose(owner, _to);
    }
}

abstract contract IssuerHelper is OwnerHelper {
    mapping(address => bool) public issuers;

    event AddIssuer(address indexed _issuer);
    event DelIssuer(address indexed _issuer);

    modifier onlyIssuer {
        require(isIssuer(msg.sender) == true);
        _;
    }

    constructor() {
        issuers[msg.sender] = true;
    }

    function isIssuer(address _addr) public view returns (bool) {
        return issuers[_addr];
    }

    function addIssuer(address _addr) onlyOwner public returns (bool) {
        require(issuers[_addr] == false);
        issuers[_addr] = true;
        emit AddIssuer(_addr);
        return true;
    }

    function delIssuer(address _addr) onlyOwner public returns (bool) {
        require(issuers[_addr] == true);
        issuers[_addr] = false;
        emit DelIssuer(_addr);
        return true;
    }
}

contract CredentialBox is IssuerHelper {
    uint256 private idCount;
    mapping(uint => string) private alumniEnum;
    mapping(uint => string) private statusEnum; // status 정보 추가

    struct Credential {
        uint256 id;
        address issuer;
        uint8 alumniType;
        uint8 statusType;   // 추가
        string value;
        uint256 createData; // 추가
    }

    mapping(address => Credential) private credentials;

    constructor () {
        idCount = 1;
        alumniEnum[0]= "SEB";
        alumniEnum[1]= "BEB";
        alumniEnum[2]= "AIB";
    }

    function claimCredential(address _alumniAddress, uint8 _alumniType, string calldata _value) onlyIssuer public returns (bool) {
        Credential storage credential = credentials[_alumniAddress];
        require(credential.id == 0);
        credential.id = idCount;
        credential.issuer = msg.sender;
        credential.alumniType = _alumniType;
        credential.statusType = 0;  // 추가
        credential.value = _value;
        credential.createData = block.timestamp;    // 추가

        idCount += 1;

        return true;
    }

    function getCredential(address _alumniAddress) public view returns (Credential memory) {
        return credentials[_alumniAddress];
    }

    function addAlumniType(uint8 _type, string calldata _value) onlyIssuer public returns (bool) {
        require(bytes(alumniEnum[_type]).length == 0);  //
        alumniEnum[_type] = _value;
        return true;
    }

    function getAlumniType(uint8 _type) public view returns (string memory) {
        return alumniEnum[_type];
    }

    function addStatusType(uint8 _type, string calldata _value) onlyIssuer public returns (bool) {
        require(bytes(statusEnum[_type]).length == 0);
        statusEnum[_type] = _value;
        return true;
    }

    function getStatusType(uint8 _type) public view returns (string memory) {
        return statusEnum[_type];
    }

    function changeStatus(address _alumni, uint8 _type) onlyIssuer public returns (bool) {
        require(credentials[_alumni].id != 0);
        require(bytes(statusEnum[_type]).length != 0);
        credentials[_alumni].statusType = _type;
        return true;
    }
}
```

### Issue 추가 & 삭제

OwnerHelper는 기존의 OwnerHelper와 동일하다. 하지만 IssuerHelper가 추가되었다. IssuerHelper에서는 Issuer를 추가/삭제하는 기능이 존재한다. 추가/삭제 기능은 onlyOwner로 제한되어 OWner만 컨트롤이 가능하다.

```solidity
abstract contract IssuerHelper is OwnerHelper {
    mapping(address => bool) public issuers;

    event AddIssuer(address indexed _issuer);
    event DelIssuer(address indexed _issuer);

    modifier onlyIssuer {
        require(isIssuer(msg.sender) == true);
        _;
    }

    constructor() {
        issuers[msg.sender] = true;
    }

    function isIssuer(address _addr) public view returns (bool) {
        return issuers[_addr];
    }

    function addIssuer(address _addr) onlyOwner public returns (bool) {
        require(issuers[_addr] == false);
        issuers[_addr] = true;
        emit AddIssuer(_addr);
        return true;
    }

    function delIssuer(address _addr) onlyOwner public returns (bool) {
        require(issuers[_addr] == true);
        issuers[_addr] = false;
        emit DelIssuer(_addr);
        return true;
    }
}
```

### 클레임 시간 추가하기(`claimCredential`)

`claimCredential`에서 block.timestamp를 활용해 크리덴셜을 클레이한 시간을 크리덴셜에 저장하 수 있다.

```solidity
    function claimCredential(address _alumniAddress, uint8 _alumniType, string calldata _value) onlyIssuer public returns (bool) {
        Credential storage credential = credentials[_alumniAddress];
        require(credential.id == 0);
        credential.id = idCount;
        credential.issuer = msg.sender;
        credential.alumniType = _alumniType;
        credential.statusType = 0;  // 추가
        credential.value = _value;
        credential.createData = block.timestamp;    // 추가

        idCount += 1;

        return true;
    }
```

### Alumni 타입 추가하기

alumniType은 초기에 3가지가 제공된다.

```solidity
constructor() {
        idCount = 1;
        alumniEnum[0] = "SEB";
        alumniEnum[1] = "BEB";
        alumniEnum[2] = "AIB";
}
```

이후 더 많은 type이 생길 수 있기 때문에, 이를 위해 Alumni의 타입을 추가하는 함수가 필요하다.

```solidity
function addAlumniType(uint8 _type, string calldata _value) onlyIssuer public returns (bool) {
        require(bytes(alumniEnum[_type]).length == 0);
        alumniEnum[_type] = _value;
        return true;
}
```

솔리디티 내부에는 String을 검사하는 두 가지 방법이 있다.

1. bytes로 변환하여 길이로 null인지 검사하는 방법
2. keccak256 함수를 사용하여 두 string을 해시로 변환하여 비교하는 방법

위의 코드에서는 첫 번째 방법을 이용하여 내부 alumniEnum의 Type이 중복되는 타입이 존재하는지 검사했다.

### 특정 사용자의 상태를 변경하는 기능(`changeStatus`)

`changeStatus` 함수는 특정 사용자의 상태를 변경하는 함수이다. 해당 함수를 통해 크리덴셜 내부에 존재하는 statusType의 값을 가져와 변경할 수 있다.

```solidity
function changeStatus(address _alumni, uint8 _type) onlyIssuer public returns (bool) {
        require(credentials[_alumni].id != 0);
        require(bytes(statusEnum[_type]).length != 0);
        credentials[_alumni].statusType = _type;
        return true;
}
```



***Copyright* © 2022 Song_Artish**