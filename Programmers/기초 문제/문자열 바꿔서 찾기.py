def solution(myString, pat):
    res = ""
    for i in myString:
        if i == "A":
            res += "B"
        else:
            res += "A"
    if pat in res:
        return 1
    else:
        return 0