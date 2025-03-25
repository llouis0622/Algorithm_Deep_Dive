from collections import Counter


def solution(k, tangerine):
    counter = Counter(tangerine)
    cnt = sorted(counter.values(), reverse=True)
    total = 0
    temp = 0
    for c in cnt:
        total += c
        temp += 1
        if total >= k:
            break
    return temp