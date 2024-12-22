import sys
input = sys.stdin.readline

N = int(input().strip())
lst = [[' '] * (2 * N) for _ in range(N)]


def DP(n, x, y):
    if n == 3:
        lst[x][y] = '*'
        lst[x + 1][y - 1] = '*'
        lst[x + 1][y + 1] = '*'
        lst[x + 2][y - 2] = '*'
        lst[x + 2][y - 1] = '*'
        lst[x + 2][y] = '*'
        lst[x + 2][y + 1] = '*'
        lst[x + 2][y + 2] = '*'
        return
    half = n // 2
    DP(half, x, y)
    DP(half, x + half, y - half)
    DP(half, x + half, y + half)


DP(N, 0, N - 1)
for i in lst:
    print("".join(i))