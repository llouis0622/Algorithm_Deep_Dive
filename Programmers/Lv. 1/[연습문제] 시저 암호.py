def solution(s, n):
    ans = ""
    for i in s:
        if i.isupper():
            ans += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        elif i.islower():
            ans += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        else:
            ans += i
    return ans