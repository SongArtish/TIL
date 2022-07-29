# <실습> 크립토좀비 web.js

---

[TOC]

---



## Overview

> Ethereum JavaScript API

A collection of librarie that allow you to interact with a local or remote ethereum node using HTTP, IPC or WebSocket.

- 공식 문서: https://web3js.readthedocs.io/en/v1.7.4/

스마트 컨트랙트의 함수를 실행하기 위해서는, 이더리움 네트워크를 구성하고 있는 노드들 중 하나에 query를 보내어 다음의 내용을 전달해야 한다.

1. 스마트 컨트랙트 주소
2. 실행하고자 하는 함수
3. 해당 함수에 전달하고자 하는 변수들

이더리움 노드들은 JSON-RPC라고 불리는 언어로만 소통할 수 있는데, 컨트랙트의 함수를 실행을 위한 query는 다음과 같은 형태이다.

```json
{
    "jsonrpc":"2.0",
    "method":"eth_sendTransaction",
    "params":[{
        "from":"0xb60e8dd61c5d32be8058bb8eb970870f07233155",
        "to":"0xd46e8dd67c5d32be8058bb8eb970870f07244567",
        "gas":"0x76c0",
        "gasPrice":"0x9184e72a000",
        "value":"0x9184e72a",
        "data":"0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
    }],
    "id":1
}
```

> - JSON-RPC: JSON으로 인코딩된 원격 프로시저 호출. 매우 간단한 프로토콜(XML-RPC와 매우 흡사함)로서, 소량의 데이터 타입과 명령들만을 정의하고 있다.

web3.js는 이러한 query를 작성 대신, 코드에서 쉽게 함수를 호출할 수 있게 해주는데 다음과 같은 형태이다.

```javascript
CryptoZombies.methods.createRandomZombie("Vitalik Nakamoto 🤔")
  .send({ from: "0xb60e8dd61c5d32be8058bb8eb970870f07233155", gas: "3000000" })
```



## 시작하기

web3.js를 설치한다.

```bash
npm install web3    # npm 사용 시
yarn add web3   # yarn 사용 시
bower install web3  # bower 사용 시
```



## Web3 Provider

### Infru

Infru는 <u>빠른 읽기</u>를 위한 캐시 계층을 포함하는 다수의 이더리움 노드를 운영하는 서비스이다.

다음과 같이 Infru를 web3 provider로 사용할 수 있다.

```javascript
var web3 = new Web3(new Web3.providers.WebsocketProvider("wss://mainnet.infura.io/ws"));
```

### MetaMask

메타마스크(MetaMask)는 사용자들이 이더리움 계정과 개인키를 안전하게 관리할 수 있게 해주는 Chorme과 FireFox의 브라우저 확장 프로그램이다. 그리고 해당 계정들로 web3.js를 사용하는 웹사이트들과 상호작용할 수 있게 해준다.

다음과 같이 MetaMask의 web3 provider로 web3.js를 초기화할 수 있다.

```javascript
window.addEventListener('load', function() {

  // Web3가 브라우저에 주입되었는지 확인(Mist/MetaMask)
  if (typeof web3 !== 'undefined') {
    // Mist/MetaMask의 프로바이더 사용
    web3js = new Web3(web3.currentProvider);
  } else {
    // 사용자가 Metamask를 설치하지 않은 경우에 대해 처리
    // 사용자들에게 Metamask를 설치하라는 등의 메세지를 보여줄 것
  }

  // 이제 자네 앱을 시작하고 web3에 자유롭게 접근할 수 있네:
  startApp()

})
```



## 사용자 계정 가져오기

주입되어 있는 `web3` 변수에 현재 활성화된 계정이 무엇인지 다음과 같이 확인할 수 있다.

```javascript
var userAccount = web3.eth.accounts[0]
```

사용자가 언제든지 MetaMask에서 활성화된 계정을 바꿀 수 있기 때문에, 앱에서는 변수 값 변경 여부를 계속 감시해야 한다. 이를 위해 `setInterval`을 사용한다.

```javascript
var accountInterval = setInterval(function() {
  // 계정이 바뀌었는지 확인
  if (web3.eth.accounts[0] !== userAccount) {
    userAccount = web3.eth.accounts[0];
    // 새 계정에 대한 UI로 업데이트하기 위한 함수 호출
    updateInterface();
  }
}, 100);    // 100 ms마다 확인
```



## 컨트랙트 인스턴스화

컨트랙트 ABI 파일을 가져와서 import한다.

```html
<head>
    ...
    <!-- src에는 ABI 파일의 위치 및 파일명을 적절하게 입력한다. -->
    <script language="javascript" type="text/javascript" src="contractAbi.js"></script>
</head>
```

아래 코드와 같이 컨트랙트를 인스턴스화 할 수 있다.

```javascript
// myContract 인스턴스화
var myContract = new web3js.eth.Contract(myABI, myContractAddress);
```

아래 코드는 컨트랙트 인스턴스화 예시이다. `contractABI`에는 위에서 import한 `contractAbi.js`에 선언된 ABI 변수명을 입력한다.

```javascript
var contract_name

function startApp() {
var contract_address = "YOUR_CONTRACT_ADDRESS";
contract_name = new web3js.eth.Contract(contractABI, contract_address);
}
```



## 컨트랙트 함수 호출

web3.js에는 컨트랙트 함수 호출을 위한 메소드가 2가지 있다.

1. **call**: `view`와 `pure` 함수 호출을 위해 사용
    로컬 노드에서만 실행되고, 블록체인에 트랜잭션을 만들지는 않는다. web3.js를 사용하여, 다음과 같이 `123`을 매개 변수로 `myMethod`라는 이름의 함수를 `call`할 수 있다.
    ```javascript
    myContract.methods.myMethod(123).call()
    ```
2. **send**: 트랜잭션을 만들고 블록체인 상의 데이터를 변경함
    `view`와 `pure`가 아닌 모든 함수에 사용하며, 사용 시 가스를 지불해야 한다. web3.js를 사용하여, 다음과 같이 `123`을 매개 변수로 `myMethod`라는 이름의 함수를 호출하는 트랜잭션을 `send`할 수 있다.
    ```javascript
    myContract.methods.myMethod(123).send()
    ```

### 데이터 받아오기

Solidity에서는 `public`으로 변수를 선언하면 자동으로 같은 이름의 퍼블릭 "getter" 함수를 만든다.

```soliditiy
Zombie[] public zombies;
```

다음과 같이 좀비 ID를 받아 컨트랙트에 query를 보내고, 결과를 반환하는 javascript 함수를 작성할 수 있다. (여기서는 callback 대신 Promise를 사용함)

```javascript
function getZombieDetails(id) {
    return cryptoZombies.methods.zombies(id).call()
}

// 함수를 호출하고 결과를 가지고 무언가를 처리:
getZombieDetails(15)
.then(function(result) {
    console.log("Zombie 15: " + JSON.stringify(result));
});
```

Promise가 만들어지면(web3 provider로부터 응답을 받으면) `then` 문장이 실행되고 다음과 같은 `result` 결과가 표시된다.

```json
{
    "name": "H4XF13LD MORRIS'S COOLER OLDER BROTHER",
    "dna": "1337133713371337",
    "level": "9999",
    "readyTime": "1522498671",
    "winCount": "999999999",
    "lossCount": "0" // Obviously.
}
```

### 화면에 보여주기

컨트랙트로부터 받은 데이터를 html 문서에서 보여준다.

```html
<div id="zombies"></div>
```

여기서는 jQuery를 사용하여 간단한 예제를 다룬다.

```javascript
function displayZombies(ids) {
// 초기화
    $("#zombies").empty();
    for (id of ids) {
        getZombieDetails(id)
        .then(function(zombie) {
        // HTML에 변수를 넣기 위해 ES6의 "template literal" 사용
        // 각각을 #zombies div에 붙여넣기
        $("#zombies").append(`<div class="zombie">
            <ul>
            <li>Name: ${zombie.name}</li>
            <li>DNA: ${zombie.dna}</li>
            <li>Level: ${zombie.level}</li>
            <li>Wins: ${zombie.winCount}</li>
            <li>Losses: ${zombie.lossCount}</li>
            <li>Ready Time: ${zombie.readyTime}</li>
            </ul>
        </div>`);
        });
    }
}
```

### 트랜잭션 보내기

`send` 함수를 이용해 스마트 컨트랙트의 데이터를 변경한다.

아래의 예제는 MetaMask를 사용해 web3.js에서 위 함수를 호출한다.

```javascript
function createRandomZombie(name) {
    // 시간이 꽤 걸릴 수 있으니, 트랜잭션이 보내졌다는 것을
    // 유저가 알 수 있도록 UI를 업데이트해야 함
    $("#txStatus").text("Creating new zombie on the blockchain. This may take a while...");
    // 우리 컨트랙트에 전송하기:
    return CryptoZombies.methods.createRandomZombie(name)
    .send({ from: userAccount })
    .on("receipt", function(receipt) {
        $("#txStatus").text("Successfully created " + name + "!");
        // 블록체인에 트랜잭션이 반영되었으며, UI를 다시 그려야 함
        getZombiesByOwner(userAccount).then(displayZombies);
    })
    .on("error", function(error) {
        // 사용자들에게 트랜잭션이 실패했음을 알려주기 위한 처리
        $("#txStatus").text(error);
    });
}
```

여기서 `send` 부분에 작성된 `createRandomZombie` 함수의 솔리디티 코드는 다음과 같다.

```solidity
function createRandomZombie(string _name) public {
  require(ownerZombieCount[msg.sender] == 0);
  uint randDna = _generateRandomDna(_name);
  randDna = randDna - randDna % 100;
  _createZombie(_name, randDna);
}
```



## Payable 함수 호출하기

아래 코드를 활용해 eth 단위를 wei 단위로 변환할 수 있다. (1 eth = 10^18 wei)

```javascript
// 1 ETH를 Wei로 바꾼다
web3js.utils.toWei("1");
```

다음 코드는 `levelup` 함수를 호출할 때 사용자가 0.001 이더를 보낼 수 있게 해준다.

```javascript
CryptoZombies.methods.levelUp(zombieId)
.send({ from: userAccount, value: web3js.utils.toWei("0.001") })
```



## 이벤트(Event) 구독하기

`zombiefactory.sol`에는 새로운 좀비가 생성될 때마다 매번 호출되던 `NewZombie`라는 이벤트가 선언되어 있다.

```solidity
event NewZombie(uint zombieId, string name, uint dna);
```

web3.js에서 이 이벤트를 구독하여, 해당 이벤트가 발생할 때마다 Web3 Provider가 javascript 코드 내의 특정 로직을 실행시키도록 할 수 있다.

```javascript
cryptoZombies.events.NewZombie()
.on("data", function(event) {
  let zombie = event.returnValues;
  // `event.returnValue` 객체에서 이 이벤트의 세 가지 반환 값에 접근할 수 있다.
  console.log("새로운 좀비가 태어났습니다!", zombie.zombieId, zombie.name, zombie.dna);
}).on("error", console.error);
```

**`indexed` 사용하기**

이벤트를 필터링하고 현재 사용자와 연관된 변경만을 수신하기 위해, ERC721의 `Transfer` 이벤트 코드처럼 솔리디티 컨트랙트에 `indexed` 키워드를 사용해야 한다.

```solidity
event Transfer(address indexed _from, address indexed _to, uint256 _tokenId);
```

이 경우, `_from`과 `_to`가 `indexed` 되어 있기 떄문에, 앱의 event listener에서 필터링을 할 수 있다.

```javascript
// `filter`를 사용해 `_to`가 `userAccount`와 같을 때만 코드를 실행
cryptoZombies.events.Transfer({ filter: { _to: userAccount } })
.on("data", function(event) {
  let data = event.returnValues;
  // 현재 사용자가 방금 좀비를 받았네!
  // 해당 좀비를 보여줄 수 있도록 UI를 업데이트할 수 있도록 여기에 추가
}).on("error", console.error);
```

**지난 이벤트에 대한 query**

`getPastEvents`를 이용해 지난 이벤트들에 대해 query하고, `fromBlock`과 `toBlock` 필터들을 이용해 이벤트 로그에 대한 시간 범위를 솔리디티에 전달할 수 있다. (여기서 "block"은 이더리움 블록 번호를 나타낸다.)

```javascript
cryptoZombies.getPastEvents("NewZombie", { fromBlock: 0, toBlock: "latest" })
.then(function(events) {
  // `events`는 우리가 위에서 했던 것처럼 반복 접근할 `event` 객체들의 배열이다.
  // 생성된 모든 좀비의 목록을 우리가 받을 수 있다.
});
```

이벤트는 저렴한 형태의 storage로 사용하는 것이다. 여기서 단점이 되는 부분은 스마트 컨트랙트 자체 안에서는 이벤트를 읽을 수 없다는 것이다. 하지만 히스토리로 블록체인에 기록하여 앱의 FE에서 읽기 원하는 데이터가 있다면, 위와 같이 사용해야 한다.


***Copyright* © 2022 Song_Artish**