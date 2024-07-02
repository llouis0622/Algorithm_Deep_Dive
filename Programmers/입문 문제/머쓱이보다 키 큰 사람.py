def solution(array, height):
    return sum(1 for i in array if i > height)