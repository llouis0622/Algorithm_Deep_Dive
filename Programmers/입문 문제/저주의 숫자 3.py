def solution(n):
    ans = []
    i = 1
    while len(ans) < n:
        if '3' in str(i) or i % 3 == 0:
            i += 1
            continue
        ans.append(i)
        i += 1
    return ans[n - 1]