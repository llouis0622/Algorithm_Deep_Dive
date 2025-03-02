import sys

case = 1
while True:
    N = int(sys.stdin.readline().strip())
    if N == 0:
        break
    num = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    DP = [[float('inf')] * 3 for _ in range(N)]
    DP[0][1] = num[0][1]
    DP[0][2] = DP[0][1] + num[0][2]
    for i in range(1, N):
        DP[i][0] = num[i][0] + min(DP[i - 1][0], DP[i - 1][1])
        DP[i][1] = num[i][1] + min(DP[i - 1][0], DP[i - 1][1], DP[i - 1][2], DP[i][0])
        DP[i][2] = num[i][2] + min(DP[i - 1][1], DP[i - 1][2], DP[i][1])
    print(f"{case}. {DP[N - 1][1]}")
    case += 1