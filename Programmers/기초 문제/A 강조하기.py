def solution(myString):
    ans = ""
    for i in myString:
        if i == 'a':
            ans += 'A'
        elif i.isupper() and i != 'A':
            ans += i.lower()
        else:
            ans += i
    return ans