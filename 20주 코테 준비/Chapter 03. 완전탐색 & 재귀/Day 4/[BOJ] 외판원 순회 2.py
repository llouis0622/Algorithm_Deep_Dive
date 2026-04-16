import sys

input = sys.stdin.readline
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
ans = float('inf')


def dfs(start, now, cnt, cost):
    global ans
    if cost >= ans:
        return
    if cnt == N:
        if W[now][start] != 0:
            ans = min(ans, cost + W[now][start])
        return
    for i in range(N):
        if not visited[i] and W[now][i] != 0:
            visited[i] = True
            dfs(start, i, cnt + 1, cost + W[now][i])
            visited[i] = False


visited[0] = True
dfs(0, 0, 1, 0)
print(ans)
