class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for m in range(n):
            l = r = m
            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
            l, r = m, m + 1
            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        return ans
