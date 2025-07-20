def solution(m, n, puddles):
    MOD = 1_000_000_007
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for x, y in puddles:
        dp[y][x] = -1
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if dp[y][x] == -1:
                dp[y][x] = 0
                continue
            if x > 1:
                dp[y][x] += dp[y][x - 1]
            if y > 1:
                dp[y][x] += dp[y - 1][x]
            dp[y][x] %= MOD
    return dp[n][m]