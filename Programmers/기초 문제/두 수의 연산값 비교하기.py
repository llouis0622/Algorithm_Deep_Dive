def solution(a, b):
    x = str(a) + str(b)
    y = 2 * a * b
    return int(x) if int(x) > y else y