import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    res = input().strip()
    N = int(len(res) ** 0.5)
    temp = [[''] * N for _ in range(N)]
    idx = 0
    for i in range(N):
        for j in range(N):
            temp[i][j] = res[idx]
            idx += 1
    ans = ''
    for j in range(N - 1, -1, -1):
        for i in range(N):
            ans += temp[i][j]
    print(ans)