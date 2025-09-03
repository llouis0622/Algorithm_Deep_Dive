import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
left = [1] * n
for i in range(n):
    temp = a[i]
    m = 1
    for j in range(i):
        if a[j] < temp and left[j] + 1 > m:
            m = left[j] + 1
    left[i] = m
right = [1] * n
for i in range(n - 1, -1, -1):
    temp = a[i]
    m = 1
    for j in range(i + 1, n):
        if temp > a[j] and right[j] + 1 > m:
            m = right[j] + 1
    right[i] = m
ans = 0
for i in range(n):
    num = left[i] + right[i] - 1
    if num > ans:
        ans = num
print(ans)