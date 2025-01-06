def solution(n):
    num = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            num += 1
    return num