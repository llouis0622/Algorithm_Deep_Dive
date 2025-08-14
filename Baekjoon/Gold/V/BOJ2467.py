import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))
l, r = 0, n - 1
MAX = 2_000_000_001
ans = (a[l], a[r])
while l < r:
    s = a[l] + a[r]
    if abs(s) < MAX:
        MAX = abs(s)
        ans = (a[l], a[r])
        if MAX == 0:
            break
    if s < 0:
        l += 1
    else:
        r -= 1
print(ans[0], ans[1])