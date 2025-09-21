import sys
from collections import deque

N = int(sys.stdin.readline().strip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ax = ay = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            ax, ay = i, j
            board[i][j] = 0
temp = 2
eat, ans = 0, 0
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def BFS(x, y, sz):
    dist = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((x, y))
    dist[x][y] = 0
    check = None
    tx = ty = None
    while q:
        cx, cy = q.popleft()
        d = dist[cx][cy]
        if check is not None and d > check:
            break
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
                if board[nx][ny] <= sz:
                    dist[nx][ny] = d + 1
                    if 0 < board[nx][ny] < sz:
                        if check is None or d + 1 < check or (d + 1 == check and (nx < tx or (nx == tx and ny < ty))):
                            check = d + 1
                            tx, ty = nx, ny
                    else:
                        q.append((nx, ny))
    if check is None:
        return None
    return tx, ty, check


while True:
    res = BFS(ax, ay, temp)
    if not res:
        break
    x, y, t = res
    ans += t
    eat += 1
    board[x][y] = 0
    ax, ay = x, y
    if eat == temp:
        temp += 1
        eat = 0
print(ans)