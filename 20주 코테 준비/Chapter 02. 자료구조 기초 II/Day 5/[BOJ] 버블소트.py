import sys

input = sys.stdin.readline
N = int(input())
arr = [(int(input()), i) for i in range(N)]
arr.sort()
ans = 0
for i in range(N):
    ans = max(ans, arr[i][1] - i)
print(ans + 1)
