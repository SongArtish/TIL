# 분할정복 & 백트래킹

2020.11.02

:star:정리 필요!!!!

---

[TOC]

---



## 1. 분할정복

### 1.1 병합 정렬(Merge Sort)

> 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
>
> - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어낸다. (top-down 방식)
> - 시간 복잡도 : O(n log n)

```python
# Merge Sort
'''
합병정렬

1. 자료를 최소단위(1개)까지 쪼갬
2. 정렬을 하면서 합침
2-1. 2를 1개의 집합(배열)이 될 때까지 반복
'''
# 합병과정
def merge(left, right):
    result = [] #정렬결과를 담을 배열
    while len(left) > 0 or len(right) > 0 : #배열에 자료가 있는동안 반복
        if len(left) > 0 and len(right) > 0 :
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:     #왼쪽 자료가 있는경우
            result.append(left.pop(0))
        elif len(right) > 0 :   #오른쪽 배열 자료가 있는경우
            result.append(right.pop(0))
    return result

#분할과정
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    left = []   #왼쪽 배열
    right =[]   #오른쪽 배열
    mid = len(arr)//2   #절반으로 자르기 위한 변수
    for i in range(len(arr)):
        if i < mid :
            left.append(arr[i])
        else:
            right.append(arr[i])

    left = merge_sort(left)    #왼쪽에 대해서 분할 -> 재귀
    right = merge_sort(right)   #오른쪽에 대해서 분할 -> 재귀
    return merge(left,right)

arr = [69,10,30,2,16,8,31,22]
arr_result = merge_sort(arr)
print(arr_result)
```



### 1.2 퀵 정렬

> 주어진 배열을 두 개로 분할하고, 각각을 정렬한다.
>
> - 작은 것은 왼편, 큰 것은 오른편에 위치시킨다.

# 소스코드 다시찾기!!!!!!!!!!!!!!!!!!!!!!!

```python
# Qucik Sort
# 피봇을 기준으로 자리를 재배치 하고 기준점을 리턴
def partition(arr, low, high):
    pivot = arr[low]    # 기준점 설정
    i = low     # i 시작점 설정
    j = high    # j 시작점 설정
    while i <= j:   # i와 j가 서로 만나기 전까지 반복
        while i <= high and arr[i] <= pivot:
            i += 1  # i를 1 늘림 => 오른쪽으로 탐색
        while j >= low and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)



arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)
```



```pseudocode
quickSort(A[], l, r)
	if l < r
		s <- partition(a, L, r)
		quickSort(A[], l, s-1)
		quickSort(A[], s+1, r)
```

- 파티션(partition)

```pseudocode
// Hoare-Partition 알고리즘

partition(A[], l, r)
	p <- A[i]	// p: 피봇 값
	i <- l, j <- r
	WHILE i < j
		WHILE i <= j and A[i] <= p : i++
		WHILE i <= j and A[j] >= p : j--
		IF i < j : swap(A[i], A[j])
		
	swap(A[l], A[j])
	RETURN j
```

```pseudocode
// Lomuto partition 알고리즘
partition(A[], p, r)	// p = left
	x <- A[r]
	i <- p-1
	
	FOR j in p -> r-1
		IF A[j] <= x
			i++, swap(A[i], A[j])
	swap(A[i+1], A[r])
	RETURN i + 1
```



### 1.3 이진 검색

> 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
>
> - 자료가 정렬된 상태여야 한다!

- 퀵 정렬, 병합 정렬
- 이진트리



## 2. 백트래킹



### 2.1 트리

> 트리(Tree)는 싸이클이 없는 무향 연결 그래프이다.



이진트리 순회

1. 전위 순회(VLR)
2. 중위 순회(LVR)
3. 후위 순회(RVL)

- 연결리스트를 이용하여 트리를 표현할 수 있다.





## 힙

> **`완전 이진 트리`**에 있는 노드 중에서 키 값이 가장 큰 노드나 키 값이 가장 작은 노드를 찾기 위해서 만든 자료구조

최대 힙(max heap)

- 키 값이 가장 큰 노드를 찾기 위한 완전 이진 트리
- 부모 노드의 키 값 > 자식 노드의 키 값

최소 힙(min heap)

- 키 값이 가장 작은 노드를 찾기 위한 완전 이진 트리
- 부모 노드의 키 값 < 자식 노드의 키 값

```python
# 최소힙
# 1차원 배열로 구현

# 삽입
def heappush(value):
    global heapcount    #마지막 위치
    heapcount += 1      #지금 들어온 원소가 저장될 위치
    heap[heapcount] = value
    cur = heapcount  # 방금 들어온 값 위치
    parent = cur // 2  # cur의 부모
    # 루트 아니고 부모노드값 > 자식노드 값 => 바꾸기
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2


# 삭제
def heappop():
    global heapcount
    retValue = heap[1]  # 루트의 값을 리턴하기위해 준비
    heap[1] = heap[heapcount]  # 루트값 <- 마지막 원소로
    heap[heapcount] = 0  # 마지막원소 지우기
    heapcount -= 1  # 힙카운트 줄이기

    parent = 1      #root부터 시작
    child = parent * 2  # 왼쪽 자식

    if child + 1 <= heapcount:  # 오른쪽 자식 존재
        if heap[child] > heap[child + 1]:
            # 오른쪽 자식 < 왼쪽자식 => 우리는 둘중에 작은 값 찾아야함
            child = child + 1  # 부모랑 비교할 자식을 오른쪽으로
    # 자식 노드가 존재하고, 부모 노드 > 자식노드 => 바꾸기
    while child <= heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child  # 부모 <- 자식으로 갱신
        child = parent * 2  # 현 부모의 자식을 찾기
        if child + 1 <= heapcount:  # 오른쪽 자식있으면 둘중 작은 값을 찾음
            if heap[child] > heap[child]:
                child = child + 1
    return retValue

temp = [7, 2, 5, 3, 4, 6]
N = len(temp)   
heapcount = 0   #마지막으로 원소가 들어간 곳
heap = [0] * (N + 1)    #heap을 위한 배열 생성
for i in range(N):
    heappush(temp[i])
for i in range(N):
    print(heappop(), end=" ")
print()

# -------------------------
# 라이브러리
import heapq

heap1 = [7, 2, 5, 3, 4, 6]
print(heap1)
heapq.heapify(heap1)
print(heap1)
heapq.heappush(heap1, 1)
print(heap1)
while heap1:
    print(heapq.heappop(heap1), end=' ')
print()
# ------------------------------
# 최대힙
heap1 = [7, 2, 5, 3, 4, 6]
heap2 = []
for i in range(len(temp)):
    heapq.heappush(heap2, (-temp[i], temp[i]))  # 우선순위, 데이터
heapq.heappush(heap2, (-1, 1))
print(heap2)
while heap2:
    print(heapq.heappop(heap2)[1], end=" ")

```





***Copyright* © Song_Artish**

