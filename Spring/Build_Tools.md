# 빌드 도구

---

[TOC]

---



## Ant

- XML(`Extensible Markup Language`) 기반으로 빌드 스크립트를 작성한
- 자유롭게 빌드 단위 지정 가능
- 간단하고 사용하기 쉽다.
- 유연하지만 프로젝트가 방대해지는 경우 스크립트 관리나 빌드 과정이 복잡해진다.
- 생명주기(Lifecycle)을 갖지 않아 각각의 결과물에 대한 의존관계 등을 정의해야 한다.



## Maven

- XML 기반으로 작성
- 생명주기(Lifecycle)와 프로젝트 객체 모델(POM, Project Object Model)이란 개념이 도입되었다.
- Ant의 장황한 빌드 스크립트를 개선
- `pom.xml`에 필요한 라이브러리를 선언하면 자동으로 해당 프로젝트를 불러와 편리
- 상대적으로 학습 장벽이 높다.
- 라이브러리가 서로 의존하는 경우 복잡해질 수 있다.



## Gradle

> [Gradle(그래들)](https://github.com/gradle/gradle)은 그루비(Groovy)를 기반으로 한 빌드 도구이다.

- `Ant`와 `Maven`과 같은 이전 세대 빌드 도구의 단점을 보완하고 장점을 취합하여 만든 오픈소스로 공개된 빌드 도구
- 의존성 관리를 위한 다양한 방법을 제공
- 빌드 스크립트를 XML 언어가 아닌 JVM에서 동작하는 스크립트 언어 `그루비` 기반의 DSL(Domain Specific Language)를 사용
  - **그루비(Groovy)**
    - 자바 문법과 유사하여 자바 개발자가 쉽게 익힐 수 있는 장점이 있다.
    - `Gradle Wrapper`를 이용하면 Gradle이 설치되지 않은 시스템에서도 프로젝트를 빌드할 수 있다.



***Copyright* © 2021 Song_Artish**

