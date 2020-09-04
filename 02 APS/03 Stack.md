# Stack

2020.08.26

---

[TOC]

---



**표**

|   층    |        의미        |
| :-----: | :----------------: |
| `code`  |                    |
| `data`  | 정적변수(전역변수) |
| `heap`  |      동적할당      |
| `stack` |      지역변수      |



ADT(Abstract Data Type, 추상자료형)에는 `stack`, `queue`가 있다.



## Stack의 개념

> 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조로, 저장된 자료는 선형 구조(자료 간 1대1 관계)이며, 후입선출된다.
>
> - 자료구조 : `list`

### Stack의 연산

**`push` - 저장소에 자료를 저장**

```python
# push
def push(item):
    global stack
    stack.append(item)
```

**`pop` - 저장소에서 자료를 꺼낸다**

```python
# pop
def pop():
    if len(stack) == 0:		# isEmpty
        return
    else:
        return stack.pop()
```

- `.pop(i)`는 i 위치에 있는 값을 삭제하고 반환 (i가 없으면 마지막 항목 삭제)

`isEmpty` - stack이 공백인지 아닌지 확인

`peek` - 스택의 top에 있는 item을 반환

### 스택의 응용1 : 괄호검사

```
괄호의 종류 : 대괄호 `[]`, 중괄호 `{}`, 소괄호 `()`
```

> **아이디어**
> 좌괄호를 만나면 `push`, 우괄호를 만나면 `pop`을 하여, 중간에 비어있거나 모두 돌았는데 남았다면 짝이 안 맞는 것이다. 

```python
# 괄호 검사
def check(arr):
    for i in range(len(arr)):
        if arr[i] == '(':   # 왼쪽 괄호면 push
            stack.append(arr[i])
        elif arr[i] == ')':   # 오른쪽 괄호면 pop하고 비교
            # isEmpty
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    # 남아있으면
    if stack : return False
    else : return True
```



### 스택의 응용2 : Function Call

> (함수호출) 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조이므로, 스택을 이용하여 수행 순서 관리

**<참고> 재귀함수**

자기 자신을 호출하여 순환 수행되는 함수 (간결)

```python
# 재귀함수의 기본구조
def recursive(input):
    if <기본파트>:
        <코드블럭>
    else <유도파트>:
        <재귀함수>
```

- (예시: 팩토리얼, 피보나치 수열) 하지만 피보나치 수를 구하는 함수를 재귀함수로 구현한 알고리즘은 *엄청난 중복 호출이 존재한다*.



## DP(동적계획법)

> `Dynamic Programming`은 알고리즘은 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘



### Memoization

> 동적계획법(DP)의 핵심이 되는 기술로, 프로그램을 실행 시 이전에 계산한 값을 메모리에 저장해서 실행속도를 빠르게 한다.

```python
# 피보나치 수열 memoization
def fibo(n):
    if n >= 2 and len(memo) <= 2:
        memo.append(fibo(n-1)+fibo(n-2))
    return memo[n]

memo = [0, 1]   # 참조형(RW) - global
memo2 = 0   # value형(R) - global X
print(fibo(5))
```

- 필요한 `fibo` 함수를 먼저 다 구해놓고, 각 함수값을 찾으므로 실행시간이 `O(n)`으로 줄어든다.



### DP

> 먼저 <u>입력 크기가 작은 부분 문제들을 모두 해결한 후</u>에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결, 최종적으로 원래 주어진 입력 문제를 해결하는 알고리즘
>
> - `memoization`이 recursive 방식이며, `DP`는 iterative 방식 

```python
# 피보나치 수 DP 적용 알고리즘
def fibo(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]
```

- 0부터 n까지 각각 자리의 수를 list에 차례대로 저장해서 list의 n번째 요소를 반환한다.



## DFS​(​깊이우선탐색):star:

> 비선형구조인 <u>그래프</u> 구조(tree)는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요하며, 이러한 경우 `깊이우선탐색(Depth First Search)`을 사용한다.

|    구조    |              표현              |   순회   |
| :--------: | :----------------------------: | :------: |
|  선형구조  |              배열              |   for    |
| 비선형구조 | 인접행렬, 인접리스트, 간선배열 | DFS, BFS |

- 두가지 방법
  - **깊이 우선 탐색 (Depth First Search, DFS)** >> 재귀, stack
  - **[너비 우선 탐색 (Breadth First Search, BFS)](04 Queue.md)** >> queue

- 재귀는 코드가 더 간단하여 많이 사용되며, stack은 반복을 사용하여 속도가 더 빠르다.



:raised_hand_with_fingers_splayed:**그래프**

> 그래프는 `N:N` 관계 자료구조로, 그래프 G는 (V, E)의 집합이다.

- `정점(Vertex)` - 아이템

- `간선(Edge)` - 각 정점 간의 관계(연결)

- `인접` - 정점 간 이어져 있으면, 즉 (v1, v2)라는 간선이 있으면 이 정점들을 인접한다라고 한다.

- 그래프의 표현

  - 인접 행렬: `N*N`  크기의 행렬로, (v1, v2)라는 간선이 있다면 행렬 (v1, v2) = 1, 아니면 0으로 표현한다. 
  - 인접리스트, 간선배열
  - 그래프 종류에 따라 `무방향 그래프(대칭 정렬)`, `방향 그래프`로 표현된다.

  

```python
# DFS 재귀적 구조

def dfs(v):	# v는 시작위치, 이후 현재 정점
    # 방문체크
    visited[v] = 1
    print(v, end = " ")		# 현재 정점위치를 출력
    # v에 인접합 정점 중 방문 안한 정점을 재귀호출
    for w in range(1, N+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

# 정점 개수, 간선 개수
N, E = map(int, input().split())
# 간선 정보
temp = list(map(int, input().split()))
# 인접행렬
G = [[0] * (N+1) for _ in range(N+1)]
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s][e] = 1
    G[e][s] = 1
# 방문배열(1차원)
visited = [0] * (N+1)

dfs(1)
```

```python
# DFS 반복적 구조
    while (top >= 0):   #스택이 비어있지 않는 동안 반복
        n = stack.pop(top)  #스택에서 하나 꺼내오기
        top-=1
        print(n,end=' ')
        for i in range(1, V+1):
            # n에 인접하고 아직 방문하지 않은 정점 i라면
            if adj[n][i] == 1 and visited[i] == 0:
                top += 1
                stack[top] = i
                visited[i] = 1  #방문여부 체크
```



## 계산기

> 문자열로 된 계산식이 주어질 때, 스택을 이용하여 해당 계산식의 값을 구하는 것.
>
> - `중위표기법(Infix Notation)` - 연산자를 피연산자의 가운데 표기하는 방법 (A+B)
> - `후위표기법(Postfix Notation)` - 연산자를 피연산자 뒤에 표기하는 방법 (AB+)

**방법**

1. 중위 표기법의 수식을 **후위 표기법**으로 변경(스택 이용)

```
# 예시

A*B-C/D
1단계 ((A*B)-(C/D))
2단계 ((A B)*(C D)/)-
3단계 AB*CD/-
```

```python
# in-coming priority
    icp = {'*': 2, ',': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    # in-stack priority
    isp = {'*': 2, ',': 2, '/': 2, '+': 1, '-': 1, '(': 3}
```

```
# pseudocode
if (icp > isp)	push()
else pop()
```

- 피연산자는 바로 출력하며, 연산자(괄호 포함)들을 stack에 저장한다.
-  `)`(닫는 괄호)가 나오면 `(`(여는 괄호)가 나올때까지 stack의 항목을 출력한다.

2. 후위 표기법의 수식을 **스택을 이용하여 계산**한다.

- 피연산자는 stack에 저장하고, 연산자를 만나면 필요한 만큼 출력한다.



## 백트래킹:star:

> 해를 찾는 도중에 해가 아니면 되돌아가서 다시 해를 찾아 가는 기법으로, 최적화(optimization) 문제와 결정(decision) 문제를 해결할 수 있으며, 어떤 노드의 유망성을 점검한 후에 유망하지 않다고 결정되면 그 노드의 부모로 되돌아가 다음 자식 노드로 간다(가지치기).
>
> - 완전검색(재귀) + 가지치기
> - **활용**: 미로 찾기, n-Queen 문제, Map coloring, 부분 집합의 합(Subset Sum) 문제 등

**방법**

1. 상태 공간 트리의 **깊이 우선 검색**을 실시한다.
2. 각 노드가 유망한지를 점검한다.
3. 만일 그 노드가 유망하지 않으면 ,그 노드의 부모 노드로 돌아가서 검색을 계속한다.



### 부분집합:raised_hand_with_fingers_splayed:

```python
# 재귀 호출을 이용한 부분집합 생성 알고리즘

arr = [1, 2, 3]
N = len(arr)
A = [0] * N  # 해당 원소의 포함여부를 저장 (0, 1)

def powerset(n, k):	# n: 원소의 갯수, k: 현재 depth
    # print(A, end=" : ")
    if n == k:	# Basis Part
        for i in range(n):
            if A[i]:
                print(arr[i], end=" ")
        print()
    else:	# Inductive Part
        # k번째 요소 선택
        A[k] = 1
        powerset(n, k+1)	# 다음 요소 포함 여부 결정
        # k번째 요소 비선택
        A[k] = 0
        powerset(n, k+1)	# 다음 요소 포함 여부 결정

powerset(N, 0)
```



### 순열:raised_hand_with_fingers_splayed:

```python
# swap을 이용한 순열 생성
def perm(n, k):
    if k == n:
        print(arr)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            # 원래대로 제자리로 되돌려놓아야 한다.
            arr[k], arr[i] = arr[i], arr[k]

arr = [1, 2, 3]
N = len(arr)
perm(N, 0)  # 원하는 depth, 현재 depth
```

```python
# 방문행렬을 이용한 순열 생성
def perm(k):
    if k == N:
        print(select)
    for i in range(N):
        if not visited[i]:
            select[k] = arr[i]
            visited[i] = 1
            perm(k+1)
            visited[i] = 0

arr = [1, 2, 3]
N = len(arr)
select = [0] * N    # 생성할 순열을 저장할 배열
visited = [0] * N
perm(0)
```



*Copyright* © Song_Artish