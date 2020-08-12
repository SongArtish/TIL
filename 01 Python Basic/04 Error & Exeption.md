# 에러 & 예외 처리

2020.07.27.



[TOC]



## 1. 에러(Error)

### 1) 문법 에러(Syntax Error)

> 문법 에러가 있는 프로그램은 실행되지 않는다.

- 에러 발생 시 `SyntaxError`라는 키워드와 함께 에러의 상세 내용을 보여준다.
-  `파일이름`과 `줄번호`, `^` 문자를 통해 파이썬이 코드를 읽어 들일 때(`parser`) 문제가 발생한 위치를 표현한다.
-  `parser`는 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 작은 '화살표(`^`)'를 표시한다. (통역문제)

```python
# 예시1: Invalid syntax(문법 오류)
if True:
    print('참')
else
    print('거짓')
   
SyntaxError: invalid syntax

# 예시2: EOL 오류(따옴표 오류, end of line)
print('hi)
      
SyntaxError: EOL while scanning string literal

# 예시3: EOF 오류(괄호 닫기 오류, end of file)
print('hi'
      
SyntaxError: unexpected EOF while parsing
      
# 정확한 위치를 지정하지 않을 수도 있으므로 지정된 위치 전후를 모두 확인해야한다.
if True print('참')
      
  File "<ipython-input-7-57130936c62c>", line 2
    if True print('참')
                ^
SyntaxError: invalid syntax
```



## 2. 예외(Exception)

> 실행 도중 예상하지 못한 상황(exception)을 맞이하면, 프로그램 실행을 멈춘다. (문법적으로는 타당)

```python
# 예시1: ZeroDivisionError - 0으로 나눌 경우
10 * (1/0)

ZeroDivisionError: division by zero

# 예시2: NameError - 정의되지 않은 변수를 호출할 경우
print(abc)

NameError: name 'abc' is not defined
    
# 예시3: TypeError - 자료형에 대한 타입 자체가 잘못 되었을 경우
1 + '1'

TypeError: unsupported operand type(s) for +: 'int' and 'str'

round('3.5')

TypeError: type str doesn't define __round__ method
    
# 예시4: TypeError - 함수호출 과정 중 필수 argument 누락한 경우
import random
random.sample([1, 2, 3])

TypeError: sample() missing 1 required positional argument: 'k'

# 예시5: TypeError - 함수호출 과정 중 argument 개수 초과한 경우
random.choice([1, 2, 3], 6)

TypeError: choice() takes 2 positional arguments but 3 were given
    
# 예시6: ValueError - 자료형에 대한 타입은 올바르나 값이 적절하지 않는 경우
int('3.5')	# float이기 때문에(int는 가능)

ValueError: invalid literal for int() with base 10: '3.5'

# 예시7: ValueError - 존재하지 않는 값을 찾고자 할 경우
numbers = [1, 2]
numbers.index(3)

ValueError: 3 is not in list
    
# 예시8: IndexError - 존재하지 않는 index를 조회할 경우
empty_list = []
empty_list[-1]

IndexError: list index out of range

# 예시9: KeyError - 딕셔너리에서 key가 없는 경우
songs = {'sia': 'candy cane lane'}
songs['queen']

KeyError: 'queen'
    
# 예시10: ModuleNotFoundError - 모듈을 찾을 수 없는 경우
import reque	# deque의 오타

ModuleNotFoundError: No module named 'reque'
    
# 예시11: ImportError - 모듈을 찾았으나 존재하지 않는 클래스/함수 호출한 경우
from random import sampl

ImportError: cannot import name 'sampl' from 'random' (c:\users\bulge\appdata\local\programs\python\python37\lib\random.py)
    
# 예시12: KeyboardInterrupt - ctrl+c를 통해 종료했을 경우
while True:
    continue
    
KeyboardInterrupt: 
```



## 3. 예외 처리(Exception Handling)

> `try` & `except`문을 이용하여 예외 처리를 할 수 있다.

```python
try:
    <코드 블럭 1>
except (예외):
    <코드 블럭 2>
```

### 1) 에러 메시지 처리

> `as` 키워드를 활용하여 에러 메시지를 보여줄 수도 있다.

```python
try:
    <코드 블럭 1>
except <예외> as <가변수>:
    <코드 블럭 2>
    
# 예시
try:
    empty_list = []
    print(empty_list[-1])
except IndexError as error:
    print(error)
    
list index out of range
```



### 2) 복수의 예외 처리

> 괄호가 있는 튜플로 여러 개의 예외를 지정할 수 있다.

```python
try:
    <코드 블럭 1>
except (예외1, 예외2):
    <코드 블럭 2>
    
try:
    <코드 블럭 1>
except (예외1):
    <코드 블럭 2>
except (에외2):
    <코드 브럭 3>
```

```python
# 예시1
try:
    num = input('100으로 나눌 값을 입력하시오: ')
    100/int(num)
except (ValueError, ZeroDivisionError): 
    print('무언가가 잘못 되었습니다.')
    
# 예시2
try:
    num = input('100으로 나눌 값을 입력하시오: ')
    100/int(num)
except ValueError as value:
    print(value)
except ZeroDivisionError as zero:
    print(zero)
```

- 에러가 순차적으로 수행되기 때문에, 가장 작은 범주부터 시작해야 한다.



### 3) `else`

- `try` 코드 블럭이 예외를 일으키지 않았을 때, 실행되어야 하는 코드에 사용한다.
- `else`는 `except` 코드 뒤에 와야한다.

```python
try:
    <코드 블럭 1>
except 예외:
    <코드 블럭 2>
else:
    <코드 블럭 3>
```

```python
# else 구문 예시
try:
    numbers = [1, 2, 3]
    number = numbers[2]
except IndexError:
    print('오류 발생')
else:
    print(number)
```



### 4) `finally`

> 예외의 발생 여부와 관계없이 어떤 경우에든 반드시 실행해야하는 코드에 활용한다.

```python
try:
    <코드 블럭 1>
except 예외:
    <코드 블럭 2>
finally:
    <코드 블럭 3>
```

```python
# finally 구문 예시
try:
    languages = {'python': 'good'}
    languages['java']
except KeyError as err:
    print(f'{err}는 딕셔너리에 없는 키입니다.')
finally:
    print('감사합니다')
```



## 4. 예외 발생 시키기(Exception Raising)

### 1) `raise`

> `raise`를 통해 예외를 강제로 발생시킬 수 있다.

```python
raise <에러>('메시지')
```

```python
# 예시
raise NameError('이름이 없습니다')

def my_div(num1, num2):
    try:
        num1 // num2
    except ZeroDivisionError:
        print('division by zero 오류가 발생하였습니다.')
    except TypeError:	# TypeError(string 입력)를 ValueError로 출력
       raise ValueError('숫자를 넣어주세요.')
    else:
        return num1//num2
```



### 2) `assert`

> 예외를 발생시키는 다른 방법으로, 보통 **상태를 검증하는데 사용**되며 무조건 `AsserionError`가 발생합니다. (주로 테스트코드 쓸 때 사용)

```python
assert <Boolean expression>, <에러 메시지>
```

```python
# 예시
assert type(1) == int, '문자열을 입력하였습니다.'	# 거짓일 경우 발생
```

- `raise`는 항상 예외를 발생시키는 반면, `assert`는 지정한 예외가 발생시킨다.

*Copyright* © Song_Artish