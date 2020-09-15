# JSON

> JavaScript Object Notation. JSON은 자바스크립트의 객체를 표현하는 방식으로, key-value 쌍으로 이루어진 데이터를 전달하기 위한 개방형 표준 포맷이다. 경량의 DATA-교환 형식으로, 언어에 구속되지 않고 자료를 쉽게 주고 받을 수 있는 포맷이다.  [공식 홈페이지]( http://www.json.org/json-ko.html)

---

[TOC]

---



## 1. 데이터 타입

- `문자열(string)`
  - `char` 형식이 없고 한 글자도 `string`으로 취급된다.
- `숫자(number)`
- `boolean`
- `JSON object`
- `array`
- `null`



### 1) JSON Object

- 파이썬의 dictionary와 거의 흡사한 구조

```json
{"name" : "이송영", "age" : 12}
```

### 2) JSON Array (배열)

- 배열에 JSON 객체가 담긴 모습

```json
var array = [
    
    {"name" : "이송영", "age" : 12},
    {"name" : "이송영", "age" : 12},
    {"name" : "이송영", "age" : 12}
    
];
```



## 함수

### `JSON.parse()`

- JSON형태의 String을 객체형 object로 변경하는 메소드