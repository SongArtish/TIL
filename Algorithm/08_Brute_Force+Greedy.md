# Brute Force & Greedy

2020.10.28

> 완전 검색 & 그리디

---

[TOC]

---



## 1. 반복과 재귀

> 반복과 재귀는 유사한 작업을 수행할 수 있다.
>
> **"입력 값 n이 커질수록 재귀 알고리즘은 반복에 비해 비효율적일 수 있다."**

### 1.1 반복 (Iteration)

수행하는 작업이 완료될 때까지 계속 반복

- 루프 (for, while 구조)

```markdown
## 반복구조
- 초기화
- 조건검사 (check control expression)
- 반복할 명령문 실행 (action)
- 업데이트 (loop update)
```

```python
# 반복을 이용한 선택정렬
def SelectionSort(A):
    n = len(A)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if A[j] < A[min]:
                min = j
        A[min], A[i] = A[i], A[min]
```



### 1.2 재귀 (Recursion)

주어진 무제의 해를 구하기 위해 동일하면서 더 작은 문제의 해를 이용하는 방법

- 기본 부분(basis part)과 유도 부분(inductive part)로 구성된다.

```python
# 팩토리얼 재귀 함수
def fact(n):
    if n <= 1:	# Basis part
        return 1
    else:	# Inductive part
        return n * fact(n-1)
```



### 1.3 반복과 재귀

|                   |              **재귀**               |       **반복**        |
| :---------------: | :---------------------------------: | :-------------------: |
|     **종료**      | 재귀 함수 호출이 종료되는 base case |   반복문의 종료조건   |
|   **수행 시간**   |            (상대적) 느림            |         빠름          |
|  **메모리 공간**  |         (상대적) 많이 사용          |       적게 사용       |
| **소스코드 길이** |              짧고 간결              |         길다          |
| **소스코드 형태** |       선택 구조 (if... else)        | 반복 구조(for, while) |
|  **무한반복 시**  |           stack overflow            |  CPU를 반복해서 점유  |

- 예시) 2^k 연산에 대한 재귀와 반복

```python
# 재귀 Recursion
def Power_of_2(k):
    if k == 0:
        return 1
    else:
        return 2 * Power_of_2(k-1)

# 반복 Iteration
def Power_of_2(k):
    i = 0
    power = 1
    while i < k:
        power = power * 2
        i += 1
    return power
```



## 2. 완전검색기법

> Brute Force는 문제를 해결하기 위한 간단하고 쉬운 접근법이다.
>
> **"우선 완전 검색으로 접근하여 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직하다."**



## 3. 조합적 문제

> 다수의 알고리즘 문제들은 순서화된 요소들의 집합에서 최선의 방법을 찾는 것과 관련 있다. (ex. TSP)

### 3.1 순열

```python
# 순열 1
def perm(n, k): # n 숫자를 결정할 인덱스, k 순열의 길이
    if n == k:
        print(A)
    else:
        for i in range(n, k):
            A[n], A[i] = A[i], A[n]
            perm(n+1, k)
            A[n], A[i] = A[i], A[n]

A = [1, 2, 3]
perm(0, 3)
```

```python
# 순열 2
def perm(n, k, m):	# n : 숫자를 결정할 자리 idx, k = 순열 길이, m = 주어진 숫자의 개수
    if n == k:
        print(A[0:k])
    else:
        for i in range(n, m):   # n번과 바꿀 위치
            A[n], A[i] = A[i], A[n]
            perm(n+1, k, m)
            A[n], A[i] = A[i], A[n]

A = [1, 2, 3, 4, 5]
perm(0, 3, 5)

```

```python
# 순열 3
def perm(n, k, m):
    if n == k:
        print(p)
    else:
        for i in range(m):
            if u[i] == 0:
                u[i] = 1
                p[n] = A[i]
                perm(n+1, k, m)
                u[i] = 0

A = [1, 2, 3, 4, 5]
p = [0] * 3
u = [0] * 5
perm(0, 3, 5)
```



### 3. 2부분집합

> 집합에 포함된 원소들을 선택하는 것이다.

**바이너리 카운팅**(Binary Counting)

- 원소 수에 해당하는 N개의 비트열을 이용한다.
- n번째 비트값이 1이면 n번째 원소가 포함되었음을 의미한다.

```python
# 바이너리 카운팅

arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(0, (1<<n)):	# 1<<n : 부분집합의 개수
    for j in range(0, n):	# 원소의 수만을 비트를 비교함
        if i & (1<<j):  # i의 j번째 비트가 1이면 j번째 원소 출력
            print('%d'%arr[j], end= ' ')
    print()
```



### 3.3 조합

> 서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것을 조합(combination)이라고 부른다.

```python
# 조합

# n: c[n] 조합의 인덱스, s: 선택구간의 시작, N: 주어진 개수, r: 고를 개수
def f(n, s, N, r):
    if n == r:
        print(c)
    else:
        for i in range(s, N-r+n+1):
            c[n] = i
            f(n+1, i+1, N, r)

N = 10
r = 3
c = [0] * 3
f(0, 0, N, r)
```



## 4. 탐욕 알고리즘



***Copyright* © Song_Artish**

