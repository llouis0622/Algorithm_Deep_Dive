import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
temp, num = [], []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            temp.append((i, j))
        elif arr[i][j] == 2:
            num.append((i, j))
ans = float('inf')
for i in combinations(num, M):
    tot = 0
    for x, y in temp:
        dist = float('inf')
        for a, b in i:
            d = abs(x - a) + abs(y - b)
            if d < dist:
                dist = d
        tot += dist
    if tot < ans:
        ans = tot
print(ans)
