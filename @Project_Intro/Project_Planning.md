# 프로젝트 설계

---

[TOC]

---



## Problem Definition

### 고객여정맵

- 서비스를 이용하는 과정을 그림, 도표, 사진 등으로 시각화하는 것
- 시간/공간적 흐름에 따라 문제가 되는 지점 파악

### 매력적인 주제를 정하는 5가지 팁

> 본 내용은 2021년 1월 18일 박종철 컨설턴트님의 강의를 바탕으로한다.

```markdown
1. 불평할 것
2. 사용자의 입장에서 생각할 것
3. 작게 시작할 것
4. 서비스 추가 시 '왜?'라고 3번 물을 것
5. 사회문제에 관심을 기울일 것
```



## Design



### UI/UX 정의

> :ballot_box_with_check: 어느 플랫폼에서? (디지털 기기)
> :ballot_box_with_check: 누가? (사용자)
> :ballot_box_with_check: 어떻게 사용할 것인가? (상호 작용)



### Inspirations

- 플랫폼 개발사의 공식 문서 디자인 가이드를 배우자.
  - [Google Marterial Design](https://material.io/)
  - [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)

- 아래의 사이트에서 디자인 영감을 얻을 수 있다.

  :ballot_box_with_check: Behance

  :ballot_box_with_check: Dribbble

  :ballot_box_with_check: Pinterest

- 아래와 같은 검색 키워드로 영감을 얻을 수 있다.

  :ballot_box_with_check: `netflix ui redesing`

  :ballot_box_with_check: `Sharing App UI`

  :ballot_box_with_check: `Co work app UI`



### Color

- 색상마다 주는 인상이 다르므로, 이러한 요소를 고려하여서 색상을 활용한다.

![colors](img/colors.png)

`(출처: https://seopressor.com/wp-content/uploads/2015/06/colour-culture1.png)`

[참조 사이트](https://colorhunt.co/)



### Tools

디자이너가 가장 많이 사용하는 툴

- Photoshop
- Sketch



### 프로젝트 퀄리티를 한층 더 높여주는 5가지 작은 팁

> 2021년 2월 9일 신채원 실습코치님의 필기를 참고하였다.

**1. 파비콘 및 페이지 제목**

- 사이트의 성격을 드러내자.
  - [<title> 요소 활용하기](https://developer.mozilla.org/ko/docs/Web/HTML/Element/title)
  - [Vue Router 활용하기](https://medium.com/@hulunhao/how-to-config-title-for-each-router-in-vue-router-1cc7352bbb94)
  - [Favicon Generator](https://www.favicon-generator.org/)

**2. 메뉴 sticky 속성**

- 메뉴는 항상 보이는 곳에 두자

**3. 로딩 페이지**

- 유저를 기다리게 하지 말자
- 현재 어떤 일이 일어나고 있는지 화면에 시각적인 피드백을 제공해준다.

**4. 버튼/링크 디자인**

- 누를 수 있는 곳과 없는 곳을 확실하게 하자.

**5. tool & popup tip**

- 유저를 헤매게 하지 말자
- 툴팁과 팝업팁을 통해 유저가 참고할 수 있는 정보 또는 설명을 제공하면 좋다.



### <참고>

[모바일 UI/UX 디자인시 고려사항](https://brunch.co.kr/@chulhochoiucj0/8)



## 화면설계

### 1. Wireframe

> UI 중심의 화면 레이아웃

### 2. Mockup

> 실물과 흡사한 정적인 형태의 모형

**Tools**

- :ballot_box_with_check: justinmind
- :ballot_box_with_check: balsamiq
- :ballot_box_with_check: adobeXD
- :ballot_box_with_check: ovenapp

### 3. Prototype

> 다양한 interaction이 결합되어 실제 서비스처럼 작동하는 모형

### 4. Storyboard

> 정책, 프로세스, 와이어프레임, 디스크립션 등이 모두 포함된 설계 문서



## DB 설계

### 1. 설계를 위한 요구사항 분석

- 데이터베이스에 대한 사용자의 요구사항을 수집하고 분석해서 아래와 같이 요구사항(기능) 명세서를 작성한다.

### 2. 개념적 설계

> DB 설계는 [ERD Cloud](https://www.erdcloud.com/)를 사용하면 좋다!

- 작성한 요구사항 명세서에서 DB를 구성하는데 필요한 `개체(Entity)`, `속성(Attribute`), 개체 간의 `관계(Relationship)`를 추출하여 ERD를 생성한다.
  - 개체: 회원, 신용카드, 비행기, 좌석
  - 속성: (아이디, 비밀번호, 성명), (번호, 유효기간), (비행기 번호, 출발 날짜/시간), (좌석번호, 등급)
  - 관계: 여러 개를 저장, 회원 한 명은 좌석 하나만 예약, 한 좌석은 회원 한 명만 예약가능

### 3. 논리적 설계

- 모든 개체는 릴레이션(Table)으로 변환
  - 객체 -> 테이블
  - 속성 -> 테이블의 속성
- N:M 관계는 릴레이션(Table)으로 변환
  - 관계 -> 릴레이션 이름
  - 관계속성 -> 릴레이션 속성
- 1:N 관계는 외래키로 표현
  - 일반적으로 1:N 고나계에서 1측 개체의 깁노키를 N측 릴레이션에 포함시키고 외래키(FK)로 지정
- 1:1관계는 외래키로 표현
  - 일반적 1:1 관계는 외래키(FK)를 서로 주고 받는다.
- 다중 값 속성은 독립 릴레이션(Table)으로 변환
  - 릴레이션에서는 다중 값 속성을 가질 수 없으므로 다중 값 속성은 별도의 릴레이션으로 생성해야 한다.

### 4. 물리적 스키마 및 구현

- ERD를 실제 테이블로 생성한다.
- Workbench 같은 EB Tool이나 SQL스크립트 사용으로도 가능해야 한다.

### <참고> 반정규화

> 정규화도니 엔티티타입, 속성, 관계를 시스템의 성능향상, 개발과 운영의 단순화를 위해 모델을 통합하는 프로세스
>
> ```markdown
> <정규화 모델>
> - SQL 작성이 용이하지 않고 과다한 테이블 조인이 발생하여 성능이 저하될 가능성이 높다.
> <반정규화 모델>
> - 같은 데이터가 여러 테이블에 걸쳐 존재하므로 무결성이 깨질 우려가 높다.
> ```

**테이블 반정규화 방법**

- 1:1 관계의 테이블 병합
- 1:N 관계의 테이블 병합
- 수퍼/서브 타입 테이블 병합
- 수직 분할(집중화된 일부 컬럼을 분리)
- 수평 분할(행으로 구분하여 구간별 분리)
- 테이블 추가 (중복테이블, 통계테이블, 이력테이블, 부분테이블)

#### 1) 컬럼 반정규화

- 중복컬럼 추가(자주조회하는 컬럼이 있는 경우)
- 파생 컬럼 추가(미리 계산한 값)
- PK에 의한 컬럼 추가
- 응용시스템 오작동을 위한 컬럼 추가(이전데이터 임시 보관)

#### 2) 관계 반정규화

- 중복 관계 추가(이미 A테이블에서 C테이블의 정보를 읽을 수 있는 관계가 있음에도 관계를 중복하여 조회(Read) 경로를 단축)



***Copyright* © 2021 Song_Artish**