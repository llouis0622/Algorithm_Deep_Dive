import sys

N, M, K = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
res = 0
for i in range(N):
    check = [0] * M
    for b in range(i, N):
        for j in range(M):
            check[j] += A[b][j]
        freq = {0: 1}
        temp = 0
        for v in check:
            temp = (temp + v) % K
            res += freq.get(temp, 0)
            freq[temp] = freq.get(temp, 0) + 1
print(res)