def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    l, h = 1, distance
    ans = 0
    while l <= h:
        m = (l + h) // 2
        prev, num = 0, 0
        for i in rocks:
            if i - prev < m:
                num += 1
            else:
                prev = i
        if num <= n:
            ans = m
            l = m + 1
        else:
            h = m - 1
    return ans
