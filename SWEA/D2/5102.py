from collections import deque

T = int(input())
for i in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    S, G = map(int, input().split())
    dist = [0] * (V + 1)
    q = deque([S])
    dist[S] = 1
    while q:
        x = q.popleft()
        if x == G:
            break
        for j in adj[x]:
            if dist[j] == 0:
                dist[j] = dist[x] + 1
                q.append(j)
    ans = 0 if dist[G] == 0 else dist[G] - 1
    print(f"#{i} {ans}")