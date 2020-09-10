# Tree

2020.09.09

---

[TOC]

---



## :point_right: 자료구조



1) 단순구조

① 정수, 실수, 문자, 문자열 등의 기본 자료형

 

2) 선형구조

① 자료들 간의 앞뒤 관계가 **1:1**의 선형관계

② 리스트, 연결리스트, 스택, 큐, 덱 등

 

3) 비선형구조

① 자료들 간의 앞뒤 관계가 **1:n**, 또는 **n:n** 의 관계

② 트리, 그래프 등

 

4) 파일구조

① 레코드의 집합인 파일에 대한 구조

② 순차파일, 색인파일, 직접파일 등



| 자료 구조 | 관계 |            표현방법            |             순회             |
| :-------: | :--: | :----------------------------: | :--------------------------: |
| 선형구조  | 1:1  |              list              |            for문             |
| 이진트리  | 1:N  |     1차원 배열, 연결리스트     | 전위순회, 중위순회, 후위순회 |
|  그래프   | N:N  | 인접행렬, 인접리스트, 간선배열 |    DFS(stack), BFS(queue)    |



## 트리

> 1:N 관계를 가지는 비선형 구조의 계층형 자료구조

**용어**

- 노드(node) - 트리의 원소
- 간선(edge) - 노드를 연결하는 선(부모 노드 - 자식 노드)
- 루트 노드(root node) - 트리의 시작 노드
- 형제 노드(sibling node) - 같은 부모 노드의 자식 노드들
- 조상 노드 - 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
- 서브 트리(subtree) - 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손 노드 - 서브 트리에 있는 하위 레벨의 노드들
- 차수(degree)
  - 노드의 차수 : 노드에 연결된 자식 노드의 수
  - 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값
  - 단말 노드(리프 노드) : 차수가 0 인 노드. 자식 노드가 없는 노드
- 높이 
  - 노드의 높이 : 루트에서 노드에 이르는 간선의 수. 노드의 레벨
  - 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값. 최대 레벨.



## 이진 트리

> 모든 노드들이 최대 2개의 서브트리를 갖는 특별한 형태의 트리
>
> - 높이가 h인 이진 트리가 가질 수 있는 노드의 개수
>   `최소 = (h + 1)`, `최대 = (2 ^ (h+1) - 1)`

### 종류

#### 포화 이진 트리 (Full Binary Tree)

- 모든 레벨에 노드가 포화상태로 차 있는 이진 트리

#### 완전 이진 트리 (Complete Binary Tree) :ballot_box_with_check:

- 노드 수가 n개 일 때, 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리
- `heap`의 조건!!

#### 편향 이진 트리 (Skewed Binary Tree)

- 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리 (왼쪽 편향, 오른쪽 편향)



### 순회

> V(루트)의 순회 순서에 따라 순회의 종류를 구분한다.
>
> - 부모의 노드가 `i`일 때, 왼쪽 자식의 노드는 `2i` 오른쪽 자식의 노드는 `2i + 1`이다.
> - 자식의 노드가 `i`일 때, 부모의 노드는 `i // 2`이다.



#### 전위순회(preorder traversal) : **VLR**

1. 현재 노드 n을 방문하여 처리한다. (V)
2. 현재 노드 n의 왼쪽 서브트리로 이동한다. (L)
3. 현재 노드 n의 오른쪽 서브트리로 이동한다. (R)

```python
def preorder(idx):
    if idx <= last_idx:
        # 현재노드 방문
        print(tree[idx], end = ' ')
        # 왼쪽
        preorder(2*idx)
        # 오른쪽
        preorder(2*idx + 1)
        
preorder(1)
```



#### 중위순회(inorder traversal) : **LVR**

1. 현재 노드 n의 왼쪽 서브트리로 이동한다. (L)
2. 현재 노드 n을 방문하여 처리한다. (V)
3. 현재 노드 n의 오른쪽 서브트리로 이동한다. (R)

```python
def inorder(idx):
    if idx <= last_idx:
        inorder(2*idx)
        print(tree[idx], end= " ")
        inorder(2*idx + 1)
        
inorder(1)
```



#### 후위순회(postorder traversal) : **LRV** :ballot_box_with_check:

1. 현재 노드 n의 왼쪽 서브트리로 이동한다. (L)
2. 현재 노드 n의 오른쪽 서브트리로 이동한다. (R)
3. 현재 노드 n을 방문하여 처리한다. (V)

```python
# 후위순회 - LRV
def postorder(idx):
    if idx <= last_idx:
        postorder(2*idx)
        postorder(2*idx + 1)
        print(tree[idx], end=' ')
        
postorder(1)
```



![](img/traversal.jfif)



### 표현

#### 배열

- 메모리 공간 낭비 및 비효율적!

![배열 구현](img/array.jfif)

```python
# 트리 공백검사
def is_empty():
    return last_idx == 0

# 트리 포화검사
def is_full():
    return last_idx == size

# 원소 추가
def add(n):
    global last_idx
    if is_full():
        print("TREE IS FULL")
        return
    last_idx += 1
    tree[last_idx] = n

#-----------------------------------------------------

size = 15   # 배열의 크기
tree = [0] * (size+1)   # 배열 초기화 (0은 사용X)

last_idx = 0 # 마지막에 들어온 원소가 위치할 인덱스

# 원소 넣기 : A, B, C, D, ...
for i in range(0, 10):
    # 원소 넣기
    add(chr(i+65))
# print(tree)

# 그냥 내가 작성
i = len(tree) -1
while not tree[i]:
    tree.pop()
    i -= 1
print(tree)
```



#### **연결리스트** :star:

- 자기참조구조체

![연결리스트 구현](img/linked_list.jfif)



### [참고] 수식 트리

> 수식을 표현하는 이진 트리. **연산자**는 `루트 노드` or `가지 노드`이며, **피연산자**는 모두 `잎 노드`
>
> - <u>중위 순회로 간다!</u>

- 중위 순회 : A / B * C * D + E (식의 중위 표기법)
- 후위 순회 : A B / C * D * E + (식의 후위 표기법)
- 전위 순회 : + * * / A B C D E (식의 전위 표기법)



## 이진탐색트리 (BST)

- 모든 원소는 서로 다른 유일한 키를 가진다
- :star:`key(왼쪽) < key(루트) < key(오른쪽)`



**탐색연산**

- 탐색할 키 값 x를 루트 노드의 키 값과 비교
- 서브트리에 대해서 순환적으로 탐색 연산을 반복

**삽입연산**

- 먼저 탐색 연산 수행
- 탐색 실패한 위치에 원소를 삽입

**삭제연산**

- 루트와 가장 마지막 원소 자리 변경 (루트 값은 삭제)
- 변경한 root 값부터 탐색 연산 수행



## 힙 (Heap)

> 완전 이진 트리에 있는 노드 중에서 키값이 가장 큰 노드나 키값이 가장 작은 노드 찾기 위해서 만든 자료구조

**최대 힙(max heap)**

- 키값이 가장 큰 노드를 찾기 위한 **완전 이진 트리**
- `부모노드 key` > `자식노드 key`

**최소 힙(min heap)**

- 키값이 가장 작은 노드를 찾기 위한 **완전 이진 트리**
- `부모노드 key` < `자식노드 key`



**연산** - `삽입`, `삭제`

- 힙에서는 루트 노드의 원소만을 삭제할 수 있다.

```python
# 최소힙 구현하기

# 삽입 연산
def heapPush(value):
    global heapcount	# index 번호
    heapcount += 1
    heap[heapcount] = value
    cur = heapcount
    parent = cur//2
	
    # 반복
    # 루트가 아니고, if 부모노드값 > 자식노드값 이면 swap!
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2

# 삭제 연산
def heappop():
    global heapcount
    retValue = heap[1]
    heap[1] =heap[heapcount]	# 첫번째 원소를 삭제 후 마지막 원소를 넣기
    heap[heapcount] = 0
    heapcount -= 1

    parent = 1
    child = parent * 2

    if child + 1 <= heapcount:  # 오른쪽 자식 존재
        if heap[child] > heap[child + 1]:
            child += 1
    # 반복
    # 자식노드가 존재하고, 부모노드 > 자식노드 이면 SWAP
    while child < heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heapcount:  # 오른쪽 자식 존재
            if heap[child] > heap[child + 1]:
                child += 1

    return retValue

# 최소힙
heapcount = 0   # index 번호
temp = [7, 2, 5, 3, 4, 6]
N = len(temp)
heap = [0] * (N + 1)
for i in range(N):
    heapPush(temp[i])

for i in range(N):
    print(heappop(), end = " ")
print()


####################################
2 3 4 7 5 6
```



**라이브러리 이용 `heapq`**

- `heapq` 라이브러리는 <u>최소힙</u>만 지원한다.
- `heapq.heappop(힙)`은 가장 작은 원소를 삭제 후에 그 값을 리턴하는데, 이것을 이용해 최대힙을 구한다.

---

:heavy_check_mark:`heappush(heap, item)`

- 힙 불변성을 유지하면서, item 값을 heap으로 푸시한다.

:heavy_check_mark:`heappop(heap)`

- 힙 불변성을 유지하면서, heap에서 가장 작은 항목을 팝하고 반환한다.
- 힙이 비어 있으면, `IndexError`가 발생한다.

:heavy_check_mark:`heappushpop(heap, item)`

- 힙에 item을 푸시한 다음, heap에서 가장 작은 항목을 팝하고 반환한다.

:heavy_check_mark:`heapify(x)`

- 리스트 x를 선형 시간으로 제자리에서 힙으로 변환한다.

등등

자세한건 [공식문서](https://python.flowdas.com/library/heapq.html) 참조!

---

```python
import heapq

# heapq.heapify(힙)
heap = [7, 2, 5, 3, 4, 6]
heapq.heapify(heap)
print(heap)

# heapq.heappush(힙, 값)
heapq.heappush(heap, 1)	# 1을 더한다.
print(heap)

# heapq.heappop(힙)
while heap:
    print(heapq.heappop(heap), end = " ")
print()	
      
##########################################
[2, 3, 5, 7, 4, 6]
[1, 3, 2, 7, 4, 6, 5]
1 2 3 4 5 6 7 
      
# 최대힙 구하기      
temp = [7, 2, 5, 3, 4, 6]
heap2 = []
for i in range(len(temp)):
    heapq.heappush(heap2, (-temp[i], temp[i]))
heapq.heappush(heap2, (-1, 1))	# 1을 더한다.
# print(heap2)
while heap2:
    print(heapq.heappop(heap2)[1], end=' ')

###########################################
7 6 5 4 3 2 1
```



*Copyright* © Song_Artish