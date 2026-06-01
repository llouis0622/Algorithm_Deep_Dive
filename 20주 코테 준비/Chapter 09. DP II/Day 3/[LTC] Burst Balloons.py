class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(2, n):
            for l in range(n - i):
                r = l + i
                for j in range(l + 1, r):
                    dp[l][r] = max(dp[l][r], dp[l][j] + dp[j][r] + nums[l] * nums[j] * nums[r])
        return dp[0][n - 1]
