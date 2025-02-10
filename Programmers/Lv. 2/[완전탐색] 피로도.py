from itertools import permutations


def solution(k, dungeons):
    max_count = 0
    for order in permutations(dungeons):
        fatigue = k
        count = 0
        for req, cost in order:
            if fatigue < req:
                break
            fatigue -= cost
            count += 1
        max_count = max(max_count, count)
    return max_count