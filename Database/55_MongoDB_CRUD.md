# MongoDB CRUD

---

[TOC]

---



## CREATE

insert 명령어를 사용하여 각 도큐먼트의 고유의 값인 `_id`와 새로운 도큐먼트를 추가할 수 있다. 모든 MongoDB 도큐먼트는 `_id` 필드를 기본 값으로 가지고 있으며, `_i` 필드의 값은 각 도큐먼트를 구별하는 역할을 한다.

```shell
db.<COLLECTION_NAME>.insert({...})
# mongoDB 없데이트 후 insertOne 혹은 inserMany를 사용할 수도 있다.
```

```shell
db.zips.insert({
... "_id" : ObjectId("5c8eccc1caa187d17ca6ed16"),	# 추가하지 않아도 도큐먼트가 삽입될 때 자동적으로 추가된다.
... "city" : "ALPINE",
... "zip" : "35014",
... "loc": {
..... "y" : 33.331165,
..... "x" : 86.208934
..... },
... "pop" : 3062,
... "state" : "AL"
... })
```

위와 같이 데이터를 입력하면 WriteResult가 출력된다.

```shell
{
  acknowledged: true,
  insertedId: ObjectId("5c8eccc1caa187d17ca6ed17")
}
```

insert를 실패한 경우, `nInserted: 0`이라는 WriteResult가 나올 수 있는데, nInserted는 삽입된 도큐먼트의 수를 나타낸다. 여기서, nInserted가 0이므로 추가 실패를 의미한다.

>  **여러 개의 도큐먼트 넣기**

한 번에 다수의 도큐먼트를 삽입하기 위해서는 배열 안에 해당 도큐먼트를 담아준다.

```shell
db.<COLLECTION_NAME>.find([{...}, {...}, ...])
db.inspections.insert([{"test":"1"}, {"test":"2"}, {"test":"3"}])
```

> **ordered**

Insert 명령어를 사용하면, 주어진 도큐먼트 배열의 **인덱스 순서**로 작업이 실행된다. 그러나, **ordered**를 추가하면 **순서에 상관 없이** 고유한 `_id`를 가진 도큐먼트는 모두 컬렉션에 삽입된다.

```shell
db.<COLLECTION_NAME>.insertMany([...], {ordered: true})
```

> **없는 컬렉션에 추가하기**

MongoDB는 사용자가 쉽게 새로운 컬렉션 혹은 데이터베이스를 생성하기를 원했다. 그래서 만약 사용자가 존재하지 않는 컬렉션에 도큐먼트를 넣는 경우, 그와 동시에 컬렉션이 만들어지게 된다.



## READ

find 명령어를 이용하여 일정 조건에 따라 데이터를 조회할 하거나 데이터 수를 셀 수 있다.

```shell
db.<COLLECTION_NAME>.find({...})
db.zips.find({"city" : "ALPINE", "zip" : "35014"}) # 예시
```

find 명령어는 랜덤하게 선택된 20개 결과물까지만 출력한다. 해당 조건에 맞는 다음 도큐먼트를 조회하기 위해서는, iterate의 줄임말인 `it` 명령어를 사용해야 한다.

```shell
> Type "it" for more
it
```

> **모든 데이터 조회하기**

데이터베이스의 모든 데이터를 조회하고 싶으면, 조건 쿼리문 없이 find 명령어를 사용하면 된다.

```shell
db.<COLLECTION_NAEM>.find()
db.zips.find()	# 예시
```

> **pretty()**

데이터가 조금 더 보기 좋게 출력될 수 있도록 `pretty()` 명령어를 덧붙일 수 있다.

```shell
db.<COLLECTION_NAEM>.find().pretty()
db.zips.find().pretty()	# 예시
```

> **데이터 개수 조회하기**

데이터의 수를 조회하기 위해서는 `count()`라고 하는 명령어를 사용한다.

```shell
db.<COLLECTION_NAEM>.find().count()
db.zips.find().count()	# 예시
```

> **한 개의 결과만 조회하기**

`findOne` 명령어를 사용하면 무작위의 데이터 1개만 가져올 수도 있다.

```shell
db.<COLLECTION_NAEM>.findOne()
db.zips.findOne({"_id": ObjectId("5c8eccc1ca")})
```



## UPDATE

mongo shell에서 도큐먼트를 업데이트하기 위한 방법에는 2가지가 있다.

- **updateOne**: 주어진 기준에 맞는 다수의 도큐먼트 중 첫 번째 도큐먼트 하나만 업데이트
- **updateMany**: 쿼리문과 일치하는 모든 도큐먼트를 업데이트

아래 예시는 zips 컬렉션에서 ALPINE이라는 도시의 인구(pop)를 10씩 증가시키는 명령어이다. 여기서는 **MQL 연산자 $inc를 사용**한다.

- MQL: MongoDB Query Langauge

```shell
db.zips.updateMany(
{"city" : "ALPINE"},	# 업데이트 할 도큐먼트를 결정하는 조건
{"$inc" : {"pop" : 10}}	# $inc: 특정한 필드의 값을 주어진 만큼 증가
)
```

> **$inc 연산자**

$inc 연산자는 업데이트 하려는 필드와 증가하는 값을 작성하여 다양한 필드의 값을 동시에 업데이트 할 수 있다.

```shell
{"$inc": {
"pop": 10,
"<field1>": <increment value1>,
"<filed2>": <increment value2>, ...
}}
```

작업에 대한 응답을 살펴보면, matchedCount와 modifiedCount가 있다. 해당 부분은 명령어에 들어가는 쿼리문 n개에 대한 응답이다.

- **matchedCount**: 첫 번째 인자로 들어간 조건을 충족하는 도큐먼트의 수
- **modifiedCount**: 두 번째 인자로 들어간 업데이트 연산자(위에서는 $inc)로 인해 수정된 도큐먼트의 수

> **$set 연산자**

$set 연산자는 주어진 필드에 지정된 값을 업데이트 한다.

```shell
db.zips.updateOne({"zip": "12534"}, {"$set": {"pop": 6235}})	# pop을 6235 값으로 변경
```

> **잘못된 필드를 입력한 경우**

update 중 잘못된 필드를 입력한 경우, 해당 도큐먼트 내에 새로운 필드로 추가된다.

> **$push 연산자**

$push 연산자를 이용하면 배열로 이루어진 필드의 값에 요소를 추가할 수 있다.

```shell
db.grades.updateOne(
{"student_id": 250, "class_id": 399},	# 업데이트할 도큐먼트를 결정하는 조건
{"$push" :	# 연산자
{"scores": # 서브 도큐먼트를 삽입할 배열 타입의 값을 가지고 있는 필드
{"type": "extra credit", "score": 100}	# 추가할 서브 도큐먼트
}}
)
```



## DELETE

mongo shell을 사용하여 도큐먼트 삭제할 때, `deleteOne()`과 `deleteMany()`를 사용할 수 있다. deleteOne()을 사용하는 경우 `_id` 값으로 쿼리해 온 특정 도큐먼트를 삭제하는 것이 좋다.

- **deleteOne**: 주어진 기준에 맞는 다수의 도큐먼트 중 첫 번째 도큐먼트 하나를 삭제한다.
- **deleteMany**

```shell
db.inspections.deleteOne({"_id": "fordeleting"})
```

> **컬렉션 삭제**

컬렉션을 삭제하기 위해서는 drop이라는 명령어를 사용해야 한다.

```shell
db.<COLLECTION_NAME>.drop()
```



***Copyright* © 2022 Song_Artish**