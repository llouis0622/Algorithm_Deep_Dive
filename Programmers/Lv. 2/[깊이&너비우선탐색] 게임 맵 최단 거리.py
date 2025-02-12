from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    q = deque([(0, 0, 1)])
    while q:
        x, y, d = q.popleft()
        if x == n - 1 and y == m - 1:
            return d
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                q.append((nx, ny, d + 1))
    return -1