# 함수 (Function) II

## 1. 함수와 스코프(scope)

> 함수는 코드 내부에 공간(scope)을 생성한다. 함수로 생성된 공간은 `지역 스코프(local scope)`라고 불리며, 그 외의 공간인 `전역 스코프(global scope)`와 구분된다.
>
> - 전역 스코프(`global scope`): 코드 어디에서든 참조할 수 있는 공간
> - 지역 스코프(`local scope`): 함수를 만든 스코프로 함수 내부에서만 참조할 수 있는 공간
> - 전역 변수(`global variable`): 전역 스코프에 정의된 변수
> - 지역 변수(`local variable`): 로컬 스코프에 정의된 변수

### 1) 이름 검색(resolution) 규칙

> 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있다. 이것을 `LEGB Rule`이라고 부르며, 아래와 같은 순서로 이름을 찾아간다.
>
> - Local scope: 정의된 함수
> - Enclosed scope: 상위 함수
> - Global scope: 함수 밖의 변수 혹은 import된 모듈
> - Built-in scope: 파이썬 안에 내장되어 있는 함수 또는 속성

```python
# 예시: print(내장함수)를 식별자로 사용한 경우
print = 'ssafy'
print(3)
del print
print(3)

# 예시: 로컬 함수를 전역 함수로 변경
global_num = 3
def local_scope():
    global global_num    # global로 재 정의 후 값 입력
    global_num = 5
    return f'global_num이 {global_num}으로 설정되었습니다.'

print(local_scope())
print('global_num:', global_num)
# 하지만 이러한 방식은 좋지 않다!
```

### 2) 변수의 수명주기(lifecycle)

> 변수의 이름은 각자의 `수명주기(lifecycle)`가 있다.
>
> - 빌트인 스코프(`built-in scope`) : 파이썬이 실행된 이후부터 영원히 유지
> - 전역 스코프(`global scope`) : 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 인터프리터가 끝날 때까지 유지
> - 지역(함수) 스코프(`local scope`) : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유치 (함수 내에서 처리되지 않는 예외를 일으킬 때 삭제된다.)



## 2. 재귀 함수(recursive function)

> 재귀 함수는 함수 내부에서 자기 자신을 호출하는 함수이며, 알고리즘 설계 및 구현에서 유용하게 활용된다.
>
> - 장점: 코드가 더 직관적이고 이해하기 쉽다.
> 
>- 단점: 함수가 호출될 때마다 메모리 공간에 쌓이기 때문에, 메모리 스택이 넘치거나 프로그램 실행 속도가 늘어진다.

### 1) 팩토리얼 계산

```python
# 반복문 이용
def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        return result
    
# 재귀 이용
def factorial(n):
    if n == 1:		# 재귀함수는 종료조건이 필요 (base case)
        return n
    else:
        return n * factorial(n-1)
```

- 파이썬에서는 최대 재귀 깊이(maximun recursion depth)가 1,000으로 정해져 있다.

### 2) 피보나치 수열

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

- 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용한다.
- 재귀 호출은 `변수 사용`을 줄여줄 수 있다.