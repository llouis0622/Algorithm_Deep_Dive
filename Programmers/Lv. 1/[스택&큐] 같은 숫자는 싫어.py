def solution(arr):
    result = []
    for i in arr:
        if not result or result[-1] != i:
            result.append(i)
    return result