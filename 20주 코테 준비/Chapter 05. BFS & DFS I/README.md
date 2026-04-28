### BFS & DFS 기초

- BFS(너비 우선) : deque + visited, 최단경로 보장(비가중치), visited는 큐에 넣기 전에 체크
- DFS(깊이 우선) : 재귀 또는 스택, 경로 탐색, 사이클 감지에 적합
- 격자 이동 : dx = [-1, 0, 1, 0], dy = [0, 1, 0, -1]

```python
from collections import deque
import sys

sys.setrecursionlimit(100000)


def bfs(graph, start):
    visited = set([start])
    q = deque([start])
    while q:
        v = q.popleft()
        for i in graph[v]:
            if i not in visited:
                visited.add(i)
                q.append(i)


def dfs(graph, v, visited):
    visited.add(v)
    for i in graph[v]:
        if i not in visited:
            dfs(graph, i, visited)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
```