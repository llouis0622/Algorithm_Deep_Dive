import sys

A, B = map(int, sys.stdin.readline().split())


def cnt(n):
    if n <= 0:
        return 0
    res = 0
    i = 0
    while (1 << i) <= n:
        temp = 1 << (i + 1)
        num = (n + 1) // temp
        res += num * (1 << i)
        idx = (n + 1) % temp
        if idx > (1 << i):
            res += idx - (1 << i)
        i += 1
    return res


print(cnt(B) - cnt(A - 1))