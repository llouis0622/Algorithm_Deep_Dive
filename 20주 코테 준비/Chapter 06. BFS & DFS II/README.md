### BFS 심화 & 다익스트라

- 가중치 없는 최단경로 : BFS O(V + E)
- 가중치 있는 최단경로 : 다익스트라 O((V + E) log V)
- 다익스트라 핵심
  - heapq + dist 배열
  - if d > dist[v]: continue -> 이미 처리된 노드 스킵
  - 음수 간선 불가(벨만-포드 사용)
- 플로이드-워셜 : 모든 쌍 최단경로 O(V^3)

```python
import heapq


def dijkstra(graph, start, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        d, v = heapq.heappop(hq)
        if d > dist[v]:
            continue
        for nv, w in graph[v]:
            if dist[v] + w < dist[nv]:
                dist[nv] = dist[v] + w
                heapq.heappush(hq, (dist[nv], nv))
    return dist
```