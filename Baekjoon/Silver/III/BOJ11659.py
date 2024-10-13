import sys

input = sys.stdin.readline
cnt, num = map(int, input().split())
lst = list(map(int, input().split()))
idx = [0]
temp = 0

for i in lst:
    temp = temp + i
    idx.append(temp)

for i in range(num):
    a, b = map(int, input().split())
    print(idx[b] - idx[a - 1])