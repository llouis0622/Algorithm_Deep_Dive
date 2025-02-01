import sys
from collections import deque

input = sys.stdin.read
data = input().split("\n")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
idx = 0
T = int(data[idx])
idx += 1
res = []
for _ in range(T):
    w, h = map(int, data[idx].split())
    idx += 1
    board = [list(data[idx + i]) for i in range(h)]
    idx += h
    fq, sq = deque(), deque()
    fire = [[-1] * w for _ in range(h)]
    dist = [[-1] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                fq.append((i, j))
                fire[i][j] = 0
            elif board[i][j] == '@':
                sx, sy = i, j
                dist[i][j] = 0
                sq.append((i, j))
    while fq:
        x, y = fq.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == '.' and fire[nx][ny] == -1:
                fire[nx][ny] = fire[x][y] + 1
                fq.append((nx, ny))
    escaped = False
    while sq:
        x, y = sq.popleft()
        if x == 0 or y == 0 or x == h - 1 or y == w - 1:
            res.append(str(dist[x][y] + 1))
            escaped = True
            break
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == '.' and dist[nx][ny] == -1:
                if fire[nx][ny] == -1 or dist[x][y] + 1 < fire[nx][ny]:
                    dist[nx][ny] = dist[x][y] + 1
                    sq.append((nx, ny))
    if not escaped:
        res.append("IMPOSSIBLE")
print("\n".join(res))