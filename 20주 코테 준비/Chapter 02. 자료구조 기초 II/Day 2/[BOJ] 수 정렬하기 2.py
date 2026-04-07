import sys

input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
print(*sorted(arr), sep='\n')
