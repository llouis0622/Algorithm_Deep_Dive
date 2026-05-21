class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num_u, num_d = nums[0], nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                num_u, num_d = num_d, num_u
            num_u = max(nums[i], num_u * nums[i])
            num_d = min(nums[i], num_d * nums[i])
            ans = max(ans, num_u)
        return ans
