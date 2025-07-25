from collections import deque


def solution(board):
    h, w = len(board), len(board[0])
    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'R':
                num = (i, j)
            if board[i][j] == 'G':
                res = (i, j)
    queue = deque()
    queue.append((*num, 0))
    visited[num[0]][num[1]] = True
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y, cnt = queue.popleft()
        if (x, y) == res:
            return cnt
        for dx, dy in dirs:
            nx, ny = x, y
            while 0 <= nx + dx < h and 0 <= ny + dy < w and board[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))
    return -1