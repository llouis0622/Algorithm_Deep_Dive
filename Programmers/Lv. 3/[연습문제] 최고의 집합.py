def solution(n, s):
    if s < n:
        return [-1]
    temp = s // n
    num = s % n
    ans = [temp] * n
    for i in range(num):
        ans[n - 1 - i] += 1
    return ans