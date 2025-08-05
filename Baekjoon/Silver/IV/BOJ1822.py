import sys

N, M = map(int, sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))
print(len(sorted(A - B)))
print(*sorted(A - B))