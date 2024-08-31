def solution(n):
    num = sorted(str(n), reverse=True)
    return int(''.join(num))