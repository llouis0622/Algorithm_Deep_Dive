import math


def solve(a, b, c):
    return 0.5 * abs(a[0] * b[1] + b[0] * c[1] + c[0] * a[1]- b[0] * a[1] - c[0] * b[1] - a[0] * c[1])


x1, y1, x2, y2, x3, y3 = map(float, input().split())
a = (x1, y1)
b = (x2, y2)
c = (x3, y3)
area = solve(a, b, c)
gx = (x1 + x2 + x3) / 3
gy = (y1 + y2 + y3) / 3
vx = area * 2 * math.pi * gy
vy = area * 2 * math.pi * gx
print(f"{vx:.9f} {vy:.9f}")