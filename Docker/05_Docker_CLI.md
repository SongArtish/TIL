# Docker CLI

---

[TOC]

---



## Overview

> [공식문서](https://docs.docker.com/engine/reference/commandline/container_run/)

Docker Image 및 Container를 다루기 위한 Docker Command Line 명령어를 알아본다. 전반적인 구조는 다음과 같다.

- `Docker Hub` 등의 레지스트리에서 로컬로 이미지를 가져온다. (`docker image pull`)
- 저장한 이미지로 컨테이너를 실행한다. (`docker container run`)

> 여기서는 예제로 [docker/whalesay](https://hub.docker.com/r/docker/whalesay) 레포지토리를 사용한다.



## Image

### Image 가져오기

`docker/whalesay`의 최신(태그가 latest인) 이미지를 받아온다.

```bash
# docket image pull: 레지스트리에서 이미지 혹은 레포지토리를 가져온다.
docker image pull docker/whalesay:latest
# 혹은
docker pull docker/whalesay
```

- :warning: Ubuntu에서 실행하는 경우에는 모든 명령어 앞에 **sudo**를 붙여야 한다.

### Image 리스트 출력

이미지 리스트를 출력한다. 용량 등 이미지에 대한 정보를 확인할 수 있다.

```bash
docker image ls
```

### Image 삭제

`docker/whalesay` 이미지를 삭제한다. `docker rmi`도 같은 기능을 수행한다.

```bash
# docker image rm: 이미지를 지정해서 삭제
docker image rm IMAGE_NAME(IMAGE_ID)
docker image rm docker/whalesay	# 예시
```

만약 해당 이미지가 다른 곳에서 사용 중이어서 삭제가 안 될 경우에는 `-f` 옵션을 사용한다.

```bash
docker image rm -f IMAGE_NAME(IMAGE_ID)
docker image rm -f docker/whalesay	# 예시
```



## Container

### Container 리스트  조회

모든 컨테이너의 리스트를 출력한다.

```bash
# docker container ps: 컨테이너의 리스트를 출력한다.
docker container ps -a
```

- `-a`: Default로는 실행되는 컨테이너지만 종료된 컨테이너를 포함하여 모든 컨테이너를 출력

### Container 삭제

특정 이름을 가진 컨테이너를 삭제한다.

```bash
# docker container rm: 컨테이너를 지칭해서 삭제
docker container rm CONTAINER_NAME
```

`rm` 명령어에서 컨테이너를 명시할 때는 `ps` 명령을 통해 확인할 수 있는 NAMES 혹은 CONTAINER ID를 사용한다.

### Container 종료

실행되고 있는 container는, container 안에서 `Ctrl` + `C`로 종료할 수 있다.



## Image -> Container (Container 실행)

> [Docker run reference](https://docs.docker.com/engine/reference/run/)

받아온 이미지로 컨테이너를 실행한다. (이미지 -> 컨테이너)

```bash
# docker container run: 컨테이너를 실행한다.
docker container run --name 사용할_컨테이너_이름 IMAGE_NAME cowsay ARGUMENTS
docker container run --name 사용할_컨테이너_이름  docker/whalesay:latest cowsay boo	# 예시
```

- `[OPTIONS]` --name: 컨테이너의 이름을 할당한다.
- `[COMMAND]`: 초기 컨테이너 실행 시 수행되는 명령어로, 컨테이너 실행 시 `cowsay`를 호출한다. (node 호출하듯)
- `[ARG...]` boo: COMMAND인 cowsay에 넘겨질 파라미터

다음과 같이 `-i`, `-t`의 옵션을 사용할 수도 있다. 여기서 `-it`는 `-i`와 `-t`를 동시에 사용한 옵션이다. **사용자와 컨테이너 간의 interaction이 필요하다면** 이 옵션을 사용한다. 예시는 `danielkraic`이라는 사람이 올린 이미지 `asciiquarium`을 실행한다. 

```bash
docker container run -it --rm danielkraic/asciiquarium:latest
```

- `-i` 옵션: Keep STDIN open even if not attached
- `-t` 옵션: Allocate a pseudo-tty

아래 명령어를 사용하면, 이미지를 받아와 컨테이너 실행하고, 컨테이너와 관련된 리소스 삭제하는 작업까지 **한 번에 수행**할 수 있다.

```bash
docker container run --name 사용할_컨테이너_이름 --rm docker/whalesay cowsay boo
```





## Container -> Image

이번에는 앞서 만들어 본 Docker Container를 이미지 파일로 변환한다. 이미지로 만들어 놓았을 때의 장점은 다음과 같다.

- 이전에 작업했던 내용을 다시 한 번 수행하지 않아도 됨
- **배포 및 관리가 용이**

아래에서는 이미지를 만드는 방식 2가지를 소개한다.

### 1) Commit 이용

[docker container commit](https://docs.docker.com/engine/reference/commandline/container_commit/) 명령어를 이용한다.

```bash
docker container commit CONTAINER_NAME 사용할_이미지_이름(:태그)
docker container commit pacman-canvas my_pacman:1.0	# 예시
```

생성된 이미지가 잘 작동하는지 `900`번 포트에서 웹 서버로 구동해보고, `127.0.0.1:900` 혹은 `localhost:900`을 통해 웹서버가 작동하고 있는지 확인한다.

```bash
docker run --name 사용할_컨테이너_이름 -p PORT:사용할_로컬호스트_포트번호:컨테이너_포트번호 IMAGE_NAME
docker run --name pacman-canvas2 -p 900:80 my_pacman:1.0
```

### 2) Dockerfile 생성

> [DockerFile 공식 문서](https://docs.docker.com/engine/reference/builder/)

Dockerfile을 만들고, Dockerfile대로 이미지를 `build`할 수 있다. Dockerfile은 이미지 파일의 설명서라고 생각하면 된다.

먼저 `Dockerfile`을 생성한다. 직접 생성하거나, 명령어를 통해 생성할 수 있다.

```bash
touch Dockerfile
```

`Dockerfile`에 내용을 입력해준다.

```dockerfile
# Dockerfile 예시
FROM httpd:2.4	# 베이스 이미지를 httpd:2.4로 사용한다.
COPY ./ /usr/local/apache2/htdocs/	# 호스트의 현재 경로(./)에 있는 파일을 생성할 이미지 경로(/usr/local/apache2/htdocs/)에 복사한다.
```

다음으로 `docker build` 명령어를 입력하여 Dockerfile로 도커 이미지 파일을 생성한다.

```bash
# 지정한 경로에 있는 Dockerfile을 찾아서 빌드한다.
docker build --tag 생성할_이미지_이름:TAG
docker build --tag my_pacman:2.0	# 예시
```

- `--tag` 옵션: `name:tag` 형식으로 이미지를 생성할 수 있게 한다.

완료가 되면 생성된 이미지가 잘 작동하는지 `900`번 포트에서 웹 서버로 구동해보고, `127.0.0.1:900` 혹은 `localhost:900`을 통해 웹서버가 작동하고 있는지 확인한다.

```bash
docker fun --name my_web3 -p 901:80 my_pacman:2.0
```



## CP 이용하기

도커 이미지에 구성되어 있지 않은 내용을 추가적으로 개발해야 하는 경우, 로컬에 있는 파일과 도커 이미지를 연결해야 한다. 이를 위해서는 크게 CP(Copy)를 이용하는 방법과 Docker Volume 기능을 이용하는 방법이 있다.

- CP(Copy): 호스트와 컨테이너 사이에 파일을 **복사(Copy)**
- Volume: 호스트와 컨테이너 사이에 공간을 **마운드(Mount)**

:ballot_box_with_check: 마운트(Mount)는 저장 공간을 다른 장치에서 접근할 수 있도록 경로를 허용해서, 마치 하나의 저장 공간을 이용하는 것처럼 보이게 하는 작업이다.

### httpd 웹 서버

사용할 도커 이미지는 [httpd](https://httpd.apache.org/)(http daemon)이다. httpd는 Apache **HTTP Server를 실행할 수 있는 오픈소스 웹 서버 소프트웨어**다.

```markdown
httpd는 `/usr/local/apache2/htdocs/` 경로에 웹 서버와 관련된 파일들이 저장되어 있다면, 해당 파일을 기반으로 웹 서버가 실행되도록 한다.
```

httpd를 사용하는 경우 컨데이터를 실행시킬 때 httpd를 실행한다.

```bash
docker container run --name 사용할_컨테이너_이름 -p 사용할_로컬호스트_포트번호:컨테이너_포트번호 IMAGE_NAME
docker container run --name 사용할_컨테이너_이름 -p 818:80 httpd	# 예시
```

- `-p` 옵션: 로컬호스트의 포트와 컨테이너의 포트를 연결한다. (위 명령어에서는 818포트가 로컬호스트 포트, 80번은 컨테이너 포트이다.)
- `-d` 옵션: 컨테이너를 백그라운드에서 실행하게 해준다.

`127.0.0.1:818` 혹은 `localhost:818`을 통해 웹 서버가 작동되고 있는 것을 확인할 수 있다.

### 컨테이너 복사하기

서버가 정상적으로 열린 것을 확인한 후, 새로운 터미널을 열어 `docker container cp` 명령어를 입력해 로컬호스트에 있는 파일을 컨테이너에 전달한다.

- 경로를 입력할 때 **상대 경로와 절대 경로**를 주의해서 작업한다! (레파지토리 폴더에서 명령어를 입력한다.)

```bash
docker conatiner cp 복사_대상_위치 복사_목표_위치
docker container cp ./ 컨테이너_이름:/usr/local/apache2/htdocs	# 예시
```

이후 `127.0.0.1:818` 혹은 `localhost:818`에 접속해서 서버가 구동되는지 확인한다.



## Container 내부 터미널 접속하기

아래 명령어를 사용하면 컨테이너의 내부 터미널로 접속할 수 있다.

```bash
docker exec -it CONTAINER_NAME bash
```

- `root@` 다음에 오는 번호는 랜덤이다.

Container 내부 터미널에서는 linux 명령어를 사용할 수 있다. 다음은 예시 명령어이다.

```shell
cd /	# root 디렉토리로 이동
ls		# 폴더/파일 확인
cd data	# data라는 폴더로 이동
```

내부 터미널을 종료하는 경우 `exit` 명령어를 입력하면 된다.

```shell
exit
```



***Copyright* © 2022 Song_Artish**