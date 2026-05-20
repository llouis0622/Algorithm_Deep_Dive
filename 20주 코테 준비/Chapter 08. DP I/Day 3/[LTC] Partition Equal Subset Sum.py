class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2:
            return False
        num = tot // 2
        dp = [False] * (num + 1)
        dp[0] = True
        for i in nums:
            for j in range(num, i - 1, -1):
                dp[j] = dp[j] or dp[j - i]
        return dp[num]
