def solution(food):
    arr = ''
    for i in range(1, len(food)):
        cnt = food[i] // 2
        arr += str(i) * cnt
    return arr + '0' + arr[::-1]