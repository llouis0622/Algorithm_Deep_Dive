import sys

sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())
a = [0] + list(map(int, sys.stdin.readline().split()))
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)
d1 = [0] * (n + 1)
d2 = [0] * (n + 1)


def dfs(cur, par):
    d1[cur] = a[cur]
    d2[cur] = 0
    for nxt in adj[cur]:
        if nxt == par:
            continue
        dfs(nxt, cur)
        d1[cur] += d2[nxt]
        d2[cur] += max(d1[nxt], d2[nxt])


dfs(1, 0)
print(max(d1[1], d2[1]))