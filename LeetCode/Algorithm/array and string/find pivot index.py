class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        num = sum(nums)
        l = 0
        for i in range(len(nums)):
            if l == num - l - nums[i]:
                return i
            l += nums[i]
        return -1