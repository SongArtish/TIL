# Queue

2020.09.02

---

[TOC]

---



## Queue

> 삽입과 삭제의 위치가 제한적인 자료구조이며, 큐 뒤(rear)에서는 삽입만 하고, 큐의 앞(front)에서는 삭제만 이루어지는 구조(`FIFO`). `버퍼(buffer)`에 활용된다.
>
> - 기본연산: 삽입(`enQueue(item)`), 삭제(`deQueue()`)
> - 주요연산: 큐생성(`createQueue()`), 공백 검사(`isEmpty()`), 포화 검사(`isFull()`), front의 원소 반환(`Qpekk()`)

```python
# Python을 통한 구현
Q = []

Q.append(item)
Q.pop(0)
```



**선형큐**

- 초기 공백 상태: `front = rear = -1`

```python
# C style

# Queue 생성
Q = [0] * 100
front = rear = -1	# front와 rear는 -1로 초기화

# 삽입 함수
def enQueue(item):
    global rear
    if rear == len(Q) - 1:
        return "Queue Full"
    else:
        rear += 1
        Q[rear] = item

# 삭제 함수 - 실제로 삭제하는 것은 아니다
def deQueue():
    global front
    if front == rear:	# 공백 검사
        return "Queue Empty"
    else:
        front += 1
        return Q[front]

# 첫 번쨰(front) 항목 탐색
def Qpeek():
    if front == rear:
        return "Queue Empty"
    else:
        return Q[front + 1]

# 공백검사
def isEmpty():
    return front == rear
# 포화검사
def Full():
    return rear == len(Q) - 1
```

- 이와 같이 선형큐를 사용하게 되면 `삭제 함수`를 실행해도, 앞의 항목이 그대로 남아서 공간을 차지하게 된다. 따라서 원형큐를 사용한다.

**원형큐**

> 1차원 배열을 사용하되, 배열의 처음과 끝이 서로 연결되어 있는 순환 구조의 큐. 나머지 연산자 `mod`를 사용한다.
>
> - 초기 공백 상태: `front = rear = 0`
> - `front` 변수: 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 항상 비워둔다.

|        | 삽입 위치              | 삭제 위치                 |
| ------ | ---------------------- | ------------------------- |
| 선형큐 | rear += 1              | front += 1                |
| 원형큐 | rear = (rear +1) mod n | front = (front + 1) mod n |

```python
# C style
size = 4
Q = [0] * size
front = rear = 0	# front와 rear는 0으로 초기화

# 삽입
def enQueue(item):
    global rear
    if (rear+1) % size == front:    # 포화 검사
        return "Queue Full"
    else:
        rear = (rear+1) % size  # rear += 1
        Q[rear] = item

# 삭제
def deQueue():
    global front
    if front == rear:
        return "Queue Empty"
    else:
        front = (front+1) % size
        return Q[front]

# 첫 번쨰 항목 탐색
def Qpeek():
    if front == rear:
        return "Queue Empty"
    else:
        return Q[(front+1) % size]
```



## 우선순위 Queue

> 우선순위를 가진 항목들을 저장하는 큐로, 우선순위가 높은 순서대로 먼저 나가게 된다. (`선입선출 X`)
>
> - 배열을 이용하여 자료를 저장하며, 삽입 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조



## BFS:star::star:

> `Breadth First Search` 그래프(비선형구조)를 탐색하는 방법 중 하나로, 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식이다. `인접행렬`과 `인접리스트`로 표현한다.

- [`DFS`](03 Stack.md)는 `후입선출`이기 때문에 `stack`을 활용하는 반면, `BFS`는 `선입선출`이기 때문에 `queue`를 활용한다.

**인접행렬**

|      |  1   |  2   |  3   |
| :--: | :--: | :--: | :--: |
|  1   |  0   |  1   |  0   |
|  2   |  1   |  0   |  1   |
|  3   |  0   |  1   |  0   |

**인접리스트**

| 기준 |      |      |      |
| :--: | :--: | :--: | :--: |
|  1   |  2   |      |      |
|  2   |  1   |  3   |      |
|  3   |  2   |      |      |



*Copyright* © Song_Artish