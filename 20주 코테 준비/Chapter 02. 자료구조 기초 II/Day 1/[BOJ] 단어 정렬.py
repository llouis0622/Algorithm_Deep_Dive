import sys

input = sys.stdin.readline
N = int(input())
arr = [input().strip() for _ in range(N)]
arr = list(set(arr))
arr.sort(key=lambda x: (len(x), x))
print(*arr, sep='\n')
