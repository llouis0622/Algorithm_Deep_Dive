import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        num = sorted(zip(capital, profits))
        heap = []
        idx = 0
        for _ in range(k):
            while idx < len(num) and num[idx][0] <= w:
                heapq.heappush(heap, -num[idx][1])
                idx += 1
            if not heap:
                break
            w += -heapq.heappop(heap)
        return w
