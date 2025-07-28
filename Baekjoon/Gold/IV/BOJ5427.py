import sys
from collections import deque

input = sys.stdin.read().split()

t = int(input[0])
idx = 1
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
out = []
for _ in range(t):
    w = int(input[idx])
    h = int(input[idx + 1])
    idx += 2
    board = input[idx:idx + h]
    idx += h
    fire_q = deque()
    person_q = deque()
    fire = [[-1] * w for _ in range(h)]
    person = [[-1] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if board[y][x] == '*':
                fire_q.append((y, x))
                fire[y][x] = 0
            elif board[y][x] == '@':
                person_q.append((y, x))
                person[y][x] = 0
    while fire_q:
        y, x = fire_q.popleft()
        t_f = fire[y][x] + 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < h and 0 <= nx < w:
                if board[ny][nx] != '#' and fire[ny][nx] == -1:
                    fire[ny][nx] = t_f
                    fire_q.append((ny, nx))
    escaped = False
    while person_q and not escaped:
        y, x = person_q.popleft()
        t_p = person[y][x] + 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                out.append(str(person[y][x] + 1))
                escaped = True
                break
            if board[ny][nx] == '.' and person[ny][nx] == -1:
                if fire[ny][nx] == -1 or t_p < fire[ny][nx]:
                    person[ny][nx] = t_p
                    person_q.append((ny, nx))
    if not escaped:
        out.append("IMPOSSIBLE")
sys.stdout.write("\n".join(out))