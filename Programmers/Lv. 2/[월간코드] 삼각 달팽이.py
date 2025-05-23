def solution(n):
    tri = [[0] * (i + 1) for i in range(n)]
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    x = y = 0
    direction = 0
    num = 1
    for i in range(n * (n + 1) // 2):
        tri[x][y] = num
        num += 1
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx >= n or ny > nx or tri[nx][ny] != 0:
            direction = (direction + 1) % 3
            nx = x + dx[direction]
            ny = y + dy[direction]
        x, y = nx, ny
    ans = []
    for row in tri:
        ans.extend(row)
    return ans