import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
res, ans = float('inf'), 0
s, e = 0, 0
while True:
    if ans >= M:
        res = min(res, e - s)
        ans -= arr[s]
        s += 1
    elif e == N:
        break
    else:
        ans += arr[e]
        e += 1
print(0 if res == float('inf') else res)
