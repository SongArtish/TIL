# Solidity NatSpec Format

---

[TOC]

---



## Overview

컨트랙트의 모든 함수에서 예상되는 행동값을 주석으로 설명하기 위한 솔리디티 커뮤니티 표준 형식

- 참고 문서: https://docs.soliditylang.org/en/develop/natspec-format.html



## 예시

```solidity
/// @title 기본적인 산수를 위한 컨트랙트
/// @author H4XF13LD MORRIS 💯💯😎💯💯
/// @notice 지금은 곱하기 함수만 추가한다.
contract Math {
  /// @notice 2개의 숫자를 곱한다.
  /// @param x 첫 번쨰 uint.
  /// @param y 두 번째 uint.
  /// @return z (x * y) 곱의 값
  /// @dev 이 함수는 현재 오버플로우를 확인하지 않는다.
  function multiply(uint x, uint y) returns (uint z) {
    // 이것은 일반적인 주석으로, natspec에 포함되지 않는다.
    z = x * y;
  }
}
```

- **@notice**: 사용자에게 컨트랙트/함수가 무엇을 하는지 설명함
- **@dev**: 개발자에게 추가적인 상세 정보를 설명하기 위해 사용함
- **@param**: 함수의 매개 변수
- **@return**: 함수의 반환값



***Copyright* © 2022 Song_Artish**