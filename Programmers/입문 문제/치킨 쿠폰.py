def solution(chicken):
    ans = 0
    num = chicken
    while num >= 10:
        arr = num // 10
        ans += arr
        num = num % 10 + arr
    return ans