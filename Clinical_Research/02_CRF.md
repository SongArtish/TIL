# Case Report Form

> 계획서에 명시된 임상시험의 목적을 달성하기 위한 최소한의 data collection tool.

2021.07.08

---

[TOC]

---



## 용어

```markdown
### Hierarchy
- CRF Group (Page)
- CRF
- Question
- Item
- (Layout)
```

- Cycle & Visit, Schedule
  - Normal Visit
  - All Visit
  - Repeatable Visit(UV, Cycle 등)



## Type

### Page Type

- CRF page
- Registration Page
- Enroll/Random Page
- AE page
- SAE page
- Laboratory Test

### CRF Type

> class from SDTM

- **Event** - AE, MH, DS 등
- **Intervention** - CM, EX 등
- **Finding** - LB, VS 등
- **Special Purpose** - DM, SV 등

### QST Type

- Normal Question
- Category Question
- Table Question
- Static Rownum Question
- Paging Question
  - [참고문서](https://beta.cubecdms.com/cubedemo_2017/crf/S-3Z-053/48750)

### Layout Type

- Radio
- Check(Item Group)
- Dropdown
  - DropDown
  - DropDown_Other
  - DropDown_Other_MedCode 
- MedCode
- Date, YearMon, Time:
  - YYYY-MM-DD, HH:MM:SS 형태로 입력
  - Date의 경우 년월까지 입력하거나 혹은 년월일에 각각 UK가 적용된 형태의 달력 사용할 수 있음(2021-UK-UK)
- TextInput, TextArea



***Copyright* © 2021 Song_Artish**

