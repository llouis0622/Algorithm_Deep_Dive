import sys

input = sys.stdin.readline


def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return False
    if rank[a] < rank[b]:
        a, b = b, a
    parent[b] = a
    if rank[a] == rank[b]:
        rank[a] += 1
    return True


V, E = map(int, input().split())
edges = []
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()
parent = list(range(V + 1))
rank = [0] * (V + 1)
cnt = 0
ans = 0
for cost, a, b in edges:
    if union(a, b):
        ans += cost
        cnt += 1
        if cnt == V - 1:
            break
print(ans)

# import sys, heapq
# input = sys.stdin.readline
#
# V, E = map(int, input().split())
# adj = [[] for _ in range(V + 1)]
# for _ in range(E):
#     a, b, c = map(int, input().split())
#     adj[a].append((c, b))
#     adj[b].append((c, a))
# visited = [False] * (V + 1)
# pq = []
# visited[1] = True
# for w, v in adj[1]:
#     heapq.heappush(pq, (w, v))
# cnt = 1
# ans = 0
# while cnt < V:
#     w, v = heapq.heappop(pq)
#     if visited[v]:
#         continue
#     visited[v] = True
#     ans += w
#     cnt += 1
#     for nw, nv in adj[v]:
#         if not visited[nv]:
#             heapq.heappush(pq, (nw, nv))
# print(ans)