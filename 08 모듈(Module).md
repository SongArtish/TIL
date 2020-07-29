# 모듈(Module)

2020.07.29.

> 파일 단위의 코드 재사용

| 용어                   | 정의                                                         |
| ---------------------- | ------------------------------------------------------------ |
| 모듈                   | 특정 기능을 `.py` 파일 단위로 작성한 것                      |
| 패키지                 | 특정 기능과 관련된 여러 모듈들의 집합. 패키지 안에는 또다른 서브 패키지 포함 가능 |
| 파이썬 표준 라이브러리 | 파이썬에 기본적으로 설치된 모듈과 내장 함수를 묶어서 <br />파이썬 표준 라이브러리 (Python Standard Library, PSL)라 불림 |
| 패키지 관리자(`pip`)   | `PyPI`에 저장된 외부 패키지들을 설치하도록 도와주는 패키지   |

```cmd
# pip 설치방법
$ pip install <pip name>
$ python -m pip install <pip name>	# 이게 효과적이다.
```



## 다양한 모듈 사용법

### 모듈

```D
import module
from module import var, function, Class
from module import *
```

### 패키지

```python
from package import module
from package.module import var, function, Class
```



## 1. 모듈(Module)

> 모듈은 특정 기능을 하는 코드를 담고 있는 파일(또는 스크립트)이다.

### 모듈 생성

- `<module name>.py` 형태의 파일을 생성한다.

### 모듈 활용

- `import`문을 통해 내장 모듈을 이름 공간으로 가져와야한다.
- 함수를 변수에 할당할 수도 있다.



## 2. 패키지(Package)

> 패키지는 점(`.`)으로 구분된 모듈 이름(`package.module`)을 써서 모듈을 구조화하는 방법이다.

### 패키지 생성

```
<folder name>/
	__init__.py
	<package name>/
		__init__.py
		<file name>.py
```

- `__init__.py` (모든 `__init__.py` 파일은 비워둔다.)

  > python 3.3 버전부터는 `__init__.py` 파일이 없어도 패키지로 인식한다(PEP 420). 하지만 하위 버전 호환 및 일부 프레임워크에서의 올바른 동작을 위해 `__init__.py` 파일을 생성하는 것을 권장한다.

### 패키지 활용

```python
from <패키지> import <모듈>
from <피키지.모듈> import <데이터>
from <모듈> import *		# 모듈의 모든 변수와 함수를 가져옴
from <모듈> import <데이터> as <별명>
```



## * import의 검색순서

### 1. sys.modules

> 단순한 딕셔너리다. 현재 프로젝트에서 **사용하고 있는 모듈과 패키지가 딕셔너리형태로 담겨**있다.

### 2. built-in modules

> 내장된 모듈. 파이썬을 설치하게 되면 기본으로 제공되는 모듈

### 3. sys.path

> sys.modules가 딕셔너리 형이었다면 sys.path는 리스트다. path. 이름에서 보이는 것과 같이 경로가 문자열로 담겨 있다. 해당 경로를 하나하나 찾아 들어가 모듈과 패키지를 검색하게 된다. 막약 최종 검색 위치인 sys.path에서도 <u>해당 모듈/패키지를 찾지 못한다면 `ModuleNotFoundError`를 리턴</u>하게 된다.

*Copyright* © Song_Artish