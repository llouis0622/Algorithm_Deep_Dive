from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for i in nums:
            idx = bisect_left(lis, i)
            if idx == len(lis):
                lis.append(i)
            else:
                lis[idx] = i
        return len(lis)
