class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        s = min(strs)
        t = max(strs)
        i = 0
        while i < len(s) and s[i] == t[i]:
            i += 1
        return s[:i]