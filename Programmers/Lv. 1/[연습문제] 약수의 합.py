def solution(n):
    if n == 0:
        return 0
    return sum(i for i in range(1, n + 1) if n % i == 0)