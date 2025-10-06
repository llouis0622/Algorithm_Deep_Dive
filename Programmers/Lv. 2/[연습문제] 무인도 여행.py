from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    ans = []
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                s = 0
                while q:
                    x, y = q.popleft()
                    s += int(maps[x][y])
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                            visited[nx][ny] = True
                            q.append((nx, ny))
                ans.append(s)
    return sorted(ans) if ans else [-1]