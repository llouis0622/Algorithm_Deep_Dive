### Union-Find & 위상정렬

- Union-Find : 여러 원소를 그룹으로 묶고, 두 원소가 같은 그룹인지 O(a(N)) = O(1)에 확인
  - 경로 압축으로 최적화
  - 크루스칼 MST, 사이클 감지에 필수
- 위상정렬 : DAG에서 선행 관계를 만족하는 순서 출력
  - 진입차수 0인 노드부터 BFS
  - 결과 크기 != n이면 사이클 존재

```python
class UF:
    def __init__(self, n):
        self.p = list(range(n + 1))
        self.r = [0] * (n + 1)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.r[a] < self.r[b]:
            a, b = b, a
        self.p[b] = a
        if self.r[a] == self.r[b]:
            self.r[a] += 1
        return True


from collections import deque


def topo(n, graph, indegree):
    q = deque(v for v in range(1, n + 1) if indegree[v] == 0)
    res = []
    while q:
        v = q.popleft()
        res.append(v)
        for nv in graph[v]:
            indegree[nv] -= 1
            if indegree[nv] == 0:
                q.append(nv)
    return res if len(res) == n else []
```