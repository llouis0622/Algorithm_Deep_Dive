def solution(storey):
    ans = 0
    while storey > 0:
        r = storey % 10
        if r > 5:
            ans += 10 - r
            storey += 10
        elif r < 5:
            ans += r
        else:
            if (storey // 10) % 10 >= 5:
                storey += 10
            ans += 5
        storey //= 10
    return ans