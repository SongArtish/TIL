# Solidity 제어문

---

[TOC]

---



## 조건문(Conditional Statements)

```solidity
if (조건식 A) {
	조건식 A가 참인 경우, 여기 있는 코드 수행
}
else if (조건식 B) {
	조건식 A가 거짓이고, 조건식 B가 참인 경우, 여기 있는 코드 수행
}
else {
	조건식이 모두 거짓인 경우, 여기 있는 코드 수행
}
```

### 삼항 연산자

```solidity
MyVariable = expression ? ValueT: valueF
// 변수 = 조건식 ? 참일 경우의 값 : 거짓일 경우의 값
```

삼항 연산자로도 조건을 표현할 수 있다. 한 줄로 보다 코드의 길이를 짧게 표현할 수 있다는 장점이 있다.

```solidity
function checkCondition(uint x) public pure returns(uint result) {
	// result = 조건식 ? 참일 경우 : 거짓일 경우;
	result = x >= 1500 ? 1 : 0;
	return result
}
```



## 반복문(Loop)

반복문은 특정한 작업을 계속해서 수행해야 할 때 사용한다.

### 1. while 문

while 문은 가장 기본적인 반복문으로, 조건식이 참일 때 중괄호 안의 코드를 반복적으로 시행하고, 조건식이 거짓이 되면 반복문을 종료한다.

```solidity
while (조건식) {
	조건식이 참이면 여기 있는 코드 수행
}
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.14;

contract WhileLoop {
	uint[] data;
	uint8 j = 0;
	
	function loop() public returns(uint[] memory) {
		while(j < 5) {
			j++
			data.push(j);
		}
		return data;
	}
}	// data == [1, 2, 3, 4, 5]
```

### 2. do-while 문

do-while 문은 while 문과 매우 유사하다. 하지만 반복문의 끝에 조건식 검사가 있기 때문에, 조건식이 거짓인 경우에도 **적어도 한 번은 무조건 실행**한다는 특징이 있다.

```solidity
do
{
	최초 한번은 무조건 실행
	이후부터는 조건식이 참이면 여기 있는 코드 수행
} while (조건식);
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.14;

contract DoWhileLoop {
	uint[] data;
	uint8 j = 0;
	
	function loop() public returns(uint[] memory) {
		do {
			j++;
			data.push(j);
		} while (j < 0);
		return data;
	}
}	// data == [1] (이미 j < 0 조건식에 거짓이지만 한 번은 실행함)
```

### 3. for 문

for 문은 가장 간결한 반복문이라고 할 수 있다.

```solidity
for (초기값; 조건식; 증감식) {
	조건식이 참이면 여기 있는 코드 수행
}
```

for 문의 괄호 안에는 아래 3가지를 세미콜론으로 구분하여 넣어야 한다.

- **초기값**: 반복 횟수를 셀 변수를 초기화하는 부분
- **조건식**: 참인 경우에 반복 수행
- **증감식**: 초기값을 담은 변수를 변화시킴. 매 반복 시 한 번씩 실행

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.14;

contract ForLoop {
	uint[] data;
	
	function loop() public returns(uint[] memory) {
		for(uint i = 0; i < 5; i++) {
			data.push(i);
		}
		return data;
	}
}	// data == [0, 1, 2, 3, 4]
```



### continue

continue는 반복문 실행 도중 나머지 코드를 건너뛰고 싶을 때 사용한다. while, do-while, for 문 안에 사용할 수 있다.

```solidity
while(조건식) {
	조건식이 참이면 여기 있는 코드 수행
	<새로운 조건 추가> {
		continue;
		조건에 만족하면 아래 코드를 실행하지 않고 건너뛴다.
	}
	카운터 값 증가
}
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.14;

contract ContinueLoop {
	uint[] data;
	uint8 j = 0;
	
	function loop() public returns(uint[] memory) {
		while (j <= 100) {
			j++;
			if (j % 2 != 0) {	// j를 2로 나누었을 때 나머지가 0이 아니라면 (홀수)
				continue;	// 아래 코드를 실행하지 않고 건너뜀
			}
			data.push(j);
		}
		return data;
	}
}	// data == [2, 4, 6, 7, ... , 100]
```

### break

break는 중간에 반복문을 멈추고 바깥으로 나가고 싶을 때 사용한다.while, do-while, for 문 안에 사용할 수 있다.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.14;

contract BreakLoop {
	uint[] data;
	uint8 j = 0;
	
	function loop() public returns(uint[] memory) {
		while(j <= 100) {
			j++;
			if(j == 5) {	// j가 5가 되었을 때
				break;	// while 반복문을 빠져나감
			}
			data.push(j)
		}
		retun data;
	}
}	// data == [1, 2, 3, 4]
```



***Copyright* © 2022 Song_Artish**