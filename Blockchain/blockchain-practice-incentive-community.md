# <실습> 인센티브 커뮤니티 만들기

---

[TOC]

---


## Overview

여기서는 인센티브 커뮤니티를 만들기 위한 과정 중, 백엔드 작업 과정에 대해서 다룬다.



## 컨트랙트 배포하기

> Truffle을 이용하여 Ganache 네트워크에 컨트랙트를 배포한다.

**1. contract 전용 폴더 생성**

   truffle을 이용하여 배포할 컨트랙트 폴더를 생성한다.

   ```shell
   mkdir contract
   cd contract
   ```

**2. truffle 설치 및 초기화**

   contract 폴더에서 truffle을 설치하고 초기화한다.

   ```bash
   npm install truffle
   truffle init
   ```

   초기화가 완료되면 폴더 구조가 생성된 것을 확인할 수 있다. 각 폴더 및 파일은 다음과 같은 역할을 한다.

   - **contracts**: solidity로 개발된 스마트 컨트랙트 소스 파일 폴더
   - **contracts/Migrations.sol**: 배포를 도와주는 solidity 파일
   - **migrations**: 배포를 위한 스크립트 파일 폴더
   - **migrations/1_initial_migration.js**: 해당 js파일 안에 명시된 sol 파일을 배포하는 스크립트로, `1_initial_migration.js` 다음 `2_initial_migration.js` 이렇게 숫자 순서에 맞게 파일을 생성하여 배포할 sol 파일을 명시하면, 해당 숫자 순서대로 배포가 이루어진다.
   이를 이용하여 아직 배포 전인 컨트랙트만 확인하여 자동으로 배포가 진행된다.
   - **test**: 개발된 컨트랙트를 테스트하기 위한 폴더
   - **truffle-config.js**: truffle 설정 파일. 여기서 배포할 네트워크 설정을 하게 된다.

**3. truffle-config.js에 설정 추가**

   Ganache의 NETWORK ID와 SERVER PORT를 확인한다. 그리고 truffle-config.js에 Ganache 네트워크 아이디와 포트를 설정한다.

   ```javascript
   // truffle-config.js

      //...
      networks: {
         development: {
            host: "127.0.0.1",
            port: 7545,
            networkd_id: "5777",
         }
      },
      compilers: {
         solc: {
            version: "0.8.10,
         }
      },
      // ...
   ```

**4. 배포 후 트랜잭션 확인**

   배포할 컨트랙트 파일들을 migrations 폴더에 순서대로 배포 스크립트를 작성하면, 아래처럼 스크립트의 숫자 순서대로 배포가 진행됨을 알 수 있다.

   ```
   ㄴmigrations
      ㄴ1_initial_migration.js
      ㄴ2_initial_migration.js
      ㄴ3_initial_migration.js
   ```

   ```javascript
   // 1_initial_migration.js
   const Migrations = artifacts.require("Migrations);

   module.exports = function (deployer) {
      deployer.deploy(Migrations)
   }

   // 2_initial_migration.js
   const SimpleToken = artifacts.require("SimpleToken")

   module.exports = function (deployer) {
      deployer.deploy(SimpleToken)
   }
   // 3_initial_migration.js
   const MyNFTs = artifacts.require("MyNFTs")

   module.exports = function (deployer) {
      deployer.deploy(MyNFTs)
   }
   ```



## 서버 세팅하기

1. 서버 폴더를 npm으로 초기화하고, 프로젝트에 필요한 기본적인 패키지를 설치한다.

   ```bash
   npm init
   npm i sequelize sequelize-cli mysql2 dotenv web3 ...
   ```

2. 코드 개발에 필요한 폴더를 분리하여 생성한다. (참고 - [Route-Controller-Service Structure](https://sodocumentation.net/node-js/topic/10785/route-controller-service-structure-for-expressjs))

   - `models`: DB 스키마를 정의
   - `routes`: API route를 정의
   - `controllers`: 요청과 응답에 대한 로직 담당
   - `services`: DB와 CRUD를 하고 결과를 controller에 전달

3. Sequelize를 이용하여 DB를 세팅해준다.

   혹은 `Best Node JS Folder Structure`라는 검색어로 검색해봐도 좋다.

   ![Server Folder Structure Image](https://s3.ap-northeast-2.amazonaws.com/urclass-images/yx8-G1Ex_51qtgHSgHQqp-1660634365296.png)



## Route 설정하기

1. app.js 파일에 기본 서버를 세팅한다.
2. 설계한 API에 따라 routes 폴더에 필요한 route 파일을 생성한다.
   ```
   ㄴroutes
      ㄴindex.js
      ㄴmain.route.js
      ㄴpost.route.js
      ㄴuser.route.js
   ```
3. app.js에서 라우터 연결을 위한 설정을 한다.
   ```javascript
   // 예시
   const express = require("express")
   const app = express()
   const routes = require("./routes")  // route 폴더를 import한다.
   app.use("/", routes) // app.use()의 매개변수인 path는 originalUrl과 맞는 미들웨어가 동작할 수 있게 한다.
   ```
4. routes/index.js에는 필요한 라우터를 모두 명시해준다.
   ```javascript
   const express = require("express")
   const router = express.Router()

   const main = require("./main.route")
   const user = require("./user.route")
   const post = require("./post.route")

   router.use("/", main)
   router.use("/user", user)
   router.use("/post", post)

   module.exports = router
   ```
5. 각각의 route 파일에는 해당 엔드포인트에 따라 controller를 호출할 수 있도록 해야한다.
   ```javascript
   const express = require("express")
   const router = express.Router()
   const controller = require("../controllers/user.controller")

   router.post("/join", controller.user_join_post)
   router.post("/login", controller.user_login_post)
   router.post("/transfer", controller.user_transfer_post)

   module.exports = router
   ```



## ORM

> ORM은 Model을 기술하는 도구로, 프로그래밍 언어를 사용하여 데이터베이스를 이용할 수 있게 해준다.

여기서는 ORM을 이용하여, SQL문을 직접 작성하지 않고 엔티티를 객체로 표현하는 방법으로 Sequelize 및 Sequelize-CLI를 사용한다.

1. [Sequelize](https://sequelize.org/)를 설치한다.
2. [Sequelize-CLI](https://sequelize.org/docs/v6/other-topics/migrations/)를 설치한다.
3. Sequelize를 초기화한다.

   초기화하면 해당 디렉토리에 새로운 폴더 및 파일들이 생긴다. 생성된 파일 중 `config.json`에 사용할 데이터베이스 정보를 기입한다.

   ```bash
   sequelize init
   ```

4. Sequelize CLI를 통해서 모델을 생성할 수 있고 **마이그레이션**을 통해 실제 데이터베이스에 반영한다.

   > 마이그레이션은 스키마 변경에 따른 데이터 이주(migration)을 뜻한다. 이는 데이터를 선택, 준비, 추출 및 변환하여 한 컴퓨터 저장 시스템에서 다른 컴퓨터 저장 시스템으로 영구적으로 전송하는 프로세스를 뜻한다.

   아래 예시에서는 `User`라는 모델을 생성한다.

   ```bash
   sequelize model:generate --name User --attributes userName:string,password:string...<필요한 필드와 타입 정의>
   ```

5. 사용할 DB에 반영한다.

   ```bash
   sequelize db:migrate
   ```

6. MySQl에서 적용이 되었는지 확인한다.



## 서버 계정 생성

> Ganache 로컬 네트워크를 통해 서버 계정을 생성한다. Ganache에서는 기본적으로 10개의 계정과 각 계정마다 테스트용으로 100이더를 제공해주는데, 이를 활용해 서버 계정으로 일어나는 트랜잭션들의 가스비를 해결하게 된다.

1. web3를 설치한다.
2. 서버 파일 중 DB와 직접적으로 연동하는 controller나 service에서 web3로 가나슈 로컬 네트워크를 연결한다.
3. Ganache의 첫 번째 계정을 서버 계정으로 지정한다.
   - [web3.eth.getAccounts()](https://web3js.readthedocs.io/en/v1.5.2/web3-eth.html?highlight=web3.eth.getAccounts()#getaccounts)를 사용한다.
   
   ```javascript
   const accounts = await web3.eth.getAccounts()
   const serverAddress = accounts[0]
   ```

   account와 로컬 Ganache에 있는 accounts들이 동일한지 확인한다.

4. dotenv 라이브러리를 이용하여 privateKey는 따로 .env 파일에 저장한다.

   ```
   // .env 파일 -> 비공개
   SERVER_ADDRESS=
   SERVER_PRIVATE_KEY=
   ```

   💡 `.env` 파일 대신 `.env.example` 파일을 만들어 해당 변수들의 이름만 공개한다.

5. DB에 서버 계정 존재 여부에 따라 저장하는 로직을 수행한다.

   서버 계정은 DB 상에 한 번만 저장되어야 한다. 따라서, 이미 DB 상에 서버 계정이 등록되어 있을 경우, 해당 과정을 제외할 수 있도록 해야 한다.

6. 서버 계정으로 컨트랙트 배포 후 token_amount를 배포한 토큰의 개수만큼 업데이트한다.



## 사용자 지갑 생성

> 첫 번째 방법: `personal`

web3.eth.personal.newAccount(password)를 사용한다.

1. 회원가입 시 해당 nickname이 존재하는지 여부를 먼저 확인하고, 사용자 계정을 생성한다.
2. web3.eth.personal.newAccount(password)를 통해 사용자의 계정을 생성한다.
3. 사용자 계정 생성 후, 해당 계정을 DB에 업데이트한다.
4. 업데이트의 결과에 따라 응답을 돌려주는 로직을 구성한다.

> 두 번째 방법: `accounts`

web3.eth.accounts.create()를 사용한다.

1. 회원가입 시 해당 nickname이 존재하는지 여부를 먼저 확인하고, 사용자 계정을 생성한다.
2. web3.eth.accounts.create()를 통해 사용자의 계정을 생성한다.
3. 사용자 계정 생성 후, 해당 계정을 DB에 업데이트한다.
4. updateUser의 결과에 따라 응답을 돌려주는 로직을 구성한다.

> 두 API의 차인점은 [Stackoverflow 답변](https://stackoverflow.com/questions/50083957/what-is-the-difference-between-web3-eth-accounts-create-and-web3-eth-personal-ne)을 참고한다.



## ETH Faucet 받기

인센티브 커뮤니티에서는 사용자들이 보상으로 지급받은 토큰을 활용하기 위해 트랜잭션을 일으켜야 하며, 여기에 가스비가 소모된다.

1. 요청한 유저의 정보가 DB에 존재하는지 확인한다.

   - 만약 없다면, 에러를 띄운다.
   - 만약 있다면, 유저의 이름과 address를 사용한다.

2. Ganache의 두 번째 계정으로부터 테스트 이더를 받는 과정을 수행한다. `signTransaction` 함수를 사용해 사용자의 계정에 ETH를 전송한다. (첫 번째 계정은 서버 계정으로 사용한다.)

   - 트랜잭션에 서명하기 위해서는 web3.eth.accounts.signTransaction 메서드를 사용한다.
   - 서명할 트랜잭션을 전송하기 위해서는 web3.eth.sendSignedTransaction 메서드를 사용한다.
   - 잔액을 확인하기 위해서는 web3.eth.getBalance 메서드를 사용한다.

3. DB를 업데이트한다.



## ERC-20 토큰 전송

> 이 가이드는 eth.personal.newAccount로 만든 지갑을 기준으로 수도코드가 작성되어 있다.

### 보상 토큰 전송

사용자는 특정 행동을 하게 되면 서버 계정에서 발급한 토큰을 보상으로 받게 되는 구조로 되어 있다.

1. 배포한 컨트랙트의 address와 abi를 이용하여 컨트랙트 객체를 생성한다.

   ```javascript
   const abi = 배포한 컨트랙트의 abi
   const contractAddr = 배포한 컨트랙트의 주소
   const contract = new web3.eth.Contract(abi, contractAddr)
   ```

2. (서버 계정에서 보낼 토큰이 충분하다는 가정 하에) 서버 계정에서 발급한 토큰을 유저에게 전송한다.

   토큰 전송은 ERC-20 컨트랙트 중, `transfer` 함수와 `send` 함수를 이요한다.

   - 서버 계정에서 다른 사용자의 계정으로 토큰을 전송하는 것이므로 가스비를 내는 주체(from)가 서버가 되어야 한다.
   - 컨트랙트에 있는 함수를 실행하기 위해서는 트랜잭션에 `data` 값을 추가해야 할 수도 있다.

   ```javascript
   const result = await contract.methods.transfer(...).send(...);
   ```

3. result 값에 따라서 응답을 돌려준다.

4. 토큰이 잘 전송되었는지 컨트랙트의 balanceOf(address) 함수를 이용해 확인한 후 DB에 업데이트 한다.

   ```javascript
   // 예시
   contract.methods.balanceOf(address).call()
   ```

### 사용자 간 토큰 전송

(사용자 계정에서 보낼 토큰이 충분하다는 가정 하에) 사용자는 보상 받은 토큰을 다른 사용자에게 전송할 수 있다.

1. 배포한 컨트랙트의 address와 abi를 이용하여 컨트랙트 객체를 생성한다.

   ```javascript
   const abi = 배포한 컨트랙트의 abi
   const contractAddr = 배포한 컨트랙트의 주소
   const contract = new web3.eth.Contract(abi, contractAddr)
   ```

2. 트랜잭션에 서명하기 위해서는 계정이 unlock 상태여야 한다. 따라서, 트랜잭션을 일으키려는 유저의 Account Lock을 해제한다.

   > **unlockAccount**: 유저의 계정 권한을 해제한다. 서버에서 유저의 계정을 사용할 수 있게 된다.

   ```javascript
   web3.eth.personal.unlockAccount(address, password, unlockDuration [, callback])
   ```

3. 토큰 전송은 ERC-20 컨트랙트 중, `transfer` 함수와 `send` 함수를 이용한다.

4. result 값에 따라서 응답을 돌려준다.

5. 토큰이 잘 전송되었는지 balanceOf(address) 함수를 이용해 확인한 후, DB에 업데이트한다.

   ```javascript
   // 예시
   contract.methods.balanceOf(address).call()
   ```



## ERC-20으로 ERC-721 구매 구현

> 이 가이드는 eth.personal.newAccount로 만든 지갑을 사용한다.

1. 민팅하고자 하는 사용자의 nickname과 tokenURL을 받아온다.
2. nickname에 해당하는 사용자의 주소와 패스워드를 사용해 사용자 계정의 락을 해제한다.
3. 배포한 컨트랙트 주소와 ABI를 이용하여 contract 객체를 생성한다.

   ```javascript
   const contract = new web3.eth.Contract(erc20ABI, erc20Address)
   const contract721 = new web3.eth.Contract(erc721ABI, erc721Address)
   ```

4. 토큰을 전송 가능하도록 ERC-721 컨트랙트 계정에서 양도할 토큰의 양을 설정하는 함수를 실행한다.

   실제로 양도가 이루어지는 게 아니라 양도할 주소와 양을 정하는 과정이다.

5. 사용자가 ERC-721 컨트랙트 계정에서 양도 설정한 토큰의 양을 확인하여 함수를 실행하여 제대로 양도 설정했는지 확인할 수도 있다.
6. mintNFT 함수를 작성한다. 이 함수는 컨트랙트를 발행한 오너만 가능하다. 따라서, 서버 계정으로 트랜잭션을 생성하여, 사용자에게 해당 NFT가 민팅될 수 있도록 한다.



## Daemon 사용하여 트랜잭션 모니터링

![blockchain-practice-incentive-community-daemon.png](img/blockchain-practice-incentive-community-daemon.png)

`(출처: 코드스테이츠)`

> 이 과정은 블록체인 네트워크의 노드가 필요하며, 여기서는 Ganache를 사용했다.

백그라운드에서 주기적으로 실행되는 데몬을 생성한다. 이 데몬은 노드로부터 트랜잭션의 데이터를 조회하고, 저장하려는 특정 트랜잭션만 데이터베이스에 기록한다.

1. 블록 모니터링을 위해 필요한 모듈은 다음과 같다.

   - web3
   - Database (ex. MySQL / MongoDB)
      - (Option) ORM(ex. Sequelize, Sequelize-cli)
   - pm2
   - node-cron

2. daemon.js 파일을 서버 폴더에 생성하고 작성한다.

   ```javascript
   const cron = require("node-cron");
   const models = require("./models");
   // web3연결
   const Web3 = require("web3");

   // Ganache 블록체인 접근
   const Web3 = require("web3");
   const web3 = new Web3('HTTP://127.0.0.1:7545');

   // 노드의 최신블록넘버 조회
   const getLatestBlock = async () => {
      return await web3.eth.getBlockNumber();
   }

   // 블록정보
   const blockInfo = async (num) => await web3.eth.getBlock(num);
   // 트랜잭션정보
   const txInfo = async (tx) => await web3.eth.getTransaction(tx);

   // 블록이나 트랜잭션으로부터 필요한 정보를 DB에 저장합니다.

   // 매 초마다 실행 (실행주기를 설정할 수 있습니다.)
   const task = cron.schedule(
      "* * * * * *",
      async () => {
         // 주기적으로 실행하고자 하는 함수
         // 예시
         // getLatestBlock()
      },
      {
         scheduled: false,
      }
   );

   task.start();
   ```

3. package.json의 스크립트에 daemon을 추가한다.

   ```json
   // 파일에 맞게 설정한다
   "daemon": "pm2 start daemon.js --watch --no-daemon"
   ```

4. 실행 후 잘 작동하는지 트랜잭션을 날려본다.

   ```bash
   npm run daemon
   ```



***Copyright* © 2022 Song_Artish**