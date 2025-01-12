from collections import deque


def BFS(r, c, maze):
    fq = deque()
    jq = deque()
    ftime = [[-1] * c for _ in range(r)]
    jtime = [[-1] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 'F':
                fq.append((i, j))
                ftime[i][j] = 0
            elif maze[i][j] == 'J':
                jq.append((i, j))
                jtime[i][j] = 0
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while fq:
        x, y = fq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and ftime[nx][ny] == -1 and maze[nx][ny] == '.':
                ftime[nx][ny] = ftime[x][y] + 1
                fq.append((nx, ny))
    while jq:
        x, y = jq.popleft()
        if x == 0 or x == r - 1 or y == 0 or y == c - 1:
            return jtime[x][y] + 1
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and jtime[nx][ny] == -1 and maze[nx][ny] == '.':
                if ftime[nx][ny] == -1 or jtime[x][y] + 1 < ftime[nx][ny]:
                    jtime[nx][ny] = jtime[x][y] + 1
                    jq.append((nx, ny))
    return "IMPOSSIBLE"


r, c = map(int, input().split())
maze = [input().strip() for _ in range(r)]
print(BFS(r, c, maze))