def solution(players, m, k):
    temp = [p // m for p in players]
    check = [0] * 25
    num = 0
    ans = 0
    for t in range(24):
        num -= check[t]
        res = temp[t]
        add = res - num
        if add > 0:
            ans += add
            num += add
            if t + k <= 24:
                check[t + k] += add
    return ans