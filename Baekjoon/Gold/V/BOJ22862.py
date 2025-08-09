n, k = map(int, input().split())
arr = list(map(int, input().split()))
l = 0
cnt = 0
ans = 0
for r in range(n):
    if arr[r] % 2 == 1:
        cnt += 1
    while cnt > k:
        if arr[l] % 2 == 1:
            cnt -= 1
        l += 1
    ans = max(ans, (r - l + 1) - cnt)
print(ans)