def solution(left, right):
    ans = 0
    for i in range(left, right + 1):
        cnt = sum(1 for j in range(1, i + 1) if i % j == 0)
        if cnt % 2 == 0:
            ans += i
        else:
            ans -= i
    return ans