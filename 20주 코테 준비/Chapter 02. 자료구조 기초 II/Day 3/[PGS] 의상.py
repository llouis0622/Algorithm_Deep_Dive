from collections import defaultdict


def solution(clothes):
    arr = defaultdict(int)
    for i, j in clothes:
        arr[j] += 1
    res = 1
    for i in arr.values():
        res *= (i + 1)
    return res - 1
