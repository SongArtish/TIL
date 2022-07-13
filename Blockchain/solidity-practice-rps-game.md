# <실습> Rock Paper Scissors Game

---

[TOC]

---



## 들어가며

본격적으로 solidity 언어로 실습을 진행하기 전, Remix에서 간단하게 "Hello World"를 반환하는 컨트랙트르 작성해본다.

1. [remix.ethereum.org](remix.ethereum.org)에 접속한다.

2. helloWorld.sol 파일을 생성한다.

3. SPDX 라이센스와 pragma를 설정한다.

   ```solidity
   // SPDX-License-Identifier: MIT
   pragma solidity ^0.8.7;
   ```

4. `contract` 키워드를 사용해 `helloWorld` 컨트랙트를 만든다.

   ```solidity
   // SPDX-License-Identifier: MIT
   pragma solidity ^0.8.7;
   
   // 여기
   contract helloWorld { }
   ```

5. `renderHelloWorld` 함수를 만든다. 접근 수준은 public으로 설정한다.

   ```solidity
   // SPDX-License-Identifier: MIT
   pragma solidity ^0.8.7;
   
   contract helloWorld {
   	// 여기
   	function renderHelloWorld () public returns () { }
   }
   ```

   `renderHelloWorld` 함수는 "Hello World!"라는 문자열을 반환하는 함수이다. 따라서 returns의 형태를 string으로 설정한다. 스토리지에 영구적으로 저장하지 않기 때문에 데이터 저장 위치는 memory로 지정한다.

   ```solidity
   // SPDX-License-Identifier: MIT
   pragma solidity ^0.8.7;
   
   contract helloWorld {
   	// 여기
   	function renderHelloWorld () public returns (string memory) { }
   }
   ```

6. 함수 안에 "Hello Wolrd!"를 리턴하는 구문을 작성한다.

   ```solidity
   // SPDX-License-Identifier: MIT
   pragma solidity ^0.8.7;
   
   contract helloWorld {
   	function renderHelloWorld () public returns (string memory) {
   		// 여기
   		return "Hello World!";
   	}
   }
   ```

7. 리턴문을 다음과 같이 작성할 수도 있다.

   ```solidity
   // SPDX-License-Identifier: MIT
   pragma solidity ^0.8.7;
   
   contract helloWorld {
   	function renderHelloWorld () public returns (string memory greeting) {
   		// 여기
   		greeting = "Hello World!";
   	}
   }
   ```

8. `renderHelloWorld` 함수는 스토리지를 읽거나 쓰지 않기 때문에 `pure` 키워드를 작성하는 것이 좋다.

   ```solidity
   // SPDX-License-Identifier: MIT
   pragma solidity ^0.8.7;
   
   contract helloWorld {
   	// 여기
   	function renderHelloWorld () public pure returns (string memory greeting) {
   		greeting = "Hello World!";
   	}
   }
   ```



## Overview

Solidity를 사용해 간단한 **가위바위보** 게임 컨트랙트를 작성해본다. 두 명의 플레이어가 가위바위보 게임을 진행하고, 이긴 경우 두 참여자의 베팅 금액을 모두 가져간다.

가위바이보 컨트랙트는 다음의 함수를 가지고 있다.

- `createRoom`: 가위바위보 게임을 하기 위한 방을 만든다.
  - 방장(originator)이 호출
  - args: 자신이 낼 가위/바위/보 값, 베팅 금액
  - `createRoom`은 새로운 방을 만들고, 방의 번호를 리턴한다.
- `joinRoom`: 만들어진 방에 참가한다.
  - 참가자(taker)가 호출
  - args: 참여할 방 번호, 자신이 낼 가위/바위/보 값, 베팅 금액
  - `joinRoom`은 참가자를 방에 참여시킨다.
  - `joinRoom`은 방장과 참가자의 가위/바위/보 값을 확인하고 해당 방의 승자를 설정한다.
- `checkTotalPay`: 만들어진 방들의 총 베팅금액을 확인한다.
  - 방장(originator) 혹은 참가자(taker)가 호출
  - args: 방 번호
  - 해당 방 배팅금액을 확인한다.
- `payout`: 게임을 마치고, 결과에 따라 베팅 금액을 송금한다.
  - 방장 또는 참가자가 호출
  - args: 게임을 끝낼 방 번호
  - 게임 결과에 따라 베팅 금액을 송금



## 시작하기

먼저 컨트랙트의 틀을 작성한다.

- SPDX 라이센스는 MIT로 설정한다.
- pragma 버전은 `0.8.7`을 사용한다. (compiler 버전에 따라 조정한다.)
- 컨트랙트의 이름은 `RPS`이다.
- 해당 컨트랙트가 송금을 진행하기 위해 생성자 함수에 `payable` 키워드를 사용해 송금이 가능하다는 것을 명시한다.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract RPS {
	constructor () payable {}
}
```



## 1. 사용자와 게임 구조체 생성

### 플레이어 구조체 만들기

게임에서는 각 플레이어의 주소가 베팅 금액을 알고 있어야 한다. 따라서 플레이어 구조체를 다음과 같이 작성한다.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract RPS {
	constructor () payable {}
	
	struct Player {
		address payable addr;	// 주소
		uint256 playerBetAmount;	// 베팅 금액
	}
}
```

모든 플레이어는 자신이 낸 가위/바위/보 값이 있다. 플레이어가 낸 값은 "아직 내지 않은 상태", "가위", "바위", "보" 만 있으며, 이것을 `enum`으로 저장하고, 이외의 값을 내는 경우 예외가 발생하도록 한다.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract RPS {
	constructor () payable {}
	
	// 가위/바위/보 값에 대한 enum
	enum Hand {
		rock, paper, scissors
	}
	
	struct Player {
		address payable addr;
		uint256 playerBetAmount;
		Hand hand;	// 플레이어가 낸 가위/바위/보 값
	}
}
```

또한, 플레이어는 게임 결과에 따른 상태가 있다. 상태는 "대기중", "이김", "비김", "짐" 총 4가지가 있으며, 이외의 상태가 있을 수 없기 때문에 `enum`으로 지정한다.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract RPS {
	constructor () payable {}
	
	enum Hand {
		rock, paper, scissors
	}
	
	// 플레이어의 상태
	enum PlayerStatus {
		STATUS_WIN, STATUS_LOSE, STATUS_TIE, STATUS_PENDING
	}
	
	struct Player {
		address payable addr;
		uint256 playerBetAmount;
		Hand hand;
		PlayerStatus playerStatus;	// 사용자의 현 상태
	}
}
```

### 게임 구조체 만들기

컨트랙트에는 게임을 진행하는 여러 방(room)이 있으며, 각 방은 모두 같은 형식을 가지고 있다. 방에는 방장 정보, 참가자 정보, 총 베팅 금액이 있다.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract RPS {
	constructor () payable {}
	
	...
	struct Game {
		Player originator;	// 방장 정보
		Player taker;	// 참가자 정보
		uint256 betAmount;	//총 베팅 금액
	}
	
	// rooms[0], rooms[1] 형식으로 접근할 수 있으며, 각 요소는 Game 구조체 형식이다.
	mapping(uint => Game) rooms;
	// rooms의 키 값이다. 방이 생성될 때마다 1씩 올라간다.
	uint roomLen = 0;
}
```

게임의 상태를 `enum` 형식으로 지정한다. 게임의 상태는 다음과 같다.

1. 방만 만들어둔 상태
2. 참가자가 참여하여 게임 결과가 나온 상태
3. 게임 결과에 따라 베팅 금액을 분배한 상태
4. 게임 중간에 에러가 발생한 상태

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract RPS {
	constructor () payable {}
	
	...
	// 게임의 상태
	enum GameStatus {
		STATUS_NOT_STARTED, STATUS_STARTED, STATUS_COMPLETE, STATUS_ERROR
	}
	
	struct Game {
		Player originator;
		Player taker;
		uint256 betAmount;
		GameStatus gameStatus;	// 게임의 현 상태
	}
	
	mapping(uint => Game) rooms;
	uint roomLen = 0;
}
```



## 2. `createRoom` - 게임 생성하기

`createRoom`은 게임을 생성한다.게임을 생성한 방장은 자신이 낼 가위/바위/보 값을 인자로 보내고, 베팅 금액은 `msg.value`로 설정한다.

> `mst`는 solidity에 정의된 global variable이다. 따라서, `msg.value`는 함수를 사용할 때 입력받지만, 함수 내에서는 parameter로 설정할 필요가 없다.

```solidity
contract RPS {
	...
	// 베팅 금액을 설정하기 때문에 payable 키워드 사용
	function createRoom (Hand _hand) public payable {
	
	}
}
```

방을 만들고 나면 해당 게임의 방 번호를 반환한다.

```solidity
contract RPS {
	...
	function createRoom (Hand _hand) public payable returns (uint roomNum) {
		// 변수 roomNum의 값을 반환한다.
	}
}
```

방(게임)을 만들기 위해 `rooms`에 새로운 `Game` 구조체를 할당한다. Game 구조체의 인스턴스를 만든다.

- `betAmount`: 아직 방장만 있기 때문에 방장의 베팅 금액을 넣는다.
- `gameStatus`: 아직 시작하지 않은 상태이기 때문에 `GameStatus.STATUS_NOT_STARTED` 값을 넣는다.
- `originator`: `Player` 구조체의 인스턴스를 만들어, 방장의 정보르 넣어준다.
- `taker`: `Player` 구조체 형식의 데이터로 초기화되어야 하기 때문에 `addr`에는 방장의 주소를, `hand`는 `Hand.rock`으로 할당해둔다. (임의로 설정하는 것이다.)

만든 `Game` 인스턴스를 `room[roomLe]`에 할당한다.

```solidity
contract RPS {
	...
	function createRoom (Hand _hand) public payable returns (uint roomNum) {
		// 여기
		rooms[roomLen] = Game({
			betAmount: msg.value,
			gameStatus: GameStatus.STATUS_NOT_STARTED,
			originator: Player({
				hand: _hand,
				addr: payable(msg.sender),
				playerStatus: PlayerStatus.STATUS_PENDING,
				playerBetAmount: msg.value
			}),
			// 임의로 설정
			taker: Player({
				hand: Hand.rock,
				addr: payable(msg.sender),
				playerStatus: PlayerStatus.STATUS_PENDING,
				playerBetAmount: 0
			})
		})
		// 현재 방 번호를 roomNum에 할당시켜 return
		roomNum = roomLen;
		// 다음 방 번호 설정
		roomLen = roomLen+1;
	}
}
```

한편, 방장이 `createRoom`을 실행했을 때, 가위/바위/보 값에 다른 값이 지정될 수 있기 때문에, validation을 해준다. 이를 위해 `isValidHand`라는 함수 제어자를 만들어, `createRoom` 실행 시 확인하도록 한다.

```solidity
...
	modifier isValidHand (Hand _hand) {
		require((_hand == Hand.rock) || (_hand == Hand.paper) || (_hand == Hand.scissors));
        _;
	}
	
	function createRoom (Hand _hand) public payable isValidHand(_hand) returns (uint roomNum) {
		...
	}
...
```



## 3. `joinRoom` - 방에 참가하기

`joinRoom`은 기존에 만들어진 방에 참가한다. 참가자는 참가할 방 번호와 자신이 낼 가위/바위/보 값을 인자로 보내고, 베팅 금액을 `msg.value`로 설정한다. 가위/바위/보 값을 내기 때문에 마찬가지로 `isValidHand` 함수 제어자를 사용한다.

```solidity
contract RPS {
	...
	// 함수 작성
	function joinRoom (uint roomNum, Hand _hand) public payable isValidHand(_hand) {
		
	}
}
```

입력받은 방의 `Game` 구조체 인스턴스의 `taker`를 설정한다.

```solidity
contract RPS {
	...
	function joinRoom (uint roomNum, Hand _hand) public payable isValidHand(_hand) {
		// taker를 재설정
		rooms[roomNum].taker = Player({
			hand: _hand,
			addr: payable(msg.sender),
			playerStatus: PlayerStatus.STATUS_PENDING
			playerBetAmount: msg.value
		});
	}
}
```

참가자가 참여하면서 게임의 베팅 금액이 추가되었으므로, `Game` 인스턴스의 `betAmount`도 변경해준다.

```solidity
contract RPS {
	...
	function joinRoom (uint roomNum, Hand _hand) public payable isValidHand(_hand) {
		rooms[roomNum].taker = Player({
			hand: _hand,
			addr: payable(msg.sender),
			playerStatus: PlayerStatus.STATUS_PENDING
			playerBetAmount: msg.value
		});
		rooms[roomNum].betAmount = rooms[roomNum].betAmount + msg.value;
	}
}
```

### `compareHands()` - 게임 결과 업데이트

`joinRoom` 함수가 끝나는 시점에서, 방장과 참가자가 모두 가위바위보 값을 냈기 때문에 게임의 승패를 확인할수 있다. 게임 결과에 따라 게임 상태와 참여자들의 상태를 업데이트하는 함수 `compareHands()`를 작성해본다. 게임 결과는 `joinRoom`이 완료된 시점에서 확인할 수 있기 때문에 `joinRoom` 함수의 맨 마지막에 `compareHands` 함수를 호출하며, `compareHands`는 인자로 게임의 결과를 확인할 방 번호를 받는다.

```solidity
contract RPS {
	...
	function joinRoom (uint roomNum, Hand _hand) public payable isValidHand(_hand) {
		...
		// 게임 결과 업데이트 함수 호출
		compareHands();
	}
	
	function compareHnads(uint roomNum) private {
		
	}
}
```

> **승패 여부 확인하기**
>
> ```solidity
> enum Hand {
> 	rock, paper, scissors
> }
> ```
>
> `enum Hands`를 보면 0(rock), 1(paper), 2(scissors)의 값을 가지고 있으며, 1은 0을, 2는 1을, 0은 2를 이긴다. 즉, 상대방의 값 x와 나의 값 y에 대해, 다음 조건을 만족하면 자신(y)이 이긴 것이다.
>
> ```solidity
> (x + 1) % 3 == y
> ```
>
> 따라서 방장이 참가자를 이긴 상황을 코드로 작성하면 다음과 같다.
>
> ```solidity
> if ((takerHand + 1) % 3 == originatorHand) {
> 	// Originator Win!
> }
> ```

먼저 해당 게임의 방장과 참가자의 가위바위보 값은 `enum` 값이기 때문에 정수형으로 바꿔준다. 그리고 게임을 본격적으로 비교하기 때문에 게임의 상태르 `GameStatus.STATUS_STARTED`로 변경한다.

```solidity
	function compareHnads(uint roomNum) private {
		// 가위바위보 값을 정수형(uint8)으로 변환
		uint8 originator = uint8(rooms[roomNum].originator.hand);
		uint8 taker = uint8(rooms[roomNum].taker.hand);
		
		// gameStatus 변경
		rooms[roomNum].gameStatus = GameStatus.STATUS_STARTED;
	}
```

가위바위보 값에 따라, 방장과 참가의 `playerStatus`를 설정한다.

```solidity
        function compareHands(uint roomNum) private {
            uint8 originator = uint8(rooms[roomNum].originator.hand);
            uint8 taker = uint8(rooms[roomNum].taker.hand);

            rooms[roomNum].gameStatus = GameStatus.STATUS_STARTED;

            // 비긴 경우
            if (taker == originator) {
                rooms[roomNum].originator.playerStatus = PlayerStatus.STATUS_TIE;
                rooms[roomNum].taker.playerStatus = PlayerStatus.STATUS_TIE;
            }
            // 방장이 이긴 경우
            else if ((taker + 1) % 3 == originator) {
                rooms[roomNum].originator.playerStatus = PlayerStatus.STATUS_WIN;
                rooms[roomNum].taker.playerStatus = PlayerStatus.STATUS_LOSE;
            }
            // 참가자가 이긴 경우
            else if ((originator + 1) % 3 == taker) {
                rooms[roomNum].originator.playerStatus = PlayerStatus.STATUS_LOSE;
                rooms[roomNum].taker.playerStatus = PlayerStatus.STATUS_WIN;
            }
            // 그 외의 상황에는 게임 상태를 에러로 업데이트
            else {
                rooms[roomNum].gameStatus = GameStatus.STATUS_ERROR;
            }
        }
```



## 4. `checkTotalPay` - 방마다 베팅 금액 확인하기

각 방마다 배팅이 얼마 걸렸는지 확인할 수 있는 함수이다. 방 번호를 인자로 받아, 해당의 베팅 금액을 return한다. 컨트랙트에 있는 금액을 보기만 하기 위해 솔리디티에 내장되어 있는 `view` 함수를 사용한다.

```solidity
contract RPS {
	...
	function checkTotalPay (uint roomNum) public view returns (uint roomNumPay) {
		return rooms[roomNum].betAmount;
	}
}
```



## 5. `payout` - 베팅 금액 송금하기

`payout` 함수는 방 번호를 인자로 받아, 게임 결과에 따라 베팅 금액을 송금하고, 게임을 종료한다.

> 컨트랙트에 있는 금액을 송금하기 위해 solidity 내장 함수인 `transfer`을 사용한다.
>
> ```solidity
> ADDRESS.transfer(value)	// ADDRESS로 value만큼 송금한다.
> ```

가위바위보 컨트랙트에서는, 비긴 경우 자신의 베팅 금액을 돌려받고, 이긴 경우 전체 베팅 금액을 받는다. 다음과 같이 `payout` 함수를 작성한다.

```solidity
	function payout(uint roomNum) public payable {
		 // 비긴 경우 -> 베팅 금액을 다시 돌려줌
        if (rooms[roomNum].originator.playerStatus == PlayerStatus.STATUS_TIE && rooms[roomNum].taker.playerStatus == PlayerStatus.STATUS_TIE) {
            // ADDRESS.transfer(value) 함수를 사용하면 ADDRESS로 value만큼 송금한다.
            rooms[roomNum].originator.addr.transfer(rooms[roomNum].originator.playerBetAmount);
            rooms[roomNum].taker.addr.transfer(rooms[roomNum].taker.playerBetAmount);
        }
        else {
            // 방장이 이긴 경우
            if (rooms[roomNum].originator.playerStatus == PlayerStatus.STATUS_WIN) {
                rooms[roomNum].originator.addr.transfer(rooms[roomNum].betAmount);
            }
            // 참가자가 이긴 경우
            else if (rooms[roomNum].taker.playerStatus == PlayerStatus.STATUS_WIN) {
                rooms[roomNum].taker.addr.transfer(rooms[roomNum].betAmount);
            }
            // 오류인 경우 => 배팅 금액을 다시 돌려줌
            else {
                rooms[roomNum].originator.addr.transfer(rooms[roomNum].originator.playerBetAmount);
                rooms[roomNum].taker.addr.transfer(rooms[roomNum].taker.playerBetAmount);
            }
        }
        // 게임이 종료되었으므로, 게임 상태 변경
        rooms[roomNum].gameStatus = GameStatus.STATUS_COMPLETE;
	}
```

참가자가 중간에 자신이 낸 값을 변경할 수도 있기 때문에 `payout`을 실행하기 전 해당 함수를 실행하는 주체가 방장 또는 참가자인지 확인하는 함수 제어자 `isPlayer`를 만든다. `isPlayer`는 방 번호와 함수를 호출한 사용자의 주소를 받는다. 그리고 사용자의 주소가 방장 또는 참가자의 주소와 일치하는지 확인한다.

```solidity
modifier isPlayer (uint roomNum, address sender) {
	require(sender == rooms[roomNum].originator.addr || sender == rooms[roomNum].taker.arrd);
	_;
}

function payout(uint roomNum) public payable isPlayer(roomNum, msg.sender) {...}
```



## 전체 코드

```solidity
// RPS.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract RPS {
    // 송금 가능하다는 것 명시
    constructor () payable {}

    // 가위/바위/보 값에 대한 enum(범주형)
    enum Hand {
        rock, paper, scissors
    }

    // 플레이어의 상태
    enum PlayerStatus {
        STATUS_WIN, STATUS_LOSE, STATUS_TIE, STATUS_PENDING
    }

    // 플레이어 구조체
    struct Player {
        address payable addr;   // 주소
        uint256 playerBetAmount;    // 배팅 금액
        Hand hand;  // 플레이어가 낸 가위/바위/보 값
        PlayerStatus playerStatus;  // 사용자의 현 상태
    }

    // 게임의 상태
    enum GameStatus {
        STATUS_NOT_STARTED, STATUS_STARTED, STATUS_COMPLETE, STATUS_ERROR
    }

    // 게임 구조체
    struct Game {
        Player originator;  // 방장 정보
        Player taker;   // 참여자 정보
        uint256 betAmount;  // 총 베팅 금액
        GameStatus gameStatus;  // 게임의 현 상태
    }

    // mapping: python의 dict 형태
    // rooms 변수에 uint 형식의 key 값: Game 형태의 value 값을 저장 (스토리지에 저장)
    mapping(uint => Game) rooms;    // rooms[0], rooms[1] 형식으로 접근할 수 있으며, 각 요소는 Game 구조체 형식
    uint roomLen = 0;   // rooms의 키 값으로, 방이 생성될 때마다 1씩 올라감

    // 방장이 낸 값(가위/바위/보)이 올바른지 확인하기 위한 제어자
    modifier isValidHand (Hand _hand) {
        require((_hand == Hand.rock) || (_hand == Hand.paper) || (_hand == Hand.scissors));
        _;
    }
    // 1. 방장(originator)가 createRoom을 호출
    // args: 가위/바위/보 값, 베팅 금액
    // 새로운 방을 만들고, 방 번호를 return
    function createRoom (Hand _hand) public payable isValidHand(_hand) returns (uint roomNum) {   // 베팅 금액 설정하기 때문에 payable
        rooms[roomLen] = Game({
            betAmount: msg.value,   // msg.value는 함수 내 parameter로 따로 설정하지 않는다.
            gameStatus: GameStatus.STATUS_NOT_STARTED,
            originator: Player({
                hand: _hand,
                addr: payable(msg.sender),
                playerStatus: PlayerStatus.STATUS_PENDING,
                playerBetAmount: msg.value
            }),
            // 임의로 데이터를 넣고, Player 구조체 형식의 데이터로 초기화함
            taker: Player({
                hand: Hand.rock,
                addr: payable(msg.sender),
                playerStatus: PlayerStatus.STATUS_PENDING,
                playerBetAmount: 0
            })
        });
        roomNum = roomLen;  // 변수 roomNum 값을 return
        roomLen = roomLen+1;    // 다음 방 번호를 설정
    }
    // 2. 참가자(taker)는 joinRoom을 호출
    // args: 방 번호, 가위/바위/보 값, 베팅 금액
    // 참가자를 방에 참여시키고, 방장-참가자의 가위/바위/보 값을 확인 후 방의 승자를 설정
    function joinRoom (uint roomNum, Hand _hand) public payable isValidHand(_hand) {
        rooms[roomNum].taker = Player({
            hand: _hand,
            addr: payable(msg.sender),
            playerStatus: PlayerStatus.STATUS_PENDING,
            playerBetAmount: msg.value
        });

        // 참가자가 참여하였기 때문에, 게임 베팅 금액을 추가해준다.
        // rooms[roomNum] => Game 객체
        rooms[roomNum].betAmount = rooms[roomNum].betAmount + msg.value;

        // 게임 결과 업데이트 함수 호출
        compareHands(roomNum);
        
    }
        // 가위바위보 값에 따라, 방장과 참가자의 playerStatus를 설정
        function compareHands(uint roomNum) private {
            uint8 originator = uint8(rooms[roomNum].originator.hand);
            uint8 taker = uint8(rooms[roomNum].taker.hand);

            rooms[roomNum].gameStatus = GameStatus.STATUS_STARTED;

            // 비긴 경우
            if (taker == originator) {
                rooms[roomNum].originator.playerStatus = PlayerStatus.STATUS_TIE;
                rooms[roomNum].taker.playerStatus = PlayerStatus.STATUS_TIE;
            }
            // 방장이 이긴 경우
            else if ((taker + 1) % 3 == originator) {
                rooms[roomNum].originator.playerStatus = PlayerStatus.STATUS_WIN;
                rooms[roomNum].taker.playerStatus = PlayerStatus.STATUS_LOSE;
            }
            // 참가자가 이긴 경우
            else if ((originator + 1) % 3 == taker) {
                rooms[roomNum].originator.playerStatus = PlayerStatus.STATUS_LOSE;
                rooms[roomNum].taker.playerStatus = PlayerStatus.STATUS_WIN;
            }
            // 그 외의 상황에는 게임 상태를 에러로 업데이트
            else {
                rooms[roomNum].gameStatus = GameStatus.STATUS_ERROR;
            }
        }

    // 3. 방장(originator) 혹은 참가자(taker)는 checkTotalPay 함수를 호출
    // args: 방 번호
    // 해당 방 배팅금액 return
    function checkTotalPay (uint roomNum) public view returns (uint roomNumPay) {
        return rooms[roomNum].betAmount;
    }

    // payout 함수의 제어자
    // 참가자가 중간에 자신이 낸 값을 변경할 수도 있기 떄문에
    // payout 전, 해당 함수 실행 주체가 방장||참가자인지 확인
    modifier isPlayer (uint roomNum, address sender) {
        require(sender == rooms[roomNum].originator.addr || sender == rooms[roomNum].taker.addr);
        _;
    }

    // 4. 방장 혹은 참가자가 payout 함수 호출
    // args: 게임을 끝낼 방 번호
    // 게임 결과에 따라 베팅 금액 송금
    function payout (uint roomNum) public payable isPlayer(roomNum, msg.sender) {

        // 비긴 경우 -> 베팅 금액을 다시 돌려줌
        if (rooms[roomNum].originator.playerStatus == PlayerStatus.STATUS_TIE && rooms[roomNum].taker.playerStatus == PlayerStatus.STATUS_TIE) {
            // ADDRESS.transfer(value) 함수를 사용하면 ADDRESS로 value만큼 송금한다.
            rooms[roomNum].originator.addr.transfer(rooms[roomNum].originator.playerBetAmount);
            rooms[roomNum].taker.addr.transfer(rooms[roomNum].taker.playerBetAmount);
        }
        else {
            // 방장이 이긴 경우
            if (rooms[roomNum].originator.playerStatus == PlayerStatus.STATUS_WIN) {
                rooms[roomNum].originator.addr.transfer(rooms[roomNum].betAmount);
            }
            // 참가자가 이긴 경우
            else if (rooms[roomNum].taker.playerStatus == PlayerStatus.STATUS_WIN) {
                rooms[roomNum].taker.addr.transfer(rooms[roomNum].betAmount);
            }
            // 오류인 경우 => 배팅 금액을 다시 돌려줌
            else {
                rooms[roomNum].originator.addr.transfer(rooms[roomNum].originator.playerBetAmount);
                rooms[roomNum].taker.addr.transfer(rooms[roomNum].taker.playerBetAmount);
            }
        }
        // 게임이 종료되었으므로, 게임 상태 변경
        rooms[roomNum].gameStatus = GameStatus.STATUS_COMPLETE;
    }
}


```



***Copyright* © 2022 Song_Artish**