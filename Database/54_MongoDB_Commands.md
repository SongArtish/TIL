# MongoDB 기본 명령어

---

[TOC]

---



## MongoDB 서버 실행

cmd 창에서 아래 명령어를 실행한다.

```shell
$ mongod --dbpath <DB 경로>
```



## MongoDB Shell 실행

서버를 실행해 둔 채, cmd에서 아래 명령어를 실행한다.

```shell
$ mongo
```



## 데이터베이스 생성

```shell
use <DB이름>
```

아래 명령어를 통해 현재 생성되어 있는 db를 확인할 수 있다.

```shell
show dbs
show databases # 혹은
```

현재 사용 중인 db를 확인할 수도 있다.

```shell
db
```



## 컬렉션 생성

```shell
db.createCollection("<COLLECTION_NAME>")
```

현재 생성된 collection을 확인할 수 있다.

```shell
show collections
```

아래 명령어를 사용하면 collection을 배열 형태로 출력할 수 있다.

```shell
db.getCollectionNames()
# --> [ 'trainng', 'test' ]
```



## 컬렉션 삭제

```shell
db.<COLLECTION_NAME>.drop()
```



## Export

BSON 형식의 데이터를 내보내기 위한 `mongodump` 명령어와 JSON 형식인 데이터를 내보내기 위한 `mongoexport`, 이렇게 2가지 명령어가 있다. 이를 사용하기 위해서는 Atlas Cluster URI가 필요하다. 해당 URI는 일반 웹의 URI와 형식이 같고, username, password, cluster 주소로 이루어져 있다.

mongodump를 하는 경우에는 별다른 쿼리가 없지만, mongoexport를 하는 경우에는 해당 데이터베이스의 컬렉션 이름, 파일 이름까지 정확하게 작성해줘야 한다.

```
// Exports data in BSON
mongodump --uri "<Atlas Cluster URI>"
// Exports data in JSON
mongoexport --uri "<Atlas Cluster URI>"
			--collection=<collection name>
			--out=<filename>.json

```



## Import

가져오기도 형식에 따라 2가지 방법으로 나뉜다. BSON 형식의 데이터를 가져올 경우에는 `mongorestore`를 사용하지만, JSON 형식의 데이터를 가져올 경우에는 `mongoimport`를 사용한다. Export와 마찬가리도 URI를 사용해서 작성하며, 기존에 있는 데이터를 삭제하기 위한 옵션인 drop 쿼리문은 선택적으로 사용할 수 있다.

```
// Import data in BSON dump
mongorestore --uri "<Atlas Cluster URI>"
			--drop dump
// Import data in JSON
mongoimport --uri "<Atlas Cluster URI>"
			--drop=<filename>.json
```



***Copyright* © 2022 Song_Artish**