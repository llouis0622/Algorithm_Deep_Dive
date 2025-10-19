from collections import deque


def solution(n, vertex):
    g = [[] for _ in range(n + 1)]
    for a, b in vertex:
        g[a].append(b)
        g[b].append(a)
    dist = [-1] * (n + 1)
    dist[1] = 0
    q = deque([1])
    while q:
        u = q.popleft()
        for v in g[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    num = max(dist[1:])
    return sum(1 for d in dist[1:] if d == num)