from math import gcd

def solution(numer1, denom1, numer2, denom2):
    ans = denom1 * denom2
    num = numer1 * denom2 + numer2 * denom1
    res = gcd(num, ans)
    num //= res
    den = ans // res
    return [num, den]