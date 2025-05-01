import sys


def multi(A, B):
    n = len(A)
    lst = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                lst[i][j] += A[i][k] * B[k][j]
            lst[i][j] %= 1000
    return lst


def pow(A, temp):
    n = len(A)
    lst = [[int(i == j) for j in range(n)] for i in range(n)]
    while temp:
        if temp & 1:
            lst = multi(lst, A)
        A = multi(A, A)
        temp >>= 1
    return lst


N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = pow(A, B)
for row in ans:
    print(*row)