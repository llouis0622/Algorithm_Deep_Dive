import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
D = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def BFS():
    res = [[False] * M for _ in range(N)]
    q = deque([(0, 0)])
    res[0][0] = True
    while q:
        r, c = q.popleft()
        for dr, dc in D:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not res[nr][nc] and A[nr][nc] == 0:
                res[nr][nc] = True
                q.append((nr, nc))
    return res


t = 0
while True:
    res = BFS()
    temp = []
    for i in range(N):
        for j in range(M):
            if A[i][j] == 1:
                cnt = 0
                for dr, dc in D:
                    ni, nj = i + dr, j + dc
                    if 0 <= ni < N and 0 <= nj < M and res[ni][nj]:
                        cnt += 1
                if cnt >= 2:
                    temp.append((i, j))
    if not temp:
        break
    for i, j in temp:
        A[i][j] = 0
    t += 1
print(t)