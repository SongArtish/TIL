# cubeBUILDER DCL

> Entry와 ECS에 포함되지 않는 **기타 기능**을 집합

2021.07.XX

---

[TOC]

---



## 1. Normal Range



## 2. Medical Coding

> `DCL > Medical Coding` 메뉴에서는 **연구자가 입력한 병력/약력에 대해서 DM이 다시 코딩을 하는 기능을 세팅**한다.

- `Create` 버튼을 눌려서 카테고리 및 coder를 입력한다.
  - 예시 - MH(Category ID), Medical History(Category label, Description)
- Categoruy type 및 dictionary에서 적절한 값을 설정해준다.
  - 예시 - Medical Term > MedDRA
- :arrow_forward: 아래의 리스트는 **CMDS 코딩 메뉴에 있는 리스트의 column을 설정**하는 곳이다.
  - :exclamation: 필수로 체크되어 있는 `AE_NAME` column의 우측 item 창을 클릭해서 item을 연결해준다.
    - 예시 - `MHTERM(MH)`
  - relationship이 있는 항목의 경우, `RELATION`에 visible을 체크해주고, 아이템에 `-REL`도 추가해준다.
- 그리고 저장을 해준다.
- 실습에서는 <u>MT, AE, CM</u>을 Medical Coding List에 추가해준다.



## 3. Menu



***Copyright* © 2021 Song_Artish**
