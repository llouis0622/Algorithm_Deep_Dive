from collections import deque


def bfs(start, graph, visited):
    q = deque([start])
    visited[start] = True
    cnt = 1
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1
    return cnt


def solution(n, wires):
    ans = n
    for cut in wires:
        graph = [[] for _ in range(n + 1)]
        for i in wires:
            if i == cut:
                continue
            v1, v2 = i
            graph[v1].append(v2)
            graph[v2].append(v1)
        visited = [False] * (n + 1)
        temp = bfs(1, graph, visited)
        res = abs(temp - (n - temp))
        ans = min(ans, res)
    return ans