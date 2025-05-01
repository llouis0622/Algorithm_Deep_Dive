import sys
sys.setrecursionlimit(10 ** 6)

S = sys.stdin.readline().rstrip()
n = len(S)
check = [False] * n


def solve(l, r):
    if l > r:
        return
    temp = '{'
    idx = l
    for i in range(l, r + 1):
        if not check[i] and S[i] < temp:
            temp = S[i]
            idx = i
    check[idx] = True
    print(''.join(S[i] for i in range(n) if check[i]))
    solve(idx + 1, r)
    solve(l, idx - 1)


solve(0, n - 1)