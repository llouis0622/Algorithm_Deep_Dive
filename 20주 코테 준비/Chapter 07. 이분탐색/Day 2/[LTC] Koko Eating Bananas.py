class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            m = (l + r) // 2
            time = 0
            for i in piles:
                time += (i + m - 1) // m
            if time <= h:
                r = m - 1
            else:
                l = m + 1
        return l
