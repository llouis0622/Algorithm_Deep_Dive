import sys

N = int(sys.stdin.buffer.readline())
A = list(map(int, sys.stdin.buffer.readline().split()))
MAX = 1_000_000
temp = [-1] * (MAX + 1)
for i, v in enumerate(A):
    temp[v] = i
res = [0] * N
for i, v in enumerate(A):
    x = v + v
    while x <= MAX:
        j = temp[x]
        if j != -1:
            res[i] += 1
            res[j] -= 1
        x += v
print(' '.join(map(str, res)))