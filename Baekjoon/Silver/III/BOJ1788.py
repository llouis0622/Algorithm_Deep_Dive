n = int(input())
MOD = 1_000_000_000


def mat_mult(A, B):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]]


def mat_pow(M, exp):
    res = [[1, 0], [0, 1]]
    while exp:
        if exp % 2:
            res = mat_mult(res, M)
        M = mat_mult(M, M)
        exp //= 2
    return res


def fibonacci(n):
    if n == 0:
        return 0
    if n > 0:
        return mat_pow([[1, 1], [1, 0]], n - 1)[0][0]
    f = mat_pow([[1, 1], [1, 0]], -n - 1)[0][0]
    return f if n % 2 else -f


fib = fibonacci(n)
print(1 if fib > 0 else -1 if fib < 0 else 0)
print(abs(fib) % MOD)