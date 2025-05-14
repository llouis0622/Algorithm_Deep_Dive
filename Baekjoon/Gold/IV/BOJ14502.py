import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

zero = [(i, j) for i in range(N) for j in range(M) if lst[i][j] == 0]
virus = [(i, j) for i in range(N) for j in range(M) if lst[i][j] == 2]


def BFS(w):
    grid = [row[:] for row in lst]
    for x, y in w:
        grid[x][y] = 1
    dq = deque(virus)
    while dq:
        x, y = dq.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
                grid[nx][ny] = 2
                dq.append((nx, ny))
    return sum(row.count(0) for row in grid)


ans = 0
for w in combinations(zero, 3):
    temp = BFS(w)
    if temp > ans:
        ans = temp
print(ans)