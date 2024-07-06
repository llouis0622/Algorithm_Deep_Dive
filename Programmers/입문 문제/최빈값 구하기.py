from collections import Counter


def solution(array):
    cnt = Counter(array)
    num = max(cnt.values())
    ans = [i for i, j in cnt.items() if j == num]
    if len(ans) > 1:
        return -1
    else:
        return ans[0]