import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, graph, N):
    distance = [INF] * (N + 1)
    distance[start] = 0
    heap = [(0, start)]
    while heap:
        dist, now = heapq.heappop(heap)
        if dist > distance[now]:
            continue
        for i, j in graph[now]:
            temp = dist + j
            if temp < distance[i]:
                distance[i] = temp
                heapq.heappush(heap, (temp, i))
    return distance


N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
rgraph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))
    rgraph[v].append((u, t))
s = dijkstra(X, rgraph, N)
e = dijkstra(X, graph, N)
num = 0
for i in range(1, N + 1):
    num = max(num, s[i] + e[i])
print(num)