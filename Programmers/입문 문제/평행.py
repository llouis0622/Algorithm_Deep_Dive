def solution(dots):
    pairs = [
        (0, 1, 2, 3),
        (0, 2, 1, 3),
        (0, 3, 1, 2)
    ]

    for i in pairs:
        i1, i2, i3, i4 = i
        if (dots[i2][1] - dots[i1][1]) * (dots[i4][0] - dots[i3][0]) == (dots[i4][1] - dots[i3][1]) * (dots[i2][0] - dots[i1][0]):
            return 1
    return 0