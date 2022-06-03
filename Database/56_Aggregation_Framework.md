# Aggregation Framework

---

[TOC]

---



## Overview

Aggregation Framework는 MongoDB에서 데이터를 쿼리하는 가장 간단한 방법 중 하나로, MQL보다 다양한 쿼리를 작성할 수 있다. MQL을 사용하는 모든 쿼리는 Aggregation Framework에서도 수행할 수 있다.



## Syntax

Aggregation Framework에서는 find가 아닌 aggregate 명령을 사용한다. 각 단계의 이름 앞에는 `$`가 있고 그 뒤에는 실행할 작업에 대한 설명이 온다.

- aggregate를 사용하면 도큐먼트를 필터링하지 않고 그룹으로 데이터를 집계하거나 데이터를 수정할 수 있다.
- aggregate를 사용하면 데이터 찾기 및 프로젝션 없이 작업을 수행하거나 계산할 수 있다.
- aggregate를 사용할 때 대괄호를 이용해 배열을 인자로 사용한다. (파이프라인처럼 배열 요소를 순서대로 작업 때문)

```shell
# MQL로 작성하는 경우
db.listingsAndReviews.find(
	{"amenities": "Wifi"},	# query
	{"price": 1 "address": 1, "_id": 0}	# project
).pretty()
# $aggregate 문법을 사용하는 경우
db.listingsAndReviews.aggregate([
	{$match: {"amenities": "Wifi"}},	# query
	{$project: {"price": 1 "address": 1, "_id": 0}}	# project
]).pretty()
```

### $match

조건에 맞는 데이터를 필터해준다.

### $project

결과에 표시할 필드를 선택할 수 있다.

### $group

들어온 데이터 스트림을 여러 개로 그룹화하는 연산자이다. $group 단계는 이전 단계에서 도큐먼트를 받을 때 `_id` 필드에 표현식을 사용하여 이 도큐먼트가 속한 그룹을 식별한다. $group 구문은 두 번째 부분을 사용하여 파이프라인을 통해 들어오는 데이터에 대해 더 많은 양적 분석을 수행할 수 있다.

```shell
# 컬렉션에 있는 국가와 각 국가에 있는 숙소의 수를 group화한다.
db.listingsAndReviews.aggregate([
	{$project: {"address": 1, "_id": 0}},
	{$group:
        {
            _id: "$address.country",	# 표현식을 기준으로 그룹화
            "count": {"$sum": 1},
            <FIELD_1>: {<ACCUMULATOR_1>: <EXPRESSION_1>},
            ...
        }
	}
])
```



## 작동 원리

### 파이프라인

Aggregation Framework에서는 파이프라인의 단계에 따라 데이터를 처리할 수 있다. 각각의 처리 작업은 나열한 배열의 순서에 의해 결정되며, 마지막으로 변환된 데이터가 파이프라인 끝에 나타난다.

### 필터링

Aggregation Framework에서는 $match 등과 같은 필터링 단계가 없으면, 데이터 요약, 계산 및 그룹화를 수행할 때 원본 데이터를 수정하지 않는다. 필터링 단계가 있다면 이를 통과한 데이터를 다음 단계에서 작업한다.



***Copyright* © 2022 Song_Artish**