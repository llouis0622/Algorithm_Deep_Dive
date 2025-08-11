def solution(stones, k):
    l, r = 1, max(stones)
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        cnt = 0
        check = True
        for stone in stones:
            if stone - mid < 0:
                cnt += 1
                if cnt >= k:
                    check = False
                    break
            else:
                cnt = 0
        if check:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans