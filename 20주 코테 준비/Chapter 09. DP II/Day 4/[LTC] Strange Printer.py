class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(2, n + 1):
            for l in range(n - i + 1):
                r = l + i - 1
                dp[l][r] = dp[l + 1][r] + 1
                for k in range(l + 1, r + 1):
                    if s[l] == s[k]:
                        dp[l][r] = min(dp[l][r], dp[l + 1][k - 1] + dp[k][r])
        return dp[0][n - 1]
