import sys
from itertools import permutations

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [i + 1 for i in range(N)]
for i in permutations(arr, M):
    print(*i)


# import sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# visited = [False] * (N + 1)
# res = []
#
#
# def dfs():
#     if len(res) == M:
#         print(*res)
#         return
#     for i in range(1, N + 1):
#         if not visited[i]:
#             visited[i] = True
#             res.append(i)
#             dfs()
#             res.pop()
#             visited[i] = False
#
#
# dfs()