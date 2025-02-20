import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
dp = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + p[j - 1])
print(dp[n])