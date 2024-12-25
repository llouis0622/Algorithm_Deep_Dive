import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N = int(input())
lst = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)
num = 20
depth = [0] * (N + 1)
parent = [[0] * (N + 1) for _ in range(num)]


def DFS(u, d):
    depth[u] = d
    for v in lst[u]:
        if depth[v] == 0 and v != 1:
            parent[0][v] = u
            DFS(v, d + 1)


DFS(1, 1)
for i in range(1, num):
    for v in range(1, N + 1):
        parent[i][v] = parent[i - 1][parent[i - 1][v]]


def LCA(a, b):
    if depth[a] < depth[b]:
        a, b = b, a
    temp = depth[a] - depth[b]
    for i in range(num):
        if temp & (1 << i):
            a = parent[i][a]
    if a == b:
        return a
    for i in reversed(range(num)):
        if parent[i][a] != parent[i][b]:
            a = parent[i][a]
            b = parent[i][b]
    return parent[0][a]


M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    print(LCA(x, y))