import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
MAX = 100000
dist = [-1] * (MAX + 1)
temp = [0] * (MAX + 1)
dq = deque([n])
dist[n] = 0
temp[n] = 1
while dq:
    x = dq.popleft()
    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx <= MAX:
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                temp[nx] = temp[x]
                dq.append(nx)
            elif dist[nx] == dist[x] + 1:
                temp[nx] += temp[x]
print(dist[k])
print(temp[k])