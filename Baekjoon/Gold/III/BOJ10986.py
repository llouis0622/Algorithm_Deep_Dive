import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
arr = [0] * n
idx = [0] * m
arr[0] = lst[0]
ans = 0

for i in range(1, n):
    arr[i] = arr[i - 1] + lst[i]

for i in range(n):
    num = int(arr[i] % m)

    if num == 0:
        ans += 1

    idx[num] += 1

for i in range(m):
    if idx[i] > 1:
        ans += (idx[i] * (idx[i] - 1) / 2)

print(int(ans))