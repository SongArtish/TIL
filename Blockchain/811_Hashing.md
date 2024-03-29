# Hashing

---

[TOC]

---

## 해시 함수

해싱(Hashing)은 다양한 크기의 입력값을 고정된 크기의 출력값으로 생성해내는 과정을 의미한다. 지금까지 배운 암호화는 암호화-복호화 세트로 '원본 보존이 가능한' 암호화인 반면, 해시 함수는 한 번 해싱하면 그 해싱된 값을 통해 입력 값을 유추할 수 없기 때문에 `단방향 암호`라고 부른다. 오늘날에는 여러 종류의 해시 함수가 존재하며, 그중 **암호 해시 함수**는 블록체인 및 다양한 분산 시스템에 데이터 무결성과 보안을 보장하는데 사용된다.

**블록체인에서 해싱의 역할**

기존 해싱은 DB 조회, 파일 분석, 데이터 관리 등에 사용되어 왔으나, 암호 해시 함수는 메시지 인증, 디지털 서명 등 보안 애플리케이션에서 사용될 수 있다. 특히, 암호화폐 프로토콜에서 가장 중요한 기술 중 하나로, 사용자에게 익명성을 보장하고, 트랜잭션을 하나로 연결 및 압축하며, 블록을 연결하는 동시에 그 무결성을 보장하는 역할을 한다.

1. 해시값을 사용해 익명성 보장: 공개키로 해싱한 값을 지갑 주소로 사용해 거래를 익명화

2. 무결성 검증
   
   ```markdown
   1. 블록의 헤더에 있는 `이전 블록 해시`는 `이전 블록의 값을 해싱한 값`을 사용해 이전 블록을 가리킨다.
   만약 이전 블록을 해싱한 값이 달라진 경우, 해당 블록 또는 이전 블록에 위변조를 알 수 있다.
   2. 블록에 저장된 모든 트랜잭션을 머클 트리 알고리즘을 사용해 하나의 해시값으로 저장하여 `머클 루트`를 만든다.
   만약 트랜잭션이 하나라도 변한 경우, 머클 루트의 값이 변했다는 것을 통해 위변조를 알 수 있다.
   3. 입력값을 일정한 길이의 값으로 축약해주는 특성을 사용하여 대용량 파일의 문서를 해싱한 뒤, 해싱된 값만 비교하여 위변조를 알 수 있다.
   ```
   
   이러한 방식은 고정된 크기의 해시값만 비교하기 때문에 많은 양의 데이터를 저장할 필요 없이 무결성을 검증할 수 있다.

3. 해시값을 사용해 채굴 노드를 정함: PoW 방식에서는 특정 조건을 만족하는 해시값을 만족하기 위해 입력값인 Nonce를 찾아야 한다.

## 해시 알고리즘

- **Division Method**: Number type의 key를 저장소의 크기로 나누어, 나온 나머지를 index로 사용하는 방법이다. 이때 저장소의 크기를 Prime Number(소수)로 정하고 2의 제곱수와 먼 값을 사용하는 것이 효과가 좋다. 예를 들어 key 값이 23일 때, 테이블 크기가 7이라면 index는 2가 된다.

- **Digit Folding**: key의 문자열을 ASCII 코드로 바꾸고 그 값을 합해 저장소에서 index로 사용하는 방법이다. 만약 이때 index가 저장소의 크기를 넘어간다면 `Division Method`를 적용할 수 있다.

- **Multiplication Method**: 숫자로 된 key 값 K와 0과 1 사이의 실수 A, 보통 2의 제곱수인 m을 사용하여 다음과 같이 계산한 값을 사용한다.
  
  $$
  index = (KA mod 1)m
  $$

- **Universal Hashing**: 다수의 해시함수를 만들어  특정한 장소에 넣어두고, 무작위로 해시함수를 선택해 해시값을 만드는 기법이다.

## SHA

SHA(Secure Hash Algorithm)는 해시함수를 이용해 만든 해시 암호화 알고리즘의 모음이다. SHA는 미 국가보안국(NSA)에서 1993년 처음 설계하였으며, 미국 국립표준기술연구소(NIST)에서 발전시켜 오늘날 미국의 국가표준으로 자리잡았다.

SHA의 종류로는 `SHA-0`, `SHA-1`, `SHA-2`, `SHA-3` 등이 있으며, `SHA-0`과 `SHA-1`은 충돌이 감지되어 더 이상 사용되지 않으며, 오늘날 많이 사용되는 함수군은 `SHA-2`이다. SHA-2에는 SHA-224, SHA-256, SHA-364, SHA-512가 있다.

일반적인 암호화 알고리즘은 데이터를 숨기고 안전하게 전달하는 기밀성이 목적이지만, SHA의 목적은 데이터의 위변조가 불가능함을 보장하는 **무결성**이다. 실제 비트코인이나 이더리움에서 블록헤더, 디지털 서명, 공개 키에서는 데이터 무결성을 위해 SHA를 사용한다.

## 해시 함수 안전성 평가 요소

앞서 살펴본 것처럼 해시 함수는 '항상 고정된 길이의 출력값' 때문에 **해시 충돌**이 발생할 수도 있다. 충돌은 해시 함수를 만들 때 가장 중요한 요소 중 하나로 작용한다.

> 해시 충돌: 서로 다른 입력값을 해시 하수에 넣었는데 동일한 출력값을 내뱉는 경우

이를 종합해보면 암호 해시 함수의 안전성을 평가하는 요소를 다음 세 가지로 볼 수 있다.

- **충돌 저항성**: 어떤 해시 함수가 충돌하는 서로 다른 두 입력값을 가졌는지 발견되지 않은 상태.
  
  SHA-256은 2^256개의 경우의 수를 가지기 때문에 충돌을 찾는 것은 불가능에 가깝다. 따라서 충돌이 없는 해시 함수는 존재하지 않지만, 충돌 저항성이 있다고 간주되는 해시 함수는 존재한다.

- **역상 저항성**(Preimage Resistance): 어떤 해시 함수가 특정한 값을 출력하는 입력값을 찾을 확률이 매우 낮을 경우

- **제2 역상 저항성**: 충돌 저항성과 역상 저항성이 복합적으로 작용한 경우로, A라는 입력값의 해시값과 동일한 해시값을 내는 B 입력값을 누군가가 알고 있지 않은 경우 (만약 알고 있는 경우 제2 역상 공격이 가능하다.)

## 해시 충돌 해결법

### Open Addressing(개방 연결법)

#### Linear Probing

선형 프로빙은 **충돌이 발생할 경우 빈 slot이 나올 때까지 탐색 후, 빈 slot이 나오면 위치가 결정**된다.
$$
h(k, i) = (h'(k)+i) mod m
$$
(여기서 k는 key, i는 충돌 횟수, h()는 해시 함수, m은 해시 테이블 크기)

구현은 매우 쉬우나 primary clustering 문제가 있다.

> **Primary Clustering**: 한 번 충돌이나면 집중적으로 충돌이 발생하는 것을 의미하여, 이로 인해 평균 검색 시간이 증가한다.

#### Quadratic Probing

이차식 프로빙은 다음과 같은 해시 함수를 사용한다. i에 대한 2차 함수 꼴로 slot을 이동하면서 빈 slot을 찾는다.
$$
h(k, i) = (h'(k) + c_1i+c_2i^2) mod m
$$
(여기서 h는 보조 해시 함수, c1, c2는 0이 아닌 상수)

선형 프로빙(Linear Probing)에 비해 충돌은 적지만, secondary clustering이 발생한다.

> **Secondary Clustering**: 처음 충돌한 위치가 같다면 다음 충돌할 위치도 반복적으로 계속 충돌이 나게 되는 것

#### Double Hashing Probing

이중 해시는 다음과 같은 형태의 해시 함수를 사용한다. 충돌이 없을 때는 h1으로 위치를 탐색하고, 충돌이 있으면 `h_2 mod m`만큼 이동하면서 탐색한다.
$$
h(k, i) = (h_1(k) + ih_2(k)) mod m
$$

### Separate Chaining(분리 연결법)

**충돌 시 연결 리스트에 추가하는 방식**이다. 이 방법은 연결 리스트로 인해 최악의 경우 수행 시간이 O(n)이 된다.

***Copyright* © 2022 Song_Artish**