class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        N = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[N] = nums[i]
                N += 1
        for i in range(N, len(nums)):
            nums[i] = 0