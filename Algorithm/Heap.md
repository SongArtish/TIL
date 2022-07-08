# Heap

---

[TOC]

---



## Heap

힙(Heap)이란 트리 기반 자료구조로, 힙 속성을 만족하는 거의 완전한 트리이다.

- 힙 속성: 예를 들어, 최대힙(Max Heap)일 경우, 부모 노드는 반드시 자식 노드보다 값이 커야 한다는 법칙

이러한 힙의 특성으로 힙은 우선순위 큐를 구현하는데 적합한 자료구조이다.



## Binary Heap

이진 힙(Binary Heap)은 힙 중 가장 널리 쓰이는 형태 중 하나로, 이진 트리 형태인 힙이다. 이진 트리는 각 노드의 자식 노드가 반드시 2개 이하인 트리이다.

이진 힙은 완전 이진 트리라는 조건을 만족해야 한다. 완전 이진 트리는 모든 레벨의 노드가 채워져 있어야 하고, 마지막 레벨은 왼쪽부터 차 있어야 한다.



## Max Heap

최대 트리(Max Tree)는 각 노드의 key 값이 (자식 노드가 있다면) 그 자식의 key 값보다 작지 않은 트리이다. 최대 힙(Max Heap)은 최대 트리이면서 완전 이진 트리이다.



## Min Heap

최소 트리(Min Tree)는 각 노드의 key 값이 (자식 노드가 있다면) 그 자식의 key 값보다 크지 않은 트리이다. 최소 힙(Min Heap)은 최소 트리이면서 완전 이진 트리이다.



***Copyright* © 2022 Song_Artish**