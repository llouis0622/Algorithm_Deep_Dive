def solution(n):
    i = 1
    fac = 1
    while fac <= n:
        i += 1
        fac *= i
    return i - 1