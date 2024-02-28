import sys

L = [int(sys.stdin.readline()) for _ in range(9)]
print(max(L))
print(L.index(max(L)) + 1)