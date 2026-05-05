from collections import deque


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))
        dist = [float('inf')] * n
        dist[src] = 0
        q = deque()
        q.append((src, 0))
        num = 0
        while q and num <= k:
            size = len(q)
            temp = dist[:]
            for _ in range(size):
                node, cost = q.popleft()
                for nxt, price in graph[node]:
                    if cost + price < temp[nxt]:
                        temp[nxt] = cost + price
                        q.append((nxt, cost + price))
            dist = temp
            num += 1
        return dist[dst] if dist[dst] != float('inf') else -1
