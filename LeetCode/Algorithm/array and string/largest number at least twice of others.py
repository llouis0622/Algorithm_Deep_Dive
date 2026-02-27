class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        num, idx = -1, -1
        for i in range(len(nums)):
            if nums[i] > num:
                num = nums[i]
                idx = i
        for i in range(len(nums)):
            if i != idx and num < 2 * nums[i]:
                return -1
        return idx