from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0

        def bfs(x, y):
            q = deque([(x, y)])
            grid[x][y] = 0
            area = 1
            while q:
                cx, cy = q.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        q.append((nx, ny))
                        area += 1
            return area

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res = max(res, bfs(i, j))
        return res
