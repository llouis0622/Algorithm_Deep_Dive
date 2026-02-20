from collections import deque

T = int(input().strip())
for i in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    q = deque([S])
    visited[S] = 1
    ans = 0
    while q:
        v = q.popleft()
        if v == G:
            ans = 1
            break
        for j in adj[v]:
            if not visited[j]:
                visited[j] = 1
                q.append(j)
    print(f"#{i} {ans}")