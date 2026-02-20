from collections import deque

T = int(input().strip())
for i in range(1, T + 1):
    N = int(input().strip())
    G = [input().strip() for _ in range(N)]
    a = b = x = y = -1
    for j in range(N):
        row = G[j]
        for k in range(N):
            c = row[k]
            if c == '2':
                a, b = j, k
            elif c == '3':
                x, y = j, k
    if a == -1 or x == -1:
        print(f"#{i} error")
        continue
    q = deque([(a, b)])
    vis = [[0] * N for _ in range(N)]
    vis[a][b] = 1
    ans = 0
    while q:
        r, c = q.popleft()
        if r == x and c == y:
            ans = 1
            break
        nr = r + 1
        nc = c
        if 0 <= nr < N and not vis[nr][nc] and G[nr][nc] != '1':
            vis[nr][nc] = 1
            q.append((nr, nc))
        nr = r - 1
        nc = c
        if 0 <= nr < N and not vis[nr][nc] and G[nr][nc] != '1':
            vis[nr][nc] = 1
            q.append((nr, nc))
        nr = r
        nc = c + 1
        if 0 <= nc < N and not vis[nr][nc] and G[nr][nc] != '1':
            vis[nr][nc] = 1
            q.append((nr, nc))
        nr = r
        nc = c - 1
        if 0 <= nc < N and not vis[nr][nc] and G[nr][nc] != '1':
            vis[nr][nc] = 1
            q.append((nr, nc))
    print(f"#{i} {ans}")