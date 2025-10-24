import sys

n, m = map(int, sys.stdin.buffer.readline().split())
p = list(range(n))
temp = [1] * n


def find(x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x


def union(a, b):
    x, y = find(a), find(b)
    if x == y:
        return False
    if temp[x] < temp[y]:
        x, y = y, x
    p[y] = x
    temp[x] += temp[y]
    return True


for i in range(1, m + 1):
    a, b = map(int, sys.stdin.buffer.readline().split())
    if not union(a, b):
        print(i)
        break
else:
    print(0)