def solution(s):
    n = len(s)
    if n == 0:
        return 0
    
    
    def expand(l, r):
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1
    
    
    ans = 1
    for i in range(n):
        x = expand(i, i)
        y = expand(i, i + 1)
        ans = max(ans, x, y)
    return ans