def solution(dots):
    x = [i[0] for i in dots]
    y = [i[1] for i in dots]
    return (max(x) - min(x)) * (max(y) - min(y))