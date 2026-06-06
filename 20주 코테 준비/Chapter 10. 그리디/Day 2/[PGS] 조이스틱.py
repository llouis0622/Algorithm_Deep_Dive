def solution(name):
    ans = 0
    res = len(name) - 1
    for i, char in enumerate(name):
        ans += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        temp = i + 1
        while temp < len(name) and name[temp] == 'A':
            temp += 1
        res = min(res, i * 2 + len(name) - temp, (len(name) - temp) * 2 + i)
    return ans + res
