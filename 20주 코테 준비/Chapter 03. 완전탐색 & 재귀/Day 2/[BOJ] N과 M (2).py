import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [i + 1 for i in range(N)]
for i in combinations(arr, M):
    print(*i)


# import sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# res = []
#
#
# def dfs(x):
#     if len(res) == M:
#         print(*res)
#         return
#     for i in range(x, N + 1):
#         res.append(i)
#         dfs(i + 1)
#         res.pop()
#
#
# dfs(1)