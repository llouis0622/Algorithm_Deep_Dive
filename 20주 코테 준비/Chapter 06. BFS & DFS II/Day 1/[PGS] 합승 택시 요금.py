import heapq


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))

    def dijkstra(start):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            cost, node = heapq.heappop(pq)
            if dist[node] < cost:
                continue
            for nxt, weight in graph[node]:
                temp = cost + weight
                if temp < dist[nxt]:
                    dist[nxt] = temp
                    heapq.heappush(pq, (temp, nxt))
        return dist

    dist_s, dist_a, dist_b = dijkstra(s), dijkstra(a), dijkstra(b)
    ans = float('inf')
    for i in range(1, n + 1):
        ans = min(ans, dist_s[i] + dist_a[i] + dist_b[i])
    return ans
