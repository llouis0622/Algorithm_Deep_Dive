def solution(n, times):
    l, r = 1, max(times) * n
    ans = r
    while l <= r:
        mid = (l + r) // 2
        temp = sum(mid // t for t in times)
        if temp >= n:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans