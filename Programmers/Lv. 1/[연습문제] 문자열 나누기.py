def solution(s):
    cnt = 0
    i = 0
    while i < len(s):
        x = s[i]
        num = 0
        temp = 0
        while i < len(s):
            if s[i] == x:
                num += 1
            else:
                temp += 1
            i += 1
            if num == temp:
                break
        cnt += 1
    return cnt