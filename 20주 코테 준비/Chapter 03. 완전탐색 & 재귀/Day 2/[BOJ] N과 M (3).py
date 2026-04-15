import sys
from itertools import product

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [i + 1 for i in range(N)]
for i in product(arr, repeat=M):
    print(*i)


# import sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# res = []
#
#
# def dfs():
#     if len(res) == M:
#         print(*res)
#         return
#     for i in range(1, N + 1):
#         res.append(i)
#         dfs()
#         res.pop()
#
#
# dfs()