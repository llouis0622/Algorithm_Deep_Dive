def solution(myString, pat):
    cnt = 0
    res = len(pat)
    for i in range(len(myString) - res + 1):
        if myString[i:i + res] == pat:
            cnt += 1
    return cnt