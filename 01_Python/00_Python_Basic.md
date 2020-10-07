# Python 기초



[TOC]



## 1. 기초 문법(Syntax)

### 주석(Comment)

- 한 줄: `#(파운드)`
- 여러 줄: `"""` 또는 `'''` (multiline string)

### 코드 라인

- 1줄 1문장(statement)이 원칙

- 한 줄로 표기할 때는 `;`을 작성하여 표기

```python
# 한 줄 표기
print('hello'); print('world')

hello
world
```

- 줄을 여러줄 작성할 때는 역슬래시`\`도 사용 가능
- `[]`{}`()`는 `\`없이도 가능



## 2. 변수(Variable)

### 할당 연산자(ASsignment Operator): `=`

- 할당: `=`
- 해당 데이터 타입 확인: `type()`
- 해당 값의 메모리 주소 확인: `id()` - 변수에 값이 아닌 해당 값의 메모리 주소를 할당하는 것
- 같은 값 동시 할당 가능

```python
# 동일 값 동시 할당
x = y = 'ssafy'
print(x)
print(y)

ssafy
ssafy
```

- 다른 값 동시 할당 가능 (단, 변수와 값의 개수가 같아야 한다.)

```python
# 다른 값 동시 할당
a, b = 2020, 4
print(a)
print(b)

2020
4
```

- 서로 값을 바꾸고 싶을 경우 다음과 같이 활용

```python
a, b = 10, 20
(a, b) = (b, a)
print(a)
print(b)

20
10
```

### 식별자(Identifiers)

> 파이썬에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름(name)이다.

- 식별자의 이름은 영문알파벳(대/소문자 구분), 밑줄(_), 숫자로 구성된다.
- 예약어는 사용할 수 없다.

```python
# 예약어 리스트 확인
import keyword
print(keyword.kwlist)

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

- 내장함수나 모듈 등의 이름으로도 만들면 안된다.

```python
# 내장함수 예시
print = 'ssafy'
print(print)
del print
print('hello')

hello
```



## 3. 데이터 타입(Data Type)

### 1) 숫자(Number) 타입

(1) `int` (정수, integer)

- 모든 정수는`int`로 표현된다.
-  2진수: `0b` (`bin()`) / 8진수: `0o`  (`oct()`) /  16진수: `0x` (`hex()`)로도 표현 가능하다.

arbitrary-precision arthmetic(파이썬에서 아주 큰 정수를 표현할 때 사용하는 메모리의 크기 변화)을 사용하여 오버플로우(overflow)가 없다.

```python
# 파이썬에서 표현할 수 있는 가장 큰 수
import sys		# system
print(sys.maxsize)
print(sys.maxsize * sys.maxsize)

# 혹은
float('inf')
float('-inf')
```

(2) `float` (부동소수점, 실수, floating point number)

- 실수는 `float`으로 표현된다.
- 실수를 표현하는 과정에서 부동소수점을 사용하여, floating point rounding error가 존재한다.

```python
# floating point rounding error
3.5 - 3.2 == 0.3		# False
round(3.5 - 3.2, 2) == 0.3		# True
```
- 따라서 다음과 같은 방법으로 처리할 수 있다.

```python
# 2 sys 모듈을 통한 처리방법
# 'epsilon'은 부동소수점 연산에서 반올림을 함으로써 발생하는 오차 상환
import sys
print(sys.float_info.epsilon)
a = 3.5 - 3.2
b = .3
abs(a - b) <= sys.float_info.epsilon

2.220446049250313e-16
True
```

```python
# 3 math 모듈을 통한 처리방법
import math
math.isclose(a, b)

True
```

```python
# 컴퓨터식 지수 표현 방식
b = 314e-2		# 3.14 = 314*10^-2
print(b)

3.14
```

(3) `complex`(복소수, complex number)

- 복소수는 허수부를 `j`로 표현

```python
# 문자열 변환시, 문자열 중앙의 + 또는 - 연산자 주위에 공백을 포함해서는 안 된다.
c = complx('3+4j')
```

### 2) 문자(String) 타입

- Single quotes(`'`')나 Double quotes(`"`) 호은 삼중 따옴포를 활요하여 표현 가능

- 문자열 안에 문장부호(`'`,`"`)가 사용될 경우 이스케이프 문자(`\`)를 활용 가능

```python
# 문자열 안 문장부호 활용
"그의 이름은 \"SSAFY\"였다."

'그의 이름은 "SSAFY"였다.'
```

- 문자열은 연산자로 이어붙이거나, 반복, 변수화도 가능

**이스케이프 시퀸스**

> <u>문자열을 활용하는 경우</u> 특수문자 혹은 조작을 하기 위하여 사용되는 것으로 `\`를 활용하여 이를 구분한다.

| 예약문자 |    내용(의미)     |
| :------: | :---------------: |
|  **\n**  |      줄 바꿈      |
|  **\t**  |        탭         |
|  **\r**  |    캐리지리턴     |
|  **\0**  |     널(Null)      |
|  **\\**  |        `\`        |
|  **\'**  | 단일인용부호(`'`) |
|    \"    | 이중인용부호(`"`) |

```python
# \n
print('안녕\n나는\npython\t이야')

안녕
나는
python	이야

# end 옵션
print('hello', end = '2020')
print('ssafy')

hello2020ssafy

# sep 옵션
print('hello', 'ssafy', sep = ',')
hello,ssafy
```

**String interpolation** - `f-strings`

```python
# %-formatting
name = 'song'
print('내 이름은 $s 입니다.' % name)		# C스타일

# str.format()
print('내 이름은 {} 입니다.'.format(name))

# f-string
print(f'내 이름은 {name} 입니다.)

# 결과값
내 이름은 song 입니다.
```

```python
# datetime 모듈 활용
import datetime
now = datetime.datetime.now()
now.today()

# now.today()
#f'오늘은 {now:%Y}입니다.'			#:%y는 year만 뽑아온다. (Y,y 구분있음)
f'올해는 {now:%Y}년 이번달은 {now:%m}월 오늘은 {now:%d}일'

'올해는 2020년 이번달은 07월 오늘은 20일'
```

### 3) 참/거짓(Boolean) 

- type은 `bool`

```python
# False로 변환되는 것
0, 0.0, (), [], {}, '', None		# 0이거나 빈 것

# 나머지는 다 True로 변환된다.
bool('love')
```

**형변환(Type conversion, Typecasting)**

1) 암시적 형변환(Implicit Type Conversion)

> 사용자가 의도하지 않았지만, 파이썬 내부적으로 자동으로 형변환 하는 경우
>
> - bool
> - Numbers (int, float, complex)

2) 명시적 형변환(Explicit Type Conversion)

> 위의 상황을 제외하고는 모두 명시적으로 형 변환 필요
>
> - string -> integer : 형식에 맞는 숫자만 가능
> - integer -> string : 모두 가능

- `int()` : string, float를 int로 변환
- `float()` : string, int를 float로 변환
- `str()` : int, float, list, tuple, dictionary를 문자열로 변환



## 4. 연산자

### 1) 산술 연산자

| 연산자 |      내용      |
| :----: | :------------: |
|   +    |      덧셈      |
|   -    |      뺄셈      |
|   *    |      곱셈      |
|   /    |     나눗셈     |
|   //   |       몫       |
|   %    | 나머지(modulo) |
|   **   |    거듭제곱    |

- 나눗셈(`/`)은 항상 float를 돌려준다.

```python
# divmod 함수
a, b = divmod(10, 3)
print(a); print(b)

3; 1
```



### 2) 비교 연산자

| 연산자 |         내용         |
| :----: | :------------------: |
|   <    |         미만         |
|   <=   |         이하         |
|   >    |         초과         |
|   >=   |         이상         |
|   ==   |         같음         |
|   !=   |       같지않음       |
|   is   |    객체 identity     |
| is not | 부정된 객체 identity |

- `is`연산자를 통해 동일한 object(id)인지 확인할 수 있다.

  ```python
  a = [1, 2, 3]
  b = [1, 2, 3]
  print(a is b)		# print(id(a) == id(b))
  ```

### 3) 논리 연산자

| 연산자  |             내용             |
| :-----: | :--------------------------: |
| a and b |  a 와 b 모두 True시만 True   |
| a or b  | a 와 b 모두 False시만 False  |
|  not a  | True -> False, False -> True |

- `&`(and), `|`(or)은 파이썬에서 비트 연산자이다.

단축평가 (short-circuit evaluation)

> 첫 번째 값이 확실할 때, 두 번째 값은 확인하지 않음. 조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도 향상.

### 4) 복합 연산자

> 복합 연산자는 연산과 대입이 함께 이루어진다.
>

|  연산자  |    내용    |
| :------: | :--------: |
|  a += b  | a = a + b  |
| a - = b  | a = a - b  |
|  a *= b  | a = a * b  |
|  a /= b  | a = a / b  |
| a //= b  | a = a // b |
|  a %= b  | a = a % b  |
| a ** = b | a = a ** b |

```python
# 복합연산자 예시
cnt = 0			    # count
while cnt < 5:
    print(cnt)
    cnt += 1		# cnt = cnt + 1
```

### 5) 기타 연산자

**Concatenation**

> 숫자가 아닌 자료형(str, list)은 `+` 연산자를 통해 합칠 수 있다.

**Containment Test**

> `in` 연산자를 통해 요소가 속해있는지 여부를 확인할 수 있다.

```python
# 문자열
'a' in 'hello'

# list
0 in [1, 3, 5, 7]

# range
22 in range(2, 23)		# 0부터 시작, 45 미만
```

**Indexing/Slicing**

> `[]`를 통한 값을 접근하고, [:]을 통해 리스트를 슬라이싱할 수 있다. 

```python
[1, 2, 3, 4, 5][0:3]		# 시작부터 미만까지 슬라이싱

[1, 2, 3]
```

연산자 우선순위

0. `()`을 통한 grouping
1. Slicing
2. Indexing
3. 제곱연산자` **`
4. 단항연산자 `+`, `-` (음수/양수 부호)
5. 산술연산자 `*`, `/`, `%`
6. 산술연산자 `+`, `-`
7. 비교연산자 `in`, `is`
8. `not`
9. `and`
10. `or`

```python
-3 ** 6

=-729		# 제곱연산자가 우선이 되어 음수가 나옴
```



## [참고] 표현식 (Expression) & 문장 (Statement)

표현식 (Expression)

> 하나의 값(value)으로 환원(reduce)될 수 있는 문장
>
> 표현식 => `evaluate` => 값

- `식별자`, `값`(리터럴), `연산자`로 구성됨

문장 (Statement)

> 파이썬이 실행 가능한 최소한의 코드 단위 (a syntatic unit of programming)

![](https://user-images.githubusercontent.com/9452521/87640197-55a7f280-c781-11ea-9cff-19c022ce704a.png)

*Copyright* © Song_Artish