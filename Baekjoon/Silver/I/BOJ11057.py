import sys

n = int(sys.stdin.readline())
dp = [[0] * 10 for _ in range(n + 1)]
for i in range(10):
    dp[1][i] = 1
for i in range(2, n + 1):
    for j in range(10):
        dp[i][j] = sum(dp[i - 1][k] for k in range(j + 1)) % 10007
print(sum(dp[n]) % 10007)