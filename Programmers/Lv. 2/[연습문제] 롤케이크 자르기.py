from collections import defaultdict


def solution(topping):
    ans = 0
    left = set()
    right = defaultdict(int)
    for t in topping:
        right[t] += 1
    for i in range(len(topping) - 1):
        left.add(topping[i])
        right[topping[i]] -= 1
        if right[topping[i]] == 0:
            del right[topping[i]]
        if len(left) == len(right):
            ans += 1
    return ans