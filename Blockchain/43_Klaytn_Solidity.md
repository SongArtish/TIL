# Klaytn Solidity

---

[TOC]

---



## Version

솔리디티는 2014년 8월 처음 제안된 이후로 계속해서 업그레이드가 되고 있으며 현재 최신 버전은 0.8.14이다. 그에 반해 클레이튼(Klaytn)에서는 솔리디티 0.5.6 버전을 사용하고 있다.

**0.5와 0.8 버전의 주요 차이점**

|                   차이점                   |                           0.5 버전                           |                           0.8 버전                           | 업데이트 버전 |
| :----------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :-----------: |
|           **배열의 length 권한**           | length의 값을 변경하여 스토리지에 저장된 배열의 크기를 변경할 수 있음 |                      length는 read-only                      |      0.6      |
|          **push(value) 반환 값**           |                   새로운 배열의 길이 반환                    |                   아무 것도 반환하지 않음                    |      0.6      |
|             **fallback 함수**              |                        익명 함수 형태                        |  fallback과 receive 키워드를 사용해 fallback 함수 지정 가능  |      0.6      |
|         **now와 block.timestamp**          |        글로벌 변수 now가 블록 생성 시간을 값으로 가짐        |        now는 deprecated되고, blcok.timestamp로 대체됨        |      0.7      |
|               **UTF-8 지원**               |                              -                               | 유니코드 문자열 지원<br />문자열 앞에 unicode 키워드를 붙여 사용 가능<br />(ex. unicode"Hello😄") |      0.7      |
|           **상태 변환성 키워드**           |                              -                               | pure와 view 키워드로 함수에서 일어나는 스토리지 CRUD 여부를 나타냄 |      0.7      |
|         **누승법(exponentiation)**         |   왼쪽에서부터 파싱 a**b**c 연산은 (a**b)**c 순서로 수행됨   | 오른쪽에서부터 파싱<br />a**b**c 연산은 a**(b**c) 순서로 수행됨 |      0.8      |
|             **this, super, _**             |                   모든 함수에서 사용 가능                    |          public 함수와 이벤트를 제외하고 사용 불가           |      0.8      |
|  **address 타입과 address payable 타입**   |           address 타입 자체로 송금 가능한 주소 값            | address 타입 자체는 송금이 불가능한 주소 타입<br />address 타입을 payable(address 타입 변수)로 변환해야 송금 가능한 주소값(address type)이 됨 |      0.8      |
| **글로벌 변수 tx.origin, msg.sender 타입** |                     address payable 타입                     |                    송금이 안 되는 address                    |      0.8      |



***Copyright* © 2022 Song_Artish**