# 최단거리 문제

---

[TOC]

---



## Dijkstra Algorithm

그래프에서 한 정점(노드)에서 다른 정점까지의 최단 경로를 구하는 알고리즘으로, 이 과정에서 도착 정점 뿐만 아니라 모든 다른 정점까지 최단경로로 방문하며 각 정점까지의 최단 경로를 모두 찾게 된다. 매번 최단 경로의 정점을 선택해 탐색을 반복하는 것이다.

**수행 과정**

1. 출발 노드와 도착 노드를 설정한다.
2. '최단 거리 테이블'을 초기화한다.
3. 현재 위치한 노드의 인접 노드 중 방문하지 않은 노드를 구별하고, 방문하지 않은 노드 중 거리가 가자 짧은 노드를 선택한다. 그 노드를 방문 처리한다.
4. 해당 노드를 거쳐 다른 노드로 넘어가는 간선 비용(가중치)을 계산해 '최단 거리 테이블'을 업데이트한다.
5. 3 ~ 4의 과정을 반복한다.

```javascript
function createGraphByMatrix(num, edges) {
  const matrix = [];
  const INF = 101;
  for (let i = 0; i <= num; i++) {
    matrix.push(Array(num + 1).fill(INF));
    matrix[i][i] = 0;
  }
  edges.forEach(([src, dst, weight]) => {
    matrix[src][dst] = matrix[dst][src] = weight;
  });
  return matrix;
}

// 인접 행렬을 통한 구현: O(V^2)
// V는 정점의 개수
function Dijkstra(num, edges, start, end) {
  // 그래프를 생성한다.
  const matrix = createGraphByMatrix(num, edges);
  // dist는 출발 정점으로부터 모든 정점까지의 최단 거리를 저장하는 배열
  // 처음에는 주어진 간선의 정보로 초기화
  const dist = matrix[start].slice();
  // 최단 거리 계산이 완료된 정점을 표시하는 배열
  const visited = Array(num + 1).fill(false);
  // 출발 정점까지의 거리는 0으로 이미 계산된 상태로 볼 수 있다.
  visited[start] = true;

  // 최단 경로를 저장하기 위한 배열
  // 각 정점별로 해당 정점에 도달하기 위한 최단 경로 중 바로 직전의 정점을 저장
  // 계산이 완료된 후에 역으로 추적해서 경로 생성 가능
  // 최단 경로가 계산되기 이전의 상태를 표시하기 위해 -1로 초기화
  const before = Array(num + 1).fill(-1);

  // 출발 정점에서 바로 가는 경로가 존재하는 정점은
  // 출발 정점이 최단 경로 상의 직전 정점이라고 가정한다.
  edges.forEach(([src, dst]) => {
    if (src === start) before[dst] = src;
    if (dst === start) before[src] = dst;
  });

  // 아직 최단 거리 계산이 안 된 정점들 중에서
  // 출발 정점과의 거리가 가장 짧은 정점을 리턴한다.
  const getNextNearestIdx = (dist) => {
    let min = Number.MAX_SAFE_INTEGER;
    for (i = 1; i <= num; i++) {
      if (dist[i] < min && visited[i] === false) {
        min = dist[i];
        target = i;
      }
    }
    return target;
  };

  // 출발 정점은 이미 계산된 상태이므로 1개를 제외하고
  // 매 루프를 통해서 (다음으로) 출발 정점과의 거리가 가장 짧은 정점이 계산되므로
  // 총 루프의 회수는 num - 2 이다.
  for (let round = 0; round < num - 2; round++) {
    // 현재 시점에서 출발 정점까지의 거리가 가장 짧은 정점(v1)은
    // 이미 계산이 완료되었다고 볼 수 있다.
    // 다른 정점(v2)은 출발 정점과의 거리가 v1에 비해 길고 (v1이 가장 짧은 거리를 가졌으므로)
    // 따라서 다른 정점을 통해 v1으로 가는 경로가 더 길 수 밖에 없다.
    const nearest = getNextNearestIdx(dist);
    // 이미 계산이 된 정점을 중복해서 고려할 필요가 없기 때문에 표시를 한다
    visited[nearest] = true;
    visited.forEach((calculated, v) => {
      // 계산이 완료된 정점은 보지 않아도 된다.
      if (calculated === false) {
        // 현재 시점에서 출발 정점과 (이미 계산된 정점을 제외하고 다음으로)
        // 가장 가까운 정점(nearest)을 기준으로
        // nearest를 통해서 가는 방법이 기존의 방법보다 좋으면, 즉 더 짧으면
        // 더 짧은 거리로 갱신한다.
        // 알 수 있는 사실: 최단경로의 부분 경로 역시 최단경로이다.
        if (dist[nearest] + matrix[nearest][v] < dist[v]) {
          dist[v] = dist[nearest] + matrix[nearest][v];

          // 최단 경로가 갱신되므로, 정점 v에 도달하는 최단 경로 상에서
          // 바로 직전 정점은 nearest 이다.
          before[v] = nearest;
        }
      }
    });
  }

  // 최단 경로를 end 부터 역추적한다.
  function getPath(before, start, end) {
    let vertex = before[end];
    const path = [end, vertex];
    while (vertex !== start) {
      vertex = before[vertex];
      path.push(vertex);
    }
    return path.reverse();
  }
  const path = getPath(before, start, end);

  return dist[end];
}

```



## Floyd–Warshall Algorithm

변의 가중치가 음(-)이거나 양(+)인 (음수 사이클은 없는) 가중 그래프에서 **최단 경로**들을 찾는 알고리즘이다. '모든 정점'에서 '모든 정점'으로의 최단 경로를 구하고 싶을 때 사용한다.

> '거쳐가는 정점'을 기준으로 최단 거리를 구한다.

```javascript
function createGraphByMatrix(num, edges) {
  const matrix = [];
  const INF = 101;
  for (let i = 0; i <= num; i++) {
    matrix.push(Array(num + 1).fill(INF));
    matrix[i][i] = 0;
  }
  edges.forEach(([src, dst, weight]) => {
    matrix[src][dst] = weight;
  });
  return matrix;
}

// 인접 행렬을 통한 구현: O(V^3)
// V는 정점의 개수
function FloydWarshall(num, edges) {
  // dist는 두 정점간의 최단 거리를 저장하는 인접 행렬
  // dist[src][dst]는 정점 src로부터 정점 dst까지의 최단 거리
  // 처음에는 최초의 간선말고는 정보가 없으므로 그래프와 똑같이 초기화한다.
  const dist = createGraphByMatrix(num, edges);
  for (let stopover = 1; stopover <= num; stopover++) {
    for (let src = 1; src <= num; src++) {
      for (let dst = 1; dst <= num; dst++) {
        if (dist[src][stopover] + dist[stopover][dst] < dist[src][dst]) {
          dist[src][dst] = dist[src][stopover] + dist[stopover][dst];
        }
      }
    }
  }

  const INF = 101;
  const nulled = dist.map((row) =>
    row.map((col) => {
      if (col === INF) return null;
      else return col;
    })
  );
  return nulled.slice(1).map((row) => row.slice(1));
}

```



## Bellman-Ford Algorithm

벨만-포드 알고리즘은 한 노드에서 다른 노드까지의 최단 거리를 구하는 알고리즘으로, 간선의 가중치가 음수일 때도 최단 거리를 구할 수 있다.

**Dijkstra vs Bellman-Ford**

- `Dijkstra`
  - 매번 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하여 한 단계씩 최단거리를 구해나간다.
  - 음수 간선이 없다면, 최적의 해를 찾을 수 있다.
  - 시간 복잡도가 빠르다. (`O(V * LogV)`) -> 개선된 Dijkstra 알고리즘 (우선순위 큐 사용)
- `Bellman-Ford`
  - (정점-1)번의 매 단계마다 모든 간선을 전부 확인하면서 모든 노드 간의 최단 거리를 구해나간다.
  - <u>음수 간선</u>이 있어도 최적의 해를 찾을 수 있다.
  - 시간 복잡도가 느리다. (`O(V * E)`)

**수행 과정**

1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 다음의 과정을 (정점-1)번 반복한다.
    1. 모든 간선 E개를 하나씩 확인한다.
    2. 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
- 만약 음수 간선 순환이 발생하는지 체크하고 싶다면 3번 과정을 한 번 더 수행한다. (이때 최단 거리 테이블이 갱신된다면 음수 간선 순환이 존재하는 것이다.)

```javascript
// 그래프 구현이 필요없는 알고리즘: O(V * E)
// V는 정점의 개수, E는 간선의 개수
function BellmanFord(num, edges, start) {
  const INF = Number.MAX_SAFE_INTEGER;
  const dist = Array(num + 1).fill(INF);
  dist[start] = 0;

  for (let v = 1; v <= num - 1; v++) {
    edges.forEach((e) => {
      const [src, dst, weight] = e;
      // 최단경로의 부분 경로 역시 최단경로이다.
      // dist[dst], 즉 start에서 dst까지의 최단 경로는
      //  1) 중간에 거쳐서 갈 수 있는 경로가 존재하고 (dist[src] !== INF)
      //  2) 그 경로를 통해서 가는 방법이 보다 짧으면,
      //     즉 start에서 src까지 갔다가 (dist[src]), src에서 dst까지 가는 (weight) 방법이 더 짧으면,
      // 해당 방법으로 갱신(update)한다.
      if (dist[src] !== INF && dist[src] + weight < dist[dst]) {
        dist[dst] = dist[src] + weight;
      }
    });
  }

  // 음의 사이클이 존재하는지 확인하고
  // 존재하면 빈 배열을 리턴한다.
  const hasNegCycle = edges.some((e) => {
    const [src, dst, weight] = e;
    if (dist[src] !== INF && dist[src] + weight < dist[dst]) {
      return true;
    }
  });

  return hasNegCycle ? [] : dist.slice(1);
}
```



***Copyright* © 2022 Song_Artish**