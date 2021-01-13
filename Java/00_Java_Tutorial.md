

# Java 튜토리얼

2021.01.13

> 자바 개발환경을 구축하고 이클립스 기본 사용법에 대해서 학습한다.
>
> [참고 영상](https://www.youtube.com/watch?v=wjLwmWyItWI)

---

[TOC]

---



## JDK 설치

> JDK는 자바의 기본적인 개발을 가능하게 해주는 개발 환경이다.

**파일 설치**

- [오라클 사이트](https://www.oracle.com/kr/java/technologies/javase-downloads.html)에 접속하여 운영체제에 맞는 JDK를 설치한다.

**환경변수 설정**

`javac` 명령 사용을 위해 환경변수를 설정한다.

- `Program Files > Java > jdk폴더 > bin` 위치로 이동해 해당 위치주소를 복사한다.
- `환경 변수 > Path`에 복사한 위치를 추가한다.
- `시스템 변수 > 새로 만들기`에서 `JAVA_HOME`과 `Program Files > Java > jdk폴더` 위치를 입력하고 변수를 생성한다.
- `cmd`에서 `javac` 명령어를 입력하고 작동하는지 확인한다.



## Eclipse 설치

> 이클립스는 자바를 개발할 때 더욱 효율적인 개발을 가능하게 해주는 개발 환경이다.

- [이클립스 사이트](https://www.eclipse.org/downloads/)에서 프로그램을 설치한다.
- 설치 프로그램에서 자바 개발자를 위한 이클립스( `Eclipse IDE for Java Developers`를 설치한다.
- 이후 과정에서는 default 값으로 설치를 진행하면 된다.



## Eclipse 사용

### 프로젝트 생성

- 이클립스에서 새로운 프로젝트를 생성한다.
- 프로젝트 이름의 경우 일반적으로 `파스칼표기법`(HelloWorld)를 따른다.



### 클래스 생성

- 프로젝트에서 우클릭하여 클래스를 생성한다.
- 일반적으로 프로젝트에서 첫번째로 실행되는 클래스의 이름을 `Main`이라고 한다.
- 클래스 생성시 아래 체크박스에서 `public static void main(String[] args)`를 체크하면 자동으로 메인 함수(메소드), 즉 실행되는 함수를 만들 수 있다.



### 출력하기

- 메인 함수에서 `System.out.println();`을 입력하여 출력할 수 있다.

```java
System.out.println("Hello World");
```



***Copyright* © 2021 Song_Artish**