

# 변수

2021.01.13

> 변수 설정 및 사용 방법에 대해서 학습한다.
>
> [참고 영상](https://www.youtube.com/watch?v=cOHYKJD_-bc)

---

[TOC]

---



## 1. 자료형

### 1.1 정수

> `int`

- 예시

```java
int intType = 100;
```

- :ballot_box_with_check: 정수 변수 안에 실수를 넣으면 **정수 부분만** 변수에 저장되며, `형변환`을 통해 저장할 수 있다.

  ```java
  int a = (int) 0.5;
  ```



### 1.2 실수

> `double`

- 예시

```java
double doubleType = 150.5;
```



### 1.3 문자 

> `String`

- 예시

```java
String stringType = "name";
```

**활용 예시**

```java
public class Main {
	
	public static void main(String[] args) {
		int intType = 100;
		double doubleType = 150.5;
		String stringType = "name";
		
		System.out.println(intType);
		System.out.println(doubleType);
		System.out.println(stringType);
	}
    
}
```



## 2. 상수

> `final`

- 상수의 경우  main 함수 밖에서 정의된다.

- 예시

  ```java
  final static double PI = 3.141592;
  ```

  - `final`: 상수(한 번 선언되면 변경될 수 없음)
  - `static`: 하나의 클래스에서 공유하는 자원으로 지정
  - `double`: 실수형

**활용 예시**

- 반지름이 `r`인 원의 넓이를 구하는 코드

  ```java
  public class Main {
  	
   	final static double PI = 3.141592;
  	
  	public static void main(String[] args) {
  		
  		int r= 30;
  		System.out.println(r * r * PI);
  	}
  
  }
  ```



## 3. Overflow

- `int`형 자료형이 가질 수 있는 값의 범위는  `[-2,147,483,647, 2,147,483,647]`이다.

- 예시

  ```java
  public class Main {
  	
  	final static int INT_MAX = 2147483647;
  	
  	public static void main(String[] args) {
  		
  		int a = INT_MAX;
  		System.out.println(a+1);
  	}
  
  }
  ```

  - 위 코드를 실행하면 `overflow`가 발생하여 `-2147483647`이라는 오류 값이 출력된다.



## 4. 사칙연산

```java
public class Main {
	
	public static void main(String[] args) {
		
		int a = 1;
		int b = 2;
		System.out.println("a + b = " + (a + b));
		System.out.println("a - b = " + (a - b));
		System.out.println("a * b = " + (a * b));
		System.out.println("a / b = " + (a / b));

	}

}
```



***Copyright* © 2021 Song_Artish**