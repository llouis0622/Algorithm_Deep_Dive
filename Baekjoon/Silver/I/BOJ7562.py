from collections import deque


def knight(l, start, end):
    directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    visited = [[False] * l for _ in range(l)]
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True
    while queue:
        x, y, moves = queue.popleft()
        if (x, y) == end:
            return moves
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))
    return -1


t = int(input())
res = []
for _ in range(t):
    l = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    res.append(knight(l, start, end))
for res in res:
    print(res)