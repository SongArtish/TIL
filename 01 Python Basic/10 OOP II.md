# OOP (Object Oriented Programming) II

2020.07.29.

```
<Index>
1. 인스턴스 & 클래스 변수
2. 인스턴스 & 클래스 간의 이름공간
3. 인스턴스 & 클래스 메서드(+ 스태틱 메서드)
```

```python
<정리>
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



## 1. 인스턴스 & 클래스 변수

### 1) 인스턴스 변수

```python
class <Class명>:
    def __init__(self, name):	# 인스턴스 메서드 (생성자)
        self.name = name		# 인스턴스 변수 - 메서드 정의 시: self.변수
        
# '인스턴스.변수명'으로 접근
```

### 2) 클래스 변수

```python
class Person:
    species = 'human'			# 클래스 변수
    
   	def info(self):
        return Person.species
    
# '클래스.변수명' 혹은 '인스턴스.변수명'으로 접근
```



## 2. 인스턴스 & 클래스 간의 이름공간

[이름 공간 원칙]

- 인스턴스 => 클래스 (=> 상위 클래스) 순으로 탐색한다.



## 3. 인스턴스 & 클래스 메서드 (+스태틱 메서드)

### 1) 인스턴스 메서드(instance method)

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

### 2) 클래스 메서드(class method)

```python
class MyClass:
    @classmethod
    def class_method(cls, arg1, arg2, ...):
        [코드블럭]
        
# 호출 시, 첫 번째 인자로 클래스 cls 전달
MyClass.class_method(MyClass, arg1, arg2, ...)
```

### 3) 스태틱 메서드(static method)

- 클래스가 사용할 메서드

```python
class MyClass:
    @staticmethod
    def static_method(arg1, arg2, ...):
        [코드블럭]
        
# 호출시, 어떤 인자도 전달되지 않음
MyClass.static_method(arg1, arg2)
```

*Copyright* © Song_Artish