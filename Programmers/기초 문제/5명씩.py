def solution(names):
    ans = []
    for i in range(0, len(names), 5):
        ans.append(names[i])
    return ans