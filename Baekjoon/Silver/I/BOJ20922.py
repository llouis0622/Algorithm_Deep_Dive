from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = defaultdict(int)
l = 0
ans = 0
for r in range(n):
    cnt[arr[r]] += 1
    while cnt[arr[r]] > k:
        cnt[arr[l]] -= 1
        l += 1
    ans = max(ans, r - l + 1)
print(ans)