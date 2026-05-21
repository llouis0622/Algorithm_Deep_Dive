class Solution:
    def canJump(self, nums: List[int]) -> bool:
        temp = 0
        for i in range(len(nums)):
            if i > temp:
                return False
            temp = max(temp, i + nums[i])
        return True
