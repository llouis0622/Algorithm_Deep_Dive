import sys

input = sys.stdin.readline
N = int(input())
arr = [input().split() for _ in range(N)]
arr = [(int(i), int(j)) for i, j in arr]
arr.sort()
for i, j in arr:
    print(i, j)
