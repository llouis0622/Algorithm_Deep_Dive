import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    arr = list(map(int, sys.stdin.readline().split()))
    k = arr[0]
    seq = arr[1:]
    for i in range(k - 1):
        u = seq[i]
        v = seq[i + 1]
        adj[u].append(v)
        indegree[v] += 1
q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
res = []
while q:
    x = q.popleft()
    res.append(x)
    for idx in adj[x]:
        indegree[idx] -= 1
        if indegree[idx] == 0:
            q.append(idx)
if len(res) != n:
    print(0)
else:
    print("\n".join(map(str, res)))