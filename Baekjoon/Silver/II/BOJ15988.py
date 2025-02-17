import sys

MOD = 1_000_000_009
MAX_N = 1_000_000
dp = [0] * (MAX_N + 1)
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, MAX_N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])