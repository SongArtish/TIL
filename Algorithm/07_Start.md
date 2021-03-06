# Start

2020.10.23

---

[TOC]

---



**SW 문제 해결 역량**

> 프로그램을 하기 위한 많은 제약 조건과 요구사항을 이해하고 최선의 방법을 찾아내는 능력

**문제 해결 과정**

1. 문제를 읽고 이해한다.
2. 문제를 익숙한 용어로 재정의한다.
3. 어떻게 해결할지 계획을 세운다.
4. 계획을 검증한다.
5. 프로그램으로 구현한다.
6. 어떻게 풀었는지 돌아보고, 개선할 방법이 있는지 찾아본다.



## 1. 복잡도 분석

> - `공간적 효율성` : 연산량 대비 얼마나 적은 메모리 공간을 요하는 가를 지칭
> - `시간적 효율성` : 연산량 대비 얼마나 적은 시간을 요하는 가를 지칭

점근적 표기 (Asymptotic Notation)

**O(Big-Oh) - 표기**

> 복잡도의 점근적 상한

```markdown
실행시간이 ~에 비례!
```

**Ω(Big-Omega) - 표기**

> 복잡도의 점근적 하한

```markdown
최소한 이만한 시간은 걸린다.
```

**θ(Big-Theta) - 표기**

```markdown
_과 동일한 증가율을 가진다!
```



**자주 사용하는 O - 표기**

|   기호   |      의미       |                  |
| :------: | :-------------: | :--------------: |
|   O(1)   |    상수 시간    |  Constant time   |
| O(logn)  | 로그(대수) 시간 | Logarithmic time |
|   O(n)   |    선형 시간    |   Linear time    |
| O(nlogn) | 로그 선형 시간  | Log-linear time  |
|  O(n^2)  |    제곱 시간    |  Quadratic time  |
|  O(n^3)  |   세제곱 시간   |    Cubic time    |
|  O(2^n)  |    지수 시간    | Exponential time |



## 2. 표준 입출력 방법

> Python3의 표준입출력 방벙을 다룬다.

**입력**

**`input()`**

- Raw 값의 입력. 받은 입력값을 문자열로 취급한다.

**`eval(input())`**

- Evaluated된 값 입력. 받은 입력값을 평가된 데이터 형으로 취급한다.



**출력**

**`print()`**

- 표준 출력 함수. 출력값의 마지막에 개행 문자 포함

**`print('text', end= ' ')`**

- 출력 시 마지막에 개행문자 제외할 시

**`print('%d' % number)`**

- Formatting된 출력

```python
import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

text = input()
print(text)
```



## 3. 비트 연산

### 3.1 비트 연산자

| 연산자 |                       기능                       |     예시     |
| :----: | :----------------------------------------------: | :----------: |
|  `&`   |                     AND 연산                     | num1 & num2  |
|  `|`   |                     OR 연산                      | num1 \| num2 |
|  `^`   |           XOR 연산 (같으면 0 다르면 1)           | num1 ^ num2  |
|  `~`   | 단항 연산자로 피연산자의 모든 비트를 반전시킨다. |     ~num     |
|  `<<`  |    피연산자의 비트 열을 왼쪽으로 이동시킨다.     |   num << 2   |
|  `>>`  |   피연산자의 비트 열을 오른쪽으로 이동시킨다.    |   num >> 2   |



### 3.2 활용

**`1 << n`**

- `2^n`의 값을 갖는다.

- 원소가 n개일 경우의 모든 부분집합의 수(`Power set`)를 의미한다.

- 예시

  ```python
  0001 << 0	# 0001 = 1
  0001 << 1	# 0010 = 2
  0001 << 2	# 0100 = 4
  0001 << 3	# 1000 = 8
  ```

  

**`i & (1 << j)`**

- 계산 결과는 i의 j번째 비트가 1인지 아닌지를 의미한다.

```python
# 부분 집합의 합 구하기
a = [1, 2, 3]
n = 3
for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=' ')
        print()
```

```markdown
1. i=0일 때
0 & (1<<0) = 0000 & 0001 => 0000 => 0
0 & (1<<1) = 0000 & 0010 => 0000 => 0
0 & (1<<2) = 0000 & 0100  => 0000 => 0

2. i=1일 때
1 & (1<<0) = 0001 & 0001 => 0001 => 1
1 & (1<<1) = 0001 & 0010 => 0000 => 0
1 & (1<<2) = 0001 & 0100 => 0000 => 0

3. i=2일 때
2 & (1<<0) = 0010 & 0001 => 0000 => 0
2 & (1<<1) = 0010 & 0010 => 0010 => 1
2 & (1<<2) = 0010 & 0100 => 0000 => 0

...
```



### 3.3 엔디안

> Endianness. 컴퓨터의 메모리와 같은 1차원 공간에 여러 개의 연속된 대상을 배열하는 방법을 의미하며 HW 아키텍처마다 다르다.

- 빅 엔디안(Big-endian) : 보통 큰 단위가 앞에 나옴. 네트워크.
- 리틀 엔디안(Little-endian) : 작은 단위가 앞에 나옴. 대다수 데스크탑 컴퓨터

|    종류     | 0x1234의 표현 | 0x12345678의 표현 |
| :---------: | :-----------: | :---------------: |
|  빅 엔디안  |     12 34     |    12 34 56 78    |
| 리틀 엔디안 |     34 12     |    78 56 34 12    |

- 엔디안 확인 코드

```python
n = 0x00111111
if n & 0xff:
    print("little endian")
else:
    print("big endian")
```





## 4. 진수

- 2진수, 8진수, 10진수, 16진수

**10진수 -> 타 진수로 변환**

> 원하는 타진법의 수로 나눈 뒤 나머지를 거꾸로 읽는다.
>
> 예제) (149)10 = (10010101)2 = (225)8 = (95)16

**타 진수 - 10진수로 변환**

> 예) (135.12)8 = `1*8^2 + 3*8^1 +5*8^0 + 1*8^-1 + 2*8^-2` = (93.15625)10



컴퓨터에서의 음의 정수 표현 방법

- 1의 보수 : 부호와 절대값으로 표현된 값을 부호 비트를 제외한 나머지 비트들을 0은 1로, 1은 0로 변환한다.
  - -6 : 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 : 부호와 절대값 표현
  - -6 : 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 : 1의 보수표현
- 2의 보수 : 1의 보수방법으로 표현된 값의 최하위 비트에 1을 더한다.
  - -6 : 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 : 2의 보수표현



## 5. 실수

**실수의 표현**

- 컴퓨터는 실수를 표현하기 위해 부동 소수점(floating-point) 표기법을 사용한다.

- 부동 소수점 표기 방법은 소수점의 위치를 고정시켜 표현하는 방식이다.

  - 소수점의 위치를 왼쪽의 가장 유효한 숫자 다음으로 고정시키고 밑수의 지수승으로 표현

    ```markdown
    1001.0011 = 1.0010011 * 2^3
    ```

**실수를 저장하기 위한 형식**

- 단정도 실수(32비트)

- 배정도 실수(64비트)

  ```markdown
  단정도 실수
  부호 1비트 + 지수 8비트 + 가수 23비트
  배정도 실수
  부호 1비트 + 지수 11비트 + 가수 52비트
  ```

  - 가수부(mantissa) : 실수의 유효 자릿수들을 부호화된 고정 소수점으로 표현한 것
  - 지수부(exponent) : 실제 소수점의 위치를 지수 승으로 표현한 것





*Copyright* © Song_Artish