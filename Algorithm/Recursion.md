# 재귀

---

[TOC]

---



## Recursion

재귀 함수(Recursive Function)는 **자기 자신을 호출하는 함수**이다. 구조가 비슷한 더 작은 문제를 쪼갤 수 있는 문제를 풀 때 유용한 접근법이다. 보통은 아래와 같은 형태로 작성이 가능하다.

```javascript
// factorial.js
function factorial(n) {
    // 탈출 코드
    if (n <= 1) {
        return n
    }
    // 수행 코드
    return n * factorial(n-1)
}
```

재귀 함수는 호출 시마다 stack 공간에 데이터를 저장하기 때문에, 무리하게 호출하면 Stack Overflow가 발생할 수 있다.



## Tail Recursion

꼬리재귀(Tail Recursion)는 기존 재귀 함수의 단점을 보완한 방법 중 하나이다. **재귀 호출이 끝나면 아무 일도 하지 않고 결과만 바로 반환**되도록 하는 방법이다.

```javascript
function factorial(n, sum = 1) {
    if (n <= 1) {
        return s
    }
    // 별도의 계산 없이 재귀 함수에서 모든 연산을 처리한다.
    return factorial(n-1, n*sum)
}
```



***Copyright* © 2022 Song_Artish**