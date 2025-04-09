N = int(input())
lst = list(map(int, input().split()))
DP = [1] * N
chk = [-1] * N
for i in range(N):
    for j in range(i):
        if lst[j] < lst[i] and DP[j] + 1 > DP[i]:
            DP[i] = DP[j] + 1
            chk[i] = j
idx = DP.index(max(DP))
temp = []
while idx != -1:
    temp.append(lst[idx])
    idx = chk[idx]
temp.reverse()
print(max(DP))
print(*temp)