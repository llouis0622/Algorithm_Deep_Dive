def solution(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]