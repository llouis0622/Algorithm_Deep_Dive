def solution(arr):
    lst = [i for i, x in enumerate(arr) if x == 2]
    if not lst:
        return [-1]
    return arr[lst[0]:lst[-1] + 1]