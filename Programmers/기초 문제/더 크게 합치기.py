def solution(a, b):
    x = str(a) + str(b)
    y = str(b) + str(a)
    return int(x) if int(x) > int(y) else int(y)