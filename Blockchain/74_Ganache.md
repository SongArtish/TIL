# Ganache

---

[TOC]

---



## Background
이더리움 노드는 Geth나 Parity를 사용하여 실제 이더리움 메인/테스트 네트워크에 접속하여 블록을 모두 동기화시켜야 한다. 하지만 블록을 동기화시키는데만 해도 2-3일 정도 소요되며, 트랜잭션을 보내도 블록을 채굴하기까지 기다려야 하는 등, 스마트 컨트랙트를 개발할 때 불편한 점이 많다.
그래서 스마트 컨트랙트를 개발할 때는 가나슈(Ganache)와 같은 **가상 혹은 프라이빗 네트워크** 상에서 스마트 컨트랙트를 구동해보고, 테스트넷을 거쳐 메인넷에 올린다.



## 개발 및 배포 과정
개발 과정은 다음과 같다.
```
TestRPC -> TestNet -> MainNet
```
- TestRPC: 가나슈를 사용해 로컬 환경에서 개발 진행
- TestNet: 개발 완료 후 MainNet과 동일한 환경에서 테스트
- MainNet: 실제 서비스에 사용할 수 있도록 배포



## Ganache 설치 및 소개
가나슈(Ganache)는 가상의 이더리움 네트워크를 생성해서 스마트 컨트랙트를 실행할 수 있도록 해주는 프로그램이다. 가나슈 등을 이용해 만든 가상 환경을 TestRPC라고 한다.
1. 가나슈 홈페이지에 접속해서 다운로드를 받고 설치한다.
> 가나슈 홈페이지: https://trufflesuite.com/ganache/
2. Ganache를 Quickstart로 실행하면 한다.
3. 화면이 표시된다.
   - 현재 가상의 이더리움 네트워크가 로컬에 운영되고 있다.
   - 해당 네트워크에 접속하려면 http://127.0.0.1:7545로 접속할 수 있다.
   - 10개의 가상 계정에는 각각 100 이더의 잔액이 충전되어 있다.
Ganache에서 mining이 활성화되어있기 때문에 바로 contract를 배포하거나 transaction을 실행할 수 있는 환경이 갖춰진다.
어플리케이션 상단에는 6개의 탭이 존재한다.
- Accounts: account들의 주소, 잔고, 트랜잭션 수
- Blocks: block 번호, 생성 시점, 사용된 가스, 포함된 트랜잭션
- Transactions: 전체 트랜잭션
- Contracts: 트러플(Truffle) 프로젝트에 포함된 스마트 컨트랙트
- Events: 이벤트 리스트
- Logs: EthereumJS VM의 로그



## Ganache-cli
- ganache-cli는 electron으로 wrapping하는 형태로 제작되어 있기 때문에, GUI가 필요없다면 ganache-cli를 사용할 수도 있다. 
- Truffle을 사용해 개발/테스트 환경을 구성할 경우, truffle develop 명령으로 ganache-cli 사용이 가능하다.
- Remix를 사용해 개발/테스트 환경을 구성할 경우, MetaMask에서 로컬 네트워크로 연결하여 사용이 가능ㅎ다.

### npm을 이용하여 Ganache-cli 설치하기
```bash
npm install -g ganache-cli
```
설치가 완료되면, 다음의 명령어로 확인한다.
```bash
ganache-cli version

...
Listening on 127.0.0.1:8545
```



## Ganache와 Remix 연동
지금까지 MetaMask와 Remix를 연동하던 방법은, 개발 및 배포과정에서 TestNet에 해당하는 과정이다. 이번에는 Remix를 이용해 TestRPC와 연동하여 사용하는 방법을 다루어본다.

### MetaMask와 Ganache 연동
1. MataMask에서 네트워크를 선택하는 항목 중, `맞춤형 RPC` 항목을 선택한다. (또는 제일 하단에 `네트워크 추가` 버튼을 누른다.)
2. 맞춤형 RPC 화면에서 네트워크 이름, 새 RPC URL, 체인 ID를 각각 입력해준다.
   - 네트워크 이름: Ganache Network
   - 새 RPC URL: http://127.0.0.1:7545
   - 체인 ID: 1337
3. 새 네트워크에 접속하여 자신의 계정이 잘 작동하는지 확인한다.
   Ganache 계정을 MetaMask로 가져와본다. Ganache 계정의 Private Key를 가져와 MetaMask에 계정을 import 한다.
4. Ganache에서 Address 옆 열쇠 버튼을 눌러 Private Key를 복사한다.
5. MetaMask에서 계정 아이콘을 클릭하여 계정 가져오기를 선택한다.
6. 복사해온 비공개 키를 입력한다.
7. 계정을 가져오는데 성공한 것을 확인할 수 있다.

### Ganache Network에 스마트 컨트랙트 배포
1. MetaMask 계정을 이용해 Remix 계정과 연동한다. ERC-20 토큰 코드를 준비한다.
2. Ganache 네트워크에 ERC-20 토큰을 배포한다.
   - `DEPLOY > NAME`: SimpleTestToken
   - `DEPLOY > SYMBOL`: STT
3. Deploy 후 Ganache를 확인해본다.
   - Current Block에 하나의 블록이 생성되어 있다.
    Deploy와 동시에 transaction을 Ganache 가상 네트워크에 전송했고, 채굴이 일어나서 블록이 1개 생성된 것이다.
   - Ropsten TestNet에서 사용했던 것처럼 네트워크에서 함수가 실행가능한 모습을 볼 수 있다. (Remix > DEPLOY & RUN TRANSACTIONS > Deployed Contracts)
   - Transaction을 눌러서 들어가면 방금 Deploy를 하면서 발생시킨 transaction이 들어있다.

### Ganache Network에서 스마트 컨트랙트 사용
1. MetaMask에서 Ganache에 배포한 토큰 주소를 이용해 토큰을 추가한다.
2. 추가된 토큰을 다른 계정을 전송해본다.
   Ganache 네트워크는 로컬 네트워크 환경이므로, MetaMask에서 새로운 계정을 만들어 전송해본다.
3. 전송이 완료되면, Ganache에서도 블록이 하나 더 채굴되어 트랜잭션이 생긴 것을 확인할 수 있다.
4. 토큰의 개수를 Remix에서 `balanceOf` 함수로 확인해본다.
   > 상태 변수가 변하지 않는 "읽기" 명령은 채굴이 일어나지 않으며, 상태 변수가 변하는 "쓰기" 명령을 수행할 때에만 채굴이 일어난다.
   
   따라서, 읽기 전용의 `balanceOf` 함수에서는 채굴이 일어나지 않는다.


***Copyright* © 2022 Song_Artish**