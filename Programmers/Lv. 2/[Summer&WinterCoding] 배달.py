import heapq


def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    heap = []
    heapq.heappush(heap, (0, 1))
    while heap:
        cost, now = heapq.heappop(heap)
        if dist[now] < cost:
            continue
        for temp, time in graph[now]:
            res = cost + time
            if res < dist[temp]:
                dist[temp] = res
                heapq.heappush(heap, (res, temp))
    ans = sum(1 for d in dist if d <= K)
    return ans