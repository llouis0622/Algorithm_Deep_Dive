def solution(a, d, included):
    ans = 0
    for i in range(len(included)):
        sum = a + i * d
        if included[i]:
            ans += sum
    return ans