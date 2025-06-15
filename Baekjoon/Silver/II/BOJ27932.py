n, k = map(int, input().split())
h = list(map(int, input().split()))
if n == 1:
    print(0)
    exit()


def check(H):
    temp = [False] * n
    for i in range(n - 1):
        if abs(h[i] - h[i + 1]) > H:
            temp[i] = True
            temp[i + 1] = True
    return sum(temp) <= k


l = 0
r = max(abs(h[i] - h[i + 1]) for i in range(n - 1))
ans = r
while l <= r:
    m = (l + r) // 2
    if check(m):
        ans = m
        r = m - 1
    else:
        l = m + 1
print(ans)