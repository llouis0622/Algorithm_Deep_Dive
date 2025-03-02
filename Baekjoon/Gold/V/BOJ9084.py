import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    coin = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline().strip())
    DP = [0] * (M + 1)
    DP[0] = 1
    for c in coin:
        for j in range(c, M + 1):
            DP[j] += DP[j - c]
    print(DP[M])