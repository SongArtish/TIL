# Index

---

[TOC]

---



## Overview

Slow query(쿼리 속도가 느려지는 경우)를 해결하기 위한 방법 중 하나로 인덱싱을 사용할 수 있다. 데이터를 탐색하기 쉬운 형식으로 인덱스를 저장한다.



## CREATE

> createIndex()

인덱스를 생성하기 위해서는 `createIndex()`라는 메소드를 사용한다. 파라미터로는 인덱스를 **적용할 필드를 전달**한다. 이에 따른 값을 1로 지정하면 오름차순, -1로 하면 내림차순으로 정렬한다. 이때, 필드명을 1개를 지정하면 단일 필드 인덱스, 필드명이 2개 이상이면 다중 인덱스(compound index)이다.

```shell
db.<COLLECTION_NAME>.createIndex({<FIELD_NAME}: 1, <FILED_NAME>: -1}) # 인덱스를 적용할 필드 전달
```

createIndex() 메소드의 두 번째 파라미터로는 **속성**을 추가할 수 있다.

```shell
db.<COLLECTION_NAME>.createIndex({<FIELD_NAME>: 1}, {<PROPERTY>: true})
```

인덱스에 적용할 수 있는 속성은 다음과 같다.

- **Unique**(유일한 속성): `_id` 필드와 같이 컬렉션에 단 한 개의 값만 존재할 수 있는 속성이다. 다음은 `members`라는 컬렉션의 각 도큐먼트에 존재하는 `user_id` 필드의 인덱스를 중복 값이 없는 유일한 필드로 생성한다.

  ```shell
  db.members.createIndex({"user_id": 1}, {unique: true})
  ```

- **Partial**(부분적 속성): 도큐먼트의 조건을 정해 일부 도큐먼트에만 인덱스를 적용한다. 이 속성을 사용하면, 필요한 부분에만 인덱스를 사용하여 효율적인 쿼리를 할 수 있는데, 이를 위해 `partialFilterExpression` 옵션을 사용한다. 아래 코드는 `restaurants`라는 컬렉션에 `cuisine`, `name`이라는 두 개의 필드를 사용하여 다중 인덱스를 생성하며, 이 인덱스는 별점이 4점 이상인 도큐먼트에만 적용된다.

  ```shell
  db.restaurants.createIndex({"cuisine": 1, "name": 1}, {partialFilterExpression: {rating: {$gt: 4}}})
  ```

- **TTL**(Time-To-Live): 이 속성은 Data 타입 혹은 Data 배열 타입의 필드에 적용 가능하다. 이 속성을 사용하면 특정 시간이 지난 후 도큐먼트를 컬렉션에서 삭제한다. 인덱스에 TTL 속성을 추가하고, 이에 따라 `lastModifiedDate`와 3600초 이상 차이가 나면 도큐먼트를 컬렉션에서 제거한다.

  ```shell
  db.eventlog.createIndex({"lastModifiedDate": 1}, {expireAfterSeconds: 3000})
  ```



## READ

> getIndexes()

생성된 인덱스를 조회할 때는 `getIndexes` 메소드를 사용한다. 인덱스를 생성하지 않았을 때는 `_id` 값만 인덱스로 생성되어 있다.

```shell
db.<COLLECTION_NAME>.getIndexes()
```



## DELETE

> dropIndex()

생성된 인덱스를 삭제할 때는 `dropIndex` 메소드를 사용한다. 인덱스마다 지정된 name이나, 삭제하려는 인덱스의 필드와 지정했던 값을 파라미터로 전달하여 삭제할 수 있다.

```shell
db.<COLLECTION_NAME>.dropIndex(name) # 여기서 name은 인덱스마다 지정된, 인덱스의 이름을 나타내는 필드
# or
db.<COLLECTION_NAME>.dropIndex({<FIELD>: 1})
```

모든 인덱스를 삭제하고 싶을 때는 다음과 같이 복수형의 메소드를 사용한다.

```shell
db.<COLLECTION_NAME>.dropIndexes()
```



***Copyright* © 2022 Song_Artish**