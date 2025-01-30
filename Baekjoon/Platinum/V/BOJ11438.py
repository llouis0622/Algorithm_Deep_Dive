import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
tree = [[0] for _ in range(N + 1)]

for _ in range(0, N - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

depth = [0] * (N + 1)
visited = [False] * (N + 1)
temp = 1
kmax = 0

while temp <= N:
    temp <<= 1
    kmax += 1

parent = [[0 for j in range(N + 1)] for i in range(kmax + 1)]


def BFS(node):
    queue = deque()
    queue.append(node)
    visited[node] = True
    level = 1
    now_size = 1
    count = 0

    while queue:
        now_node = queue.popleft()

        for next in tree[now_node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                parent[0][next] = now_node
                depth[next] = level

        count += 1

        if count == now_size:
            count = 0
            now_size = len(queue)
            level += 1


BFS(1)

for k in range(1, kmax + 1):
    for n in range(1, N + 1):
        parent[k][n] = parent[k - 1][parent[k - 1][n]]


def excuteLCA(a, b):
    if depth[a] > depth[b]:
        temp = a
        a = b
        b = temp

    for k in range(kmax, -1, -1):
        if pow(2, k) <= depth[b] - depth[a]:
            if depth[a] <= depth[parent[k][b]]:
                b = parent[k][b]

    for k in range(kmax, -1, -1):
        if a == b:
            break

        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    LCA = a

    if a != b:
        LCA = parent[0][LCA]

    return LCA


M = int(input())

for _ in range(M):
    a, b = map(int, input().split())
    print(str(excuteLCA(a, b)))
    print("\n")