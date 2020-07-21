# 제어문(Control Statement)

> 코드 실행의 순차적인 흐름을 제어(Control Flow)

## 1. 조건문(Conditional Statement)

> `if`문은 반드시 참/거짓을 판달할 수 있는 조건과 함께 사용 되어야한다.

### 1) `if` 조건문

```python
if <참/거짓 조건>:
    <코드 블럭>
else:
    <코드 블럭>
```

### 2) `elif` 복수 조건

> 2개 이상의 조건을 활용할 경우 `elif <조건>:`을 활용한다.

### 3) 중첩 조건문

> 다른 조건문에 중첩된 조건문

### 4) 조건 표현식(Conditional Expression)

> 조건 표현식은 일반적으로 조건에 따라 값을 정할 때 활용되며, 삼항 연사자(Ternary Operator)라고 부르기도 한다.

```python
true_value if <조건식> else false_value
```



## 2. 반복문(Loop Statement)

### 1) `while` 반복문

> `while`문은 조건식이 참(True)인 겨웅 반복적으로 코드를 실행하며, **반드시 종료조건을 설정해야 한다.**

```python
while <조건식>:
    <코드 블럭>
    
    
# 예시
a = 0
while a < 5:
    print(a)
    a = a + 1
print('끝')
```

### 2) `for`문

> `for`문은 시퀸스(String, Tuple, List, Range)나 다른 순회가능한 객체(iterable)의 요소들을 순회한다.

```python
for <임시변수> in <순회가능한데이터(iterable)>:
    <코드 블럭>
```

리스트(list) 순회에서 index 활용

​	`range()`

> 순회할 list의 길이를 활용하여 index를 조작할 수 있다.

​	`enumerate()`

> 내장 함수 중 하나로, 인덱스(index)와 값(value)을 함께 활용 할 수 있다. 열거 객체를 돌려준다. iterable은 시퀸스, 이터레이터 또는 이터레이션을 지원하는 다른 객체여야 한다. `enumerate()`에 의해 반환된 이터레이터의 `__next__()` 메서드는 카운트 (기본값 0을 갖는 start부터)와 iterable을 이터레이션 해서 얻어지는 값을 포함하는 튜플을 돌려준다.

### 3) 반복제어(break, contuinue, for-else)