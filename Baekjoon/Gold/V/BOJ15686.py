from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))


def calculate(check):
    tot = 0
    for hx, hy in houses:
        temp = float('inf')
        for cx, cy in check:
            dist = abs(hx - cx) + abs(hy - cy)
            temp = min(temp, dist)
        tot += temp
    return tot


res = float('inf')
for i in combinations(chickens, M):
    num = calculate(i)
    res = min(res, num)
print(res)