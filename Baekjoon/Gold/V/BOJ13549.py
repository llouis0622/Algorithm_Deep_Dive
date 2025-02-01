import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
MAX = 100000
dist = [-1] * (MAX + 1)
q = deque([N])
dist[N] = 0
while q:
    x = q.popleft()
    if x == K:
        print(dist[x])
        break
    for nx in (2 * x, x - 1, x + 1):
        if 0 <= nx <= MAX and dist[nx] == -1:
            if nx == 2 * x:
                dist[nx] = dist[x]
                q.appendleft(nx)
            else:
                dist[nx] = dist[x] + 1
                q.append(nx)