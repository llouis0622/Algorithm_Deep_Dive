def solution(n):
    dp = [0] * (n + 2)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
    return dp[n]
