import math

def solution(n, m):
    gcd = math.gcd(n, m)
    lcm = n * m // gcd
    return [gcd, lcm]