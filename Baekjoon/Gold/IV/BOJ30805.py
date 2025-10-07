import sys, bisect

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
tempa = [[] for _ in range(101)]
tempb = [[] for _ in range(101)]
for i, x in enumerate(A):
    tempa[x].append(i)
for j, x in enumerate(B):
    tempb[x].append(j)
i = j = -1
ans = []
while True:
    check = False
    for k in range(100, 0, -1):
        u, v = tempa[k], tempb[k]
        numi = bisect.bisect_right(u, i)
        numj = bisect.bisect_right(v, j)
        if numi < len(u) and numj < len(v):
            i, j = u[numi], v[numj]
            ans.append(k)
            check = True
            break
    if not check:
        break
print(len(ans))
if ans:
    print(*ans)