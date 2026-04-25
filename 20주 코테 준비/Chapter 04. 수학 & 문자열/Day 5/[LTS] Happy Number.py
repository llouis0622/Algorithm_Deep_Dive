class Solution:
    def isHappy(self, n: int) -> bool:
        arr = set()
        while n != 1:
            if n in arr:
                return False
            arr.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return True
