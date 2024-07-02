def solution(num, k):
    arr = str(num)
    idx = arr.find(str(k))
    return idx + 1 if idx != -1 else -1