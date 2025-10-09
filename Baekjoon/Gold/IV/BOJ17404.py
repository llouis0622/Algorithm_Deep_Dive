import sys

N = int(sys.stdin.readline())
temp = [None] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
INF = 10 ** 9
ans = INF
for s in range(3):
    dp = [[INF] * 3 for _ in range(N + 1)]
    dp[1][s] = temp[1][s]
    for i in range(2, N + 1):
        for c in range(3):
            dp[i][c] = temp[i][c] + min(dp[i - 1][(c + 1) % 3], dp[i - 1][(c + 2) % 3])
    for c in range(3):
        if c != s:
            ans = min(ans, dp[N][c])
print(ans)