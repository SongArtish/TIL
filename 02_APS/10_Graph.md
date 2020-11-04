# 그래프

2020.11.04

---

[TOC]

---



## 1. 서로소 집합 (Disjoint-sets)

> 서로소 또는 상호배타 집합들은 서로 중복 포함된 원소가 없는 집합들이다. 다시 말해 교집합이 없다.
>
> - 표현 방법: 연결 리스트, 트리

상호배타 집합 연산

| .           | .                                                  |
| ----------- | -------------------------------------------------- |
| Make-Set(x) |                                                    |
| Find-Set(x) |                                                    |
| Union(x, y) | x와 y를 포함하는 두 집합을 찾는 통합하는 operation |





## 최소 비용 신장 트리 (MST)

### 신장 트리

> n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리

- 표현 : 그래프, 간선들의 배열, 인접 리스트, 트리

### Prim 알고리즘

> 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식
>
> 1. `key(부모)`와 `pi(비용)`를 `none`과 `무한대`로 초기화
> 2. 임의 정점 하나 선택해서 시작
> 3. 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
> 4. 모든 정점이 선택될 때까지 `1번`, `2번` 반복

```python
'''
7 11
0 5 60
0 1 32
0 2 31
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

# 인접행렬
# 가중치 그래프를 인접행렬로 표현

V, E = map(int, input().split())    # V = 정점 개수, E = 간선 개수
adj = [[0] * V for _ in range(V)]

for i in range(E):
    # 시작정점, 끝정점, 가중치
    a, b, c = map(int, input().split())
    adj[a][b] = c   # 무방향 가중치 그래프
    adj[b][a] = c

INF = 999   # 큰 값 (무한대)
key = [INF] * V     # 가중치를 저장할 key 배열
mst = [False] * V   # mst인지 아닌지를 저장

# 시작점 선택 : 0번으로 선택한다.
key[0] = 0
cnt = 0     # 정점 선택 횟수
result = 0  # mst 가중치 저장 // sum(key)의 값과 동일하다.

while cnt < V:
    # key가 최소인 정점 u 찾기
    minV = INF
    minidx = 0
    for i in range(V):
        if not mst[i] and minV > key[i]:
            minV = key[i]
            minidx = i
    mst[minidx] = True  # mst에 포함하기
    result += minV
    cnt += 1
    # u(minidx)에 인접한 정점의 key 값 갱신
        # u에 인접한 정점 중 w 중 아직 mst가 아니고,
        # u-w 가중치가 u의 key값보다 작으면
    for w in range(V):
        target = adj[minidx][w]
        if target > 0 and not mst[w] and key[w] > target:
            key[w] = target
print(key)
print(result)   # result = sum(key)
```

### KRUSKAL 알고리즘

> 간선을 하나씩 선택해서 MST를 찾는 알고리즘
>
> 1. 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬
> 2. 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴
>    사이클이 존재하면 다음으로 가중치가 낮은 간선 선택
> 3. n-1개의 간선이 선택될 때까지 `2번` 반복



***Copyright* © Song_Artish**

