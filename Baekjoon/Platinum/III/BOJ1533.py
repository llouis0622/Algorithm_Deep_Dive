import sys

MOD = 1000003
N, S, E, T = map(int, sys.stdin.readline().split())
S -= 1
E -= 1
size = N * 5
mat = [[0] * size for _ in range(size)]


def idx(node, step):
    return node * 5 + step


for i in range(N):
    row = sys.stdin.readline().strip()
    for step in range(1, 5):
        mat[idx(i, step)][idx(i, step - 1)] = 1
    for j, c in enumerate(row):
        w = int(c)
        if w:
            mat[idx(i, 0)][idx(j, w - 1)] += 1
            mat[idx(i, 0)][idx(j, w - 1)] %= MOD


def multiply(a, b):
    res = [[0] * size for _ in range(size)]
    for i in range(size):
        for k in range(size):
            if a[i][k]:
                for j in range(size):
                    res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD
    return res


def matrix_power(base, exp):
    res = [[0] * size for _ in range(size)]
    for i in range(size):
        res[i][i] = 1
    while exp:
        if exp % 2:
            res = multiply(res, base)
        base = multiply(base, base)
        exp //= 2
    return res


ans = matrix_power(mat, T)
print(ans[idx(S, 0)][idx(E, 0)] % MOD)
