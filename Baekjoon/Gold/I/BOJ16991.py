import math
from itertools import permutations


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def TSP(n, temp):
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist[i][j] = distance(temp[i][0], temp[i][1], temp[j][0], temp[j][1])
    DP = [[float('inf')] * (1 << n) for _ in range(n)]
    DP[0][1] = 0
    for m in range(1, 1 << n):
        for u in range(n):
            if m & (1 << u):
                for v in range(n):
                    if not (m & (1 << v)) and u != v:
                        nxt = m | (1 << v)
                        DP[v][nxt] = min(DP[v][nxt], DP[u][m] + dist[u][v])
    cost = float('inf')
    for i in range(1, n):
        cost = min(cost, DP[i][(1 << n) - 1] + dist[i][0])
    return cost


n = int(input())
temp = [tuple(map(int, input().split())) for _ in range(n)]
res = TSP(n, temp)
print(f"{res:.6f}")