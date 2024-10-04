def solution(n, m, section):
    cnt = 0
    num = 0
    for i in section:
        if i > num:
            cnt += 1
            num = i + m - 1
    return cnt