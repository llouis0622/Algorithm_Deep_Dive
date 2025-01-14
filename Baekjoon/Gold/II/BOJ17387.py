def CCW(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


def between(a, b, c):
    return min(a, b) <= c <= max(a, b)


def overlap(x1, y1, x2, y2, x3, y3, x4, y4):
    return (between(x1, x2, x3) and between(y1, y2, y3)) or \
        (between(x1, x2, x4) and between(y1, y2, y4)) or \
        (between(x3, x4, x1) and between(y3, y4, y1)) or \
        (between(x3, x4, x2) and between(y3, y4, y2))


def intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    CCW1 = CCW(x1, y1, x2, y2, x3, y3)
    CCW2 = CCW(x1, y1, x2, y2, x4, y4)
    CCW3 = CCW(x3, y3, x4, y4, x1, y1)
    CCW4 = CCW(x3, y3, x4, y4, x2, y2)
    if CCW1 * CCW2 <= 0 and CCW3 * CCW4 <= 0:
        if CCW1 == 0 and CCW2 == 0 and CCW3 == 0 and CCW4 == 0:
            return 1 if overlap(x1, y1, x2, y2, x3, y3, x4, y4) else 0
        return 1
    return 0


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
print(intersection(x1, y1, x2, y2, x3, y3, x4, y4))