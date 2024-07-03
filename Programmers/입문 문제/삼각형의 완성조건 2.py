def solution(sides):
    x, y = sides
    return (x + y - 1) - (abs(x - y) + 1) + 1