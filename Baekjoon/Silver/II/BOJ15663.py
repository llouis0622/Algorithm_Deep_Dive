import sys
input = sys.stdin.readline


def DFS(depth):
    if depth == M:
        print(" ".join(map(str, lst)))
        return
    num = 0
    for i in range(N):
        if not visited[i] and arr[i] != num:
            visited[i] = True
            lst[depth] = arr[i]
            num = arr[i]
            DFS(depth + 1)
            visited[i] = False


N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
visited = [False] * N
lst = [0] * M
DFS(0)