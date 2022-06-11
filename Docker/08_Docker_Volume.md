# Docker Volume

---

[TOC]

---



## Volume

컴퓨터 운영 체제 환경에서, Volume 또는 논리 드라이브(logical drive)는 하나의 파일 시스템을 갖춘 하나의 접근 가능한 스토리지 영역이다.

도커는 하나의 이미지로부터 여러 컨테이너를 만들기 위해서 **Union File System**을 사용한다. 유니온 파일 시스템은 원본 이미지에 변경된 내용(diff)을 추가하는 방식이므로, 다른 컨테이너에서 사용할 수 없다. 애플리케이션에 따라서는 **데이터를 다른 컨테이너와 공유하거나 혹은 호스트에서 접근할 수 있어야 하는 경우**가 있는데, 이때 데이터 볼륨을 사용한다. 데이터 볼륨은 호스트의 파일 시스템을 컨테이너에서 마운트하는 방식으로 사용한다.



## 데이터 볼륨 추가

도커 컨테이너를 만들 때(docker run), **-v** 옵션을 이용해서 컨테이너에 데이터 볼륨을 추가할 수 있다. -v 뒤에 마운트할 볼륨을 나열하면 된다. 다음의 명령어를 입력하면 하나의 데이터 볼륨을 포함하는 컨테이너를 만들 수 있다.

```bash
docker run --name web -i -t -v /webapp ubuntu /bin/bash
```

컨테이너에 `/webapp` 디렉토리가 생성된다. 이 디렉토리는 호스트의 파일 시스템과 마운트된다. 마운트 경로는 **docker inspect**로 확인할 수 있다.

```bash
docker inspect web
# .....
# "Mounts": [
#	{
#		"Name": ...
#		"Source": ...
#		...
#	}
# ]
```

`/webapp` 디렉토리가 **Source**에 설정된 디렉토리에 마운트되었다. `/webapp`에 파일을 쓰면 Source 디렉토리에 파일이 만들어지는 것을 확인할 수 있다.

`-v`를 여러 개 이용해서 하나 이상의 데이터 볼륨을 만들 수 있다.



## docker-compose로 볼륨 추가

`docker-compose.yaml` 파일을 생성하고 다음과 같이 내용을 작성한다.

```yaml
# docker-compose.yaml

version: '3.8'

services:
  ...
  
  node:
    image: sebcontents/server
    restart: 'always'
    ports:
      - "4999:80"
    container_name: server
    volumes:
      - "./volumefolder:/data"
      
  ...
```

작성이 완료되면 docker-compose를 실행한다.

```bash
docker-compose up
```

docker-compose를 통해 컨테이너가 제대로 실행되었다면 **로컬**의 yaml 파일이 위치한 곳에 `volumefolder`(위에서 정의한 폴더명)라는 디렉토리를 확인할 수 있다. `volumefolder` 디렉토리 속에 임의의 텍스트 파일 하나를 생성한다. 그리고 다음 명령어로 server 컨테이너 터미널로 접속한다.

```bash
docker exec -it server bash
# 작동이 안 되는 경우
docker exec -it server sh
```

컨테이너 터미널에서 `data` 디렉토리로 이동한다.

```shell
cd /data
```

방금 `volumefolder`에 생성했던 텍스트 파일이 있는지 확인해본다.

```shell
ls
```



## <참고> 환경 변수 설정

`docker-compose.yaml` 파일을 생성하고 다음과 같이 내용을 작성한다.

```yaml
# docker-compose.yaml

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
    volumes:
      - "./volumefolder:/data"
  
  mysql:
    image: mysql:latest
    restart: 'always'
    ports:
      - "3307:3306"
    container_name: database
    environment:
      MYSQL_PORT_PASSWORD: ROOT_USER_PASSWORD
      MYSQL_DATABASE: INITIAL_CREATED_DATABASE
      MYSQL_USER: USER_NAME
      MYSQL_PASSWORD: USER_PASSWORD
```

- 참고 문서: https://hub.docker.com/_/mysql



***Copyright* ©2022 Song_Artish**