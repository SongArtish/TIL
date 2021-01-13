

# 상속

2021.01.04

---

[TOC]

---



## 1. 개념

> 부모 클래스를 상속받아 부모의 필드와 메소드를 사용할 수 있다.
>
> ```java
> class <자식 클래스> extends <부모 클래스> {
> 
> }
> ```

- 예시

```java
// Robot.java

public class Robot {
	int x, y;
	void mySituation() {
		System.out.println("나의 위치 x: " + x + ", y: " + y);
	}
}

class FishRobot extends Robot {
	int depth;
	FishRobot(int x, int y, int depth) {
		this.x = x;
		this.y = y;
		this.depth = depth;
	}
	void swim() {
		System.out.println("물고기로봇 수심: " + depth + "m");
	}
}

class DroneRobot extends Robot {
	int altitude;
	DroneRobot(int x, int y, int altitude) {
		this.x = x;
		this.y = y;
		this.altitude = altitude;
	}
	void fly() {
		System.out.println("드론로봇 높이" + altitude + "m");
	}
}
```



## 2. 접근 제한자

> 부모 클래스에서 `접근 제한자`를 사용하면 자식 클래스들이 해당 변수/메소드를 사용할 수 없다.

|    접근 클래스의 위치     | `public` | `protected` | `default` | `private` |
| :-----------------------: | :------: | :---------: | :-------: | :-------: |
|   같은 패키지의 클래스    |    O     |      O      |     O     |     X     |
| 같은 패키지의 자식 클래스 |    O     |      O      |     O     |     X     |
|   다른 패키지의 클래스    |    O     |      X      |     X     |     X     |
| 다른 패키지의 자식 클래스 |    O     |      O      |     X     |     X     |



### 2.1 `private`

> `private`이 선언된 변수는 그 클래스 안에서만 사용할 수 있기 때문에 보안성이 제일 높다.

- 예시

```java
// MyParents.java
public class MyPraents {
    private int building;
    int money = 100000;
  
}

class Children extends MyParents {
    
}
```

```java
// MainClass.java
public class MainClasss {
    public static void main(String[] ar) {
        Children child1 = new Children();
        System.out.println(child1.building); // 오류 발생
        System.out.println(child1.money);
        
        MyParents parents1 = new MyParents();
        System.out.println(parents1.building);	// 이것도 마찬가지로 오류 발생
        System.out.println(parents1.money);
    }
}
```



### 2.2 `getter()`& `setter()`: private에 접근하기

> 접근 제한자가 public인 `getter()`, `setter()` 메소드를 사용하면 private 변수에 접근할 수 있다.

- 예시

```java
// Robo.java

public class Robo {
	private String name = "마징가";
	int x;
	int y;
	public String getter() {	// getter() 메소드로 name에 접근
		return name;
	}
	public void setter(String name) {	// setter() 메소드로 name 재정의
		this.name = name;
	}
}
```

```java
// PrintRobo.java
public class PrintRobo {
	public static void main(String[] ar) {
		Robo r1 = new Robo();
		System.out.println(r1.getter());
		
		// name 덮어쓰기
		r1.setter("짱가");
		System.out.println(r1.getter());
	}
}
```

- 아래의 코드를 실행하면 원래의 `name`과 재정의 된 `name`이 잘 출력되는 것을 확인할 수 있다.



## 3. Polymorphism(다형성)

> **같은 자료형에 여러 가지 객체를 대입하여 다양한 결과를 얻어내는 성질**

### 3.1 오버라이딩

> 자식 클래스에서 동일한 이름의 부모 메소드를 재정의해서 사용하는 것

- 예시

```java
// Robot.java
public class Robot {
    void myName(String name) {
        System.out.println("My name: " + name);
    }
}

class FishRobot extends Robot {
    void myName(String name) {
        System.out.println("Fish name: " + name);
    }
}
```

```java
// MainClass.java

public class MainClass {
    public static void main(String[] ar) {
        FishRobot r1 = new FishRobot();
        r1.myName("짱가");
    }
}
```

- 아래의 코드를 실행해보면 메소드가 오버라이딩 되어 `My name: 짱가`가 아닌, `Fish name: 짱가`로 출력되는 것을 확인할 수 있다.



### 3.2 업캐스팅

> 부모 클래스 타입의 참조변수로 자식 클래스의 객체를 참조할 수 있다.

- 예시

```java
// Bot.java

public class Bot {
	int x, y;
	void move() {
		System.out.println("Move Bot");
	}
}

class FishBot extends Bot {
	void move() {
		System.out.println("Move FishBot");
	}
}

class DroneBot extends Bot {
	void move() {
		System.out.println("Move DroneBot");
	}
}
```

- 아래와 같이 바로 부모 클래스의 참조변수로 자식 클래스의 객체를 생성해서 사용할 경우에는 오류가 발생한다.

```java
// PrintBot.java
public class PrintBot {
	public static void main(String[] ar) {
		
		Bot r0 = new FishBot();
		r0.move()
	}
}
```

- :ballot_box_with_check: 자식 클래스가 부모 클래스의 메소드를 오버라이딩하여 사용할 경우에는 부모 클래스의 참조변수로 자식 클래스의 메소드에 접근할 수 있다!

```java
// PrintBot.java
public class PrintBot {
	public static void main(String[] ar) {
		
//		Bot r0 = new FishBot();
//		r0.move()
		
		FishBot r1 = new FishBot();
		r1.move();
		
		Bot r2 = new FishBot();
		r2.move();
	}
}
```



***Copyright* © 2021 Song_Artish**