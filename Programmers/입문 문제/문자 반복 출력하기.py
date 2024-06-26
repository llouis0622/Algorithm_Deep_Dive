def solution(my_string, n):
    ans = ''
    for i in my_string:
        ans += i * n
    return ans