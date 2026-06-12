import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        cmax = float('-inf')
        for i, arr in enumerate(nums):
            heapq.heappush(heap, (arr[0], i, 0))
            cmax = max(cmax, arr[0])
        l, r = float('-inf'), float('inf')
        while True:
            cmin, row, col = heapq.heappop(heap)
            if cmax - cmin < r - l:
                l, r = cmin, cmax
            if col + 1 == len(nums[row]):
                break
            temp = nums[row][col + 1]
            heapq.heappush(heap, (temp, row, col + 1))
            cmax = max(cmax, temp)
        return [l, r]
