import sys

input = sys.stdin.readline


def find(x):
    while p[x] >= 0:
        if p[p[x]] >= 0:
            p[x] = p[p[x]]
        x = p[x]
    return x


def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return
    if p[a] > p[b]:
        a, b = b, a
    p[a] += p[b]
    p[b] = a


T = int(input())
ans = []
for i in range(1, T + 1):
    n = int(input())
    k = int(input())
    p = [-1] * n
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)
    m = int(input())
    ans.append(f"Scenario {i}:")
    for _ in range(m):
        u, v = map(int, input().split())
        ans.append("1" if find(u) == find(v) else "0")
    if i != T:
        ans.append("")
print("\n".join(ans))