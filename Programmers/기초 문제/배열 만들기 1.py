def solution(n, k):
    ans = []
    for i in range(k, n + 1, k):
        ans.append(i)
    return ans