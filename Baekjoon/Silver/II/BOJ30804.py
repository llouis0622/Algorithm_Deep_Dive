import sys

input = sys.stdin.read

data = input().split()
N = int(data[0])
v = list(map(int, data[1:]))

result = 0
c = [0] * 10
l = 0
r = 0

while r < N:
    c[v[r]] += 1
    r += 1
    while 10 - c.count(0) > 2:
        c[v[l]] -= 1
        l += 1
    result = max(result, r - l)

print(result)