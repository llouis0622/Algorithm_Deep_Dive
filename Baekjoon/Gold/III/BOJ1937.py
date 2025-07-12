import sys

sys.setrecursionlimit(1000000)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
d = [[-1] * n for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def check(x, y):
    return x < 0 or x >= n or y < 0 or y >= n


def solve(x, y):
    if d[x][y] != -1:
        return d[x][y]
    d[x][y] = 1
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if check(nx, ny) or board[x][y] >= board[nx][ny]:
            continue
        d[x][y] = max(d[x][y], solve(nx, ny) + 1)
    return d[x][y]


ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, solve(i, j))
print(ans)