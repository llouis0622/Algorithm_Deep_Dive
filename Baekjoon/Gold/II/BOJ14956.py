def hilbert(N, d):
    x = y = 0
    s = 1
    t = d - 1
    while s < N:
        dx = 1 & (t // 2)
        dy = 1 & (t ^ dx)
        if dy == 0:
            if dx == 1:
                x, y = s - 1 - x, s - 1 - y
            x, y = y, x
        x += s * dx
        y += s * dy
        t //= 4
        s *= 2
    return x + 1, y + 1


N, M = map(int, input().split())
x, y = hilbert(N, M)
print(x, y)