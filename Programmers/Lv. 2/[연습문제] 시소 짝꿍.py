from collections import Counter
from fractions import Fraction


def solution(weights):
    ans = 0
    c = Counter(weights)
    for w in c:
        if c[w] >= 2:
            ans += c[w] * (c[w] - 1) // 2
    temp = [(2, 3), (2, 4), (3, 4)]
    for w in c:
        for a, b in temp:
            num = Fraction(w * a, b)
            if num in c:
                if num != w:
                    ans += c[w] * c[num]
    return ans