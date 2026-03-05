class Solution:
    def maximumGap(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        mn = min(nums)
        mx = max(nums)
        if mn == mx:
            return 0
        s = max(1, (mx - mn) // (n - 1))
        cnt = (mx - mn) // s + 1
        a = [10 ** 18] * cnt
        b = [-1] * cnt
        used = [False] * cnt
        for i in nums:
            idx = (i - mn) // s
            if not used[idx]:
                a[idx] = i
                b[idx] = i
                used[idx] = True
            else:
                if i < a[idx]:
                    a[idx] = i
                if i > b[idx]:
                    b[idx] = i
        prev = mn
        ans = 0
        for i in range(cnt):
            if not used[i]:
                continue
            ans = max(ans, a[i] - prev)
            prev = b[i]
        return ans