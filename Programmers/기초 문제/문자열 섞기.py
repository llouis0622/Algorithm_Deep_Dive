def solution(str1, str2):
    ans = ''
    for i in range(len(str1)):
        ans = ans + str1[i] + str2[i]
    return ans