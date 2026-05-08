from collections import deque


class Solution:
    def wallsAndGates(self, rooms):
        if not rooms:
            return
        n, m = len(rooms), len(rooms[0])
        q = deque()
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if rooms[nx][ny] == 2147483647:
                        rooms[nx][ny] = rooms[x][y] + 1
                        q.append((nx, ny))
