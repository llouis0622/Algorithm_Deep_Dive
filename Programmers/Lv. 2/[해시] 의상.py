from collections import defaultdict


def solution(clothes):
    cnt = defaultdict(int)
    for i, c in clothes:
        cnt[c] += 1
    res = 1
    for j in cnt.values():
        res *= (j + 1)
    return res - 1