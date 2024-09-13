def solution(n):
    num = ''
    while n > 0:
        num += str(n % 3)
        n //= 3
    return int(num, 3)