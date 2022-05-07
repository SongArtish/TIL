# MapReduce (MR)

2022.05.04

---

[TOC]

---



## Overview

**대용량 데이터 처리를 위한** 분산 프로그래밍 모델로, Map 단계와 Reduce 단계로 처리 과정을 나누어 작업한다.



## Map

흩어져 있는 데이터를 **Key, Value의 형태로 연관성 있는 데이터 분류로 묶는 작업**

| Key  | Value |
| :--: | :---: |
|  a   |  22   |
|  b   |  30   |
|  c   |   5   |
| ...  |  ...  |



## Reduce

Map화한 작업 중 중복 데이터를 제거하는 중 **정리하여 원하는 데이터를 추출하는 작업**



## 예시: wordcount

- 글에 포함된 단어 수를 세는 작업
- 작업은 아래 그림과 같이 진행된다.

![mapreduce_wordcount](img/mapreduce_wordcount.png)

(출처: cskstory.tistory.com)



***Copyright* © 2022 Song_Artish**