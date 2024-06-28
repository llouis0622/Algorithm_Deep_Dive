def solution(hp):
    one = hp // 5
    hp %= 5
    two = hp // 3
    hp %= 3
    three = hp // 1
    return one + two + three