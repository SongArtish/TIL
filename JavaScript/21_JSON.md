# JSON

---

[TOC]

---



## Overview

JSON(JavaScript Object Notation)은 자바스크립트의 객체를 표현하는 방식으로, key-value 쌍으로 이루어진 **데이터를 전달하기 위한 개방형 표준 포맷**이다. 경량의 DATA-교환 형식으로, 언어에 구속되지 않고 자료를 쉽게 주고 받을 수 있는 포맷이다.

JavaScript에서 객체(object)에 메소드(`obj.toString()`)나 형변환(`String(obj)`)을 시도하면 `[object Object]`라는 결과를 리턴한다. 이 문제를 해결하기 위해서 객체를 JSON 형태로 변환할 수 있다.

- `JSON.stringify`: Object type을 JSON으로 변환
- `JSON.parse`: JSON을 Object type으로 변환



## 기본 규칙

```json
{
    "sender": "SongArtish",
    "receiver": "Young",
    "message": "Hello World",
    "createdAt": "2022-05-13 15:28:30"
}
```

JSON은 자바스크립트 객체와 미묘한 차이가 있다.

|           | JavaScript Object                          | JSON                              |
| --------- | ------------------------------------------ | --------------------------------- |
| **Key**   | 따옴표 없이 사용 가능                      | **반드시 큰 따옴표(`""`)만 사용** |
| **Value** | 어떤 형태의 따옴표(`""`, `''`)도 사용 가능 | **반드시 큰 따옴표(`""`)만 사용** |

:warning: 그리고 JSON은 key와 value 사이, key-value의 쌍 사이에 공백이 있어서는 안 된다.



## Serialize (직렬화)

```javascript
JSON.stringify()
```

Object typedmf JSON으로 변환한다. JSON으로 변환된 객체의 타입은 문자열이다.

```javascript
var jsonObj = {"name":"hse", "age":22, "bool":false};
document.write(jsonObj);

var jsonStr = JSON.stringify(jsonObj);
documnet.write(jsonStr);
```



## Deserialize (역직렬화)

```javascript
JSON.parse()
```

JSON 데이터를 객체 형태로 변환한다.

```javascript
var jsonStr = 
'{"name":"hse", "age":12}'
var jsonObj = JSON.parse(jsonStr);

document.write(jsonObj.name+"<br>");
documnet.write(jsonObj['name']+"<br>")
```

JSON 객체로 변경한 jsonStr에서 `.key`를 이용해서 value를 꺼낼 수 있다. 이러한 접근은 JSON string이 이중삼중으로 되어있으때도, 동일하게 사용할 수 있다.



***Copyright* © 2022 Song_Artish**