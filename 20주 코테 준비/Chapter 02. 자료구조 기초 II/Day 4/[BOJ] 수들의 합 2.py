import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
cnt, ans = 0, 0
s, e = 0, 0
while True:
    if ans >= M:
        if ans == M:
            cnt += 1
        ans -= arr[s]
        s += 1
    elif e == N:
        break
    else:
        ans += arr[e]
        e += 1
print(cnt)
