def solution(my_strings, parts):
    ans = []
    for i in range(len(my_strings)):
        s, e = parts[i]
        str = my_strings[i][s:e+1]
        ans.append(str)
    return ''.join(ans)