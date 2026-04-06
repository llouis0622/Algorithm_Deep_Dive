import sys

input = sys.stdin.readline
N = int(input())
arr = [input().split() for _ in range(N)]
arr = [(int(i), j) for i, j in arr]
arr.sort(key=lambda x: x[0])
for i, j in arr:
    print(i, j)
