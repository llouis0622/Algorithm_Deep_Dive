def solution(a, b):
    start, end = min(a, b), max(a, b)
    return sum(range(start, end + 1))