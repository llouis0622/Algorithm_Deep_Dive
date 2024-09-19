def solution(s):
    arr = {}
    res = []
    for i, j in enumerate(s):
        if j in arr:
            res.append(i - arr[j])
        else:
            res.append(-1)
        arr[j] = i
    return res