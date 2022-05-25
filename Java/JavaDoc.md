

# JavaDoc

---

[TOC]

---



## Overview

인수인계 혹은 기능 명세 등 자바 소스 파일들을 문서화하는 경우 **html 형식으로 설명, 하이퍼링크를 생성**해주는 것

```java
/**
* The HelloWorld program implements an application that
* simply displays "Hello World!" to the standard output.
*
* @author  Song Artish
* @version 1.0
* @since   2022-05-25
*/
public class HelloWorld {

   public static void main(String[] args) {
      // Prints Hello, World! on standard output.
      System.out.println("Hello World!");
   }
}
```



## Annotations

- **@author** : 코드 소스 작성자
- **@deprecated** : 해당 클레스(구현체)의 삭제 또는 지원이 중단되는 것을 알려줌
- **@exception** : 예외처리할 수 있는 것들을 정의, 알파벳 순
- **@param** : 매개변수 메서드, 생성자 설명
- **@return** : 리턴값 설명
- **@see** : 파일이 참조하는 다른 클래스와 메서드 등
- **@serial** : Serializeable 인터페이스에 사용
- **@serialData** : writeObject writeExternal 메소드로 작성된 데이터 설명
- **@serialField** : serialPersistnetFields 모든 배열에 사용됨
- **@since** : 해당 클래스가 추가된 버전
- **@throws** : @exception처럼 예외처리하는 것들을 정의
- **@version** : 구현체, 패키지 버전 명시



***Copyright* © 2022 Song_Artish**