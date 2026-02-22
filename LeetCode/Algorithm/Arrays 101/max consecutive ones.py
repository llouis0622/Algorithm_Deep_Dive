class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a, cnt = 0, 0
        for i in nums:
            if i == 1:
                cnt += 1
                if cnt > a:
                    a = cnt
            else:
                cnt = 0
        return a