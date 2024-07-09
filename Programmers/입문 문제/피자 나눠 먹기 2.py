import math


def solution(n):
    ans = n * 6 // math.gcd(n, 6)
    return ans // 6