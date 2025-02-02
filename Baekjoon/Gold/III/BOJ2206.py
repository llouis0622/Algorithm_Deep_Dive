import sys
from collections import deque

input = sys.stdin.read
data = input().split("\n")

N, M = map(int, data[0].split())
tmp = [list(map(int, list(data[i + 1]))) for i in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def BFS():
    q = deque([(0, 0, 0)])
    dist = [[[float('inf')] * 2 for _ in range(M)] for _ in range(N)]
    dist[0][0][0] = 1
    while q:
        x, y, num = q.popleft()
        if x == N - 1 and y == M - 1:
            return dist[x][y][num]
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if tmp[nx][ny] == 0 and dist[nx][ny][num] == float('inf'):
                    dist[nx][ny][num] = dist[x][y][num] + 1
                    q.append((nx, ny, num))
                elif tmp[nx][ny] == 1 and not num and dist[nx][ny][1] == float('inf'):
                    dist[nx][ny][1] = dist[x][y][0] + 1
                    q.append((nx, ny, 1))
    return -1


print(BFS())