import sys

sys.setrecursionlimit(10 ** 6)

n, p, q = map(int, input().split())
memo = {}


def solve(x):
    if x == 0:
        return 1
    if x in memo:
        return memo[x]
    memo[x] = solve(x // p) + solve(x // q)
    return memo[x]


print(solve(n))