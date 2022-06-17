# 상태 관리

---

[TOC]

---



## Overview

프론트엔드 개발에서 **상태**는 UI에 동적으로 표현될 데이터를 의미한다. 상태는 특정 컴포넌트 안에서만 관리되는 **로컬 상태**와, 제품 전체 혹은 여러 컴포넌트에서 관리되는 **전역 상태**, 이렇게 2가지로 구분할 수 있다. 전역 상태에서는 특히 데이터 무결성이 지켜질 수 있도록 주의해야 하는데, 이를 위한 방법론으로는 동일한 데이터는 항상 같은 곳에서 데이터를 가지고 올 수 있도록하는 **Single source of truth**가 있다.

**Side Effect**는 함수의 입력 외에도 함수의 결과에 영향을 미치는 요인이며, 이러한 side effect는 최대한 배제하고 컴포넌트를 만들어야 한다. 하지만, 네트워크 요청, API 호출 등 불가피한 경우도 존재한다.



## 상태관리 라이브러리

상태관리 라이브러리를 사용했을 때의 장점은 다음과 같다.

1. 전역 상태를 위한 저장소를 제공
2. Props Drilling 문제 해결: A-B-C-D의 계층으로 이루어진 컴포넌트 구조에서, A, D에는 특정 데이터가 필요하지만, B, C에는 해당 데이터가 필요 없는 경우의 문제를 해결할 수 있다.

### React Context

### Redux

### MobX

### Recoil

```bash
npm install recoil
```





***Copyright* © 2022 Song_Artish**