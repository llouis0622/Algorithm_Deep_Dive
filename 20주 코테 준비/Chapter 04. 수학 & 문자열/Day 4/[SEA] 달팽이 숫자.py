T = int(input())
for i in range(1, T + 1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y, d = 0, 0, 0
    for j in range(1, N * N + 1):
        board[x][y] = j
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] != 0:
            d = (d + 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
        x, y = nx, ny
    print(f'#{i}')
    for num in board:
        print(*num)
