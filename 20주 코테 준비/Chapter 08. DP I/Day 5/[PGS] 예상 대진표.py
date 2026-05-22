def solution(n, a, b):
    ans = 0
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        ans += 1
    return ans
