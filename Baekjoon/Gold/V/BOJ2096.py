import sys

n = int(sys.stdin.readline().strip())
a, b, c = map(int, sys.stdin.readline().split())
mx = [a, b, c]
mn = [a, b, c]
for _ in range(n - 1):
    x, y, z = map(int, sys.stdin.readline().split())
    mxi = x + max(mx[0], mx[1])
    mxj = y + max(mx[0], mx[1], mx[2])
    mxk = z + max(mx[1], mx[2])
    mni = x + min(mn[0], mn[1])
    mnj = y + min(mn[0], mn[1], mn[2])
    mnk = z + min(mn[1], mn[2])
    mx[0], mx[1], mx[2] = mxi, mxj, mxk
    mn[0], mn[1], mn[2] = mni, mnj, mnk
print(max(mx), min(mn))