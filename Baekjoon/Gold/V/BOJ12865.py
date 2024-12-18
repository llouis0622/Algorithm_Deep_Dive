N, K = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(N)]
DP = [0] * (K + 1)
for w, v in lst:
    for c in range(K, w - 1, -1):
        DP[c] = max(DP[c], DP[c - w] + v)
print(DP[K])