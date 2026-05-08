from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        check = False

        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= n:
                return
            if grid[x][y] != 1:
                return
            grid[x][y] = 2
            q.append((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x + dx, y + dy)

        for i in range(n):
            if check:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    check = True
                    break
        num = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            return num
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 2
                            q.append((nx, ny))
            num += 1
