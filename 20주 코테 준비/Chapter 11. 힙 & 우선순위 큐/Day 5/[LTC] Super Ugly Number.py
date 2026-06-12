import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        heap = [(i, i, 0) for i in primes]
        heapq.heapify(heap)
        while len(ugly) < n:
            val, num, idx = heapq.heappop(heap)
            if val != ugly[-1]:
                ugly.append(val)
            heapq.heappush(heap,(num * ugly[idx + 1], num, idx + 1))
        return ugly[-1]
