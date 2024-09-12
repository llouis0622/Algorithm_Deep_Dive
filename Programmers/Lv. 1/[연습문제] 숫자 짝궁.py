from collections import Counter


def solution(X, Y):
    cntx = Counter(X)
    cnty = Counter(Y)
    res = []
    for i in range(10):
        arr = str(i)
        if arr in cntx and arr in cnty:
            res.extend([arr] * min(cntx[arr], cnty[arr]))
    if not res:
        return "-1"
    res.sort(reverse=True)
    if res[0] == '0':
        return "0"
    return ''.join(res)