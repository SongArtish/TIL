# Solidity 연산자

---

[TOC]

---



## Overview

솔리디티는 다음과 같은 유형의 연산자를 지원한다.

- 산술 연산자(Arithmetic Operators)
- 비교 연산자(Comparison Operators)
- 논리 연산자(Logical Operators)
- 할당 연산자(Assignment Operators)
- 비트 연산자(Bitwise Operators)
- 조건부 연산자(Conditional Operator)



## 산술 연산자(Arithmetic Operators)

피연산자의 수학적 연산을 수행하는데 사용한다.

| 연산자 |                           의미                           |
| :----: | :------------------------------------------------------: |
|   +    |                           덧셈                           |
|   -    |                           뺄셈                           |
|   *    |                           곱셈                           |
|   /    |                    나눗셈(분자/분모)                     |
|   %    | 첫 번째 피연산자를 두 번째 피연산자로 나눈 나머지를 제공 |
|   ++   |                    정수 값을 1씩 증가                    |
|   --   |                    정수 값을 1씩 감소                    |

```solidity
// SPDX-License_Identifier: MIT
pragma solidity ^0.8.14;
// 컨트랙트 생성
contract SolidityTest {
	// 변수 선언 및 초기화
	uint16 public a = 20;
	uint16 public b = 10;
	// + 연산자를 활용한 덧셈 및 초기화
	uint public sum = a + b;
	// - 연산자를 활용한 뺄셈 및 초기화
	uint public dif = a - b;
	// * 연산자를 활용한 곱셈 및 초기화
	uint public mul = a * b;
	// / 연산자를 활용한 나눗셈 및 초기화
	uint public div = a / b;
	// % 연산자를 활용한 나머지 계산 및 초기화
	uint public mod = a % b;
	// ++ 연산자를 활용한 1 증가
	uint public inc = ++a;
	// -- 연산자를 활용한 1 감소
	uint public dec = --b;
}
```



## 비교 연산자(Comparison Operators)

피연산자를 서로 비교하는데 사용한다.

| 연산자 |                             의미                             |
| :----: | :----------------------------------------------------------: |
|   ==   |           두 값이 같으면 true, 아니면 false를 반환           |
|   !=   |        두 값이 같지 않으면 true, 아니면 false를 반환         |
|   >    | 왼쪽 값이 오른쪽 값보다 더 크다면 true, 아니면 false를 반환  |
|   <    | 왼쪽 값이 오른쪽 값보다 더 작다면 true, 아니면 false를 반환  |
|   >=   | 왼쪽 값이 오른쪽 값보다 더 크거나 같다면 true, 아니면 false를 반환 |
|   <=   | 왼쪽 값이 오른쪽 값보다 더 작거나 같다면 true, 아니면 false를 반환 |

```solidity
// SPDX-License_Identifier: MIT
pragma solidity ^0.8.14;
// 컨트랙트 생성
contract SolidityTest {
	// 변수 선언 및 초기화
	uint16 public a = 20;
	uint16 public b = 10;
	// == 연산자를 활용한 비교 및 초기화
	bool public eq = a == b;
    // != 연산자를 활용한 비교 및 초기화
	bool public noteq = a != b;
    // > 연산자를 활용한 비교 및 초기화
	bool public gtr = a > b;
    // < 연산자를 활용한 비교 및 초기화
	bool public les = a < b;
    // >= 연산자를 활용한 비교 및 초기화
	bool public gtreq = a >= b;
    // <= 연산자를 활용한 비교 및 초기화
	bool public leseq = a <= b;
}
```



## 논리 연산자(Logical Operators)

둘 이상의 조건을 결합하는데 사용한다.

| 연산자 |                           의미                           |
| :----: | :------------------------------------------------------: |
|   &&   |     두 조건이 모두 참이면 true, 아니면 false를 반환      |
|  \|\|  | 최소 하나 이상의 조건이 참이면 true, 아니면 false를 반환 |
|   !    |           true를 false로, false를 true로 반환            |

```solidity
// SPDX-License_Identifier: MIT
pragma solidity ^0.8.14;
// 컨트랙트 생성
contract SolidityTest {
	// 변수 선언 및 초기화
	bool public a = true;
	bool public b = false;
	// && 연산자를 활용한 조건 결합 및 초기화
	bool public and = a && b;
	// || 연산자를 활용한 조건 결합 및 초기화
	bool public or = a || b;
	// ! 연산자를 활용한 조건 반전 및 초기화
	bool public not = !a;
}
```



## 할당 연산자(Assignment Operators)

변수에 값을 할당하기 위해 사용한다. 왼쪽 피연산자에 오른쪽의 피연산자를 할당하며, 산술 연산자와 `=` 연산자가 조합된 것이다.

| 연산자 |                          의미                           |
| :----: | :-----------------------------------------------------: |
|   =    |         오른쪽 피연산자를 왼쪽 피연산자에 할당          |
|   +=   |  오른쪽 피연산자를 왼쪽 피연산자에 더하고 그 값을 할당  |
|   -=   |  왼쪽 피연산자에서 오른쪽 피연산자를 빼고 그 값을 할당  |
|   *=   |           피연산자를 모두 곱하고 그 값을 할당           |
|   /=   |  왼쪽 피연산자를 오른쪽 피연산자로 나누고 그 값을 할당  |
|   %=   | 왼쪽 피연산자를 오른쪽 피연산자로 나눈 나머지 값을 할당 |

```solidity
// SPDX-License_Identifier: MIT
pragma solidity ^0.8.14;
// 컨트랙트 생성
contract SolidityTest {
	// 변수 선언 및 초기화
	uint16 public assignment = 20;
	uint public assignment_add = 50;
	uint public assign_sub = 50;
	uint public assign_mul = 10;
	uint public assign_div = 50;
	uint public assign_mod = 32;
	
	function getResult() public {
		assignment_add += 10;	// += 연산자 사용, 60
		assign_sub -= 20;	// -= 연산자 사용. 30
		assign_mul *= 10;	// *= 연산자 사용. 100
		assign_div /= 10;	// /= 연산자 사용. 5
		assign_mod %= 20;	// %= 연산자 사용. 12
		return ;
	}
}
```



## 비트 연산자(Bitwise Operators)

비트 수준 연산을 수행하는데 사용한다.

| 연산자 |                             의미                             |
| :----: | :----------------------------------------------------------: |
|   &    |           정수의 각 비트에 대해 bool AND 연산 수행           |
|   \|   |           정수의 각 비트에 대해 bool OR 연산 수행            |
|   ^    |        정수의 각 비트에 대해 bool 배타적 OR 연산 수행        |
|   ~    |           정수의 각 비트에 대해 bool NOT 연산 수행           |
|   <<   | 왼쪽 피연산자의 모든 비트를 오른쪽 피연산자에 의해 지정된 위치 수만큼 왼쪽으로 디오 |
|   >>   | 왼쪽 피연산자의 모든 비트를 오른쪽 피연산자에 의해 지정된 위치 수만큼 오른쪽으로 이동 |

| X    | Y    | X & Y | X ^ Y | ~X   |
| ---- | ---- | :---: | :---: | ---- |
| 0    | 0    |   0   |   1   |      |
| 0    | 1    |   0   |   0   |      |
| 1    | 0    |   0   |   0   |      |
| 1    | 1    |   1   |   1   |      |

```solidity
// SPDX-License_Identifier: MIT
pragma solidity ^0.8.7;
// 컨트랙트 생성
contract SolidityTest {
	// 변수 선언 및 초기화
	uint16 public a = 20;	// 10100
	uint16 public b = 10;	// 01010
	
	uint16 public and = a & b;	// 0
	uint16 public or = a | b;	// 30
	uint16 public xor = a ^ b;	// 30
	uint16 public leftshift = a << b;	// to '<<' value
	uint16 public rightshift = a >> b;	// to '>>' value
	uint16 public not = ~a;
}
```



## 조건부 연산자(Conditional Operator)

```solidity
MyVariable = expression ? ValueT: valueF
// 변수 = 조건식 ? 참일 경우의 값 : 거짓일 경우의 값
```

조건식의 true, false 반환 값에 따라 특정 값을 반환하고자 할 때 사용한다. **삼항 연산자**라고도 한다.

```solidity
// SPDX-License_Identifier: MIT
pragma solidity ^0.8.14;
// 컨트랙트 생성
contract SolidityTest {
	function sub(uint a, uint b) public view returns (uint) {
		uint result = (a > b ? a-b : b-a);
		return result
	}
}
/*
만약 a = 2, b = 1이면, a > b가 true가 되어 a-b의 값을 리턴
만약 a = 1, b = 1이면, a > b가 false가 되어 b-a의 값을 리턴
만약 a = 1, b = 2이면, a > b가 false가 되어 b-a의 값을 리턴
*/
```



***Copyright* © 2022 Song_Artish**