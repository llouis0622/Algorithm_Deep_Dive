class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        l = 0
        s = 0
        ans = n + 1
        for i in range(n):
            s += nums[i]
            while s >= target:
                if i - l + 1 < ans:
                    ans = i - l + 1
                s -= nums[l]
                l += 1
        return 0 if ans == n + 1 else ans