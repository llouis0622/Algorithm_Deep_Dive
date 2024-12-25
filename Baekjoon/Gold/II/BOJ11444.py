def m_mul(A, B, mod):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]]


def m_pow(matrix, power, mod):
    res = [[1, 0], [0, 1]]
    base = matrix
    while power:
        if power % 2:
            res = m_mul(res, base, mod)
        base = m_mul(base, base, mod)
        power //= 2
    return res


def DP(n, mod=1000000007):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    matrix = [[1, 1], [1, 0]]
    num = m_pow(matrix, n - 1, mod)
    return num[0][0]


N = int(input().strip())
print(DP(N))