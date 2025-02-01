import sys
from collections import deque

input = sys.stdin.read
data = input().split("\n")

N = int(data[0])
tmp = [list(map(int, data[i + 1].split())) for i in range(N)]
H = max(map(max, tmp))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def BFS(x, y, visited, rain_level):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and tmp[nx][ny] > rain_level:
                visited[nx][ny] = True
                q.append((nx, ny))


cnt = 1
for rain_level in range(H):
    visited = [[False] * N for _ in range(N)]
    num = 0
    for i in range(N):
        for j in range(N):
            if tmp[i][j] > rain_level and not visited[i][j]:
                BFS(i, j, visited, rain_level)
                num += 1
    cnt = max(cnt, num)
print(cnt)