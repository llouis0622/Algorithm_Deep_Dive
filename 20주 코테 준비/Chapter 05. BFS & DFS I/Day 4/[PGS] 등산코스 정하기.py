import heapq


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    for a, b, w in paths:
        graph[a].append((b, w))
        graph[b].append((a, w))
    temp = set(summits)
    num = [float('inf')] * (n + 1)
    heap = []
    for i in gates:
        num[i] = 0
        heapq.heappush(heap, (0, i))
    while heap:
        cur, node = heapq.heappop(heap)
        if cur > num[node]:
            continue
        if node in temp:
            continue
        for nxt, weight in graph[node]:
            nxt_num = max(cur, weight)
            if nxt_num < num[nxt]:
                num[nxt] = nxt_num
                heapq.heappush(heap, (nxt_num, nxt))
    ans = [0, float('inf')]
    for i in sorted(summits):
        if num[i] < ans[1]:
            ans = [i, num[i]]
    return ans
