class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            N = abs(i) - 1
            if nums[N] > 0:
                nums[N] = -nums[N]
        arr = []
        for i in range(len(nums)):
            if nums[i] > 0:
                arr.append(i + 1)
        return arr