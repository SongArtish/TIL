# 함수 (Function) I

```한국어
# function vs method

<function>
print()
sum()

<method> - 특정 객체에서만 작동하는 함수
dictionary = {}
dictiopnary.get()
```

## 1. 함수(function)?

> 특정한 기능(function)을 하는 코드의 묶음

- 함수를 쓰는 이유 - 가독성, 재사용성, 유지보수

### 1) 함수의 선언과 호출

```python
def <함수이름>(parameter1, parameter2):
    <코드 블럭>
    return value
```

- 함수는 `매개변수(parameter)`를 넘겨줄 수도 있다.
- 함수는 동작후에 `return`을 통해 결과값을 전달 할 수도 있다. (`return` 값이 없으면, `None`을 반환한다.)

```python
# 입력 받을 수를 세제곱하여 반환(return)하는 함수 cube() 예시
	# 2 ** 3`# pow(2, 3)
def cube(num):
    # num이라는 이름의 parameter 정의
    cubed = num ** 3
    # 임시 변수 cubed 사용
    return cubed
```

![function description](https://user-images.githubusercontent.com/18046097/61181742-2984fd80-a665-11e9-9d5c-c90e8c64953e.png)

![function example](https://dl.dropbox.com/s/o6v9c0vxpdww1lm/function-argument.png)



## 2. 함수의 Output

함수의 `return`

> 함수의 반환되는 값으로, 오직 한 개의 객체만 반한된다.



## 3. 함수의 Input

매개변수(parameter) & 인자(argument)

```python
def func(x):
    retunr x + 4
func(2)
```

- `x`는 매개변수(parameter)
- `2`는 (전달)인자(arguement)

함수의 인자

> 함수는 입력값(input)으로 `인자(arguement)`를 넘겨줄 수 있다.

### 1) 위치 인자 (Positional Arguments)

> 함수는 기본적으로 인자를 위치로 판단한다.

```python
# 예시: 원기둥의 부피
def cylinder(r, h):
    volume = 3.14 * (r ** 2) * h
    return volume
print(cylinder(5,2))
print(cylinder(2,5))
```

### 2) 기본 인자 값 (Default Argument Values)

> 함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있으며, 호출시 인자가 없으면 기본 인자 값이 활용된다. (단, 기본 인자값을 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수는 없다.)

```python
def func(p1=va):
    return p1

# 예시: 기본 인자 값 활용
def greeting(name = '익명'):
    return f'{name}. 안녕?'
```

### 3) 키워드 인자 (Keyword Arguments)

> 키워드 인자는 직접 변수의 이름으로 특정 인자를 전달할 수 있다.

```python
# 예시
def greet (age, name = '익명'):
    return f'{age}세 {name}님 환영합니다.'
>greet('홍길동', 20)	# 오류
>greet(name = '홍길동', age = 20)
```

### 4) 정해지지 않은 여러 개의 인자 처리

![](https://user-images.githubusercontent.com/18046097/61181751-2b4ec100-a665-11e9-9a7c-a19a8c445cfa.png)

- print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

#### (1) 가변(임의) 인자 리스트(Arbitrary Argument Lists)

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

#### 2) 가변(임의) 키워드 인자(Arbitrary Keyword Arguments)

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

*Copyright* © Song_Artish