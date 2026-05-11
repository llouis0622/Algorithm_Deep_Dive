def solution(n, times):
    l, h = 1, max(times) * n
    ans = 0
    while l <= h:
        m = (l + h) // 2
        num = sum(m // i for i in times)
        if n <= num:
            ans = m
            h = m - 1
        else:
            l = m + 1
    return ans
