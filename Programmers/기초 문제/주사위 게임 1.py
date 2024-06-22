def solution(a, b):
    if a % 2 != 0 and b % 2 != 0:
        return a ** 2 + b ** 2
    elif a % 2 != 0 or b % 2 != 0:
        return 2 * (a + b)
    else:
        return abs(a - b)