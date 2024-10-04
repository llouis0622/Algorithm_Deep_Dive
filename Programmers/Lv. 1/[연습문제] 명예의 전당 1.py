def solution(k, score):
    arr = []
    res = []
    for i in score:
        if len(arr) < k:
            arr.append(i)
        else:
            if i > min(arr):
                arr.remove(min(arr))
                arr.append(i)
        res.append(min(arr))
    return res