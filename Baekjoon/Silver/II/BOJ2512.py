n = int(input())
temp = list(map(int, input().split()))
m = int(input())
if sum(temp) <= m:
    print(max(temp))
else:
    l, r = 0, max(temp)
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        tot = sum(min(i, mid) for i in temp)
        if tot <= m:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    print(ans)