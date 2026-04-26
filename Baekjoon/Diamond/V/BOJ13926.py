import sys
from math import gcd
import random

input = sys.stdin.readline


def miller_rabin(n, a):
    if n % a == 0:
        return n == a
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(r - 1):
        x = x * x % n
        if x == n - 1:
            return True
    return False


def is_prime(n):
    if n < 2:
        return False
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n == a:
            return True
        if not miller_rabin(n, a):
            return False
    return True


def factorize(n):
    if n == 1:
        return {}
    if is_prime(n):
        return {n: 1}
    for p in [2, 3, 5, 7, 11, 13]:
        if n % p == 0:
            res = factorize(n // p)
            res[p] = res.get(p, 0) + 1
            return res
    d = None
    while d is None:
        c = random.randint(1, n - 1)
        x = random.randint(2, n - 1)
        y = x
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = gcd(abs(x - y), n)
        if d == n:
            d = None
    res = factorize(d)
    for k, v in factorize(n // d).items():
        res[k] = res.get(k, 0) + v
    return res


def euler_phi(n):
    if n == 1:
        return 1
    result = n
    for p in factorize(n):
        result = result // p * (p - 1)
    return result


n = int(input())
print(euler_phi(n))
