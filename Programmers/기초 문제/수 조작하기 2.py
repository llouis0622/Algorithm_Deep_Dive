def solution(numLog):
    ans = ''
    for i in range(1, len(numLog)):
        if numLog[i-1] + 1 == numLog[i]:
            ans += 'w'
        elif numLog[i-1] - 1 == numLog[i]:
            ans += 's'
        elif numLog[i-1] + 10 == numLog[i]:
            ans += 'd'
        else:
            ans += 'a'
    return ans