class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        num = [True] * n
        num[0] = num[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if num[i]:
                for j in range(i * i, n, i):
                    num[j] = False
        return sum(num)
