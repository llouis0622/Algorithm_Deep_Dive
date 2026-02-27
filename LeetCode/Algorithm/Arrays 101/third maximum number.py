class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = b = c = None
        for i in nums:
            if i == a or i == b or i == c:
                continue
            if a is None or i > a:
                c = b
                b = a
                a = i
            elif b is None or i > b:
                c = b
                b = i
            elif c is None or i > c:
                c = i
        return c if c is not None else a