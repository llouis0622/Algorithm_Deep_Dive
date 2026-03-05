class Solution:
    def smallestTrimmedNumbers(self, nums, queries):
        n = len(nums)
        m = len(nums[0])
        arr = [[] for _ in range(m + 1)]
        for i, (k, t) in enumerate(queries):
            arr[t].append((k, i))
        o = list(range(n))
        ans = [0] * len(queries)
        for t in range(1, m + 1):
            pos = m - t
            cnt = [[] for _ in range(10)]
            for idx in o:
                d = ord(nums[idx][pos]) - 48
                cnt[d].append(idx)
            new_o = []
            for d in range(10):
                new_o.extend(cnt[d])
            o = new_o
            for k, qi in arr[t]:
                ans[qi] = o[k - 1]
        return ans