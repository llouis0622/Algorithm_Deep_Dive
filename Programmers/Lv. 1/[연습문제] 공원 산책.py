def solution(park, routes):
    H, W = len(park), len(park[0])
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                x, y = i, j
                break
    direction = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    for i in routes:
        op, n = i.split()
        n = int(n)
        dx, dy = direction[op]
        nx, ny = x, y
        move = True
        for _ in range(n):
            nx += dx
            ny += dy
            if not (0 <= nx < H and 0 <= ny < W):
                move = False
                break
            if park[nx][ny] == 'X':
                move = False
                break
        if move:
            x, y = nx, ny
    return [x, y]