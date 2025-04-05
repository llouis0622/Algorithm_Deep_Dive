import sys

input = sys.stdin.readline


def bellman_ford(N, edge):
    dist = [0] * (N + 1)
    for i in range(N):
        for u, v, cost in edge:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                if i == N - 1:
                    return True
    return False


TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    edge = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        edge.append((S, E, T))
        edge.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edge.append((S, E, -T))
    if bellman_ford(N, edge):
        print("YES")
    else:
        print("NO")