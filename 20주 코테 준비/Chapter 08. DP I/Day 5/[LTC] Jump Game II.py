class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        num = 0
        temp = 0
        for i in range(len(nums) - 1):
            temp = max(temp, i + nums[i])
            if i == num:
                ans += 1
                num = temp
        return ans
