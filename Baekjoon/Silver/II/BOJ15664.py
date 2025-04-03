def DFS(depth, start):
    if depth == M:
        print(*path)
        return
    prev = 0
    for i in range(start, N):
        if not check[i] and arr[i] != prev:
            check[i] = True
            path.append(arr[i])
            prev = arr[i]
            DFS(depth + 1, i + 1)
            check[i] = False
            path.pop()


N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
check = [False] * N
path = []
DFS(0, 0)