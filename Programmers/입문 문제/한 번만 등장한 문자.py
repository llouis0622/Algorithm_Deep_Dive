def solution(s):
    ans = [i for i in s if s.count(i) == 1]
    return ''.join(sorted(ans))