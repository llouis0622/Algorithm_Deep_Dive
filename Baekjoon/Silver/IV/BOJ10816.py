import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
targets = list(map(int, input().split()))
for t in targets:
    lower = bisect_left(a, t)
    upper = bisect_right(a, t)
    print(upper - lower)