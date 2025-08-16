MOD = 1_000_000_003
N = int(input())
K = int(input())
dp = [[0] * (K + 1) for _ in range(N + 1)]
for n in range(N + 1):
    dp[n][0] = 1
    if n >= 1 and K >= 1:
        dp[n][1] = n
for n in range(2, N + 1):
    for k in range(2, min(K, (n + 1) // 2) + 1):
        dp[n][k] = (dp[n - 1][k] + dp[n - 2][k - 1]) % MOD
if K > N // 2:
    print(0)
else:
    case1 = dp[N - 1][K]
    case2 = dp[N - 3][K - 1] if N >= 3 and K >= 1 else 0
    print((case1 + case2) % MOD)