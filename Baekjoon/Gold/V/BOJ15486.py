import sys

input = sys.stdin.readline
n = int(input())
consults = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)
for i in range(n):
    t, p = consults[i]
    if i + t <= n:
        dp[i + t] = max(dp[i + t], dp[i] + p)
    dp[i + 1] = max(dp[i + 1], dp[i])
print(dp[n])