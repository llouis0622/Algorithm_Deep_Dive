def solution(a, b, c, d):
    lst = [a, b, c, d]
    cnt = {}
    for i in lst:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    v = list(cnt.values())
    k = list(cnt.keys())
    if len(cnt) == 1:
        return 1111 * k[0]
    if 3 in v:
        x = k[v.index(3)]
        y = k[v.index(1)]
        return (10 * x + y) ** 2
    if len(cnt) == 2 and v.count(2) == 2:
        x, y = k
        return (x + y) * abs(x - y)
    if 2 in v and 1 in v:
        y = k[v.index(1)]
        z = k[v.index(1, v.index(1) + 1)]
        return y * z
    return min(lst)