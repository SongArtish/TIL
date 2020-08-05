# OOP (Object Oriented Programming) I

2020.07.29.

> 객체 지향 프로그래밍 (object가 중심이 되는 프로그래밍)
>
>  컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것.

```
<Index>
1. 객체(Object)
2. 클래스(Class)
```

```python
<정리>
# 객체(Object)
- 객체는 자신 고유의 속성(attribute)을 가지며 클래스에서 정의한 행위(behaviour)를 수행할 수 있다.
# 클래스(Class)
- 공통된 속성(attribute)과 행위(behavior)를 정의한 것으로 객체지향 프로그램의 기본적인 사용자 정의 데이터형(user_defined data type)
# 인스턴스(Instance)
- 특정 class 로부터 생성된 해당 클래스의 예시(instance)
# 속성(Attribute)
- 클래스/인스턴스가 가지는 속성(값/데이터)
# 메서드(Method)
- 클래스/인스턴스에 적용 가능한 조작법(method) & 클래스/인스턴스가 할 수 있는 행위(함수)
```



## 1. 객체(Object)

> Python에서 모든 것이 객체이며, 모든 객체는 **타입(type), 속성(attribute), 조작법(method)**을 가진다.

- 타입(type): 어떤 연산자(operator)와 조작(method)이 가능한가?
- 속성(attribute): 어떤 상태(데이터)를 가지는가?
- 조작법(method): 어떤 행위(함수)를 할 수 있는가?

### 1) 타입(Type)

> 공통된 속성(attribute)과 조작법(method)을 가진 객체들의 분류

| type   | instance                 |
| ------ | ------------------------ |
| `int`  | `0`, `1`, `2`            |
| `str`  | `''`, `hello`, `123`     |
| `list` | `[]`, `['a', 'b']`       |
| `dict` | `{}`, `{'key': 'value'}` |

#### 인스턴스(Instance)

> 특정 타입(type)의 실제 데이터 에시(instance)이다. 파이썬에서 모든 것은 객체이고, 모득 객체는 특정 타입의 인스턴스이다.

```python
# 예시
a = int(10)
b = int(20)

type(a) == int
isinstance(a, int)
# a, b는 객체
# a, b 는 int 타입(type)의 인스턴스

```



### 2) 속성(Attribute)

> 객체의 상태/데이터

```python
<객체>.<속성>

# 예시 - complex 타입 인스턴스가 가진 속성
3+4j.real
```

### 3)  메서드(Method)

> 특정 객체에 적용할 수 있는 행위(behavior)

```python
<객체>.<조작법>()

# 예시 - list 타입 인스턴스에 적용 가능한 조작법
[3, 2, 1].sort()
dir(list)	# 기타 조작법 확인하기
```

| type      | attributes      | methods                                |
| --------- | --------------- | -------------------------------------- |
| `complex` | `.real`,`.imag` |                                        |
| `str`     | _               | `.capitalize()`, `.join()`, `.split()` |
| `list`    | _               | `.append()`, `.reverse()`, `.sort()`   |
| `dict`    | _               | `.keys()`, `.values()`, `.items()`     |



## 2. 객체 지향 프로그래밍(Object-Oriented Programming)

### 절차 중심 vs. Object 중심

>프로그래밍 패러다임: 어떻게 프로그램을 정돈(organize)할 것인가?

### Object 중심의 장점

- 코드의 **직관성**
- 활용의 **용이성**
- 변경의 **유연성**



## 3. 클래스(Class)와 객체(Object)

> `type`: 공통 속성을 가진 객체들의 분류(class)
>
> `class`: 객체들의 분류(class)를 정의할 때 쓰이는 키워드

### 1) 클래스(Class) 생성

```python
class <클래스이름>:
    <메소드>
    
# 이유
공통적인 속서과 메서드를 정의하기 위해서~!!!!!
```

- `<클래스이름>`은 `PascalCase`(첫 단어를 대문자로 시작하는 표기법 ex. ArtBook)로 정의
- 클래스 내부에는 데이터와 함수를 정의할 수 있고, 이때 정의된 함수는 **메서드(method)**로 불린다.

### 2) 인스턴스(Instance) 생성

```python
# 예시
person1 = Person()
```

```python
# 예시 - __doc__ 출력
class Person:
    """
    이것은 Person 클래스(class)입니다.
    """
person1 = Person()
print(person1.__doc__)    # 설명을 출력하기 위해서 사용하는 메서드
```

### 3) 메서드(Method)

> 특정 데이터 타입(또는 클래스)의 객체에 공통적으로 적용 가능한 행위(behavior)들을 의미한다.

```python
# 메서드 예시
class Person:
    # 메서드(method)
    def talk(self):
        return '안녕'
    def eat(self, food="(먹을거줘)"):
        return f'{food} 냠냠'
```

#### (1) 생성자(constructor) 메서드

> 인스턴스 객체가 생성될 때 호출되는 함수

```python
def __init__(self):
    <코드블럭>
```

- 인스턴스가 생성될 때 인스턴스의 속성을 정의할 수 있다.

#### (2) 소멸자(destructor) 메서드

> 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 함수

```python
def __del__(self):
    <코드블럭>
```

### 4) 속성 정의

> 특정 데이터 타입(또는 클래스)의 객체들이 가지게 될 상태/데이터를 의미

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        return f'안녕, 나는{self.name}'
```

### 5) 매직메서드

> 더블언더스코어(`__`)가 있는 메서드 (스페셜 메서드)

```python
__new__
__reduce__
__reduce_ex__
__repr__
__rmod__
__rmul__
__setattr__
__sizeof__
__str__(self)	# 특정 객체를 출력(print())할 때 보여줄 내용 정의

# dir() 함수를 통한 특정 객체의 메서드 확인
dir('')
```

### 6) `self`: 인스턴스 자신(self)

> Python에서 메서드는 **호출 시 첫번째 인자로 인스턴스 자신이 전달**ㄷ되게 설계되었으며, 보통 매개변수명으로 `self`를 첫번째 인자로 설정(다른 이름도 가능)

*Copyright* © Song_Artish