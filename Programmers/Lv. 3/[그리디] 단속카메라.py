def solution(routes):
    routes.sort(key=lambda x: x[1])
    ans = 0
    num = -30001
    for i in routes:
        if i[0] > num:
            num = i[1]
            ans += 1
    return ans