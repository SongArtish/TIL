# Solidity Intro

---

[TOC]

---



## Overview

솔리디티는 **컨트랙트 기반**의 객체 지향(Object-Oriented), 정적 타입(Static Typed), 고급(High-Level) 스크립트 언어로, EVM에서 실행된다. **이더리움 블록체인 플랫폼**에서 다양한 스마트 컨트랙트를 작성할 때 사용된다.



## 특징

- **정적 타입의 중괄호 언어**: 솔리디티는 정적 타입(static-typed)의 중괄호(curly-braces) 프로그래밍 언어이다. 컴파일 시 변수에 타입이 결정되며, 그렇기 때문에 소스 코드에 타입을 명확하게 정의해줘야 한다
- **Ethereum Virtual Machine**: 솔리디티는 EVM이라는 이더리움 가상 스택 머신 위에서 동작한다.
- **세미콜론(`;`)**: 문장의 끝에 반드시 세미콜론(`;`)을 붙여야 한다.

### 튜링 완전 언어

```markdown
#### 튜링 머신
1930년대 Alan Turing은 Universal Turing Machine이라는 개념을 고안했다. 튜링 머신은 실제로 구현된 기계가 아니라, 이론 상으로 존재하는 기계로, 오늘날 우리가 구축할 수 있는 가장 강력한 기계 컴퓨터를 설명할 때 사용하는 수학적 연산 모델이다.

어떤 프로그래밍 언어나 추상 기계가 튜링 머신과 동일한 연산 능력을 가질 때, 우리는 그것이 튜링 완전(Turing-Complete)하다고 말하며, 반대로 튜링 머신보다 연산 능력이 떨어질 경우 튜링 불완전(Turing-Incomplete)하다고 한다.
```

비트코인 스마트 컨트랙트에서는 Opcode를 사용해 스크립트를 구성했는데, 사토시 나카모토는 무한 반복 공격과 같은 보안 상의 이슈를 고려해 의도적으로 반복문 Opcode를 제외하였고, 결국 비트코인 스크립트에서는 몇 가지 Opcode를 사용할 수 없다. 따라서 비트코인 스크립트를 두소 **튜링 불완전**하다고 한다.

이더리움은 개발자가 원하는 스마트 컨트랙트를 유연하게 구현할 수 있도록 튜링 완전을 제공한다. EVM은 반복문 Opcode들을 지원하는 대표적인 튜링 완전 머신이며, 솔리디티는 튜링 완전 머신을 동작하게 하는 튜링 완전 언어이다.



## 컨트랙트 구조

컨트랙트는 다음과 같이 구성된다.

- 상태 변수(State Variables)
- 구조체(Struct Types)
- 열거형(Enum Types)
- 함수(Functions)
- 함수 제어자(Function Modifiers)
- 이벤트(Events)
- 에러(Errors)
- 상속(Inheritance)
- ...



## 데이터 저장 위치

```markdown
- 변수
  보통 프로그래밍 언어라면 변수는 스택, 힙 등 `메모리`에 저장되지만, 솔리디티는 변수를 `메모리`뿐 아니라 하드 디스크 등과 같은 `스토리지`에 저장하기도 한다.
  
- 함수 인자
  `calldata`라는 영역에 저장된다. `calldata`는 메모리처럼 동작하지만 수정 불가능하고 비영구적인 영역이다.
```

**솔리디티 데이터 저장 위치**

- 메모리
- 스토리지
- calldata

**강제 데이터 위치**

- 외부 함수의 매개 변수(return 값 미포함): calldata
- 상태 변수: 스토리지

**기본 데이터 위치**

- 함수의 매개변수(반환 값 포함): 메모리
- 모든 지역 변수: 스토리지



## 개발 도구

dApp의 백엔드 개발 도구는 대표적으로 다음과 같다.

- **Remix IDE**

  Remix는 솔리디티를 사용한 dApp 개발을 도와주는 통합 개발 환경이다. Remix IDE는 JavaScript로 만들어졌기 때문에 브라우저에서 사용가능하며, 로컬이나 데스크톱 버전을 사용할 수도 있다.

- **solc**

  솔리디티는 고급 언어이기 때문에 가상 머신인 EVM은 솔리디티를 읽을 수 없다. 따라서 솔리디티를 바이트코드로 컴파일해야 하는데, 이때 사용하는 컴파일러가 solc이다.

- **Ganache**

  Ganache는 개발 단계에서 시뮬레이션 테스트 환경을 구성해주는 도구이다. 실제 이더리움 메인넷에서 테스트를 하기 위해서는 이더를 내야하지만, Ganache를 사용하면 채굴 없이 가상 이더리움 환경에서 트랜잭션 제한 없이 테스트를 할 수 있다.

- **TestNet**

  이더리움에서 제공하는 퍼블릭 테스트 네트워크를 TestNet이라고 한다. 테스트 네트워크는 실제 이더리움과 비슷하지만 실제 트랜잭션이 이루어지지는 않는다. 이더리움은 현재 Ropsten, Kovan, Rinkeby 세 개의 퍼블릭 테스트넷이 제공되고 있다.

- 프레임워크 : **Truffle, Embark, Dapple**

  솔리디티 코드를 이더리움 네트워크에 올리기 위한 여러 복잡한 과정을 해결해주는 다양한 프레임워크들이 있다. 이 프레임워크들은 솔리디티 코드에 대해 테스트, 디버깅, 컴파일, 배포를 제공한다.



## 시작하기

### SPDX License Identifier

스마트 컨트랙트에 대한 신뢰를 높이고, 저작권과 같은 문제를 해소하기 위해 솔리디티 코드의 최상단에 SPDX 라이센스를 명시해야 한다. SPDX 라이센스는 주석으로 표기한다.

```solidity
// SPDX-License-Identifier: MIT
```

```solidity
// SPDX-License-Identifier: GPL-3.0
```

SPDX 라이센스 리스트는 https://spdx.org/licenses/에서 확인할 수 있다.

### Pragma

`pragma` 키워드는 특정 컴파일러의 버전을 표기할 때 사용한다. `pragma`는 모든 소스 코드 파일에 있어야 하며, 다른 파일을 import 하더라도 pragma는 자동으로 import되지 않는다. 일반적으로 다음과 같이 파일 최상단에 작성한다.

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.14;	// 0.8.14 버전을 사용
```

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.14;	// 0.8.14 이상의 버전을 사용
```

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.0 <0.9.0;	// 0.4.0 이상 0.9.0 미만의 버전을 사용
```

그 외에도 다양한 버전 규칙을 사용할 수 있으며, 버전 규칙은 [npm 버전 규칙](https://docs.npmjs.com/cli/v6/using-npm/semver)과 동일하다.

### Contract

솔리디티 계약은 이더리움 블록체인의 특정 주소를 가진 **기능(`함수`)**와 **상태(`변수`)**의 모음이다. 마치 일반적인 객체 지향 언어의 클래스를 정의하듯이, 하나의 contract(계약)을 정의한다.

```solidity
contract SimpleStorgage {
	uint storedData;	// 상태 변수
	// 함수
	function set(uint x) public {
		storedData = x;
	}
	// 함수
	function get() public view returns (uint) {
	return storedData;
	}
}
```

### Import

파일을 import하는 방식은 JavaScript에서 사용하는 방식과 동일하다.

```solidity
import "파일이름";

// import하는 파일을 symbolName이라는 이름으로 사용
import * as symbolName from "파일이름";
import "파일이름" as symbolName;

// 파일의 일부분만 import하는 경우
import {symbol1 as alias, symbol2} from "파일이름";
```

### 주석

단일 라인 주석 처리는 `//`, 여러 라인 주석 처리는 `/*...*/`로 진행한다.

```solidity
// 단일 라인 주석

/*
이것은
여러 라인 주석
*/
```



***Copyright* © 2022 Song_Artish**