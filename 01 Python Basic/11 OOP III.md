# OOP (Object Oriented Programming) III

2020.07.30.

```
<Index>
1. 상속(Inheritance)
2. 메서드 오버라이딩(Method Overriding)
3. 다중 상속(Multiple Inheritance)
```



## 1. 상속(Inheritance)

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
# 예시1
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
        
# 예시2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2* (self.length + self.width)

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
```



## 2. 메서드 오버라이딩(Method Overriding, 메서드 재정의)

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
        super().__init__(name, age, number, email)
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



## 3. 다중 상속

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