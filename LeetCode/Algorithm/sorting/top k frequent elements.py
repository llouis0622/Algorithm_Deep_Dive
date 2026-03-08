class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        arr = list(freq.items())
        arr.sort(key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(arr[i][0])
        return res