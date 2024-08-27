def solution(x):
    num = sum(int(i) for i in str(x))
    return x % num == 0