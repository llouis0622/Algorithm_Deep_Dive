import sys

input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
board = [list(map(int, i.split())) for i in data[1:]]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
visited = [[False] * M for _ in range(N)]
sum = 0


def check(y, x):
    global sum
    if y + 1 < N and x + 2 < M:
        sum = max(sum, board[y][x] + board[y][x + 1] + board[y][x + 2] + board[y + 1][x + 1])
    if y + 2 < N and x + 1 < M:
        sum = max(sum, board[y][x] + board[y + 1][x] + board[y + 1][x + 1] + board[y + 2][x])
    if y - 1 >= 0 and x + 2 < M:
        sum = max(sum, board[y][x] + board[y][x + 1] + board[y][x + 2] + board[y - 1][x + 1])
    if y + 2 < N and x - 1 >= 0:
        sum = max(sum, board[y][x] + board[y + 1][x] + board[y + 1][x - 1] + board[y + 2][x])


def DFS(l, num, y, x):
    global sum
    if l == 3:
        sum = max(sum, num)
        return
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = True
            DFS(l + 1, num + board[ny][nx], ny, nx)
            visited[ny][nx] = False


def max_find():
    for y in range(N):
        for x in range(M):
            check(y, x)
            visited[y][x] = True
            DFS(0, board[y][x], y, x)
            visited[y][x] = False


max_find()
print(sum)