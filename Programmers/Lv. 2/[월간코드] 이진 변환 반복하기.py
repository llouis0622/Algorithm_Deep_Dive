def solution(s):
    cnt = 0
    num = 0
    while s != "1":
        temp = s.count("0")
        num += temp
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        cnt += 1
    return [cnt, num]