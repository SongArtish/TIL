# Vuex

2020.11.13

> Vue.js 애플리케이션에 대한 상태 관리 패턴 + 라이브러리 (중앙 집중식 저장소)

---

[TOC]

---



## 상태관리패턴

```markdown
Vuex는 모든 컴포넌트를 트리에 상관없이 상태(data)에 액세스하거나 동작을 트리거 할 수 있게 해주는 라이브러리이며 중대형 규모의 SPA에 적합하다.
```

**Vuex Concept**

![Vuex Concept](img/vuex_concept.png)

- `state`: 앱을 작동하는 원본 소스이다.
- `view` : 상태의 선언적 매핑
- `action` : 뷰에서 사용자 입력에 대해 반응적으로 상태를 바꾸는 방법



## :black_large_square: State

중앙에서 관리하는 모든 `데이터(data)`



## :black_large_square: Getter

저장소의 상태를 기준으로 계산해야 하는 값. `computed`와 유사하며, 실제 상태(data)를 변경하지는 않는다.



## :black_large_square: Mutations

State를 변경하는 로직

- 동기적인 작업
- 메서드 호출 : `commit`
- 첫 번째 인자 : `state`

상태를 변경시키기 때문에 첫 번째 인자로 항상 state를 받는다.

```javascript
mutations: {
    <함수명>: function (state, <매개변수>) {
        <코드블럭>
    }}
```



## :black_large_square: Action

state를 직접 변경하지 않고 mutations에 정의된 메서드를 호출해서 변경한다. (데이터 fetch 및 처리 & 가공)

- 비동기 작업
- 메서드 호출 : `dispatch`
- 첫 번째 인자 : `context`

```javascript
actions: {
    <함수명>: function (context, <매개인자>) {
        <코드블럭>
    }}
```



***Copyright* © 2020 Song_Artish**