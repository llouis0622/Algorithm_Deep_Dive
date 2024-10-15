import sys

input = sys.stdin.readline
N = int(input())
M = int(input())

lst = list(map(int, input().split()))
lst.sort()

cnt = int(0)
i = int(0)
j = int(N - 1)

while i < j:
    if lst[i] + lst[j] < M:
        i += 1
    elif lst[i] + lst[j] > M:
        j -= 1
    else:
        cnt += 1
        i += 1
        j -= 1

print(cnt)