from collections import deque

n, m = map(int, input().split())
move = {i: i for i in range(1, 101)}
for _ in range(n):
    x, y = map(int, input().split())
    move[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    move[u] = v


def bfs():
    queue = deque([(1, 0)])
    visited = [False] * 101
    visited[1] = True
    while queue:
        cur, num = queue.popleft()
        if cur == 100:
            return num
        for i in range(1, 7):
            next = cur + i
            if next <= 100 and not visited[next]:
                visited[next] = True
                queue.append((move[next], num + 1))


print(bfs())