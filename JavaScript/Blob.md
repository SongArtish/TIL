# Blob

> Binary Large Object

2021.03.30

---

[TOC]

---



## 개념

> **Bloc(Binary Large Object, 블랍)**은 JavaScript에서 이미지, 사운드, 비디오와 같은 **멀티미디어 데이터**를 다룰 때 사용한다.

- 데이터의 크기(Byte) 및 MIME 타입을 알아낼 때
- 데이터 송수신을 위한 작은 Blob 객체로 나누는 작업을 할 때

**File 객체**도 `name`과 `lastModifiedData` 속성이 존재하는 Blob 객체이다.

```javascript
// 예시
File {name: "Ari_logo.png", lastModified: 1508417967000}
```



## 생성

- 생성 시 인수로 `array`와 `options`를 받는다.

```javascript
const newBlob = new Blob(array, options);
```



***Copyright* © 2021 Song_Artish**