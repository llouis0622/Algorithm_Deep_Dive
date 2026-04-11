import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
X = int(input())
arr.sort()
cnt, tot = 0, 0
s, e = 0, N - 1
while s < e:
    tot = arr[s] + arr[e]
    if tot == X:
        cnt += 1
        s += 1
        e -= 1
    elif tot < X:
        s += 1
    else:
        e -= 1
print(cnt)
