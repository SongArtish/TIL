# 컨테이너 (Container)

> 여러 개의 값을 저장할 수 있는 객체

## 1. 시퀀스(Sequence)형 컨테이너

> `시퀀스`는 데이터가 순서대로 나열된(ordered) 형식을 나타내며, 특정 위치의 데이터를 가리킬 수 있다. (단, 정렬된[sorted] 것은 아니다.)

### 1) 리스트(list)

```python
[value1, value2, value3]
```

- 대괄호 `[]` 및 `list()`를 통해 만들 수 있다.
- 값에 대한 접근은 `list[i]`을 통해 한다.

```python
# 리스트 값 접근
list(2, 4, 6)
list[0]

2
```

### 2) 튜플(tuple)

```python
(value1, value2)
```

- `()`로 묶어서 표현하며 수정 불가능(불변, immutable)

```python
# swap 코드 역시 tuple 활용
x, y = y, x
print(x, y)

# 하나의 항목으로 구성된 튜플은 값 뒤에 쉼표를 붙여서 만든다
num = (1,)
print(type(num))

<class 'tuple'>
```

### 3) 레인지 (range)

> `range`는 숫자의 시퀸스를 나타내기 위해 사용된다.

- 기본형 : `range(n)`
- 범위 지정 : `range(n, m)`
- 범위 및 스텝 지정 : `range(n, m, s)

> n부터 m-1까지 +s만큼 증가한다.

### 4) 문자형(string)

### 5) 바이너리(binary)

**시퀀스에서 활용할 수 있는 연산자/함수**

|  operation   |          설명           |
| :----------: | :---------------------: |
|   x `in` s   |    containment test     |
| x `not in` s |    containment test     |
|  s1 `+` s2   |      concatenation      |
|   s `*` n    | n번만큼 반복하여 더하기 |
|    `s[i]`    |        indexing         |
|   `s[i:j]`   |         slicing         |
|  `s[i:j:k]`  |    k간격으로 slicing    |
|    len(s)    |          길이           |
|    min(s)    |         최솟값          |
|    max(s)    |         최댓값          |
|  s.count(x)  |        x의 개수         |

```python
# containment test
a = 'apple'
'a' not in a
cart = ['apple','banana']
'banana' in cart

False
True

# Concatenation (연결, 연쇄)
[1, 2] + [3, 4]

[1, 2, 3, 4]

# indexing과 slicing
location = ['서울', '대전', '대구', '부산']
location[1 :3]

['대전', '대구']
```



## 2. 비 시퀸스(Non-sequence)형 컨테이너

> 순서가 없는 (unordered) 데이터

### 1)  셋 (set)

> 순서가 없는 자료구조 (집합)

```python
{value1, value2, value3}
```



- 중괄호 `{}`를 통해 만들며, 순서가 없고 중복된 값이 없다.
- 빈 집합을 만들려면 `set()`을 사용
- `list`의 중복된 값을 손쉽게 제거 가능

### 2) 딕셔너리 (dictionary)

> `key`와 `value`가 쌍으로 이뤄져있으며, 궁극의 자료구조

```python
{Key1 : Value1, Key2 : Value2, Key3 : Value3, ...}
```

- `key`는 변경 불가능(immutable)한 데이터만 가능 (보통 거의 string)
- `value`는 `list`, `dictionary`를 포함한 모든 것이 가능

```python
# key와 value
cart = {'a' : 'apple', 'b' : 'banana', 'c' : 'carrot'}
print(cart.values())
print(cart.items())

cart.items()

# tuple 형식으로 반환
for item in cart.items():
    print(item)
    
# item을 사용하는 주된 방법
for item in cart.item():
    key, value = item
    print(key, value)
    
# 간단한 방법
for key, value in cart.item():
    print(key, value)
    
a apple
b banana
c carrot
```

<컨테이너형 형변환>

![](https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png)



## 3. 데이터의 분류

> `mutable` vs. `immutable`

1) 변경 불가능한(`immutable`) 데이터

- 단일 데이터: 숫자, 글자, 참/거짓
- `range()`, `tuple()`, `forzenset`

2) 변경 가능한(mutable) 데이터

- 컨테이너: `list`, `dict`, `set`, 사용자가 만든 데이터 타입



## 정리

![](https://user-images.githubusercontent.com/18046097/61180439-44e60d80-a651-11e9-9adc-e60fa57c2165.png)