import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    adj = [[] for _ in range(n + 1)]
    d = [-1] * (n + 1)
    for _ in range(k):
        u, v = map(int, input().split())
        adj[v].append(u)
    w = int(input())


    def solve(x):
        if d[x] != -1:
            return d[x]
        d[x] = 0
        for nxt in adj[x]:
            d[x] = max(d[x], solve(nxt))
        d[x] += a[x]
        return d[x]


    print(solve(w))