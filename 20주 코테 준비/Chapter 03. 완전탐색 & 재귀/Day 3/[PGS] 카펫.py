def solution(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            num = yellow // i
            if 2 * num + 2 * i + 4 == brown:
                return [num + 2, i + 2]
