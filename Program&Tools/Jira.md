# Jira

> 애자일 소프트웨어 개발을 위한 이슈 추적 시스템으로 버그 추적, 이슈 추적, 프로젝트 관리 기능을 제공한다.

---

[TOC]

---



## 이론적 배경

**애자일(Agile) 모델**

```markdown
Agile software development is an approach to software development under which requirements and solutions evolve through the collaborative effort of self-organizing and cross-functional teams and their customer(s)/end user(s).
```

`(출처: 위키피디아)`

- 기존의 `Waterfall Model(폭포수 모델)`은 프로젝트 규모가 커지면 요구사항 변화에 대한 유연한 대처가 어려웠는데, 이러한 한계점을 극복하기 위해 `애자일 모델`이 등장하게 되었다.
- 애자일 방법론을 도와주는 대표적인 소프트웨어 툴
  - `Jira`
  - `Trello`
  - `Redmine`

**스크럼(Scrum)**

> 스크럼(Scrum)은 익스트림 프로그래밍, 칸반(Kanban) 등 애자일 모델의 여러가지 방법론 중 하나이다.

```markdown
## Scrum의 특성

- 솔루션에 포함할 기능/개선점에 대한 우선 순위를 부여한다.
- 개발 주기는 30일 정도로 조절하고 개발 주기마다 실제 동작할 수 있는 결과를 제공하라.
- 개발 주기마다 적용할 기능이나 개선에 대한 목록을 제공하라.
- 날마다 15분 정도 회의를 가져라.
- 항상 팀 단위로 생각하라.
- 원활한 의사소통을 위하여, 구분 없는 열린 공간을 유지하라.
```

`(출처: 위키피디아)`

**DevOps** 

> 소프트웨어의 개발(Development)과 운영(Operations)의 합성어로서, 소프트웨어 개발자와 정보기술 전문가 간의 소통, 협업 및 통합을 강조하는 개발 환경이나 문화

DevOps라는 개념을 잘 수행하기 위하여 아래의 조건이  필요하다.

- tool을 이용한 반복적인 작업의 자동화
- 팀원 모두가 알고 있는 하나의 공유된 지표 필요
- 장애/이슈 발생 시 팀원들과 공유 필요

이러한 맥락에서 등장한 tool 중 하나가 `Jira`이다.



## 시작하기

> **KEYWORD**
>
> - :ballot_box_with_check: `스프린트(Sprint)`:  일정한 주기를 바탕으로 반복되는 개발 주기
> - :ballot_box_with_check: `이슈(Issues)`: 제품에 관해 회사에서 대화의 대상이 되는 거의 모든 것. 쉽게 말하면 `일감`
>   - 이슈의 3가지 카테고리: `Task`, `Bug`, `Story`
>
> [참고사이트](https://hanminwoo.com/60)

| Issue Type |                             설명                             |                          예시                           |
| :--------: | :----------------------------------------------------------: | :-----------------------------------------------------: |
|    Epic    | 최상위 수준의 기능/작업 단위<br />(프로젝트 전반 또는 여러 Sprint에 걸쳐 진행할 정도의 범위) |                 회원 관리, 로그인 관리                  |
|   Story    |         epic에 대한 하위 Level 수준의 기능/작업 단위         | 회원 가입, 회원 정보 수정, 회원 탈퇴, 로그인, 비번 찾기 |
|    Bug     |             프로젝트 개발/검증 중 발견도니 버그              |       상품 검색 시 특정 상품이 조회되지 않는 문제       |
|    Task    | 개발에 직접 해당되지는 않으나 Sprint 안에 포함하여 해야 할 일 |               ERD 작성, 테스트케이스 작성               |
|  Sub-task  |   위 Issue들과 관련하여 세부 단위 작업 등이 필요할 때 등록   |                                                         |



### 1. 스프린트 만들기

- 프로젝트를 시작하고 스프린트를 설정한다.
- `Backlog` 메뉴에서 `스프린트 만들기`를 클릭한다.

### 2. 스프린트에 이슈 등록하기

> 이슈 등록에서 `요약(summary)`과 `설명(description)`이 가장 중요하다.

- 스프린트에서 이슈를 등록한다.
- `summary`와 `description`을 잘 작성하도록 한다.
- 이슈 연결 (이슈 관계)
  - A `cause`s B
    - A가 B의 원인이다.
  - A `block`s B
    - A를 끝내야 B를 할 수 있다.
    - When one issue blocks another, it means that the first issue should be resolved before the second one is resolved.
    - [참고 문서](https://developers.google.com/issue-tracker/guides/block-issue)
  - `clone`
    - 복사, 기존 이슈를 복사하고 싶을 때 clone 사용
  - `duplicate`
    - 중복, 실수로 같은 이슈를 2개 이상 올렸을 때 duplicate로 처리
  - `splite to`, `split from`
    - 분리
  - `relates to`
    - 연관

### 3. 스프린트 시작하기

> 스프린트에 이슈가 1개 이상 있으면 스프린트를 시작할 수 있다.

:ballot_box_with_check: 스프린트에서 중요한 것

- 스프린트 주기
- 시작날짜
- 종료날짜
- 스프린트 목표

### 4. 백로그에 이슈 등록하기

> 스프린트를 시작한 이후 이슈를 등록해야하는 경우, 백로그에서 이슈를 생성하여 등록할 수 있다.

- :white_check_mark: 백로그에만 이슈를 등록하면 활성 스프린트 보드에는 표시가 안된다.
  - 이런 경우, 해당 이슈를 등록할 때 스프린트에 현재 스프린트를 선택해준다!



## JQL

> **Jira Query Language**는 Jira Issue를 구조적으로 **검색**하기 위해 제공하는 언어이다.
>
> - SQL(Standard Query Language)와 비슷한 문법
> - Jira의 각 필드들에 맞는 특수한 예약어 제공
> - 쌓인 Issue들을 재가공해 유의미한 데이터를 도출해 내는데 활용 (Gadget, Agile Board 등)

### 1 JQL Operators

- [x] =, !=, >, >=
- [x] in, not in
- [x] ~ (contains), !~ (not contains)
- [x] is empty, is not empty, is null, is not null
- [x] was, was in, was not in
- [x] changed (from xxx to xxx)

### 2. Relatvie Dates

상대적 날짜값을 사용할 수도 있다.

- 예시

```markdown
- 1d, 2d, 3d
- -1d, -2d, -3d
- 1w, 2w
- -1w, -2w
```

### 3. JQL Keywords

- [x] AND
- [x] OR
- [x] NOT
- [x] EMPTY
- [x] NULL
- [x] ORDER BY (DESC, ASC)

### 4. JQL Funcionts

- [x] endOfDay(), startOfDay()
  - 오늘 24시, 오늘 00시
- [x] endOfWeek(), startOfWeek()
  - Saturday, Sunday
- [x] endOfMonth(), startOfMonth(), endOfYear(), startOfYear()
- [x] currentLogin()
- [x] currnetUser()
- [x] updatedBy(user, dateFrom(optional), dateTo(optional))



## JQL 활용 예시

### 1. Filter share

### 2. Dashboard, Gadget

> Jira 메인 페이지에서 Dashboard를 만들 수 있다.

`Dashboards > Manage Dashboards > Create New Dashboard`

- 대시보드를 생성 후 favorite에 추가하면 메인 페이지에 표시할 수 있다.
- 내 대시보드 관리 페이지에서 gadget을 추가할 수도 있다.

### 3. Agile Board

`Project 메인 > 왼쪽 상단 프로젝트 아이콘 > Create board`에서 생성할 수 있다.

### 4. Issue Export

- 나의 미완료 이슈를 확인하는 페이지에서 `우측 상단 Export 버튼 > (주로) Excel 버튼`을 클릭하면 해당 이슈들을 파일로 다운받아 볼 수 있다.



***opyright* © 2021 Song_Artish**