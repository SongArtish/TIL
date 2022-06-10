# Dockerizing

---

[TOC]

---



## Overview

도커라이징(Dockerizing) 혹은 컨테이너화는, 애플리케이션을 도커 컨테이너에서 돌릴 수 있도록 이미지를 만드는 과정을 의미한다.



## Node.js 웹 앱의 도커라이징

다음은 node 및 express를 이용해 단순한 앱을 컨테이너화 하는 튜토리얼이다. 먼저 간단한 Node.js 웹 애플리케이션을 만든 후에 이 애플리케이션을 위한 Docker 이미지를 만들어서 컨테이너로 실행한다.

> [공식 문서](https://nodejs.org/ko/docs/guides/nodejs-docker-webapp/)

### 1. Node.js 앱 생성

먼저 디렉토리를 생성하고, 해당 디렉토리에 애플리케이션과 의존성을 알려주는 `package.json` 파일을 생성한다. (`npm init` 명령어를 통해서 생성할 수도 있다.)

```json
// package.json
{
  "name": "docker_web_app",
  "version": "1.0.0",
  "description": "Node.js on Docker",
  "author": "First Last <first.last@example.com>",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.16.1"
  }
}
```

`package.json` 파일을 만든 후, `npm install`을 실행해서 패키지를 설치하고, `package-lock.json` 파일을 생성한다.

이제 Express.js 프레임워크로 웹앱을 정의하는 `server.js`를 만든다.

```javascript
// server.js
'use strict';

const express = require('express');

// 상수
const PORT = 8080;
const HOST = '0.0.0.0';

// 앱
const app = express();
app.get('/', (req, res) => {
  res.send('Hello World');
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
```

### 2. Dockerfile 생성

이번에는 Docker 이미지를 생성한다. `Dockerfile`이라는 빈 파일을 생성한다.

```shell
touch Dockerfile
```

선호하는 텍스트 에디터로 `Dockerfile`을 연다. 그리고 Dockerfile을 작성해준다.

```dockerfile
# 어떤 이미지를 사용해서 빌드한 것인지 정의 (node 버전 12)
FROM node:12

# 앱 디렉토리 생성
WORKDIR /usr/src/app

# 앱 의존성 설치
# 가능한 경우(npm@5+) package.json과 package-lock.json을 모두 복사하기 위해
# 와일드카드 사용
COPY package*.json ./

RUN npm install
# 프로덕션을 위한 코드를 빌드하는 경우
# RUN npm ci --only=production

# 앱 소스 추가
# Docker 이미지 안에 앱의 소스코드를 넣기 위해서는 COPY 지시어 사용
COPY . .

# 앱이 8080포트에 바인딩 되어 있으므로
# EXPOSE 지시어를 사용해서 docker 데몬에 매핑
EXPOSE 8080

# 런타임을 정의하는 CMD로, 앱을 실행하는 명령어 정의
# 여기서는 npm start인 `node server.js`를 실행하도록
CMD ["node", "server.js"]
```

### 3. .dockerignore 파일

`Dockerfile`과 같은 디렉토리에 `.dockerignore` 파일을 생성한 후 아래 내용을 입력한다.

```
node_modules
npm-debug.log
```

이는 Docker 이미지에 로컬 모듈과 디버깅 로그를 복사하는 것을 막앗서 이미지 내에서 설치한 모듈을 덮어쓰지 않게 한다.

### 4. 이미지 빌드

작성한 `Dockerfile`이 있는 디렉토리로 가서 Docker 이미지를 빌드하는 다음 명령어를 실행한다. `-t` 플래그로 이미지에 태그를 추가할 수 있으며, 나중에 `docker images` 명령어로 쉽게 찾을 수 있다.

```bash
docker build . -t <TAG_NAME>
docker build . -t bulgen/node-web/app # 예시
```

태그 설정을 완료하고 Docker가 빌드한 이미지를 보여줄 것이다.

```bash
docker images
# 예시
REPOSITORY                      TAG        ID              CREATED
node                            12         1934b0b038d1    5 days ago
<your username>/node-web-app    latest     d64d3505b0d2    1 minute ago
```

### 5. 이미지 실행

- `-d`  flag: 분리 모드로 컨테이너를 실행해서 백그라운드에서 컨테이너가 돌아가도록 함
- `-p` flag: 공개 포트를 컨테이너 내의 비공개 포트로 redirect한다.

앞에서 만든 이미지를 실행한다.

```bash
docker run -p 49160:8080 -d <TAG_NAME>
docker run -p 49160:8080 -d bulgen/node-web/app # 예시
```

앱의 로그를 출력한다.

```bash
# 컨테이너 아이디를 확인합니다
$ docker ps

# 앱 로그를 출력합니다
$ docker logs <container id>
# 예시
Running on http://localhost:8080
```

컨테이너 안에 들어가봐야 한다면 `exec` 명령어를 사용할 수 있다.

```bash
# 컨테이너에 들어갑니다
$ docker exec -it <container id> /bin/bash
```

### 6. 테스트

앱을 테스트하려면 Docker 매핑된 앱 포트를 확인한다.

```bash
$ docker ps
# 예시
ID            IMAGE                                COMMAND    ...   PORTS
ecce33b30ebf  <your username>/node-web-app:latest  npm start  ...   49160->8080
```

위 예시에서는 Docker가 컨테이너 내의 `8080` 포트를 머신의 `49160` 포트로 매핑했다. 이제 `curl`로 앱을 호출할 수 있다.

```bash
$ curl -i localhost:49160

HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 12
ETag: W/"c-M6tWOb/Y57lesdjQuHeB1P/qTV0"
Date: Mon, 13 Nov 2017 20:53:59 GMT
Connection: keep-alive

Hello world
```



***Copyright* ©2022 Song_Artish**