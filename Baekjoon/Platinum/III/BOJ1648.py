N, M = map(int, input().split())
MOD = 9901
DP = [[0] * (1 << N) for _ in range(M + 1)]
DP[0][0] = 1
for col in range(M):
    for i in range(1 << N):
        if DP[col][i] == 0:
            continue
        stk = [(0, i, 0)]
        while stk:
            row, curr, next = stk.pop()
            if row == N:
                DP[col + 1][next] = (DP[col + 1][next] + DP[col][curr]) % MOD
                continue
            if (curr & (1 << row)) == 0:
                stk.append((row + 1, curr, next | (1 << row)))
                if row + 1 < N and (curr & (1 << (row + 1))) == 0:
                    stk.append((row + 2, curr, next))
            else:
                stk.append((row + 1, curr, next))
print(DP[M][0])