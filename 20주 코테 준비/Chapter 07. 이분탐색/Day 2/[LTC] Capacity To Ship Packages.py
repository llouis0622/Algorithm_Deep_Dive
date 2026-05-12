class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l <= r:
            m = (l + r) // 2
            num, cur = 1, 0
            for i in weights:
                if m < cur + i:
                    num += 1
                    cur = 0
                cur += i
            if num <= days:
                r = m - 1
            else:
                l = m + 1
        return l
