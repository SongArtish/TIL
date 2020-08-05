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
  - 셀렉션 알고리즘(Selection Algorithm)
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

|    알고리즘     | 평균 수행시간 | 최악 수행시간 | 알고리즘 기법 |                   비고                    |
| :-------------: | :-----------: | :-----------: | :-----------: | :---------------------------------------: |
|  **버블** 정렬  |    O(n^2)     |    O(n^2)     |  비교와 교환  |             코딩이 가장 쉽다.             |
| **카운팅** 정렬 |    O(n+k)     |    O(n+k)     |  비교환 방식  |         n이 비교적 작을 때만 가능         |
|  **선택** 정렬  |    O(n^2)     |    O(n^2)     |  비교와 교환  | 교환횟수가 <br />버블, 삽입정렬보다 작다. |
|   **퀵** 정렬   |  O(n log n)   |    O(n^2)     |   분할 정복   |          평균적으로 가장 빠르다.          |
|  **삽입** 정렬  |    O(n^2)     |    O(n^2)     |  비교와 교환  |         n의 개수가 작을 때 효과적         |
|  **병합** 정렬  |  O(n log n)   |  O(n log n)   |   분할 정복   |       연결리스트의 경우 가장 효율적       |



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

### 3) 선택 정렬(Selection Sort) - O(n^2)

### 4) 퀵 정렬(Quick Sort)  - O(nlogn)

### 5) 삽입 정렬(Insertion Sort) - O(n^2)

### 6) 병합 정렬(Merge Sort) - O(nlogn)



#### 완전검색

> 모든 경우의 수를 나열해보고 확인하는 기법. 모든 경우의 수를 생성하고 테스트해서 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인한다.
>
> - 기본 단계에서는 주로 for문을 사용한다.
> - 완전검색(재귀) + 가지치기 = BT(Back Tracking)



# 2차원 배열



## 4.  배열

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
for j in range(len(Array[i])):
    for i in range(len(Array)):
        Array[i][j]	# 필요한 연산 수행
```

- 지그재그 순회

```python
# i 행의 좌표
# j 열의 좌료
for i in range(len(Array)):		    # len(Array) = n-1
    for j in range(len(Array[i])):	# len(Array[i]) = m-1, 왜 m-1인 것이지?
        Array[i][j + (m-1-2*j) * (i %2)]	
        # 필요한 연산 수행
        
        # 홀수 행은 정방향, 짝수 행은 역방향 (i=0부터 시작)
        # i = 홀수, Array[i][j]
        # i = 짝수, Array[i][len(Array[i])-j]		전체 길이에서 j만큼 빼준다.
```

#### 2) 델타 탐색

> 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법. 변화량(현재위치기준). 상하좌우 탐색

```python
arr[0...n-1][0...n-1]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for x in range (len(arr)):
    for y in range(len(arr[x])):
        for z in range(4):
            testX = x + dx[z]
            testY = y + dy[z]
            # +1 혹은 -1로 벗어나는 index 체크
            if testX < 0 or testX >= len(arr) or testY < 0 or testY >= len(arr[i]):
                continue
            print(ary[testX][testY])
```

### 2차원 배열의 <u>활용</u>

### 1) 전치 행렬

```python
# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
arr = [[1,2,3],[4,5,6],[7,8,9]]	# 3*3 행렬

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```

### 2) 부분집합

집합의 원소가 n개일 때, 공집합을 포함한 부분집합의 수는 2^n개이다.

#### (1) loop(순환) 이용

```python
# 예시
def printlist(arr, bit):
    for i in range(len(bit)):
        if bit[i]:	# bit의 i번째 요소가 True(1)이면
            print(arr[i], end = " ")
    print()

arr = [1, 2, 3, 4]
bit = [0] * len(arr)
for i in range(2):
    bit[0] = i					# 0번째 원소
    for j in range(2):
        bit[1] = j				# 1번쨰 원소
        for k in range(2):
            bit[2] = k			 # 2번쨰 원소
            for l in range(2):
                bit[3] = l		 # 3번쨰 원소
                # print(bit)	# bit 요소 0,1의 모든 경우의 수 출력
                printlist(arr, bit)	# 그곳에 arr의 요소 씌우기
```

- 4중 for문 및 일일이 작성해야한다는 복잡성과 번거로움의 문제가 있다.

#### (2) 비트연산자 활용

| 비트 연산자 | 설명                                        |
| ----------- | ------------------------------------------- |
| `&`         | 비트 단위로 `AND` 연산을 한다.              |
| `|`         | 비트 단위로 `OR` 연산을 한다.               |
| `<<`        | 피연산자의 비트 열을 왼쪽으로 이동시킨다.   |
| `>>`        | 피연산자의 비트 열을 오른쪽으로 이동시킨다. |

- **`<<`(shift)** 연산자
  - 예시)  `1 << 3`을 하면, 0001 => 1000. ( 2^3 만큼 이동. 즉, 1을 2^3으로 변환)
  - 활용) `1 << n` ( = `2^n`)  : 원소가 n개일 경우의 모든 부분집합의 수를 의미

- **`&`** 연산자
  - 정의) `i & j`: i와 j의 각각의 자리가 모두 1이면 1을 리턴, 아니면 0을 리턴한다.
  - 활용) `i & (1<<j)`: i의 j번째 비트가 1인지 아닌지를 리턴한다. (1<<j는 j번째 자리 이외의 자리는 모두 0이기 떄문이다.)

```python
# 부분집합 활용 예시
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)	# n: 원소의 개수

for i in range(1<<n):	# 부분 집합의 개수(1<<n, 2^n)만큼 시행
    # 0~n까지 생성해서 후에 비트연산자를 활용해 2^n개의 비트(즉, 부분집합)를 생성
    for j in range(n):	# 원소의 수만큼 비트를 비교함 (원소 수만큼 반복문 돌림)
        if i & (1<<j):	# i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=",")
    print()
print()

# i=0(처음)에는 공백 후 줄바꾸기를 출력한다.
```



## 5. 검색

> 탐색 키(search key): 자료를 구별하여 인식할 수 있는 키
>
> [검색 종류]
>
> 1. **순차 검색**(sequential search)
> 2. **이진 검색**(binary search) - 정렬 필수 !
> 3. **해쉬**(hash) - 해쉬함수를 만들어서 사용. 어떤 값을 넣으면 바로 탐색

### 1) 순차 검색(Sequential Search)

>  일렬로 되어 있는 자료를 순서대로 검색하는 방법

( i ) 정렬되어 있지 않은 경우

- 찾고자 하는 원소의 순서에 따라 비교횟수가 결정된다. (시간복잡도 O(n))

```python
def seq_search(arr, length, key):	# length = len(arr)
    i = 0   # index
    while i < length and arr[i] != key:
        i += 1
    if i < length:
        return i
    else:
        return -1   # 없을 경우 -1을 반환
```

( ii ) 정렬되어 있는 경우

- 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것을 의미한다.
-  평균 비교 횟수가 ( i )에 비해 절반으로 줄어든다. (시간복잡도 O(n))

```python
def seq_search_sorted(arr, length, key):	# length = len(arr)
    i = 0   # index
    while i < length and arr[i] < key:
        i += 1
    if i < length and arr[i] == key:
        return i
    else:
        return -1   # 없을 경우 -1을 반환
```

### 2) 이진 검색(Binary Search)

- 자료의 중앙 원소를 목표 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
- 자료가 정렬이 되어 있어야하며, 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행한다.

```python
def binarySearch(arr, key):
    start = 0	# 첫 index
    end = len(arr)	# 마지막 index
    # start와 end를 줄여나가는 방식
    while start <= end:
        middle = (start+end) // 2
        if arr[middle] == key:
            return True, middle	# middle은 index 값
        elif arr[middle] > key:
            end = middle -1
        else:	# arr[middle] < key:
            start = middle +1
    return False, -1
```



## 6. 정렬

### 3) 선택 정렬(Selection Sort) - O(n^2)

```python
def selectionSort(arr):
    for i in range(0, len(arr)-1):	# 마지막 앞 요소까지 체크하면 정렬은 끝나기 때문!!
        min = i
        for j in range(i+1, len(arr)):	# min값 찾기
            if arr[min] > arr[j]:
                min = j				   # min값의 인덱스로 치환
        arr[i], arr[min] = arr[min], arr[i]		# 순서대로 min과 swap
# 순서대로 리스트의 맨 앞의 값과, 뒤쪽에서 찾은 min의 값을 swap한다.
```

### 셀렉션 알고리즘(Selection Algorithm)

- 정렬 알고리즘을 이용하여 자료를 정렬해서 원하는 값을 가져오는 알고리즘

```python
# k번째로 작은 원소를 찾는 알고리즘
def selectionAlg(arr, k):
    for i in range(len(arr) -1):
        min = i # min 값의 index
        for j in range(i+1, len(arr)):  # 시작하는 i의 다음 index부터 비교
            if arr[min] > arr[j]:
                min = j
            arr[i], arr[min] = arr[min], arr[i] # 선택 정렬을 통해서 오름차순으로 정렬
    return arr[k-1]

# 달팽이 문제
```

*Copyright* © Song_Artish