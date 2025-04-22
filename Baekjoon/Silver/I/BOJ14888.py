import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
lst = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_res = -int(1e9)
min_res = int(1e9)


def DFS(idx, res, add, sub, mul, div):
    global max_res, min_res
    if idx == N:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return
    if add:
        DFS(idx + 1, res + lst[idx], add - 1, sub, mul, div)
    if sub:
        DFS(idx + 1, res - lst[idx], add, sub - 1, mul, div)
    if mul:
        DFS(idx + 1, res * lst[idx], add, sub, mul - 1, div)
    if div:
        if res < 0:
            DFS(idx + 1, -(-res // lst[idx]), add, sub, mul, div - 1)
        else:
            DFS(idx + 1, res // lst[idx], add, sub, mul, div - 1)


DFS(1, lst[0], add, sub, mul, div)
print(max_res)
print(min_res)