import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        heap = [(0, 0)]
        ans = 0
        cnt = 0
        while cnt < n:
            cost, cur = heapq.heappop(heap)
            if visited[cur]:
                continue
            visited[cur] = True
            ans += cost
            cnt += 1
            x1, y1 = points[cur]
            for nxt in range(n):
                if not visited[nxt]:
                    x2, y2 = points[nxt]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(heap, (dist, nxt))
        return ans
