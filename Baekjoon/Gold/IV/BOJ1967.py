import sys
from collections import defaultdict, deque

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])
edges = [tuple(map(int, line.split())) for line in data[1:]]

graph = defaultdict(list)
for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))


def bfs(start):
    q = deque([(start, 0)])
    visited = [-1] * (n + 1)
    visited[start] = 0
    farthest_node, max_dist = start, 0

    while q:
        node, dist = q.popleft()
        if dist > max_dist:
            farthest_node, max_dist = node, dist
        for neighbor, weight in graph[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = dist + weight
                q.append((neighbor, dist + weight))

    return farthest_node, max_dist


farthest, _ = bfs(1)
_, diameter = bfs(farthest)
print(diameter)