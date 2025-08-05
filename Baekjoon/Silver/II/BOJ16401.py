import sys

M, N = map(int, sys.stdin.readline().split())
snacks = list(map(int, sys.stdin.readline().split()))
l, r = 1, max(snacks)
ans = 0
while l <= r:
    mid = (l + r) // 2
    cnt = sum(s // mid for s in snacks)
    if cnt >= M:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)