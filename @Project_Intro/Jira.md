# Jira

2021.01.12

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



## 시작하기

> **KEYWORD**
>
> - :ballot_box_with_check: `스프린트(Sprint)`:  일정한 주기를 바탕으로 반복되는 개발 주기
> - :ballot_box_with_check: `이슈(Issues)`: 제품에 관해 회사에서 대화의 대상이 되는 거의 모든 것. 쉽게 말하면 `일감`
>   - 이슈의 3가지 카테고리
>   - :white_check_mark: `Task`: 업무
>   - :white_check_mark: `Bug`: 수정해야 하는 오류
>   - :white_check_mark: `User Story`: 최종 사용자의 입장에서 무엇이 필요하고, 그것이 왜 필요한지를 설명하기 위한 이슈
>
> [참고사이트](https://hanminwoo.com/60)



### 1. 스프린트 만들기

- 프로젝트를 시작하고 스프린트를 설정한다.
- `Backlog` 메뉴에서 `스프린트 만들기`를 클릭한다.

### 2. 스프린트에 이슈 등록하기

> 이슈 등록에서 `요약(summary)`과 `설명(description)`이 가장 중요하다.

- 스프린트에서 이슈를 등록한다.
- `summary`와 `description`을 잘 작성하도록 한다.

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



***Copyright* © 2021 Song_Artish**