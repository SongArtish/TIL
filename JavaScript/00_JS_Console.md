# VS Code에서 자바스크립트 Console 이용하기

> **미완성!!**

---

[TOC]

---



## 1. 디버깅 기능 이용

1. `Run` > `Start Debugging` (단축기 `F5`) 메뉴에 들어간다.
2. `Chrome`을 선택한다.
3. .... ?



## 2. Snippet 예약어 기능

> window 운영체제 기준

1. `File` > `Preferences` > `User Snipets`에 들어간다
2. `javascript`를 검색/선택하여 `javascript.json` 파일로 들어간다.
3. 다음 코드를 입력한다. (코드 조각 만들기)
   - `prefix` : 호출할 예약어
   - `body`의 내용 : 예약어 호출시 출력할 코드

```json
{
  "Print to console": {
    "prefix": "log",
     "body": [
       "console.log('----------------$1----------------');",
       "console.log($2);"
     ],
     "description": "Log output to console"
   }
}
```



***Copyright* © 2020 Song_Artish**