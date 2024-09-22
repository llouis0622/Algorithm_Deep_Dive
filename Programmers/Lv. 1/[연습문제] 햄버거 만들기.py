def solution(ingredient):
    lst = []
    cnt = 0
    arr = [1, 2, 3, 1]

    for i in ingredient:
        lst.append(i)
        if lst[-4:] == arr:
            cnt += 1
            del lst[-4:]
    return cnt