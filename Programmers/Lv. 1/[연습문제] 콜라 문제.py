def solution(a, b, n):
    res = 0
    while n >= a:
        num = (n // a) * b
        n = (n % a) + num
        res += num
    return res