# 함수 (Function)

```python
Index

1. 함수의 정의
 1.1 함수의 선언
 1.2 함수의 출력(output)
 1.3 함수의 입력(input)
2. 함수의 인자(argument)
 2.1 위치 인자(Positional -)
 2.2 기본 인자 값(Default Argument Values)
 2.3 키워드 인자(Keyword -)
 2.4 가변 인자(Arbitrary -)
3. 함수와 스코프(scope)
 3.1 이름 검색 규칙
 3.2 변수의 수명주기
4. 재귀함수
```



## 1. 함수(function)의 정의

> 특정한 기능(function)을 하는 코드의 묶음. 가독성, 재사용성, 유지보수가 편리하다.

![function description](https://user-images.githubusercontent.com/18046097/61181742-2984fd80-a665-11e9-9d5c-c90e8c64953e.png)


### 1.1 함수의 선언

```python
def <함수이름>(parameter1, parameter2):
    <코드 블럭>
    return value
```

- 함수는 동작후에 `return` 값이 없으면, `None`을 반환한다.

```python
# 입력 받을 수를 세제곱하여 반환(return)하는 함수 cube() 예시
	# 2 ** 3`# pow(2, 3)
def cube(num):
    # num이라는 이름의 parameter 정의
    cubed = num ** 3
    # 임시 변수 cubed 사용
    return cubed
```

![function example](https://dl.dropbox.com/s/o6v9c0vxpdww1lm/function-argument.png)

### 1.2 함수의 Output

함수의 `return`

> 함수의 반환되는 값으로, 오직 <u>한 개</u>의 객체만 반한된다.

### 1.3 함수의 Input

매개변수(parameter) & 인자(argument)

```python
def func(x):	# x는 매개변수(parameter)
    retunr x + 4
func(2)	# 2는 (전달)인자(argument)
```

## 2. 함수의 인자

> 함수는 입력값(input)으로 `인자(arguement)`를 넘겨줄 수 있다.

### 2.1 위치 인자 (Positional Arguments)

> 함수는 기본적으로 인자를 위치로 판단한다.

```python
# 예시: 원기둥의 부피
def cylinder(r, h):
    volume = 3.14 * (r ** 2) * h
    return volume
print(cylinder(5,2))
print(cylinder(2,5))
```

### 2.2 기본 인자 값 (Default Argument Values)

> 함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있으며, 호출시 인자가 없으면 기본 인자 값이 활용된다. (단, 기본 인자값을 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수는 없다.)

```python
def func(p1=va):
    return p1

# 예시: 기본 인자 값 활용
def greeting(name = '익명'):
    return f'{name}. 안녕?'
```

### 2.3 키워드 인자 (Keyword Arguments)

> 키워드 인자는 직접 변수의 이름으로 특정 인자를 전달할 수 있다.

```python
# 예시
def greet (age, name = '익명'):
    return f'{age}세 {name}님 환영합니다.'
>greet('홍길동', 20)	# 오류
>greet(name = '홍길동', age = 20)
```

### 2.4 가변 인자

#### 참고: print() 함수 

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

| argument |        option         |                    detail                     |
| :------: | :-------------------: | :-------------------------------------------: |
| *objects |                       | `*`은 개수가 정해지지 않은 임의의 인자를 받음 |
|   sep    |    `' '`(default)     |                                               |
|   end    |    `\n` (default)     |                                               |
|   file   | sys.stdout (default)  |   `write(string)` 메서드를 가진 객체여야 함   |
|  flush   | False (default), True |                                               |

- 인자가 아무것도 주어지지 않을 시, end만 사용. ex) print() => 한줄 띄우기

#### 2.4.1 가변(임의) 인자 리스트(Arbitrary Argument Lists)

> `print()`처럼 개수가 정해지지 않은 임의의 인자를 받기 위해서는 가변 인자 리스트 `*args`를 활용한다. 가변 인자 리스트는 `tuple` 형태로 처리가 되며, 매개변수에 `*`로 표현한다.

```python
def func(a, b, *args)
```

> `*args`: 임의의 개수의 위치인자를 받음을 의미 (보통 매개변수 목록의 마지막에 위치)

```python
# args 예시: max 함수 만들기
import sys

def my_max(*args):		   # args 이외 naming 가능하지만, 통상적으로 args를 사용
    value = -sys.maxsize    # 시스템의 최대값을 출력; args[0]도 가능
    for i in args:
        if value <= i:
            value = i
    return value
```

#### 2.4.2 가변(임의) 키워드 인자(Arbitrary Keyword Arguments)

> 정해지지 않은 키워드 인자들은 `dict` 형태로 처리가 되며, `**`로 표현한다. 보통 `kwargs`라는 이름을 사용하며, `**kwargs`를 통해 인자를 받아 처리할 수 있다.

```python
def func(**kwargs) :
```

> `kwargs` : 임의의 개수의 키워드 인자를 받음을 의미

```python
# kwargs 예시: 딕셔너리 만들기
def my_dict(**kwargs):
    return kwargs
my_dict(한국어 = '안녕', 영어 = 'hello')
```



## 3. 함수와 스코프(scope)

> 함수는 코드 내부에 공간(scope)을 생성하며 이를 `지역 스코프(local scope)`라고 한다.
>
> - 전역 스코프(`global scope`): 코드 어디에서든 참조할 수 있는 공간
> - 지역 스코프(`local scope`): 함수를 만든 스코프로 함수 내부에서만 참조할 수 있는 공간
> - 전역 변수(`global variable`): 전역 스코프에 정의된 변수
> - 지역 변수(`local variable`): 로컬 스코프에 정의된 변수

### 3.1 이름 검색(resolution) 규칙

> 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있다. 이것을 `LEGB Rule`이라고 부르며, 아래와 같은 순서로 이름을 찾아간다. (좁은 곳-> 넓은 곳, cf. 중2병 히키코모리 동생)
>
> - Local scope: 정의된 함수
> - Enclosed scope: 상위 함수
> - Global scope: 함수 밖의 변수 혹은 import된 모듈
> - Built-in scope: 파이썬 안에 내장되어 있는 함수 또는 속성

```python
# 예시1: print(내장함수)를 식별자로 사용한 경우
print = 'ssafy'
print(3)
del print
print(3)

# 예시2: 로컬 함수를 전역 함수로 변경
global_num = 3
def local_scope():
    global global_num    # global로 재 정의 후 값 입력
    global_num = 5
    return f'global_num이 {global_num}으로 설정되었습니다.'

print(local_scope())
print('global_num:', global_num)
# 하지만 이러한 방식은 좋지 않다!
```

### 3.2 변수의 수명주기(lifecycle)

> 변수의 이름은 각자의 `수명주기(lifecycle)`가 있다.
>
> - 빌트인 스코프(`built-in scope`) : 파이썬이 실행된 이후부터 영원히 유지
> - 전역 스코프(`global scope`) : 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 인터프리터가 끝날 때까지 유지
> - 지역(함수) 스코프(`local scope`) : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유치 (함수 내에서 처리되지 않는 예외를 일으킬 때 삭제된다.)



## 4. 재귀 함수(recursive function)

> 재귀 함수는 함수 내부에서 자기 자신을 호출하는 함수이며, 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 사용하는 것이 좋다. 재귀 호출은 `변수 사용`을 줄여줄 수 있다.
>
> - 장점: 코드가 더 직관적이고 이해하기 쉽다.
> - 단점: 함수가 호출될 때마다 메모리 공간에 쌓이기 때문에, 메모리 스택이 넘치거나 프로그램 실행 속도가 늘어진다.

```python
def recursive(n):
    if 종료조건:
        return
    else:
        return recursive(n-1)
```

### 4.1 팩토리얼 계산

```python
# 반복문 이용
def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        return result
    
# 재귀 이용
def factorial(n):
    if n <= 0:
        return 0
    if n == 1:		# 재귀함수는 종료조건이 필요 (base case)
        return n
    else:
        return n * factorial(n-1)
```

- 파이썬에서는 최대 재귀 깊이(maximun recursion depth)가 1,000으로 정해져 있다.

### 4.2 피보나치 수열

```python
# 재귀 이용
def fib(n):
   if n <= 1:
    	return n
    else:
        return fib(n-1) + fib(n-2)
    
# 반복문 이용
def fib_loop(n):
    list= []
    for i in range(0, n):	# 1. 피보나치 수열의 리스트를 작성
        if i < 2:
            list.appned(1)	# .append[x] : 특정 list 끝에 x라는 요소를 추가하는 함수
        else:
            list.append(list[i-1] + list[i-2])
     return list[n-1]	# 2. 피보나치 수열 리스트에서 가장 마지막 값을 return
```

*Copyright* © Song_Artish