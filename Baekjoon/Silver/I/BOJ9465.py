def sticker(lst):
    res = []
    for t in lst:
        n, temp = t
        if n == 1:
            res.append(max(temp[0][0], temp[1][0]))
            continue
        DP = [[0] * n for _ in range(3)]
        DP[0][0] = temp[0][0]
        DP[1][0] = temp[1][0]
        DP[2][0] = 0
        for i in range(1, n):
            DP[0][i] = max(DP[1][i - 1], DP[2][i - 1]) + temp[0][i]
            DP[1][i] = max(DP[0][i - 1], DP[2][i - 1]) + temp[1][i]
            DP[2][i] = max(DP[0][i - 1], DP[1][i - 1])
        res.append(max(DP[0][n - 1], DP[1][n - 1], DP[2][n - 1]))
    return res


T = int(input())
lst = []
for _ in range(T):
    n = int(input())
    temp = [list(map(int, input().split())) for _ in range(2)]
    lst.append((n, temp))
res = sticker(lst)
for i in res:
    print(i)