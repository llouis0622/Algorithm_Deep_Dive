def solution(order):
    return sum(1 for i in str(order) if i in '369')