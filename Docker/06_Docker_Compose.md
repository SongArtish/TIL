# Docker Compose

---

[TOC]

---



## Overview

> [공식문서](https://docs.docker.com/compose/reference/)

Compose is a tool for defining and running **multi-container Docker applications**. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.



## 기본 명령어

다음은 docker-compose CLI의 기본 명령어이다.

```bash
# docker-compose.yaml에 저의된 이미지를 컨테이너로 실행한다.
docker-compose up
docker-compose up -d
# 특정 이미지만 컨테이너로 실행한다.
docker-compose up {특정 이미지}
```

- `-d` 옵션을 사용하면 컨테이너를 백그라운드로 실행할 수 있다.

```bash
# docker-compose.yaml에 정의된 이미지를 이용해 실행된 컨테이너를 종료하다.
docker-compose down
```



## 사용하기

docker-compose를 사용하여 2개 이상의 도커 컨테이너를 연결해본다.

먼저 `docker-compose.yaml` 파일을 생성하고 다음과 같이 내용을 작성한다. 파일을 생성할 때 터미널의 위치는 무관하다.

```yaml
# docker-compose.yaml 예시
version: '3.8'

services:
  nginx:
    image: sebcontents/client
    restart: 'always'
    ports:
      - "8080:80"
    container_name: client

  node:
    image: sebcontents/server
    restart: 'always'
    ports:
      - "4999:80"
    container_name: server
```

`yaml` 파일을 실행하고, 컨테이너를 구동한다.

```bash
docker-compose up -d
```

`localhost:8080` 혹은 `127.0.0.1:8080`에서 결과를 확인할 수 있다.



***Copyright* © 2022 Song_Artish**