D = [0] * 51
lst = [0] * 51
M = int(input())
D = list(map(int, input().split()))
T = 0
for i in range(0, M):
    T += D[i]
K = int(input())
ans = 0
for i in range(0, M):
    if D[i] >= K:
        lst[i] = 1
        for k in range(0, K):
            lst[i] = lst[i] * (D[i] - k) / (T - k)
        ans += lst[i]
print(ans)