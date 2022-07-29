# <실습> 서버에서 Web3.js 라이브러리 사용하기

---

[TOC]

---



- [Web3.js 공식문서](https://web3js.readthedocs.io/en/v3.0.0-rc.5/)



## 1. 서버 구축하기

프로젝트를 위한 폴더(여기서는 `practice-webjs`)를 생성 후 터미널에서 명령어를 통해 노드 프로젝트를 시작한다.

```bash
mkdir practice-webjs
cd practice-webjs
npm init
```

npm을 통해 express와 web3를 설치한다

```bash
npm i express
npm i web3
```

프로젝트에 `index.js` 파일을 만들어 다음 내용을 입력한다.

```javascript
// index.js

const express = require('express')
const app = express()
const port = 8080

app.get('/', (req, res) => {
    res.send('Hello Node.js!')
})
app.listen(port, () => {
    console.log('Listening...')
})
```

package.json 파일에서 scripts 항목에 start를 추가한다.

```json
// package.json
    ...
    "scripts": {
        "start": "node index.js",   // 추가
        "test": "echo \"Error: no test specified\" && exit 1"
    },
    ...
```

서버를 실행한다.

```bash
npm start
```

http://localhost:8080/에 접속하여 서버가 잘 동작하는지 확인한다.



## 2. 로컬 블록체인 네트워크와 서버 연결하기

가나슈(Ganache)를 실행 후 상단 바의 `RPC SERVER`를 확인한다.

```
RPC SERVER
HTTP://127.0.0.1:7545
```

### `web3.eth.getAccounts()` - 계정 가져오기

가냐슈에 있는 계정을 가져오기 위해 아래 코드를 작성한다.

```javascript
// index.js

const express = require('express')
const app = express()
const port = 8080
const Web3 = require('web3')

function getWeb3() {
    const web3 = new Web3(new Web3.providers.HttpProvider('http://127.0.0.1:7545'))    // Ganache RPC Server
    return web3
}

async function getAccounts() {
    try {
        const accounts = await getWeb3().eth.getAccounts()
        console.log(accounts)
        return accounts
    } 
    catch (error) {
        console.log(error)
        return error
    }
}

app.get('/', (req, res) => {
    // res.send('Hello Node.js!')
    getAccounts()
        .then((accounts) => res.send(accounts))
})
app.listen(port, () => {
    console.log('Listening...')
})
```

해당 코드를 실행한다.

```bash
npm start
```

이후 http://localhost:8080 으로 접속하면 Account에 관한 계정 정보를 웹과 콘솔에서 확인할 수 있다.

위와 같은 방식으로 로컬 네트워크에서 web3 라이브러리를 활용할 수 있다. web3.js는 아래와 같은 라이브러리가 존재한다.

- [web3.eth](https://web3js.readthedocs.io/en/v3.0.0-rc.5/web3-eth.html), [web3.eth.subscribe](https://web3js.readthedocs.io/en/v3.0.0-rc.5/web3-eth-subscribe.html): 노드 관련 라이브러리
- [web3.eth.Contract](https://web3js.readthedocs.io/en/v3.0.0-rc.5/web3-eth-contract.html), [web3.eth.abi](https://web3js.readthedocs.io/en/v3.0.0-rc.5/web3-eth-abi.html): 컨트랙트 관련 라이브러리
- [web3.eth.accounts](https://web3js.readthedocs.io/en/v3.0.0-rc.5/web3-eth-accounts.html): 계정, 지갑 관련 라이브러리
- [web3.eth.personal](https://web3js.readthedocs.io/en/v3.0.0-rc.5/web3-eth-personal.html): 트랜잭션 관련 라이브러리
- [web3.*.net](https://web3js.readthedocs.io/en/v3.0.0-rc.5/web3-net.html): 이더리움이 아닌 다른 블록체인 네트워크를 추가하여 사용하는 경우
- [web3.utils](https://web3js.readthedocs.io/en/v3.0.0-rc.5/web3-utils.html): 암호화 등 유틸 라이브러리
- [web3.eth.ens](https://web3js.readthedocs.io/en/v3.0.0-rc.5/web3-eth-ens.html)
    let you interact with ENS
- [web3.eth.lban](https://web3js.readthedocs.io/en/v3.0.0-rc.5/web3-eth-iban.html)
    converts Ethereum addresses from and to IBAN and BBAN

### `web3.eth.getGasPrice()` - 가스비 확인하기

`web3.eth.getGasPrice()`는 가스비를 확인할 수 있는 함수이다. 블록체인 서비스를 제공할 때는 네트워크 사용량에 따라 변화하는 가스비를 책정해야 한다. 가스비를 잘못 책정하는 경우, 트랜잭션을 실행하다가 가스비가 부족해지면 트랜잭션이 revert되는 문제가 발생한다. 따라서 적절한 가스비를 계산해야 트랜잭션을 pending할 수 있다.

다음과 같이 코드를 작성한다.

```javascript
...

async function getGasPrice() {
    try {
        const gasPrice = await getWeb3().eth.getGasPrice()
        console.log(gasPrice)
        return gasPrice
    }
    catch (error) {
        console.log(error)
        return error
    }
}

app.get('/gasprice', (req, res) => {
    getGasPrice()
        .then((gasPrice) => res.send(gasPrice))
})

...
```

http://localhost:8080/gasprice 로 접속하면 가스비를 받아오는 것을 확인할 수 있다.

### `web3.eth.getBlock(blockHashOrBlockNumber)` - 블록 정보

`web3.eth.getBlock(blockHashOrBlockNumber)`는 블록 정보를 가져오기 위한 함수이다. 인자로는 블록의 해시값이나 블록 숫자를 넣을 수 있으며, String, Number, BN, BigNumber 타입으로 넣어야 한다. String 타입으로 값을 넣을 경우는 다음과 같다.
- `"earliest"`: 제네시스 블록
- `"latest"`: 최신 블록
- `"pending"`: 펜딩 상태인 블록

최신 블록의 정보를 가져오기 위해 다음과 같이 코드를 작성한다.

```javascript
...

async function getBlock() {
    try {
        const getBlock = await getWeb3().eth.getBlock("latest")
        console.log(getBlock)
        return getBlock
    }
    catch (error) {
        console.log(error)
        return error
    }
}

app.get('/getblock', (req, res) => {
    getBlock()
        .then((getBlock) => res.send(getBlock))
})

...
```


***Copyright* © 2022 Song_Artish**