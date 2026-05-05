import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]
        while pq:
            num, x, y = heapq.heappop(pq)
            if x == n - 1 and y == m - 1:
                return num
            if dist[x][y] < num:
                continue
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    cost = abs(heights[x][y] - heights[nx][ny])
                    temp = max(num, cost)
                    if temp < dist[nx][ny]:
                        dist[nx][ny] = temp
                        heapq.heappush(pq, (temp, nx, ny))
