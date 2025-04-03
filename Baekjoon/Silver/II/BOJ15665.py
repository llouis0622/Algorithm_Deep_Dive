N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
path = []
res = set()


def DFS(depth):
    if depth == M:
        res.add(tuple(path))
        return
    for i in range(N):
        path.append(arr[i])
        DFS(depth + 1)
        path.pop()


DFS(0)
for i in sorted(res):
    print(*i)