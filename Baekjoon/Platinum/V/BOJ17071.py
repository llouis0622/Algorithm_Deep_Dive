from collections import deque

N, K = map(int, input().split())
MAX = 500000
if N == K:
    print(0)
    exit()
visited = [[False] * (MAX + 1) for _ in range(2)]
q = deque([N])
visited[0][N] = True
time = 0
ans = -1
while q:
    time += 1
    temp = K + time * (time + 1) // 2
    if temp > MAX:
        break
    for _ in range(len(q)):
        x = q.popleft()
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not visited[time % 2][nx]:
                visited[time % 2][nx] = True
                q.append(nx)
    if visited[time % 2][temp]:
        ans = time
        break
print(ans)