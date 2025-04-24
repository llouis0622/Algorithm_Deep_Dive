N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
temp = sum(cost)
DP = [0] * (temp + 1)
for i in range(N):
    m = memory[i]
    c = cost[i]
    for j in range(temp, c - 1, -1):
        DP[j] = max(DP[j], DP[j - c] + m)
for i in range(temp + 1):
    if DP[i] >= M:
        print(i)
        break