# 배열 (Array)

2020.08.03.

```python
Index

# 1차원 배열 (리스트1)
1. 알고리즘
2. 배열: 1차원 배열
3. 정렬
 1) 버블 정렬
 2) 카운팅 정렬
- 완전검색
- 탐욕 알고리즘 (Greedy Algorithm)

# 2차원 배열 (리스트2)
4. 배열: 2차원 배열
- 부분집합 생성
5. 검색 (Search)
6. 정렬
 3) 선택 정렬 (Selection Sort)
7. 셀렉션 알고리즘(Selection Algorithm)
```



# 1차원 배열



## 1. 알고리즘

> 페르시아의 수학자 알 콰리즈미(خوارزمی)의 이름에서 유래된 것으로, 어떠한 문제를 해결하기 위한 절자이다.

### 1) 알고리즘 표현 방법:  슈도코드와 순서도

> **의사코드(슈도코드, pseudocode)**는 프로그램을 작성할 때 각 모듈이 작동하는 논리를 표현하기 위한 언어이다. 특정 프로그래밍 언어의 문법에 따라 쓰인 것이 아닌, 일반적인 언어로 알고리즘을 써놓은 **코드**를 말한다. (위키백과)

```pseudocode
# 슈도코드의 예시
def CalcSum(n):
    sum <- 0
    for i in range(1, n+1):
        sum <- sum + i;
    return sum;
```

### 2) 알고리즘 성능 측정 방법: 시간 복잡도 (Time Complexity)

> 실제 걸리는 시간을 측정하는 것으로 실행되는 명령문의 개수를 계산. 작업량.

#### 빅-오(O) 표기법 (Big-Oh Notation)

> 시간 복잡도 함수 중에서 가장 큰 영향력을 주는 n에 대한 항만을 표시하며, 계수(Coefficient)는 생략한다.
>
> 예시) O(3n+2) = O(3n) = O(n). O(2n^2+10n+100)=O(n^2)

##### (1) P 복잡도(Polynomial -, 다항식)

- O(logn) - 이진탐색
- O(n) - 순차탐색
- O(nlogn) - Quick, Merge, Heap
- O(n^2 - 선택, 버블, 삽입)

##### (2) NP 복잡도(Non-deterministic Polynomial -, 지수) - 근사알고리즘 사용

- O(2^n) - 부분집합, 조합
- O(n!) - 순열



## 2. 배열(Array)

> 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조로 파이썬에서는 list를 뜻한다. 배열을 사용하면 하나의 선언을 통해 둘 이상의 변수를 선언할 수 있다.

### 1차원 배열 <u>선언</u>

- 별도의 선언 방법이 없으면 변수에 처음 값을 할당할 때 생성

```python
Arr = list()
```

### 1차원 배열 <u>접근</u>

```python
Arr[0] = 10	# 배열 Arr의 0번째 원소에 10을 저장하라
Arr[idx] = 20	# 배열 Arr의 idx번째 원소에 20을 저장하라
```



## 3. 정렬

> 2개 이상의 자료를 특정 기준에 의해 오름차순(ascending) 혹은 내림차순(descending)으로 재배열하는 것
>
> - 종류 - 버블소트, 카운팅소트, 선택소트, 퀵소트, 삽입소트, 병합소트

### 1) 버블 정렬(Bubble Sort) - O(n^2)

> 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식 (* 거품처럼 가벼운 것이 위로 올라가기 때문에 붙은 이름이라고 한다.)

```python
def bubble_sort (a):	# 정렬할 List
    for i in range(len(a)-1, 0, -1):	# 범위의 끝 위치, 비교하는 횟수는 (a의 개수-1)회
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
```

### 2) 카운팅 정렬(Counting Sort) - O(n+k)

> 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하며 ,선형 시간에 정렬하는 효율적인 알고리즘

- 정수나 정수로 표현할 수 있는 자료에 대해서만 가능! (각 항목 발생 회수를 기록하기 때문)
- 따라서 문자열은 할 수 없으며, 문자는 아스키코드로 변환하여 사용할 수 있다.
- 카운트를 위한 공간 할당을 위해 집합 내 가장 큰 정수를 알아야한다.

```python
def counting_sort(A, B, k)
# A [] -- 입력 배열(1 to k(최대값))
# B [] -- 정렬된 배열
# C [] -- 카운트 배열

# 목표 배열의 공간 할당
C= [0] * k
# 1단계 카운팅: 각 숫자의 개수 세기
for i in range(0, len(B)):
    C[A[i]] += 1
# 2단계 누적: 각 개수를 왼쪽부터 누적시키기
for i in range(1, len(C)):
    C[i] += C[i-1]
# 3단계 소트: 입력 배열의 마지막 숫자부터 위치대로 입력해 정렬하기
for i in range(len(B)-1, -1, -1):
    B[C[A[i]]-1] = A[i]
    C[A[i]] -= -1
```

#### 완전검색

> 모든 경우의 수를 나열해보고 확인하는 기법. 모든 경우의 수를 생성하고 테스트해서 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인한다.
>
> - 기본 단계에서는 주로 for문을 사용한다.
> - 완전검색(재귀) + 가지치기 = BT(Back Tracking)



### 3) 선택 정렬(Selection Sort) - O(n^2)

### 4) 퀵 정렬(Quick Sort)  - O(nlogn)

### 5) 삽입 정렬(Insertion Sort) - O(n^2)

### 6) 병합 정렬(Merge Sort) - O(nlogn)



# 2차원 배열



## 1.  배열

### 2차원 배열의 <u>접근</u>

#### 1) 배열순회

> nxm 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법

- 행 우선 순회

```python
# i 행의 좌표
# j 열의 좌표
for i in range(len(Array)):
    for j in range(len(Array[i])):
        Array[i][j]	# 필요한 연산 수행
```



- 열 우선 순회

```python
# i 행의 좌표
# j 열의 좌료

for j in range(len(Array[0])):
    for i in range(len(Array)):
        Array[i][j]	# 필요한 연산 수행
```

- 지그재그 순회

```python
# i 행의 좌표
# j 열의 좌료

for i in range(len(Array)):
    for j in range(len(Array[0])):
        Array[i][j + (m-1-2*j) * (i %2)]
        # 필요한 연산 수행
```



#### 2) 델타 탐색

> 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법. 변화량(현재위치기준). 상하좌우 탐색

```python
ary[0...n-1][0...n-1]
dx[] <- [0, 0, -1, 1]
dy[] <- [-1, 1, 0, 0]

for x in range (len(ary)):
    for y in range(len(ary[x])):
        for mode in range(4):
            testX <- x + dx[mode]
            testY <- y + dy[mode]
            test(ary[testX][testY])
```

- 단 인덱스 체크를 해줘야 한다.

### 2차원 배열의 <u>활용</u>

### 전치 행렬

```python
# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
arr = [[1,2,3],[4,5,6],[7,8,9]]	# 3*3 행렬

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```



## 2. 부분집합 합(Subset Sum) 문제

- 유한 개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분집합 중에서 그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는지를 알아내는 문제.
- 집합의 원소가 n개일 때, 공집합을 포함한 부분집합의 수는 2^n개이다.

생성

1) 각 원소가 부분집합에 포함되었는지를 loop 이용하여 확인하고 부분집합을 생성하는 방법

```python
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i					# 0번째 원소
    for j in range(2):
        bit[1] = j				# 1번쨰 원소
        for k in range(2):
            bit[2] = k			 # 2번쨰 원소
            for l in range(2):
                bit[3] = 1		 # 3번쨰 원소
                print(bit)
```



비트연산자

| 비트 연산자 | 설명                                        |
| ----------- | ------------------------------------------- |
| `&`         | 비트 단위로 `AND` 연산을 한다.              |
| `|`         | 비트 단위로 `OR` 연산을 한다.               |
| `<<`        | 피연산자의 비트 열을 왼쪽으로 이동시킨다.   |
| `>>`        | 피연산자의 비트 열을 오른쪽으로 이동시킨다. |

<<연산자 (shift)

- 1 << n: 2^n 즉, 원소가 n개일 경우의 모든 부분집합의 수를 의미한다.
  - 예를 들어, 0001에서 1 << 3을 하면, 1000. (2^3 만큼 이동)



& 연산자

i&j: i와 j의 각각의 자리가 모두 1이면 1을 리턴, 아니면 0을 리턴한다.

i & (1<<j): i의 j번째 비트가 1인지 아닌지를 리턴한다.



보다 간결하게 부분집합을 생성하는 방법

```python
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)	# n: 원소의 개수

for i in range(1<<n):	# 1<<n: 부분 집합의 개수
    for j in range(n):	# 원소의 수만큼 비트를 비교함
        if i & (i<<J):	# i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=",")
     print()
print()
```





## 검색

- 탐색 키(search key): 자료를 구별하여 인식할 수 있는 키

검색 종류

- 순차 검색(sequential search)
- 이진 검색(binary search) - 정렬이 되어 있어야 이용가능
- 해쉬(hash) - 해쉬함수를 만들어서 사용. 어떤 값을 넣으면 바로 탐색

순차 검색(Sequential Search)

: 일렬로 되어 있는 자료를 순서대로 검색하는 방법

1) 정렬되어 있지 않은 경우

- 한고자 하는 우너소의 순서에 따라 비교횟수가 결정됨
  - 시간 복잡도: O(n)

2) 정렬되어 있는 경우

: 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것 (평균 비교 횟수가 반으로 주러든다.)

시간복잡도 O(n)



이진 검색(Binary Search)

- 자료의 중앙 원소를 목표 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
- 자료가 정렬이 되어 있어야한다.
- 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행한다.

```python
def binarySearch(a, key):
    start = 0
    end = len(a)
    while start <= end:
        middle = (start+end) // 2
        if a[middle] == key:
            return True, middle
        elif a[middle] > key:
            end = middle -1
        else:
            start = middle +1
    return False, -1
```



## 정렬

1. 선택 정렬

   [정렬과정]

   1) 주어진 리스트에서 최소값을 찾는다

   2) 리스트의 맨 앞에 위치한 값과 교환한다

   3) 미정렬 리스트에서 최소값을 찾는다

   4) 리스트의 맨 앞에 위치한 값과 교환한다.

   5) 반복 후, 미정렬 원소가 하나 남은 경우 

```python
def selectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):	# min값 찾기
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]		# 순서대로 min과 swap
```



7. 셀렉션 알고리즘(Selection Algorithm)

- 정렬 알고리즘을 이용하여 자료를 정렬해서 원하는 값을 가져오는 알고리즘

```python
# k번째로 작은 원소를 찾는 알고리즘
def select(list, k):
    for i in range(0, k):
        midIndex = i
        for j in range(i+1, len(list)):
            if list[midIndex] > list[j]:
                midIndex = j
                list[i], list[midIndex] = list[midIndex], list[i]
    return list[k-1]

arr = [64, 25, 10, 22, 11]
print(select(arr, 3))

## 오류
```



*Copyright* © Song_Artish