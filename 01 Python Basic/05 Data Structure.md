#  데이터 구조(Data Structure) 

2020.07.28.

> 데이터에 편리하게 접근하고, 변경하기 위해서 데이터를 저장하거나 조작하는 방법
>
> - Program = Data Structure + Algorithm (Niklaus Wirth)

```python
Index

# 1부 순서가 있는(ordered) 데이터 구조
1. 문자열(String)
2. 리스트(List)

# 2부 순서가 없는(unordered) 데이터 구조
3. 세트(Set)
4. 딕셔너리(Dictionary)

# 부록
5. iterable 데이터 구조에 적용 가능한 Built-in Function - map(), filter()
```



[TOC]



## 1. 문자열(String)

> **immutable, ordered, iterable**

### 1) 조회/탐색

> `.find(x)`, `.index(x)`

```python
.find(x)
# x의 첫 번째 위치를 반환한다. 없으면 "-1"을 반환한다.
```

```python
.index(x)
# x의 첫 번째 위치를 반환한다. 없으면 "오류"가 발생한다.
```

### 2) 값 변경

> `.replace(old, new, [count])`, `.strip([chars])`, `.split([chars])`, `.join(iterable)`

```python
.replace(old, new, [count])
# 바꿀 대상 글자를 새로운 글자로 바꿔서 반환 (count를 지정하면 해당 갯수만큼만 시행)
```

```python
.strip()		# 공백제거. 양쪽 제거
.strip([chars])	 # 특정 문자 제거
.lstrip()		# 왼쪽 제거
.rstip()		# 오른쪽 제거
```

```python
.split([chars])
# 문자열을 특정한 단위로 나누어 리스트로 반환

# 예시
'a_b_c'.split('_')

['a', 'b', 'c']
```

```python
'separator'.join(iterable)
# iterable 컨테이너 요소들을 separator를 구분자로 합쳐(join) 문자열로 반환

# 예시
word = '배고파'
words = ['안녕', 'hello']
'!'.join(word)
' '.join(words)

'배!고!파'
'안녕 hello'
```

### 3) 문자 변형

> `.capitalize()`, `.title()`, `.upper()`, `.lower()`, `.swapcase()`

```python
.capitalize()
# 앞글자를 대문자로 만들어 반환

.title()
# 어포스트로피나 공백 이후를 대문자로 만들어 반환

.upper()
# 모두 대문자로 만들어 반환
```

```python
.lower()
# 모두 소문자로 만들어 반환

.swapcase()
# 대/소문자로 변경하여 반환
```

### 4) 문자열 참/거짓 검증 method 

```python
.isalpha()		# 문자열이 문자인지
.isdecimal()
.isdigit()		# 문자열이 숫자인지
.isnumeric()
.isspace()
.isupper()
.istitle()
.islower()
```

```python
# 문자열 method 확인 - 참/거짓 반환
dir('string')
```



## 2. 리스트(List)

> mutable, ordered, iterable

### 1) 값 추가 및 삭제

> `.append(x)`, `.extend([iterable])`, `.insert(i, x)`, `.remove(x)`, `.pop(i)`, `.clear()`

```python
.append(x)
# 리스트에 값 추가
```

```python
.extend(iterable)
# 리스트에 iterable(list, range, tuple, string[주의]) 값을 붙일 수가 있다.
```

- append는 끝에 <u>오브젝트</u>를 추가하는 반면, extend는 iterable에서 <u>요소</u>를 추가하여 목록을 확장한다.
- append는 item을 받아서 기존의 리스트에 추가하는 반면, extend는 iterable을 받아서 기존의 리스트를 확장한다.

```python
# 예시: 차이점 확인
cafe = ['starbucks', 'tomntoms', 'hollys']
cafe.append(['coffeenie'])	# 괄호 후 append => ['coffeenie']
cafe.extend(['twosome_place'])	# 괄호 후 extend => 'twosome_place'
cafe.extend('ediya')	# 문자열 extend => 'e', 'd', 'i', 'y', 'a'

['starbucks', 'tomntoms', 'hollys', 'banapresso', 'banapresso', 'wcafe', '빽다방', ['coffeenie'], 'twosome_place', 'e', 'd', 'i', 'y', 'a']

```

```python
.insert(i, x)
# 리스트의 정해진 위치 i에 x라는 값을 추가
```

```python
.remove(x)
# 리스트에서 값이 x인 것을 "하나" 삭제
```

- remove는 값이 없으면 오류가 발생

```python
.pop(i)
# 정해진 위치 i에 있는 값을 삭제하고 반환 (i가 지정되지 않으면 마지막 항목 삭제)
```

```python
.clear()
# 리스트의 모든 항목 삭제
```

### 2) 탐색 및 정렬

> `.index(x)`, `.count(x)`, `.sort()`, `.reverse()`

```python
.index(x)
# x 값을 찾아 해당 index 값을 반환
# 찾는 값이 없으면 ValueError을 반환
```

```python
.count(x)
# 원하는 x의 개수를 확인
```

```python
# 예시: 특정 값 모두 삭제
a = [1, 2, 1, 3, 4]
target_value = 1
for i in range(a.count(target_value)):
    a.remove(target_value)
```

```python
.sort()
# 정렬

# 예시: 역정렬
import random
lotto = random.sample(range(1, 46), 6)
lotto.sort(reverse=True)
print(lotto)
```

- 내장함수 `sorted()`와는 다르게 **원본 list를 변형**시키고 `None`을 리턴

```python
.reverse()
# 그냥 반대로 뒤집는다 (정렬 아님!!!)
```

### 3) 리스트 복사

> `[:](slice)`, `list()`, `copy.deepcopy()`

```python
# 예시: 리스트 복사
original_list = [1, 2, 3]
copy_list = original_list # reference type(데이터 컨테이너) - 이름에 "주소값"이 할당된다.
```

```python
# primitive)(원시) type - 이름에 값 자체가 할당
int
float
str
bool

# reference type - 이름에 주소가 할당
dict
list
tuple
```

#### (1) slice 연산자 사용 `[:]`

```python
# 예시
a = [1, 2, 3]
b = a[:]
```

#### (2) `list()` 활용

```python
# 예시
a = [1, 2, 3]
b = list(a)
```

- 하지만! 이렇게 하는 것도 일부 상황에만 서로 다른 `얕은 복사(shallow copy)` 이다.

```python
# shallow copy가 되는 예시 - 2차원 리스트
a = [1, 2, [1, 2]]
b = a[:]

b[2][0] = 3
print(a)
```

#### (3) `deep copy`

- reference type을 완전히 다른 주소로 할당하는 방법

```python
import copy
copy.deepcopy()
```

### 4) List Comprehension

> 표현식과 제어문을 통해 리스트를 생성하는 것으로 여러 줄의 코드를 한 줄로 줄일 수 있다.

```python
[식 for 변수 in iterable]

list(식 for 변수 in iterable)	# 표현식에 list 함수를 씌워 리스트 타입으로 형변환
```

```python
# 예시
cubic_list = list(number ** 3 for number in numbers)
```

- 연습할 때는, 기본문을 만들고 list comprehension으로 변환하는 과정을 꼭 거치도록 한다!!

```python
[식 for 변수 in iterable if 조건식]

[식 if 조건식 else 식 for 변수 in iterable]

# elif는 다음과 같이 if else 열거로 사용한다
[식 if 조건식 else 식 if 조건식 else 식 if ... else ... for 변수 in iterable]
```

```python
# 예시

```



## 3. 세트(Set)

> mutable, unordered, iterable

### 추가 및 삭제

> `.add(elem)`, `.update(*others)`, `.remove(elem)`, `.discard(elem)`, `.pop()`

```python
.add(elem)
# elem을 세트에 추가

.update(*others)
# 여러가지 값을 추가. 인자로는 iterable 데이터 구조 전달
# 단, dict은 키 값만 전달
```

```python
.remove(elem)
# elem을 세트에서 삭제하고, 없으면 KeyError가 발생

.discard(elem)
# elem을 세트에서 삭제하고 없어도 에러가 발생하지 않는다.
```

```python
.pop()
# 임의의 원소를 제거해 반환
```



## 4. 딕셔너리(Dictionary)

> mutable, unordered, iterable
>
> `Key : Value` 페어(pair)의 자료구조

### 1) 조회

> `.get(key)`

```python
.get(key[, default=None])
# key를 통해 value를 가져옴
```

- default는 찾는 키값이 없는 경우 KeyError가 아닌 default값을 반환한다.

```python
# 예시
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict['pineapple']
print(my_dict.get('pineapple'))
print(my_dict.get('pineapple', 0))   # default 값을 None이 아닌 0으로 반환
```

### 2) 추가 및 삭제

> `.pop(key)`, `.update()`

```python
.pop(key[, default])
# key가 딕셔너리에 있으면 제거하고 그 값을 반환
```

- default가 없는 상태에서 딕셔너리에 없으면 `KeyError` 발생

```python
.update()
# 값을 제공하는 key, value로 덮어씀

# 예시
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict.update(apple='애플')
print(my_dict)
```

### 3) 딕셔너리 순회 (`for` 반복문 활용)

```python
# 4가지 방법
for key in dict:
    print(key)
    print(dict[key])
    
for key in dict.keys():
    print(key)
    print(dict[key])
    
for val in dict.values():
    print(val)
    
for key, val in dict.items():
    print(key, val)
```

```python
# 예시
book_title =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']
# 목표
{'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}

number = {}
for key in book_title:
    number[key] = number.get(key, 0) + 1	# get의 default값을 0으로 시작
print(number)
```

### 4) Dictionary comprehension

```python
{키: 값 for 요소 in iterable}
dict({키: 값 for 요소 in iterable})

# 예시
blood_types = {'A': 40, 'B': 11, 'AB': 4, 'O': 45}
negative_blood_types = {'-' + key : blood_types[key] for key in blood_types}
print(negative_blood_types)
```

```python
{키: 값 for 요소 in iterable if 조건식}
{키: 값 if 조건식 else 값 for 요소 in iterable}
{키: 값 if 조건식 else 식 if 조건식 else 식 if ... else ... for 요소 in iterable}
```



## 5. 순회가능한(iterable) 데이터 구조에 적용가능한 Built-in Function

> iterable 타입 - `list`. `dict`, `set`, `str`, `bytes`, `tuple`, `range`

### 1) `map(function, iterable)`

- 여러 개의 데이터를 한 번에 다른 형태로 변환하기 위해서 사용

```python
# 예시
numbers = [1, 2, 3]
new_numbers = map(str, numbers)
print(list(new_numbers))
```

### 2) `filter(function, iterable)`

- iterable에서 function의 반환된 결과가 `True`인 것들만 구성하여 반환한다.
- `filter object`를 반환한다.

```python
# 예시: filter 함수로 홀수만 출력하기
def odd(n):
    return n % 2	# True (1)
numbers = [1, 2, 3]
new_numbers = list(filter(odd, numbers))
print(new_numbers)
```

### 3) `zip(*iterables)`

- 복수의 iterable 객체를 모아 인덱스가 같은 값끼리 튜플의 모음으로 구성해 `zip obejct`를 반환한다.
- 단, iterable 객체의 길이가 다를 경우, 가장 짧은 길이까지 반환한다.

```python
# 예시: zip 함수로 남녀 pair 구성하기
girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david']
teachers = ['Anne', 'Mary', 'Jason']
pair = list(zip(teachers, girls, boys))
print(pair)
```

*Copyright* © Song_Artish