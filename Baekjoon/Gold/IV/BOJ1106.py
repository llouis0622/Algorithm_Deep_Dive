import sys

C, N = map(int, sys.stdin.readline().split())
num = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
TEMP = C + 100
INF = 10 ** 9
dp = [INF] * (TEMP + 1)
dp[0] = 0
for i, j in num:
    for c in range(j, TEMP + 1):
        nc = dp[c - j] + i
        if nc < dp[c]:
            dp[c] = nc
print(min(dp[C:]))