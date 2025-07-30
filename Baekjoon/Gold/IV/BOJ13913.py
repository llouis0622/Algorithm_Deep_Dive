from collections import deque

N, K = map(int, input().split())
MAX = 100001
dist = [-1] * MAX
prev = [-1] * MAX


def bfs(start):
    q = deque()
    q.append(start)
    dist[start] = 0
    while q:
        x = q.popleft()
        if x == K:
            return
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                prev[nx] = x
                q.append(nx)


bfs(N)
print(dist[K])
path = []
cur = K
while cur != -1:
    path.append(cur)
    cur = prev[cur]
path.reverse()
print(' '.join(map(str, path)))