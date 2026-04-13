import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            tot = arr[i] + arr[j] + arr[k]
            if tot <= M:
                ans = max(ans, tot)
print(ans)
