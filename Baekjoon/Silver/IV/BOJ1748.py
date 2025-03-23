import sys

N = int(sys.stdin.readline().strip())
l, d, cnt = 0, 1, 9
while N > cnt:
    l += d * cnt
    N -= cnt
    d += 1
    cnt *= 10
l += N * d
print(l)