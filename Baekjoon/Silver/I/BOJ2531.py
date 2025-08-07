n, d, k, c = map(int, input().split())
temp = [int(input()) for _ in range(n)]
cnt = [0] * (d + 1)
num = 0
for i in range(k):
    if cnt[temp[i]] == 0:
        num += 1
    cnt[temp[i]] += 1
ans = num + (1 if cnt[c] == 0 else 0)
for i in range(1, n):
    l = temp[i - 1]
    cnt[l] -= 1
    if cnt[l] == 0:
        num -= 1
    r = temp[(i + k - 1) % n]
    if cnt[r] == 0:
        num += 1
    cnt[r] += 1
    ans = max(ans, num + (1 if cnt[c] == 0 else 0))
print(ans)