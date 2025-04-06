T, W = map(int, input().split())
num = [int(input()) for _ in range(T)]
DP = [[0] * (W + 1) for _ in range(T + 1)]
for t in range(1, T + 1):
    for w in range(W + 1):
        tree = 1 if w % 2 == 0 else 2
        temp = 1 if num[t - 1] == tree else 0
        DP[t][w] = DP[t - 1][w] + temp
        if w > 0:
            DP[t][w] = max(DP[t][w], DP[t - 1][w - 1] + temp)
print(max(DP[T]))