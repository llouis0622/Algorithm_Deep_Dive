def solution(n, m, x, y, r, c, k):
    x -= 1
    y -= 1
    r -= 1
    c -= 1
    dist = abs(x - r) + abs(y - c)
    if dist > k or (k - dist) % 2 != 0:
        return 'impossible'
    ans = []
    directions = [
        (1, 0, 'd'),
        (0, -1, 'l'),
        (0, 1, 'r'),
        (-1, 0, 'u'),
    ]
    for i in range(k):
        for dx, dy, j in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                temp = k - (i + 1)
                dist = abs(nx - r) + abs(ny - c)
                if dist <= temp:
                    ans.append(j)
                    x, y = nx, ny
                    break
    return ''.join(ans)
