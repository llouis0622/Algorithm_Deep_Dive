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
        cost, cur = heapq.heappop(heap)
        if dist[cur] < cost:
            continue
        for i, time in graph[cur]:
            res = cost + time
            if res < dist[i]:
                dist[i] = res
                heapq.heappush(heap, (res, i))
    ans = sum(1 for d in dist if d <= K)
    return ans
