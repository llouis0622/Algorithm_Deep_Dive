from collections import deque


def BFS(s, goal, maps):
    rows, cols = len(maps), len(maps[0])
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(s[0], s[1], 0)])
    visited = set()
    visited.add(s)
    while queue:
        r, c, dist = queue.popleft()
        if (r, c) == goal:
            return dist
        for dr, dc in direction:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and maps[nr][nc] != 'X':
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1


def solution(maps):
    s, l, e = None, None, None
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                s = (i, j)
            elif maps[i][j] == 'L':
                l = (i, j)
            elif maps[i][j] == 'E':
                e = (i, j)
    to_l = BFS(s, l, maps)
    if to_l == -1:
        return -1
    to_e = BFS(l, e, maps)
    if to_e == -1:
        return -1
    return to_l + to_e