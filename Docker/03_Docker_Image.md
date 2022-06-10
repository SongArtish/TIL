# Docker Image

---

[TOC]

---



## Overview

실행되는 모든 컨테이너는 이미지로부터 생성된다. 이미지는 **애플리케이션 및 애플리케이션 구성을 담아놓은 템플릿**으로, 이를 이용해 즉시 **컨테이너를 만들 수 있다**. 이미지를 이용해 여러 개의 컨테이너를 생성할 수 있는데, 이를 활용하면 애플리케이션의 수평 확장이 가능하다.

이미지는 기본 이미지(base image)로부터 (마치 git을 사용하는 것처럼) 변경 사항을 추가/커밋해서 또 다른 이미지를 만들 수도 있다. 

<img src="img/docker_flow.png" width="60%" />

`도커 이미지가 실행되면 도커 컨테이너가 된다 (출처: codestates)`



## Image

여기서는 예제로 [docker/whalesay](https://hub.docker.com/r/docker/whalesay)라는 이미지를 사용한다. 이미지는 다음과 같이 구분된다.

```
REGISTRY_ACCOUNT/REPOSITORY_NAME: TAG
# Registry Account: docker
# Repository Name: whalesay
```

### Registry

- 도커 이미지를 관리하는 공간이다.
- 특별히 다른 것을 지정하지 않으면, Docker Hub를 기본 레지스트리로 설정한다.
- 레지스트리는 [Docker Hub](https://hub.docker.com/), Private Docker Hub, 회사 내부용 레지스트리 등으로 나뉠 수 있다.

### Repository

- 레지스트리 내에 도커 이미지가 저장되는 공간이다.
- 이미지 이름이 사용되기도 한다.

### Tag

- 같은 이미지라고 해도 버전 별로 내부 내용이 조금은 다를 수 있다.
- 해당 이미지를 설명하는 버전 정보를 주로 입력한다.
- 특별히 다른 것을 지정하지 않으면 `latest` 태그를 붙인 이미지를 가져온다.

따라서 `docker/whalesay:latest`라는 것은 다음과 같이 읽을 수 있다.

- `Docker Hub`라는 레지스트리에서
- `docker`라는 유저가 등록한 `whalesay` 이미지 혹은 레포지토리에서
- `latest` 태그를 가진 이미지



## Registry

레지스트리에는 이미지가 저장된다. 대표적인 이미지 레지스트리로는 `Docker Hub`, `Amazon ECR`이 있다. 도커 CLI에서 이미지를 이용해 컨테이너를 생성할 때, 호스트 컴퓨터에 이미지가 존재하지 않는다면, 기본 레지스트리로부터 다운로드 받게 된다.



***Copyright* © 2022 Song_Artish**