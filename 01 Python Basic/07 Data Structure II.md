# 데이터 구조(Data Structure) II

2020.07.28.

```
<Index>

[순서가 없는(unordered) 데이터 구조 - 알고리즘에 빈번히 활용되는]
1. 세트(Set)
2. 딕셔너리(Dictionary)
```



## 1. 세트(Set)

> mutable, unordered, iterable

[세트(set)의 조작법(method)]

### 추가 및 삭제

```python
.add(elem)
# elem을 세트에 추가
```

```python
.update(*others)
# 여러가지 값을 추가. 인자로는 iterable 데이터 구조 전달
```

```python
.remove(elem)
# elem을 세트에서 삭제하고, 없으면 KeyError가 발생
```

```python
.discard(elem)
# elem을 세트에서 삭제하고 없어도 에러가 발생하지 않는다.
```

```python
.pop()
# 임의의 원소를 제거해 반환
```



## 딕셔너리(Dictionary)

> mutable, unordered, iterable
>
> `Key : Value` 페어(pair)의 자료구조

[딕셔너리의 조작법(method)]

### 1) 조회

```python
.get(key[, default])
# key를 통해 value를 가져옴 
```

- KeyError 발생하지 않는다. default는 기본적으로 None이다.

```python
# 예시
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict['pineapple']
print(my_dict.get('pineapple'))
print(my_dict.get('pineapple', 0))   # default 값을 None이 아닌 0으로 반환
```

### 2) 추가 및 삭제

```python
.pop(key[, default])
# key가 딕셔너리에 있으면 제거하고 그 값을 반환
```

- key가 딕셔너리에 없으면 default를 반환
- default가 없는 상태에서 딕셔너리에 없으면 `KeyError` 발생

```python
.update()
# 값을 제공하는 key, value로 덮어씀

# 예시
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict.update(apple='애플')
print(my_dict)
```

[딕셔너리 순회 (`for` 반복문 활용)]

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



### 1) Dictionary comprehension

```python
{키: 값 for 요소 in iterable}
doct({키: 값 for 요소 in iterable})

# 예시
blood_types = {'A': 40, 'B': 11, 'AB': 4, 'O': 45}
negative_blood_types = {'-' + key : blood_types[key] for key in blood_types}
print(negative_blood_types)
```

### 2) Dictionary comprehension + 조건

```python
{키: 값 for 요소 in iterable if 조건식}
{키: 값 if 조건식 else 값 for 요소 in iterable}
{키: 값 if 조건식 else 식 if 조건식 else 식 if ... else ... for 요소 in iterable}
```



*Copyright* © Song_Artish