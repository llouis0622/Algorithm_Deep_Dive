def solution(n):
    ans = ""
    for i in range(n):
        if i % 2 == 0:
            ans += "수"
        else:
            ans += "박"
    return ans