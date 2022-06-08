# Web Security

---

[TOC]

---



## Overview

자세한 내용은 [Web security](https://developer.mozilla.org/en-US/docs/Web/Security)를 참고한다.



## Browser Security

> 클라이언트 보안 > 브라우저 보안

Browser security is the application of Internet security to web browsers in order to protect networked data and computer systems from breaches of privacy or malware. 

### CORS

CORS(Cross-Origin Resource Sharing) is a system, consisting of transmitting [HTTP headers](https://developer.mozilla.org/en-US/docs/Glossary/HTTP_header), that determines whether browsers block frontend JavaScript code from accessing responses for cross-origin requests.

The [same-origin security policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) forbids cross-origin access to resources. But CORS gives web servers the ability to say they want to opt into allowing cross-origin access to their resources.

![cors](img/cors.jpg)

### XSS 

### CSRF

CSRF(Cross Site Request Forgery)는 다른 사이트에서 유저가 보내는 요청을 조작하는 것이다. CSRF 공격을 위해서는 다음과 같은 조건이 필요하다.

- 쿠키를 사용한 로그인으로, 유저가 로그인 했을 때 쿠키로 어떤 유저인지 알 수 있어야 한다.
- 예측할 수 있는 요청/parameter를 가지고 있어야 한다. 요청에 해커가 모를 수 있는 정보가 담겨 있으면 안 된다.

따라서 이러한 CSRF는 다음과 같이 **방지**할 수 있다.

- **CSRF 토근 사용하기**: 서버 측에서 CSRF 공격에 보호하기 위한 문자열을 유저의 브라우저와 웹 앱에만 제공
- **Same-site cookie 사용하기**: 같은 도메인에서만 세션/쿠키를 사용할 수 있도록



## 암호화

암호화(Encryption)는 일련의 정보를 임의의 방식을 사용하여 다른 형태로 변환하여, 해당 방식에 대한 정보를 소유한 사람을 제외하고 이해할 수 없도록 '알고리즘'을 이용해 정보를 관리하는 과정이다.

```javascript
// 암호화 예시
shiftBy('bicycle', 2)	// => 'dkezeng'
shiftBy('dkezeng', -2)	// => 'bicycle'

const shiftBy = (content, offset) => {
    return content.split('').map(function(letter) => {
		return String.fromCharcode(letter.charCodeAt() + offset)
	}).join('')
}
```

### Hashing

임의의 문자열을 임의의 연산에 적용하여 다른 문자열로 변환하는 것

- 모든 값에 대해 해시 값을 계산하는데 오래 걸리지 않아야 한다.
- 최대한 해시 값을 피해야 하며, 모든 값은 고유한 해시 값을 가진다.
- 아주 작은 단위의 변경이라도 완전히 다른 해시 값을 가져야 한다.

### Salt

암호화해야 하는 값에 어떤 '별도의 값'을 추가하여 결과를 변형하는 것

- 암호화만 해놓으면 해시된 결과가 늘 동일하기 때문에, 해시된 값과 원래 값을 테이블(Rainbow Table)로 만들어서 decoding 해버리는 경우가 발생한다.
- 원본값에 임의로 약속된 '별도의 문자열'을 추가하여 해시를 진행한다면, 기존 해시값과 전혀 다른 해시값이 반환되어 알고리즘이 노출되더라도 원본값을 보호할 수 이도록 하는 안전 장치
- (암호화하려는 값) + (Salt용 값) => (hash 값)

```markdown
주의 사항
- Salt는 유저와 패스워드 별로 유일한 값을 가져야 한다.
- 사용자 계정을 생성할 때와 비밀번호를 변경할 때마다 새로운 임의의 salt를 사용해서 해싱해야 한다.
- Salt는 절대 재사용하지 말아야한다.
- Salt는 DB의 유저 테이블에 같이 저장되어야 한다.
```



***Copyright* © 2022 Song_Artish**