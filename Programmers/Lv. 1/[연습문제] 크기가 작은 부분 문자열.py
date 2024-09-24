def solution(t, p):
    num = len(p)
    cnt = 0
    temp = int(p)
    for i in range(len(t) - num + 1):
        arr = t[i:i + num]
        if int(arr) <= temp:
            cnt += 1
    return cnt