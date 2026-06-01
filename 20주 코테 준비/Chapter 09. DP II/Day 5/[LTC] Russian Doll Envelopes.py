from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        lis = []
        for _, i in envelopes:
            idx = bisect_left(lis, i)
            if idx == len(lis):
                lis.append(i)
            else:
                lis[idx] = i
        return len(lis)
