from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                middle = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)

    def bfs(sx, sy, ex, ey):
        q = deque()
        visited = [[False] * m for _ in range(n)]
        q.append((sx, sy, 0))
        visited[sx][sy] = True
        while q:
            x, y, dist = q.popleft()
            if x == ex and y == ey:
                return dist
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and maps[nx][ny] != 'X':
                        visited[nx][ny] = True
                        q.append((nx, ny, dist + 1))
        return -1

    d1 = bfs(start[0], start[1], middle[0], middle[1])
    d2 = bfs(middle[0], middle[1], end[0], end[1])
    if d1 == -1 or d2 == -1:
        return -1
    return d1 + d2
