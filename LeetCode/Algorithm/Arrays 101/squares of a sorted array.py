class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s = []
        for i in nums:
            s.append(i * i)
        return sorted(s)