def solution(arr):
    idx = 1
    while idx < len(arr):
        idx *= 2
    while len(arr) < idx:
        arr.append(0)
    return arr