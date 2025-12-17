import sys


def ccw(x1, y1, x2, y2, x3, y3):
    v = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if v > 0:
        return 1
    if v < 0:
        return -1
    return 0


def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    c1 = ccw(x1, y1, x2, y2, x3, y3)
    c2 = ccw(x1, y1, x2, y2, x4, y4)
    c3 = ccw(x3, y3, x4, y4, x1, y1)
    c4 = ccw(x3, y3, x4, y4, x2, y2)
    if c1 * c2 == 0 and c3 * c4 == 0:
        if max(min(x1, x2), min(x3, x4)) <= min(max(x1, x2), max(x3, x4)) and max(min(y1, y2), min(y3, y4)) <= min(max(y1, y2), max(y3, y4)):
            return True
        return False
    return c1 * c2 <= 0 and c3 * c4 <= 0


def inside(px, py, xl, xr, yb, yt):
    return xl <= px <= xr and yb <= py <= yt


t = int(sys.stdin.readline())
temp = []
for _ in range(t):
    xs, ys, xe, ye, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    xl = min(x1, x2)
    xr = max(x1, x2)
    yb = min(y1, y2)
    yt = max(y1, y2)
    check = False
    if inside(xs, ys, xl, xr, yb, yt) or inside(xe, ye, xl, xr, yb, yt):
        check = True
    else:
        if intersect(xs, ys, xe, ye, xl, yb, xr, yb):
            check = True
        elif intersect(xs, ys, xe, ye, xr, yb, xr, yt):
            check = True
        elif intersect(xs, ys, xe, ye, xr, yt, xl, yt):
            check = True
        elif intersect(xs, ys, xe, ye, xl, yt, xl, yb):
            check = True
    temp.append('T' if check else 'F')
sys.stdout.write('\n'.join(temp))