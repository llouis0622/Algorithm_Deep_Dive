import sys, math

MOD = 1_000_000_007


def fibo(n):
    if n == 0:
        return 0, 1
    a, b = fibo(n >> 1)
    c = (a * ((2 * b - a) % MOD)) % MOD
    d = (a * a + b * b) % MOD
    if n & 1:
        return d, (c + d) % MOD
    else:
        return c, d


n, m = map(int, sys.stdin.readline().split())
x = math.gcd(n, m)
print(fibo(x)[0] % MOD)