import sys

input = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))
st, en, tot = 0, 0, 0
res = int(1e9)
while True:
    if tot >= s:
        res = min(res, en - st)
        tot -= a[st]
        st += 1
    elif en == n:
        break
    else:
        tot += a[en]
        en += 1
print(res if res != int(1e9) else 0)