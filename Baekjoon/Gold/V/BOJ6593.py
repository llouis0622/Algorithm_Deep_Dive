import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

idx = 0
dz = [0, 0, 0, 0, 1, -1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

while True:
    L, R, C = map(int, data[idx].split())
    if L == 0 and R == 0 and C == 0:
        break
    idx += 1
    building = []
    start = end = None
    for l in range(L):
        floor = [list(data[idx + r]) for r in range(R)]
        building.append(floor)
        for r in range(R):
            for c in range(C):
                if floor[r][c] == 'S':
                    start = (l, r, c)
                elif floor[r][c] == 'E':
                    end = (l, r, c)
        idx += R
        if idx < len(data) and data[idx] == "":
            idx += 1


    def bfs():
        q = deque([(start[0], start[1], start[2], 0)])
        visited = [[[False] * C for _ in range(R)] for _ in range(L)]
        visited[start[0]][start[1]][start[2]] = True
        while q:
            z, x, y, time = q.popleft()
            if (z, x, y) == end:
                return f"Escaped in {time} minute(s)."
            for d in range(6):
                nz, nx, ny = z + dz[d], x + dx[d], y + dy[d]
                if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C and not visited[nz][nx][ny]:
                    if building[nz][nx][ny] != '#':
                        visited[nz][nx][ny] = True
                        q.append((nz, nx, ny, time + 1))
        return "Trapped!"


    print(bfs())