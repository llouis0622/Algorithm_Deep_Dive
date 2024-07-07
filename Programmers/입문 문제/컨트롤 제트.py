def solution(s):
    ans = 0
    num = 0
    for i in s.split():
        if i == "Z":
            ans -= num
        else:
            ans += int(i)
            num = int(i)
    return ans