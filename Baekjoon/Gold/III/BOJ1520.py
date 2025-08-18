import sys

sys.setrecursionlimit(10 ** 6)

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(y, x):
    if y == M - 1 and x == N - 1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < M and 0 <= nx < N:
            if board[ny][nx] < board[y][x]:
                dp[y][x] += dfs(ny, nx)
    return dp[y][x]


print(dfs(0, 0))