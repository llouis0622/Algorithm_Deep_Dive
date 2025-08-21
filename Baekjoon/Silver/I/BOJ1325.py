import sys
from collections import deque

input = iter(sys.stdin.buffer.read().split())
n = int(next(input))
m = int(next(input))
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a = int(next(input))
    b = int(next(input))
    g[b].append(a)
visited = [0] * (n + 1)
mark = 0
cnt = [0] * (n + 1)
dq = deque()
for s in range(1, n + 1):
    mark += 1
    visited[s] = mark
    dq.append(s)
    c = 1
    while dq:
        x = dq.popleft()
        for y in g[x]:
            if visited[y] != mark:
                visited[y] = mark
                dq.append(y)
                c += 1
    cnt[s] = c
num = max(cnt[1:])
ans = [str(i) for i in range(1, n + 1) if cnt[i] == num]
sys.stdout.write(" ".join(ans))