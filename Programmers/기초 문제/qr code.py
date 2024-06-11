def solution(q, r, code):
    ans = ""
    for i in range(len(code)):
        if i % q == r:
            ans += code[i]
    return ans