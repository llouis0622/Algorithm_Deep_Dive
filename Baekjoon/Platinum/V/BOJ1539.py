import sys

input = sys.stdin.readline

N = int(input().strip())
arr = [0] * (N + 1)
depth = [0] * N


def add(i, v):
    while i <= N:
        arr[i] += v
        i += i & -i


def sum(i):
    s = 0
    while i > 0:
        s += arr[i]
        i -= i & -i
    return s


def find(k):
    i = 0
    b = 1
    while b <= N:
        b *= 2
    b //= 2
    while b >= 1:
        t = i + b
        if t <= N and arr[t] < k:
            k -= arr[t]
            i = t
        b //= 2
    return i + 1


ans = 0
tot = 0
for _ in range(N):
    x = int(input())
    idx = x + 1
    temp = sum(idx)
    num1 = 0
    if temp > 0:
        pidx = find(temp)
        num1 = depth[pidx - 1]
    num2 = 0
    if tot - temp > 0:
        sidx = find(temp + 1)
        num2 = depth[sidx - 1]
    d = 1 + (num1 if num1 >= num2 else num2)
    depth[x] = d
    ans += d
    add(idx, 1)
    tot += 1
print(ans)