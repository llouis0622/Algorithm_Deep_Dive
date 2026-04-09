from collections import defaultdict


def solution(genres, plays):
    tot = defaultdict(int)
    arr = defaultdict(list)
    for i, (x, y) in enumerate(zip(genres, plays)):
        tot[x] += y
        arr[x].append((y, i))
    ans = []
    for i in sorted(tot, key=lambda x: tot[x], reverse=True):
        arr[i].sort(key=lambda x: (-x[0], x[1]))
        for x, y in arr[i][:2]:
            ans.append(y)
    return ans
