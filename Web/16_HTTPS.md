# HTTPS

---

[TOC]

---



## HTTPS 프로토콜

`HTTPS`는 Hypertext Transfer Protocol Secure Socket layer의 약자이다. HTTP over SSL(TLS), HTTP over Secure라고 부르기도 한다. HTTPS는 HTTP 요청을 SSL 혹은 TLS라는 알고리즘을 이용해, HTTP 통신을 하는 과정에서 내용을 암호화하여 데이터를 전송하는 방식의 인터넷 통신 프로토콜이다.

클라이언트는 서버에 데이터 요청을 하고 이를 사용하기 때문에, 요청 및 응답을 중간에서 가로채는 **중간자 공격**(man-in-the-middle)에 취약하다. 중간자 공격은 클라이언트와 서버 사이에서 공격자가 서로의 요청, 응답의 데이터를 탈취 및 변조하여 다시 전송하는 공격이다. 이를 방지하기 위해  **HTTP 프로토콜 암호화**를 통해 사용자 컴퓨터와 방문한 사이트 간에 전송되는 사용자 데이터의 무결성과 기밀성을 유지할 수 있다.



## SSL/TSL

SSL(Secure Sockets Layer)은 암호화 기반 인터넷 보안 프로토콜로, 전달되는 모든 데이터를 암호화하고 특정 유형의 사이버 공격도 차단한다. TSL(Transport Layer Security)은 SSL의 업데이트 버전이다.

SSL은 개인 정보 보호를 제공하기 위해, 웹에서 전송되는 **데이터를 암호화**한다. 따라서, 데이터를 가로채려해도 거의 **복호화가 불가능**하다. SSL은 클라이언트와 서버 간에 **핸드셰이크를 통해 인증**이 이루어진다. 또한 **데이터 무결성**을 위해 데이터에 디지털 서명을 하여 데이터가 의도적으로 도착하기 전에 조작된 여부를 확인한다.

핸드셰이크는 클라이언트와 서버 간의 메시지 교환이며, HTTPS 웹에 처음 커넥션할 때 진행된다. 핸드셰이크의 단계는 클라이언트와 서버에서 지원하는 암호화 알고리즘, 키 교환 알고리즘에 따라 달라지는데, 일반적으로 **RSA 키 교환 알고리즘**이 사용된다.



## 특징

### 인증서 (Certificate)

브라우저 응답과 함께 전달된 인증서 정보를 확인할 수 있어 데이터 제공자 신원을 보장한다. 브라우저는 인증서에서 해당 인증서를 발급한 CA(Certificate Authority, 공인인증서 발급기관) 정보를 확인하고 인증된 CA가 발급한 인증서가 아니라면 연결이 안전하지 않다는 화면을 보여준다. 또한, 인증서 내용에 서버 도메인 관련 정보가 있어 데이터 제공자의 인증을 용이하게 한다.

### CA

각 브라우저 신뢰할 수 있는 CA(Certificate Authority, 공인 인증서 발급 기관) 정보를 가지고 있다. 

### 비대칭 키 암호화

HTTPS 프로토콜은 암호화된 데이터를 주고받기 때문에, 중간에 인터넷 요청이 탈취되더라도 그 내용을 알아보기 어렵다. 전혀 다른 key 한 쌍으로 암호화 및 복호화를 할 수 있다. 



## HTTPS 서버 구현

[mkcert](https://github.com/FiloSottile/mkcert)라는 프로그램을 이용해서 로컬 환경에 신뢰할 수 있는 인증서를 만들 수 있다.

### 설치하기

다음 명령어를 이용해 설치한다.

```shell
sudo apt install libnss3-tools
wget -O mkcert https://github.com/FiloSottile/mkcert/releases/download/v1.4.3/mkcert-v1.4.3-linux-amd64
chmod +x mkcert
sudo cp mkcert /usr/local/bin/
```

> :warning: **Windows에서는 Ubuntu 환경을 따라서 하면 오류가 날 수 있다!**

Window에서는 다음과 같이 설치한다. 먼저 `cmd`를 관리자 권한으로 실행한다.

```shell
choco install mkcert
```

나머지 아래 내용은 동일하다.

### 인증서 생성

다음 명령어를 통해 로컬을 인증된 발급기관으로 추가한다.

```shell
mkcert -install
```

로컬 환경에 대한 인증서를 생성한다. `localhost`로 대표되는 로컬 환경에 대한 인증서를 만들려면 다음의 명령어를 입력한다. 아래 명령어는 옵션으로 추가한 `localhost`, `127.0.0.1`(IPv4), `::1`(IPv6)에서 사용할 수 있는 인증서를 만든다.

```shell
mkcert -key-file key.pem -cert-file cert.pem localhost 127.0.0.1 ::1
```

`cert.pem`, `key.pem`이라는 파일이 생성된 것을 확인할 수 있다. 인증서(`cert.pem`)는 공개키와 인증기관 서명을 포함하고 있으므로 공개되어도 상관 없지만, `key.pem`은 개인키이므로 git에 commit하지 않고 암호처럼 다루어야 한다.

### HTTPS 서버 작성

node.js 환경에서 HTTPS 서버를 작성하기 위해서는 `https` 내장 모듈을 이용할 수 있다. 먼저 방금 생성한 인증서 파일들을 HTTPS 서버에 적용해준다.

```javascript
// https 모듈 이용
const https = require('https')
const fs = require('fs')

https
    .createServer(
        {
            key: fs.readFileSync(__dirname + '/key.pem', 'utf-8'),
            cert: fs.readFileSync(__dirname + '/cert.pem', 'utf-8'),
        },
        function (req, res) {
            res.write('Congrats! You made https server now :)')
            res.end()
        }
    )
    .listen(3001)

// https://localhost:3001로 접속
```

express.js를 이용해 https 서버를 만들 수도 있다.

```javascript
// express.js 이용
const https = require('https')
const fs = require('fs')
const express = require('express')  // npm install express

const app = express()

https
    .createServer(
        {
            key: fs.readFileSync(__dirname + '/key.pem', 'utf-8'),
            cert: fs.readFileSync(__dirname + '/cert.pem', 'utf-8'),
        },
        app.use('/', (req,res) => {
            res.send('Congrats! You made https server now :)')
        })
    )
    .listen(3001)

// https://localhost:3001로 접속
```

### 서버 실행

이제 서버를 실행한 후 https://localhost:3001로 접속하면 브라우저의 url창 왼쪽에 자물쇠가 잠겨 있는 `HTTPS` 프로토콜을 이용한다는 것을 확인할 수 있다.



***Copyright* © 2022 Song_Artish**
