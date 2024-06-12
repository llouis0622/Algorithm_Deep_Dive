def solution(my_string):
    ans = [0] * 52
    for i in my_string:
        if 'A' <= i <= 'Z':
            ans[ord(i) - ord('A')] += 1
        elif 'a' <= i <= 'z':
            ans[ord(i) - ord('a') + 26] += 1
    return ans