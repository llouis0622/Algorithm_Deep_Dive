t = int(input())
for _ in range(t):
    c = input()
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = y = 0
    d = 0
    min_x = max_x = 0
    min_y = max_y = 0
    for i in c:
        if i == 'F':
            x += dx[d]
            y += dy[d]
        elif i == 'B':
            x -= dx[d]
            y -= dy[d]
        elif i == 'L':
            d = (d + 3) % 4
        elif i == 'R':
            d = (d + 1) % 4
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    w = max_x - min_x
    h = max_y - min_y
    print(w * h)