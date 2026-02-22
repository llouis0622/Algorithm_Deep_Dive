class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[n - 1]:
                nums[n] = nums[i]
                n += 1
        return n