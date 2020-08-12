# OOP (Object Oriented Programming)

2020.07.29.

> 객체 지향 프로그래밍 (object가 중심이 되는 프로그래밍)
>

```python
Index

# 1부 기본 개념
1. 객체 지향 프로그래밍(OOP)
2. 객체(Object)

# 2부 객체 생성
3. 클래스(Class)
4. 인스턴스 & 클래스 변수
5. 인스턴스 & 클래스 메서드

# 3부 객체 상속
6. 상속(Inheritance)
7. 메서드 오버라이딩(Method Overriding)
8. 다중 상속(Multiple Inheritance)
```

[TOC]


```python
<1부 정리>
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

```python
<2부 정리>
# 인스턴스와 메서드
- 인스턴스는 3가지 종류의 메서드 모두에 접근 가능

# 클래스와 메서드
- 클래스 또한 3가지 종류의 메서드 모두에 접근 가능
- 클래스 자체(cls)와 그 속성에 접근할 필요가 있다면 클래스 메서드로 정의
- 클래스와 클래스 속성에 접근할 필요가 없다면 정적 메서드로 정의

# 클래스메서드와 정적메서드
- 공통점: 인스턴스 없이 호출 가능
- 차이점: 클래스 메서드는 메서드 안에서 클래스 속성/메서드에 접근해야 할 때 사용
    	그렇지 않을 경우 정적메서드 사용
```



## 1. 객체 지향 프로그래밍 (Object-Oriented Programming)

> 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 **객체**들의 모임으로 파악하고자 하는 것. 기존의 프로그래밍 패러다임은 어떻게 프로그램을 정돈(organize)할 것인가에 대해 절차 중심적이었다면, python은 Object 중심이다.
>
> - Object 중심의 장점: 코드의 **직관성**, 활용의 **용이성**, 변경의 **유연성**



## 2. 객체(Object)

> Python에서 모든 것이 객체이며, 모든 객체는 **타입(type), 속성(attribute), 조작법(method)**을 가진다.

- 타입(type): 어떤 연산자(operator)와 조작(method)이 가능한가?
- 속성(attribute): 어떤 상태(데이터)를 가지는가?
- 조작법(method): 어떤 행위(함수)를 할 수 있는가?

### 2.1 타입(Type)

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
a = int(10)			# a는 객체
type(a) == int		# a는 int 타입
isinstance(a, int)	 # a는 int 타입(type)의 인스턴스
```

### 2.2 속성(Attribute)

> 객체의 상태/데이터

```python
<object>.<attribute>
```

```python
# 예시 - complex 타입
3+4j.real	# 복소수의 실수 부분
3+4j.imag	# 복소수의 허수 부분
```

### 2.3  메서드(Method)

> 특정 객체에 적용할 수 있는 행위(behavior)

```python
<object>.<method>()
```
```python
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



## 3. 클래스(Class)

> `type`: 공통 속성을 가진 객체들의 분류(class)
>
> `class`: 객체들의 분류(class)를 정의할 때 쓰이는 키워드

### 3.1클래스(Class) 생성

```python
class <클래스이름>:
    <메소드>
    
# 이유
공통적인 속성과 메서드를 정의하기 위해서~!!!!!
```

- `<클래스이름>`은 `PascalCase`(첫 단어를 대문자로 시작하는 표기법 ex. ArtBook)로 정의
- 클래스 내부에는 데이터와 함수를 정의할 수 있고, 이때 정의된 함수는 **메서드(method)**로 불린다.

### 3.2 인스턴스(Instance) 생성

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

### 3.3 메서드(Method)

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

#### 3.3.1 생성자(constructor) 메서드

> 인스턴스 객체가 생성될 때 호출되는 함수

```python
def __init__(self):
    <코드블럭>
```

- 인스턴스가 생성될 때 인스턴스의 속성을 정의할 수 있다.

#### 3.3.2 소멸자(destructor) 메서드

> 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 함수

```python
def __del__(self):
    <코드블럭>
```

### 3.4 속성 정의

> 특정 데이터 타입(또는 클래스)의 객체들이 가지게 될 상태/데이터를 의미

```python
class Person:
    def __init__(self, name):
        self.name = name	# 속성
    
    def talk(self):
        return f'안녕, 나는{self.name}'	# 메서드
```

### 3.5 매직메서드

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

### 3.6 `self`: 인스턴스 자신(self)

> Python에서 메서드는 **호출 시 첫번째 인자로 인스턴스 자신이 전달**되게 설계되었으며, 보통 매개변수명으로 `self`를 첫번째 인자로 설정(다른 이름도 가능)



## 4. 인스턴스 & 클래스 변수

### 4.1 인스턴스 변수

```python
class <Class명>:
    def __init__(self, name):	# 인스턴스 메서드 (생성자)
        self.name = name		# 인스턴스 변수 - 메서드 정의 시: self.변수
        
# '인스턴스.변수명'으로 접근
```

### 4.2 클래스 변수

```python
class Person:
    species = 'human'			# 클래스 변수
    
   	def info(self):
        return Person.species
    
# '클래스.변수명' 혹은 '인스턴스.변수명'으로 접근
```

### 4.3 인스턴스 & 클래스 간의 이름 공간

- 인스턴스 => 클래스 (=> 상위 클래스) 순으로 탐색한다.



## 5. 인스턴스 & 클래스 메서드

### 5.1 인스턴스 메서드(instance method)

```python
class MyClass:
    # 클래스 내부 정의되는 메서드 기본값은 인스턴스 메서드
    def instance_method(self, arg1, arg2, ...):
        [코드블럭]

my_instance = MyClass()
my_instance.instance_method(arg1, arg2)

# 호출 시, 철번째 인자로 자기자신 self 전달
MyClass.instance_method(my_instance, arg1, arg2)
```

### 5.2 클래스 메서드(class method)

- `@classmethod`와 `cls`를 꼭 입력해준다.

```python
class MyClass:
    @classmethod	# 꼭 적어야 한다!
    def class_method(cls, arg1, arg2, ...):	# 첫번째 인자로 cls 입력
        [코드블럭]
        
MyClass.class_method(arg1, arg2, ...)
<instance>.class_method(arg1, arg2, ...)
```

### 5.3 스태틱 메서드(static method, 정적 메서드)

- 클래스가 사용할 메서드로서, 클래스의 인스턴스 없이 호출이 가능하며, 인스턴스에서는 호출 할 수 없다.

```python
class MyClass:
    @staticmethod	# 꼭 적어야 한다!
    def static_method(arg1, arg2, ...):
        [코드블럭]
        
# 호출시, 어떤 인자도 전달되지 않음
MyClass.static_method(arg1, arg2)
```



## 6. 상속(Inheritance)

> 부모 클래스의 모든 속성을 자식 클래스에게 상속하여 코드 재사용성을 높이는 것

```python
class ChildClass(ParentClass):
    <코드블럭>

# super() - 추가로 지정해줄 때 사용
class ChildClass(ParentClass):
   def method(self, arg):
    super().method(arg)
```

`super()`

- 자식 클래스에 메서드를 추가로 구현할 수 있다.
- 부모 클래스의 내용을 사용하고자 할 때, `super()`를 사용할 수 있다.

```python
# 예시
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
        
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)
        self.student_id = student_id
```



## 7. 메서드 오버라이딩(Method Overriding, 메서드 재정의)

> 자식 클래스에서 부모 클래스의 메서드를 재정의하는 것
>
> - 인스턴스 -> 자식 클래스 -> 부모 클래스 -> 전역

```python
# 예시
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')

class Soldier(Person):
    def __init__(self, name, age, number, email, army):
        super().__init__(name, age, number, email)	# 이 과정을 거치면 부모 클래스의 다른 모든 메서드가 상속되는 것 같다.
        self.army = army
        
    # method overriding    
    def greeting(self):
        print(f'충성! {self.army} {self.name}')

s = Soldier('굳건이', 25, '0101234', 'soldier@roka.kr', '하사')
s.greeting()
a = Person('굳건이', 25, '0101234', 'soldier@roka.kr')
a.greeting()
# greeting을 재정의
```



## 8. 다중 상속

> 두 개 이상의 클래스를 상속받는 경우로, 상속의 순서(왼쪽->오른쪽)가 중요 (존재만 알고 있자!)

```python
# 예시
class Person:
    def __init__(self, name):
        self.name = name
    
    def breath(self):
        return '날숨'
    
    def greeting(self):
        return f'hi, {self.name}'

class Mom(Person):
    gene = 'XX'
    
    def swim(self):
        return '첨벙첨벙'

class Dad(Person):
    gene = 'XY'
    
    def walk(self):
        return '성큼성큼'

class FirstChild(Dad, Mom):  # 상속의 순서가 중요합니다.(왼쪽에서 오른쪽)
    def swim(self):  # Mom의 swim 메서드를 overriding 한다.
        return '챱챱'
    def cry(self):  # Child 만이 가지는 인스턴스 메서드다.
        return '응애'

class SecondChild(Mom, Dad):  
    def walk(self):  # Dad 의 walk 메서드를 override 합니다.
        return '아장아장'
    def cry(self):  
        return '응애'
```

*Copyright* © Song_Artish