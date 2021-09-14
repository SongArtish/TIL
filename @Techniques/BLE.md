# BLE

> Bluetooth Low Energy (저전력 근거리 통신 기술)

---

[TOC]

---



## 개념

> Bluetooth 4.0부터 새롭게 포함된 저전력 통신 기술

- 저전력을 최우선시하는 통신 기술
  - 단, 데이터 전송 속도도 느리고 한 번에 전달하는 양도 적다!
- wibree라는 이름으로 개발되었으나 BT의 명성을 이용해서 빠르게 확대됨
  - BT: Bluetooth Technology
- BT와 BLE의 기술 조합 기준
  - Classic(BT)
  - Smart(BLE)
  - Smart Ready



## 핵심 기술

### 1. Advertise Mode

> Advertising Packet을 보내고 누군가는 그것을 찾아서 연결을 시도하는 과정이 이루어짐

- (= Broadcast Mode)
- Advertising Packet: 두 기기가 무선 통신을 하기 위해 서로의 존재를 알리는 신호

```markdown
Beacon
> 근거리에 있는 스마트 기기를 자동으로 인식하여 필요한 데이터를 전송할 수 있는 무선 통신 장치

- Advertising Packet 신호를 하루 종일 1년 12달 자신을 알리는 신호로 쏘고 있는 것
- 최대 50m 거리까지 동작
- 작은 버튼 셀 배터리로도 1~2년 동안 사용 가능
```

- Scan Request, Scan Response로 추가 정보를 주고 받는 기능도 구현할 수 있다.



### 2. Connection Mode

> Advertise Mode에서 알게된 기기 중에 하나를 선택해서 1:1로 연결하는 것

- Connection Mode로 전환되고 나서는 서로 타이밍을 맞춰서 데이터를 주고 받는다.
- 이전 모드에서 진행했던 과정은 더 이상 진행하지 않는다 - Advertising과 Scan



***Copyright* © 2021 Song_Artish**