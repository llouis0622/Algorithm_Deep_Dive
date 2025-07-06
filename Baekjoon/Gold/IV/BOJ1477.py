n, m, l = map(int, input().split())
if n:
    rest = list(map(int, input().split()))
else:
    rest = []
rest.append(0)
rest.append(l)
rest.sort()


def check(num):
    cnt = 0
    for i in range(1, len(rest)):
        dist = rest[i] - rest[i - 1]
        if dist > num:
            cnt += (dist - 1) // num
    return cnt <= m


left, right = 1, l
ans = 0
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)