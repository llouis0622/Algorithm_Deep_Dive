from collections import defaultdict


def solution(genres, plays):
    tot = defaultdict(int)
    temp = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        tot[g] += p
        temp[g].append((p, i))
    num = sorted(tot.keys(), key=lambda g: -tot[g])
    ans = []
    for g in num:
        song = sorted(temp[g], key=lambda x: (-x[0], x[1]))
        ans.extend(i for _, i in song[:2])
    return ans