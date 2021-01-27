# Docker

2021.01.27

---

[TOC]

---



## 개념

> OS 레벨 가상화를 이용하여 컨테이너화 된 소프트웨어 패키징/관리가 가능한 가상화 도구

- 가상화 컨테이너에 application 배포를 자동화 시켜주는 오픈 소스 엔진이다.
- 컨테이너를 통한 가상화 기술은 호스트 OS의 커널과 하드웨어르 바로 사용할 수 있어 overhead가 적고 가볍다.
- Linux의 커널 기능을 활용해서 구현

**`image` vs `container`**

> 컨테이너화를 하기 위해서는 서버를 기술한 설계도인 Dockerfile이 필요하다. Dockerfile을 빌드하면 OS와 앱이 포함된 image가 생기며, `image`를 run하면 앱이 실행되고 있는 `container`가 생긴다.

- image와 container의 관계는 class와 instance의 관계와 비슷하다.
- image는 스택처럼 쌓인 구조를 가지고 있으며, 자식 이미지는 부모 이미지를 reference한다.
- image는 read only지만, container는 writable하다.

**장점**

- Speed: No OS to boot
- Portability: Less dependencies btw proccess layers
- Efficiency: Less OS overhead, imporved resource efficiency



## 예시

```
$ docker run busybox echo hello world
```

- docker가 `busybox` 이미지를 다운받아 컨테이너를 만들어 실행한 후, `hello world`를 출력하고 죽는다.

```
$ docker run alpine cat /etc/issue
```

- 호스트 OS에 상관없이 위 명령어를 실행하면 docker 위에서 alpine 리눅스를 사용할 수 있다.
  - `alpine`은 경량화된 데비안 계열의 리눅스이다.

```
$ docker images
```

- 내려 받아진 이미지들을 확인할 수 있다.



***Copyright* © 2021 Song_Artish**