class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        while l <= r:
            m = (l + r) // 2
            temp, cur = 1, 0
            for i in nums:
                if cur + i > m:
                    temp += 1
                    cur = 0
                cur += i
            if temp <= k:
                r = m - 1
            else:
                l = m + 1
        return l
