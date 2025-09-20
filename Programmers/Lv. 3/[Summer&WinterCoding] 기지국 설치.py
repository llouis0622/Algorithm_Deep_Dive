def solution(n, stations, w):
    temp = 2 * w + 1
    num = 1
    ans = 0
    for i in stations:
        s = i - w
        if s > num:
            res = s - num
            ans += (res + temp - 1) // temp
        num = max(num, i + w + 1)
    if num <= n:
        res = n - num + 1
        ans += (res + temp - 1) // temp
    return ans