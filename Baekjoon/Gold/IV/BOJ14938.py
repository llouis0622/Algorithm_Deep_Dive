import sys, heapq

n, m, r = map(int, sys.stdin.readline().split())
temp = [0] + list(map(int, sys.stdin.readline().split()))
adj = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    adj[a].append((b, l))
    adj[b].append((a, l))


def dijkstra(s):
    dist = [10 ** 9] * (n + 1)
    dist[s] = 0
    q = [(0, s)]
    while q:
        d, u = heapq.heappop(q)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            num = d + w
            if num < dist[v]:
                dist[v] = num
                heapq.heappush(q, (num, v))
    return dist


ans = 0
for s in range(1, n + 1):
    dist = dijkstra(s)
    tot = 0
    for i in range(1, n + 1):
        if dist[i] <= m:
            tot += temp[i]
    if tot > ans:
        ans = tot
print(ans)