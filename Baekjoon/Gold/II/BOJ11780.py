import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
dist = [[INF] * n for _ in range(n)]
nxt = [[-1] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if dist[a][b] > c:
        dist[a][b] = c
        nxt[a][b] = b
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                nxt[i][j] = nxt[i][k]
for i in range(n):
    for j in range(n):
        print(0 if dist[i][j] == INF else dist[i][j], end=' ')
    print()


def get_path(u, v):
    if nxt[u][v] == -1:
        return []
    path = [u]
    while u != v:
        u = nxt[u][v]
        path.append(u)
    return path


for i in range(n):
    for j in range(n):
        if dist[i][j] == INF or i == j:
            print(0)
        else:
            path = get_path(i, j)
            print(len(path), ' '.join(str(x + 1) for x in path))