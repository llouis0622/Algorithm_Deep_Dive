import bisect

t = int(input())
res = []
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    cnt = 0
    for i in a:
        cnt += bisect.bisect_left(b, i)
    res.append(cnt)
for i in res:
    print(i)