from collections import deque


def BFS(s, t):
    queue = deque([(s, "")])
    visited = [False] * 10000
    visited[s] = True
    while queue:
        cur, num = queue.popleft()
        if cur == t:
            return num
        next = (cur * 2) % 10000
        if not visited[next]:
            visited[next] = True
            queue.append((next, num + "D"))
        next = (cur - 1) % 10000 if cur != 0 else 9999
        if not visited[next]:
            visited[next] = True
            queue.append((next, num + "S"))
        next = (cur % 1000) * 10 + cur // 1000
        if not visited[next]:
            visited[next] = True
            queue.append((next, num + "L"))
        next = (cur % 10) * 1000 + cur // 10
        if not visited[next]:
            visited[next] = True
            queue.append((next, num + "R"))


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(BFS(A, B))