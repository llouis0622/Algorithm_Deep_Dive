import sys
input = sys.stdin.readline


def find(x):
    while x != p[x]:
        p[x] = p[p[x]]
        x = p[x]
    return x


def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return False
    if r[a] < r[b]:
        a, b = b, a
    p[b] = a
    if r[a] == r[b]:
        r[a] += 1
    return True


N = int(input().strip())
W = [0] + [int(input().strip()) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]
edges = []
for i in range(1, N + 1):
    edges.append((W[i], 0, i))
for i in range(N):
    for j in range(i + 1, N):
        edges.append((P[i][j], i + 1, j + 1))
edges.sort()
p = list(range(N + 1 + 1))
r = [0] * (N + 1 + 1)
cnt = 0
ans = 0
for w, a, b in edges:
    if union(a, b):
        ans += w
        cnt += 1
        if cnt == N:
            break
print(ans)

# import sys, heapq
# input = sys.stdin.readline
#
# N = int(input().strip())
# W = [0] + [int(input().strip()) for _ in range(N)]
# P = [list(map(int, input().split())) for _ in range(N)]
# adj = [[] for _ in range(N + 1)]
# for i in range(1, N + 1):
#     adj[0].append((W[i], i))
# for i in range(N):
#     for j in range(i + 1, N):
#         c = P[i][j]
#         a, b = i + 1, j + 1
#         adj[a].append((c, b))
#         adj[b].append((c, a))
# visited = [False] * (N + 1)
# pq = []
# visited[0] = True
# for w, v in adj[0]:
#     heapq.heappush(pq, (w, v))
# cnt = 0
# ans = 0
# while cnt < N:
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