import sys
input = sys.stdin.readline

N, R, Q = map(int, input().split())
temp = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    temp[u].append(v)
    temp[v].append(u)
p = [0] * (N + 1)
o = [R]
p[R] = -1
for v in o:
    for w in temp[v]:
        if w == p[v]:
            continue
        p[w] = v
        o.append(w)
num = [1] * (N + 1)
for v in reversed(o):
    for w in temp[v]:
        if w == p[v]:
            continue
        num[v] += num[w]
res = []
for _ in range(Q):
    u = int(input())
    res.append(str(num[u]))
print("\n".join(res))