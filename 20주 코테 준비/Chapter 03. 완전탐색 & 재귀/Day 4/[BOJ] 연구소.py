import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
empty = []
virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            empty.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(board):
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
    temp = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                temp += 1
    return temp


ans = 0
for i in combinations(empty, 3):
    board = [num[:] for num in arr]
    for x, y in i:
        board[x][y] = 1
    ans = max(ans, bfs(board))
print(ans)
