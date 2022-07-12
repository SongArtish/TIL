# Remix

---

[TOC]

---



## Remix

Remix는 솔리디티 개발을 위한 웹 기반 IDE이다. 자체적으로 솔리디티 개발을 위한 컴파일, 배포, 테스트, 디버깅 기능을 내장하고 있기 때문에 별도 프레임워크나 라이브러리를 설치하지 않아도 쉽게 솔리디티 코드 작성부터 테스트넷 배포까지 할 수 있다.



## 시작하기

1. remix.ethereum.org에 접속한다.
2. 가장 왼쪽에는 세로로 메뉴바가 있다.
   - File Explorers: 새로운 파일/폴더를 만들거나, github 연동, 로컬 컴퓨터에서 파일 업로드를 할 수 있다.
   - Solidity Compiler: 작성한 컨트랙트 코드를 컴파일한다.
   - Deploy & Run Transactions: 컴파일한 코드를 배포하고, 배포한 컨트랙트를 실행한다.
   - Plugin Manager: 컨트랙트 개발에 필요한 모듈을 설치 및 관리한다.



## 파일 생성 및 코드 작성

1. 새로운 파일을 만든다. contracts 폴더 아래 `simpleStorage.sol`을 생성한다. 생성한 파일에 다음의 코드를 작성하고 저장한다.

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



## 컨트랙트 코드 컴파일

1. `simpleStorage.sol` 파일을 열어둔 상태에서, 두 번째 탭인 `"SOLIDITY COMPILER" 탭을 들어간다. 그리고 다음과 같이 옵션을 선택되어 있는지 확인한다.

   - COMPILER: `0.8.7+commit.e28d00a7`

     솔리디티 코드를 어떤 버전으로 컴파일할 것인지 지정할 수 있다.

   - LANGUAGE: `Solidity`

     어떤 언어를 컴파일 하는지 지정한다.

   - EVM VERSION: `compiler default`

     EVM은 버전에 따라 각기 다른 특징을 가지고 있다. `byzantium`이 디폴트 값이다. (다양한 버전에 대해서는 [공식 문서](https://docs.soliditylang.org/en/v0.5.3/using-the-compiler.html#target-options) 참고)

2. "compile simpleStorage.sol" 버튼을 누르면 솔리디티 파일에 대한 컴파일이 시작된다.

3. 컴파일이 완료되면 <u>아래</u> "CONTRACT" 옵션에 우리가 만든 컨트랙트가 `컨트랙트명(파일명)` 형식으로 출력된다.

4. "Compilation Details" 버튼을 누르면 컨트랙트에 대한 메타데이터 및 ABI 데이터, 바이트코드를 확인할 수 있다.

5. "CONTRACT" 옵션 아래에 있는 ABI와 Bytecode 버튼을 눌러 바로 복사하여 확인할 수도 있다.

   ```solidity
   // ABI
   [
   	{
   		"inputs": [],
   		"name": "get",
   		"outputs": [
   			{
   				"internalType": "uint256",
   				"name": "",
   				"type": "uint256"
   			}
   		],
   		"stateMutability": "view",
   		"type": "function"
   	},
   	{
   		"inputs": [
   			{
   				"internalType": "uint256",
   				"name": "x",
   				"type": "uint256"
   			}
   		],
   		"name": "set",
   		"outputs": [],
   		"stateMutability": "nonpayable",
   		"type": "function"
   	}
   ]
   ```

   ```solidity
   // Bytecode
   {
   	"functionDebugData": {},
   	"generatedSources": [],
   	"linkReferences": {},
   	"object": "608060405234801561001057600080fd5b50610150806100206000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c806360fe47b11461003b5780636d4ce63c14610057575b600080fd5b6100556004803603810190610050919061009d565b610075565b005b61005f61007f565b60405161006c91906100d9565b60405180910390f35b8060008190555050565b60008054905090565b60008135905061009781610103565b92915050565b6000602082840312156100b3576100b26100fe565b5b60006100c184828501610088565b91505092915050565b6100d3816100f4565b82525050565b60006020820190506100ee60008301846100ca565b92915050565b6000819050919050565b600080fd5b61010c816100f4565b811461011757600080fd5b5056fea26469706673582212208fa8ae7ffbb4baa0ee9c21e033d63c9fc2a2e2a709e1a3576078c20a7d06551164736f6c63430008070033",
   	"opcodes": "PUSH1 0x80 PUSH1 0x40 MSTORE CALLVALUE DUP1 ISZERO PUSH2 0x10 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH2 0x150 DUP1 PUSH2 0x20 PUSH1 0x0 CODECOPY PUSH1 0x0 RETURN INVALID PUSH1 0x80 PUSH1 0x40 MSTORE CALLVALUE DUP1 ISZERO PUSH2 0x10 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH1 0x4 CALLDATASIZE LT PUSH2 0x36 JUMPI PUSH1 0x0 CALLDATALOAD PUSH1 0xE0 SHR DUP1 PUSH4 0x60FE47B1 EQ PUSH2 0x3B JUMPI DUP1 PUSH4 0x6D4CE63C EQ PUSH2 0x57 JUMPI JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH2 0x55 PUSH1 0x4 DUP1 CALLDATASIZE SUB DUP2 ADD SWAP1 PUSH2 0x50 SWAP2 SWAP1 PUSH2 0x9D JUMP JUMPDEST PUSH2 0x75 JUMP JUMPDEST STOP JUMPDEST PUSH2 0x5F PUSH2 0x7F JUMP JUMPDEST PUSH1 0x40 MLOAD PUSH2 0x6C SWAP2 SWAP1 PUSH2 0xD9 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST DUP1 PUSH1 0x0 DUP2 SWAP1 SSTORE POP POP JUMP JUMPDEST PUSH1 0x0 DUP1 SLOAD SWAP1 POP SWAP1 JUMP JUMPDEST PUSH1 0x0 DUP2 CALLDATALOAD SWAP1 POP PUSH2 0x97 DUP2 PUSH2 0x103 JUMP JUMPDEST SWAP3 SWAP2 POP POP JUMP JUMPDEST PUSH1 0x0 PUSH1 0x20 DUP3 DUP5 SUB SLT ISZERO PUSH2 0xB3 JUMPI PUSH2 0xB2 PUSH2 0xFE JUMP JUMPDEST JUMPDEST PUSH1 0x0 PUSH2 0xC1 DUP5 DUP3 DUP6 ADD PUSH2 0x88 JUMP JUMPDEST SWAP2 POP POP SWAP3 SWAP2 POP POP JUMP JUMPDEST PUSH2 0xD3 DUP2 PUSH2 0xF4 JUMP JUMPDEST DUP3 MSTORE POP POP JUMP JUMPDEST PUSH1 0x0 PUSH1 0x20 DUP3 ADD SWAP1 POP PUSH2 0xEE PUSH1 0x0 DUP4 ADD DUP5 PUSH2 0xCA JUMP JUMPDEST SWAP3 SWAP2 POP POP JUMP JUMPDEST PUSH1 0x0 DUP2 SWAP1 POP SWAP2 SWAP1 POP JUMP JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH2 0x10C DUP2 PUSH2 0xF4 JUMP JUMPDEST DUP2 EQ PUSH2 0x117 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP JUMP INVALID LOG2 PUSH5 0x6970667358 0x22 SLT KECCAK256 DUP16 0xA8 0xAE PUSH32 0xFBB4BAA0EE9C21E033D63C9FC2A2E2A709E1A3576078C20A7D06551164736F6C PUSH4 0x43000807 STOP CALLER ",
   	"sourceMap": "73:197:0:-:0;;;;;;;;;;;;;;;;;;;"
   }
   ```

   

## 컨트랙트 코드 배포

1. `simpleStorage.sol` 파일을 열어둔 상태에서, 세 번째 탭인 "DEPLOY & RUN TRANSACTIONS" 탭에 들어간다. 다음과 같이 옵션이 잘 선택되었는지 확인한다.

   - ENVIRONMENT: `JavaScript VM (London)`

     컨트랙트 코드를 배포할 네트워크를 의미한다. Injected Web3를 선택하여 지갑관 연동하거나, Web3 Provider를 선택하여 Geth를 통해 접속한 네트워크에 연결할 수 있다. (여기서는 Remix가 제공하는 가상 네트워크를 사용할 예정이기 때문에 JavaScript VM (London)을 선택한다.)

   - ACCOUNT: `0x5B3...eddC4 (100 ehter)`

     컨트랙트 코드를 배포할 계정이다. JavaScript VM에서 사용할 수 있는 가상 계정을 선택한다. (계정 정보는 조금씩 다를 수 있다.)

   - GAS LIMIT: `3000000`

     컨트랙트 실행 시 사용할 가스의 한도

   - VALUE: `0` `wei`

     전송할 이더의 양

   - CONTRACT: `SimpleStorage - contracts/simpeStorage.sol`

     트랜잭션으로 올릴 컨트랙트를 선택한다.

2. 주황식 "Deploy" 버튼을 누르면 배포가 시작된다.

3. 배포가 성공적으로 완료되면 터미널 창에 트랜잭션에 대한 정보가 출력된다.

4. 메뉴창 하단의 "DEPLOYED CONTRACTS"에서는 배포한 컨트랙트의 함수가 버튼으로 표시된다.

   - `set` 함수는 인자를 받아 컨트랙트 내 state를 변경하는 함수이다. (상태변경 함수는 주황색으로 표시됨)
   - `get` 함수는 컨트랙트 내의 state를 반환하는 함수이다.

5. `set` 함수에 '3'이라는 값을 넣고 주황색 `set` 버튼을 눌러 컨트랙트 내 함수를 실행하는 트랜잭션을 보내본다.

   `set` 함수를 실행한 트랜잭션의 정보가 터미널 창에 출력되는 것을 확인할 수 있다. 트랜잭션 정보에 'decoded input'을 확인하면 다음과 같이, 입력한 값이 16진수 형태로 나타난다.

   ```
   decoded input: {
   	"uint256 x": {
   		"_hex": "0x03",
   		"_isBigNumber": true
   	}
   }
   ```

6. `get` 버튼을 눌러 컨트랙트의 `get` 함수를 실행하는 트랜잭션을 보내본다.

   결과가 터미널 창에 뜨는 것을 확인할 수 있다. 'decoded outputs'를 확인하면, 'set' 함수에서 저장한 state가 반환됨을 확인할 수 있다.

   ```
   decoded outputs: {
   	"0": "uint256: 3"
   }
   ```



## Remix Plugin 사용하기

Remix에서 PLUGIN MANAGER 탭을 선택하면 다양한 플러그인을 확인할 수 있다. 원하는 플러그인이 있을 경우, `Search`에서 검색하여 확인할 수 있다.

`Activate` 버튼을 누르면 해당 플러그인이 설치된다. 자세한 내용은 [문서](https://remix-ide.readthedocs.io/en/latest/plugin_manager.html)를 참고한다.



## Remixd: 로컬 컴퓨터에 Remix 코드 저장하기

> **Remixd란?**
>
> Remix IDE는 웹 브라우저에서 동작하기 때문에, 브라우저 캐시가 지워지는 경우 작성된 파일도 함께 삭제될 수 있다. Remixd는 로컬 컴퓨터에 저장되어 있는 소스 코드 파일 또는 폴더를 Remix IDE와 로컬호스트에서 웹소켓 통신으로 연결한다. Remix IDX에서 연결된 파일 또는 폴더가 변경될 경우, 로컬 컴퓨터에도 자동으로 저장된다. 따라서 Remixd를 사용해 편리하게 코드를 백업할 수 있다.
>
> - Remixd Github: https://github.com/ethereum/remix-project/tree/master/libs/remixd

npm을 사용해 Remixd를 설치하고 사용해본다.

1. VS Code를 열고, 새로운 폴더 `remixd_practice`를 만든다.

2. 터미널에서 다음 명령어를 실행하여 `package.json` 파일을 생성한다.

   ```bash
   npm init
   ```

   옵션은 임의로 설정하면 된다.

3. 터미널에 다음의 명령어를 입력하여 remixd를 설치한다.

   ```bash
   npm install -g @remix-project/remixd
   ```

4. 폴더 내에 `remixd_test.sol` 파일을 만들고, 다음의 코드를 작성하여 저장한다.

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

5. 터미널에 다음과 같은 명령어를 입력한다.

   이 명령어는 해당 디렉토리를 Remix IDE와 웹소켓으로 연결한다.

   ```bash
   remixd -s <remixd_practice 폴더의 절대경로> --remix-ide https:/remix.ethereum.org
   ```

   - 명령어 예시

   ```bash
   remixd -s C:\Users\bulge\Documents\code_states\Blockchain\remixd_practice --remix-ide https://remix.ethereum.org
   ```

   - :warning: 위의 "절대 경로" 명령어가 작동하지 않을 경우 다음의 명령어로 실행해본다.

   ```bash
   remixd -s . --remix-ide https://remix.ethereum.org
   ```

   정상적으로 연결되면 `remixd is listening on ~`, `slither is listening on~`과 같은 메시지가 표시된다.

6. remix.ethereum.org에 접속한다.

7. Workspaces에서 `-connect to [localhost] -`를 선택한다.

8. "Connect to localhost" 창이 뜨면 connect 버튼을 누른다.

9. File Explorers 탭에서 VS Code의 디렉토리와 동일하게 구성된 것을 확인할 수 있다.

10. remix IDE에서 `remixd_test.sol` 폴더에 `//Hello, wolrd!`라는 주석을 추가하고 저장해본다.

    ```solidity
    // SPDX-License-Identifier: GPL-3.0
    pragma solidity >=0.4.16 <0.9.0;
    
    contract SimpleStorage {
    	...
    	// Hello, World!
    }
    ```

11. VS Code의 `remixd_test.sol`에도 동일한 주석이 자동으로 추가된 것을 확인할 수 있다.

12. 반대로, VS Code에서도 코드를 수정해보고, Remix IDE에 어떻게 적용되는지 확인한다.

    Remix IDE에서는 팝업창이 발생하면서, 해당 수정 사항을 받을 것인지 아니면 현재 사항을 유지할 것인지 선택할 수 있다.



## MetaMask 연결하기

Remix에서 MetaMask를 연결하여, 웹 브라우저로 스마트 컨트랙트를 빌드하고 배포할 수 있다.

- **Remix에 MetaMask를 연결하기 위해, MetaMask 확장 프로그램에 로그인된 상태여야 한다.**
- 이전에 진행한 `simpleStorage` 컨트랙트에서 진행한다.

1. Remix에 접속한 다음, 왼쪽 탭에서 `Deploy & run transactions` 탭을 선택한다.
2. 왼쪽 상단의 `ENVIRONMENT`를 선택하고, `Injcted Web3`를 선택한다.
3. 팝업창으로 <u>자동</u> 실행된 MetaMask에서 연결하려는 지갑을 선택하고 `다음` 버튼을 누른다.
   - MetaMask 팝업창 표시되지 않는 경우, 페이지를 새로고침 후 다시 시도해본다.
4. 이어지는 화면에서 `연결` 버튼을 눌러 MetaMask와 Remix를 연결한다.
5. MetaMask의 네트워크가 `Ropsten 테스트 네트워크`가 맞는지 다시 한 번 확인한다.
6. Remix 화면에 나타난 `Account`의 지갑 주소가 MetaMask의 지갑 주소와 같다면, 정상적으로 연결이 된 것이다.



***Copyright* © 2022 Song_Artish**