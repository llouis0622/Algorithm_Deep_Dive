import sys
from collections import deque

input = list(map(int, sys.stdin.read().split()))
n, m = input[0], input[1]
lst = [[] for _ in range(n + 1)]
idx = 2
for _ in range(m):
    a, b = input[idx], input[idx + 1]
    lst[a].append(b)
    lst[b].append(a)
    idx += 2
dist = [-1] * (n + 1)
dist[1] = 0
q = deque([1])
while q:
    x = q.popleft()
    if dist[x] == 2:
        continue
    for y in lst[x]:
        if dist[y] == -1:
            dist[y] = dist[x] + 1
            q.append(y)
ans = sum(1 for i in range(2, n + 1) if 1 <= dist[i] <= 2)
print(ans)