def solution(s):
    cnt, num = 0, 0
    while s != '1':
        num += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        cnt += 1
    return [cnt, num]
