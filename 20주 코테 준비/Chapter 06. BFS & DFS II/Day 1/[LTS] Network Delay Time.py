import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        pq = [(0, k)]
        while pq:
            time, node = heapq.heappop(pq)
            if dist[node] < time:
                continue
            for nxt, w in graph[node]:
                temp = time + w
                if temp < dist[nxt]:
                    dist[nxt] = temp
                    heapq.heappush(pq, (temp, nxt))
        num = max(dist[1:])
        return num if num != float('inf') else -1
