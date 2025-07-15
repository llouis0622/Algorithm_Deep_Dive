import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(int(input()) for _ in range(n))
res = int(1e10)
en = 0
for st in range(n):
    while en < n and a[en] - a[st] < m:
        en += 1
    if en == n:
        break
    res = min(res, a[en] - a[st])
print(res)