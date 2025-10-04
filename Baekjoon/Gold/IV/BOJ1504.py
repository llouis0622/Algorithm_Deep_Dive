import sys
import heapq

N, E = map(int, sys.stdin.readline().split())
g = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    g[a].append((b, c))
    g[b].append((a, c))
v1, v2 = map(int, sys.stdin.readline().split())
INF = 10 ** 18


def dijkstra(s):
    dist = [INF] * (N + 1)
    dist[s] = 0
    h = [(0, s)]
    while h:
        d, u = heapq.heappop(h)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            num = d + w
            if num < dist[v]:
                dist[v] = num
                heapq.heappush(h, (num, v))
    return dist


djk = dijkstra(1)
dV1 = dijkstra(v1)
dV2 = dijkstra(v2)
path1 = djk[v1] + dV1[v2] + dV2[N]
path2 = djk[v2] + dV2[v1] + dV1[N]
ans = min(path1, path2)
print(ans if ans < INF else -1)