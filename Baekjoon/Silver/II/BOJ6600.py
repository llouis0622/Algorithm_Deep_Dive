import math
import sys

PI = 3.141592653589793


def distance(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)


def radius(x1, y1, x2, y2, x3, y3):
    a = distance(x2, y2, x3, y3)
    b = distance(x1, y1, x3, y3)
    c = distance(x1, y1, x2, y2)
    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    if area == 0:
        return 0
    return (a * b * c) / (4 * area)


for line in sys.stdin:
    if not line.strip():
        continue
    x1, y1, x2, y2, x3, y3 = map(float, line.strip().split())
    R = radius(x1, y1, x2, y2, x3, y3)
    ans = 2 * PI * R
    print(f"{ans:.2f}")