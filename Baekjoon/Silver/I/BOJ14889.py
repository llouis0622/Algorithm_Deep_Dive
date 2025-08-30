import sys
from itertools import combinations

n = int(sys.stdin.readline())
s = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
p = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        v = s[i][j] + s[j][i]
        p[i][j] = v
        p[j][i] = v
ans = 10 ** 9
num = range(n)
for c in combinations(range(1, n), n // 2 - 1):
    start = (0,) + c
    check = [False] * n
    for x in start:
        check[x] = True
    temp = [i for i in num if not check[i]]
    a = 0
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            a += p[start[i]][start[j]]
    b = 0
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            b += p[temp[i]][temp[j]]
    d = abs(a - b)
    if d < ans:
        ans = d
    if ans == 0:
        print(0)
        sys.exit(0)
print(ans)