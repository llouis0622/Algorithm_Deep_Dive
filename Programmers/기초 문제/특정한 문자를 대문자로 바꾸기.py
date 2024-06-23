def solution(my_string, alp):
    ans = ""
    for i in my_string:
        if i == alp:
            ans += i.upper()
        else:
            ans += i
    return ans