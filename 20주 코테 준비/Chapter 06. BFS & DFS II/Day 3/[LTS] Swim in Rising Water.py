import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        pq = [(grid[0][0], 0, 0)]
        while pq:
            t, x, y = heapq.heappop(pq)
            if x == n - 1 and y == n - 1:
                return t
            if visited[x][y]:
                continue
            visited[x][y] = True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[nx][ny]:
                        heapq.heappush(pq, (max(t, grid[nx][ny]), nx, ny))
