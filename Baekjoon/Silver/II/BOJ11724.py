import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)


def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)


for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)
cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        DFS(i)
print(cnt)