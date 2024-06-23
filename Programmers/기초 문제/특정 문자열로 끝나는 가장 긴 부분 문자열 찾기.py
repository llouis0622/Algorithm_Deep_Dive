def solution(myString, pat):
    ans = len(pat)
    for i in range(len(myString) - ans, -1, -1):
        if myString[i:i + ans] == pat:
            return myString[:i + ans]
    return ""