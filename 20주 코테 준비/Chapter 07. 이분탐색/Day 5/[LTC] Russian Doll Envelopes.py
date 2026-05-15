from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        arr = []
        for _, h in envelopes:
            idx = bisect_left(arr, h)
            if idx == len(arr):
                arr.append(h)
            else:
                arr[idx] = h
        return len(arr)
