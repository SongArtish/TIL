# ABI

---

[TOC]

---



## ABI

ABI(Application Binary Interface)는 **런타임 시 바이너리 코드와 상호작용하기 위한 인터페이스**로,  바이너리 형태로 되어있는 스마트 컨트랙트가 어떤 인터페이스를 가지고 있는지 알려주는 역할을 한다.



## ABI를 사용해 Contract ABI Call하기

다음의 코드를 작성한다.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity 0.8.7;

contract helloWorld {
    function renderHelloWorld () public pure returns (string memory greeting) {
        greeting = "Hello World!";
    }
}
```

위 코드를 remix에서 컴파일하고, 완료되면 "Compilation Details" 버튼을 눌러 컨트랙트 세부 정보를 확인해본다. Compilation Details 화면에서는 컴파일된 컨트랙트에 대한 세부적인 정보를 확인할 수 있다.

이 중 ABI 토클을 열어 확인해본다. ABI를 통해 컨트랙트 내 함수를 어떻게 사용하는지 확인할 수 있다. Web3.js에서는 `web3.eth.Contract()`에 ABI를 인자로 넣어 컨트랙트를 구현한다.

WEB3DEPLOY 토글에서는 컨트랙트를 배포하고 트랜잭션을 보내는 코드를 제공한다. ABI와 Web3.js를 이용해 컨트랙트를 바로 배포할 수 있는 자바스크립트 코드이다.

```javascript
var helloworldContract = new web3.eth.Contract([{"inputs":[],"name":"renderHelloWorld","outputs":[{"internalType":"string","name":"greeting","type":"string"}],"stateMutability":"pure","type":"function"}]);
var helloworld = helloworldContract.deploy({
     data: '0x608060405234801561001057600080fd5b5061017c806100206000396000f3fe608060405234801561001057600080fd5b506004361061002b5760003560e01c8063942ae0a714610030575b600080fd5b61003861004e565b60405161004591906100c4565b60405180910390f35b60606040518060400160405280600b81526020017f48656c6c6f20576f726c64000000000000000000000000000000000000000000815250905090565b6000610096826100e6565b6100a081856100f1565b93506100b0818560208601610102565b6100b981610135565b840191505092915050565b600060208201905081810360008301526100de818461008b565b905092915050565b600081519050919050565b600082825260208201905092915050565b60005b83811015610120578082015181840152602081019050610105565b8381111561012f576000848401525b50505050565b6000601f19601f830116905091905056fea264697066735822122096669d076d49e0f6c42cb12336c7554897eed6ff4361476391c02f31ec95b6ad64736f6c63430008070033', 
     arguments: [
     ]
}).send({
     from: web3.eth.accounts[0], 
     gas: '4700000'
   }, function (e, contract){
    console.log(e, contract);
    if (typeof contract.address !== 'undefined') {
         console.log('Contract mined! address: ' + contract.address + ' transactionHash: ' + contract.transactionHash);
    }
 })
```

Compilation Details > ABI 메뉴 옆 복사 버튼, 또는 Compilation Details 아래에 있는 ABI 복사 버튼으로 ABI를 복사할 수 있다. ABI는 다음과 같은 형태이다.

```
[
	{
		"inputs": [],
		"name": "renderHelloWorld",
		"outputs": [
			{
				"internalType": "string",
				"name": "greeting",
				"type": "string"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	}
]
```

이를 Ganache에 배포 후 다음과 같은 코드를 작성한다.

```javascript
const express = require('express')
const app = express()
const port = 8080
const Contract = require('web3-eth-contract')

async function helloWorld() {
    try {
        const abi = [
            {
                "inputs": [],
                "name": "renderHelloWorld",
                "outputs": [
                    {
                        "internalType": "string",
                        "name": "greeting",
                        "type": "string"
                    }
                ],
                "stateMutability": "pure",
                "type": "function"
            }
        ]
        const address = '0x8dc3cDBd43a06772CeB2637e762D6Cf369b44b19'    // contract address
        Contract.setProvider('http://127.0.0.1:7545')
        const contract = new Contract(abi, address)
        const result = await contract.methods.renderHelloWorld().call()
        console.log(result)
        return result
    }
    catch(error) {
        console.log(error)
        return error
    }
}

app.get('/helloworld', (req, res) => {
    helloWorld()
        .then((result) => {
            res.send(result)
        })
})

app.listen(port, () => {
    console.log('Listening')
})
```

브라우저에서 http://localhost:8080/helloworld를 호출하면, 화면에 `Hello Wolrd!`가 표시된다.

> `web3.eth.Contract()`
> - params: ABI, 계정 주소
> - return: 컨트랙트 객체

이 컨트랙트 객체는 자바스크립트 객체처럼 사용할 수 있으며, 컨트랙트 내의 상태변수와 함수를 속성과 메서드처럼 사용할 수 있다.

```javascript
const contract = new Contract(abi, address)
```

이렇게 만들어진 컨트랙트 객체에 있는 함수를 사용하기 위해서는 `contract.methods.함수명().call()`과 같이 사용할 수 있다.

- `contract.methods.함수명()`: 컨트랙트에 있는 함수를 실행하는 트랜잭션 객체를 생성한다.
- `contract.methods.함수명().call()`: 트랜잭션을 실행한 결과를 Promise 형태로 반환한다.

아래 코드는 컨트랙트의 `renderHelloWorld()` 함수를 실행하는 트랜잭션 객체를 call하여 함수를 실행한 결과를 `result` 변수에 담아 콘솔창에 출력한다. Contract ABI를 이용해 함수를 호출했기 때문에 Contract ABI Call이라고 한다.

```javascript
const result = await contract.methods.renderHelloWorld().call();
console.log(result);
```

Remix에서도 Web3.js를 사용하여 GUI로 ABI Call을 할 수 있도록 지원한다.



## 바이트코드를 사용해 배포해보기

바이트코드를 받아와 노드를 통해 직접 배포하는 트랜잭션을 보내본다. Remix를 사용하며, 이 외에도 CLI를 통해 solc로 컴파일하여 사용해도 된다.

아래는 ERC-20 토큰 코드이다.

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.10;

interface ERC20Interface {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function transferFrom(address spender, address recipient, uint256 amount) external returns (bool);
    
    event Transfer(address indexed from, address indexed to, uint256 amount);
    event Transfer(address indexed spender, address indexed from, address indexed to, uint256 amount);
    event Approval(address indexed owner, address indexed spender, uint256 oldAmount, uint256 amount);
}

contract SimpleToken is ERC20Interface {
    mapping (address => uint256) private _balances;
    mapping (address => mapping (address => uint256)) public _allowances;

    uint256 public _totalSupply;
    string public _name;
    string public _symbol;
    uint8 public _decimals;
    
    constructor(string memory getName, string memory getSymbol) {
        _name = getName;
        _symbol = getSymbol;
        _decimals = 18;
        _totalSupply = 100000000e18;
        _balances[msg.sender] = _totalSupply;
    }
    
    function name() public view returns (string memory) {
        return _name;
    }
    
    function symbol() public view returns (string memory) {
        return _symbol;
    }
    
    function decimals() public view returns (uint8) {
        return _decimals;
    }
    
    function totalSupply() external view virtual override returns (uint256) {
        return _totalSupply;
    }
    
    function balanceOf(address account) external view virtual override returns (uint256) {
        return _balances[account];
    }
    
    function transfer(address recipient, uint amount) public virtual override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }
    
    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }
    
    function approve(address spender, uint amount) external virtual override returns (bool) {
        uint256 currentAllownace = _allowances[msg.sender][spender];
        require(currentAllownace >= amount, "ERC20: Transfer amount exceeds allowance");
        _approve(msg.sender, spender, currentAllownace, amount);
        return true;
    }
    
    function transferFrom(address sender, address recipient, uint256 amount) external virtual override returns (bool) {
        _transfer(sender, recipient, amount);
        emit Transfer(msg.sender, sender, recipient, amount);
        uint256 currentAllowance = _allowances[sender][msg.sender];
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, msg.sender, currentAllowance, currentAllowance - amount);
        return true;
    }
    
    function _transfer(address sender, address recipient, uint256 amount) internal virtual {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        uint256 senderBalance = _balances[sender];
        require(senderBalance >= amount, "ERC20: transfer amount exceeds balance");
        _balances[sender] = senderBalance - amount;
        _balances[recipient] += amount;
    }
    
    function _approve(address owner, address spender, uint256 currentAmount, uint256 amount) internal virtual {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");
        require(currentAmount == _allowances[owner][spender], "ERC20: invalid currentAmount");
        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, currentAmount, amount);
    }
}
```

컴파일러에서 컴파일을 진행하고, Compilation Details를 확인한다. Bytecode에서는 objects에 해당하는 결과만, ABI 모두, 각각 복사해 변수로 할당한다.

```javascript
const express =require('express');
const app = express();
const port = 8080;
const Contract = require('web3-eth-contract');

async function deploySimpleToken() {
    try {
        const abi = [
            {
                "inputs": [
                    {
                        "internalType": "string",
                        "name": "getName",
                        "type": "string"
                    },
                    {
                        "internalType": "string",
                        "name": "getSymbol",
                        "type": "string"
                    }
                ],
                "stateMutability": "nonpayable",
                "type": "constructor"
            },
            ...
        ] // abi 붙여넣기
        const byteCode = "0000"; // 바이트코드 붙여넣기
        Contract.setProvider('http://127.0.0.1:7545');
        const contract = new Contract(abi);
        const receipt = await contract.deploy({data:"0x" + byteCode, arguments: ["ErcSimpleToken", "EST"]}).send({from:"0x156650ee0E930d0749a6122f9FB290554b0ED5e7", gas: 2000000, gasPrice:'1000000000000'});
        // from에 account address를 입력
        console.log(receipt);
        return receipt;
    } catch(e) {
        console.log(e);
        return e;
    }
}

app.get('/deploy', (req, res) => {
    deploySimpleToken().then((result) => {
        res.send(result);
    })
})

app.listen(port, () => {
	console.log('Listening...');
});
```

서버 실행 후 http://localhost:8080/deploy로 접속하여 실행해본다. Deploy가 성공하면 Ganache 블록에 올라간 주소를 찾을 수 있다.

해당 주소(contract address)를 Remix > DEPLOY & RUN TRANSACTIONS > At Address에 입력하고 불러올 수 있다.
 

***Copyright* © 2022 Song_Artish**