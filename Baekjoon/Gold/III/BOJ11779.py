import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)
prev = [-1] * (n + 1)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
start, end = map(int, input().split())


def dijkstra(start):
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cost, u = heapq.heappop(pq)
        if dist[u] < cost:
            continue
        for v, w in graph[u]:
            new_cost = cost + w
            if dist[v] > new_cost:
                dist[v] = new_cost
                prev[v] = u
                heapq.heappush(pq, (new_cost, v))


def reconstruct_path(start, end):
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path


dijkstra(start)
path = reconstruct_path(start, end)
print(dist[end])
print(len(path))
print(*path)