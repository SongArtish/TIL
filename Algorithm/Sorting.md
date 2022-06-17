# Sorting Algorithm

---

[TOC]

---



## Overview

In computer science, a [sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm) is an algorithm that puts elements of a list into an order.



## Comparison



## 1. Simple sorts

### 1.1 Insertion sort

### 1.2 선택 정렬(Selection Sort)

## 2. Efficient sorts

### 2.1 Merge sort

### 2.2 Heapsort

### 2.3 Quicksort

### 2.4 Shellsort

## 3. Bubble sort and variants

### 3.1 버블 정렬(Bubble Sort)

```javascript
const bubbleSort = function (arr) {
}
```



### 3.2 Comb sort

### 3.3 Exchange sort

## 4. Distribution sorts

### 4.1 계수 정렬(Counting sort)

최대값과 입력 배열의 원소 값 개수를 누적함으로 구성한 배열의 정렬을 수행한다. 주어진 배열의 값 범위가 작은 경우 빠른 속도를 갖는 정렬 알고리즘이다.

- 시간 복잡도: O(n+k)

  k는 배열의 최대값

계수 정렬 수행 과정은 다음과 같다.

1. 배열 최대값과 Counting Array 만들기
2. Counting Array를 누적합 배열로 만들기
3. 입력 배열과 누적합 배열을 이용한 정렬 수행

```python
def counting(arr):
    m = max(K)
    # Counting Array 만들기
    C = [0] * (m + 1)
    for a in arr:
        C[a] += 1
    # 누적합 배열 만들기
    for i in range(1, m + 1):
        C[i] += C[i - 1]
    # 결과 배열 만들기
    result = [0] * len(arr)
    for a in arr:
        # 1씩 빼준다
        result[C[a] - 1] = a
        C[a] -= 1
    return result
a = [3, 1, 2, 5, 4, 6]
b = [6, 5, 4, 3, 2, 1]
c = [5, 5, 3, 3, 1, 1]
print(f'counting a:{counting(a)}, b:{counting(b)}, c:{counting(c)}')
```



### 4.2 Bucket sort

### 4.3 기수 정렬(Radix Sort)

데이터를 구성하는 기본 요소(radix)를 이용하여 정렬을 진행하는 방식으로, 낮은 자리수부터 비교하여 정렬해 간다는 것을 기본 개념으로 하는 정렬 알고리즘이다. 기수정렬은 비교 연산을 하지 않으며 정렬 속도가 빠르지만 데이터 전체 크기에 기수 테이블의 크기만한 메모리가 더 필요하다.

- 시간 복잡도: O(d(n+b))

  d는 정렬할 숫자의 자릿수, b는 10

- 장점:문자열, 정수 정렬 가능

- 단점: 자릿수가 없는 것은 정렬할 수 없음(부동 소수점). 중간 결과를 저장할 bucket 공간이 필요함.

기수 정렬 수행 과정은 다음과 같다.

1. 1의 자리 숫자를 0부터 9까지 숫자별로 나눈다.
2. 10의 자리 숫자를 0부터 9까지 숫자별로 나눈다.
3. 100의 자리 숫자를 0부터 9까지 숫자별로 나눈다.
4. ... (최대값의 자릿수까지 진행)

```javascript
// num의 i번째 자릿수를 구하는 함수
function getDigit(num, i) {
  return Math.floor(Math.abs(num) / Math.pow(10, i) % 10)
}

function radixSort(arr) {
  let posArr = []
  let negArr = []
  arr.forEach((el) => {
    if (el >= 0) posArr.push(el)
    else negArr.push(el)
  })

  // 양수 계산
  let maxNum = Math.max(...posArr)
  let maxDigit = String(maxNum).length

  for (let i = 0; i < maxDigit; i++) {
    let buckets = Array.from({ length: 10 }, () => [])
    for (let j = 0; j < posArr.length; j++) {
      let digit = getDigit(posArr[j], i)
      buckets[digit].push(posArr[j])
    }
    posArr = [].concat(...buckets)
  }

  // 음수 계산
  let minNum = Math.min(...negArr)
  let minDigit = String(minNum).length-1

  for (let i = 0; i < minDigit; i++) {
    let buckets = Array.from({ length: 10 }, () => [])
    for (let j = 0; j < negArr.length; j++) {
      let digit = getDigit(negArr[j], i)
      buckets[digit].push(negArr[j])
    }
    negArr = [].concat(...buckets)
  }
  negArr.reverse()
  // 합치기
  return negArr.concat(...posArr)
}
```



***Copyright* © 2022 Song_Artish**