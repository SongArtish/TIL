

# Data Driven 디자인

---

[TOC]

---



## 데이터 중심적 사고

### 가설과 검증

```markdown
**과정**
1. 가설
2. 실험
3. 검증 및 가설 수정
```

**가설**

```
어떤 문제나 사안에 대해서 우리가 가지고 있는 예측
```

**지표**

```
성과, 상태를 측정해서 수치화한 것
```

> 분석의 본질은 매우 중요한 지표를 추적하는 것이다.

- 좋은 지표의 조건

  ```
  1. 상대적이다 (ex. 전환율이 지난 주보다 2% 증가)
  2. 이해하기 쉽다
  3. 의사결정에 도움이 된다.
  ```

<참고> 효과적인 데이터 분석에 도움이 되는 4개의 중요 질문

```
- 어떤 목표의 프로젝트인가?
- 가설은 무엇인가?
- 무엇을 개선하려고 하는가?
- 어떻게 검증할 것인가?
```

### OMTM

> One Metric That Matters

- 정말로 중요한 한 개의 지표
- 늘 바라보고 방향을 잡을 수 있다는 점에서 북극성(the north start metric)이라고도 한다.
- Resource가 제한적인 상황에서 너무 여러 가지 목표를 추구하면 우선순위를 잃기 쉬우니 정말 중요한 지표 하나에만 역량을 집중할 수 있게 해준다.



## Data Driven Design

1. 사용자들에 대한 정량적인 행동패턴과 양상 파악
2. 고객이 직접 말하지 않는 요구사항 파악

### 데이터의 구분

1. 내부 데이터
   - DB에 저장
2. 외부 데이터
   - 특정 코드를 삽입하여 외부 서비스를 통해 분석

### 데이터 분석 Tool

#### 1. Google Analytics (GA)

- 웹사이트 방문자의 데이터를 수집해서 분석
- 웹 서비스의 성과를 측정하고 개선
- 방문자별 유입채널, 나라별 분포, 디바이스 사용도 등의 간단한 분포 등 뿐만 아니라 키워드 별 유입률과 전환률 등 의사결정을 위한 리포트를 제공

#### 2. Crazy Egg

- 마우스 클릭, 스크롤, hover 등 사용자가 서비스를 이용하는 행태를 정량적으로 확인 가능
- **Confetti** 기능: 시간, 유입경로, 지역에 따라 다른 색으로 표기하여 기준에 따른 경향성 파악 가능
- 이와 비슷한 서비스로 **Beasable**이 있음

#### 3. Firebase

- 모바일 앱의 방문자 데이터를 수집해서 분석
- iOS, 안드로이드 모두 분석 가능
- 앱 설치율, 이탈률, 리텐션 등 다양한 데이터를 제공

>  아래는 모바일 앱 분석 Tool이다.

#### 4. Adjust

- 광고매체 효율 분석

#### 5. Amplitude

- 사용자 행동 데이터 분석

#### 6. Braze

- 푸시 메시지 최적화

#### 7. SQL

> 내부 데이터 분석 Tool

- 내부 데이터를 관리하고 효과적인 분석이 가능
- 데이터 구조를 생각하며 디자인하게 된다.
- 필요할 때 데이터를 빠르게 확인할 수 있어 의사 결정 속도가빨라진다.



***Copyright* © 2022 Song_Artish**
