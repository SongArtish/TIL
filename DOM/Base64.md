# Base 64

2021.04.01

---

[TOC]

---



## 개념

> 8비트 2진 데이터를 (플랫폼의) 문자 코드에 영향을 받지 않는 **공통 ASCII 영역**의 문자들로만 이루어진 일련의 문자열로 바꾸는 **인코딩 방식**

- Base 64는 데이터를 64진법으로 나타낸다.
- Base 64의 정확한 규격은 RFC 1421, RFC 2045에 정의된다.

**Caution**

- *base64를 사용하면 encoding과 decoding 과정에서 시간이 많이 걸릴 수도 있다.*



## 변환 과정

1. 24비트 버퍼에 위쪽(MSB)부터 1바이트 (8비트)씩 3바이트를 채운다.
2. 3바이트 보다 미만이라면, 버퍼의 남은 부분은 0으로 채워넣는다.
3. 버퍼의 위쪽부터 6비트씩 잘라 그 값을 읽어, Base 64 의 값으려 변경한다.
4. 버퍼의 남은 부분을 0으로 채운 값을 1바이트당 = 코드로 변경한다



## JavaScript에서의 Base 64 변환

### btoa()

- (DOMString data) **DOMString**
- 입력 문자열을 Base 64로 표현되는 문자열로 반환
- 만약 입력 문자열에 unicode 같은 btoa에서 이해할 수 없는 문자열이 들어오면 `InvalidaCharacterError`가 발생

### atob()

- (DOMString data) **ByteString**
- 인코딩된 Base 64 문자열을 디코드
- 만약 입력 문자열에 Base 64에 포함되지 않는 문자가 입력되면 `DOMException`이 발생

```javascript
window.btoa('Man');
// TWFu
window.btoa('TWFu');
// Man
window.btoa('\u');
// Uncaught SyntaxError: Invalid Unicode escape sequence
window.atob('🙂');
// Uncaught DOMException: Failed to execute 'atob' on 'Window'
```



***Copyright* © 2021 Song_Artish**