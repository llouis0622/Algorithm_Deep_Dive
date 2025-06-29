def solution(sequence, k):
    n = len(sequence)
    s, e = 0, 0
    cur = sequence[0]
    ans = [0, n - 1]
    while s <= e and e < n:
        if cur < k:
            e += 1
            if e < n:
                cur += sequence[e]
        elif cur > k:
            cur -= sequence[s]
            s += 1
        else:
            if (e - s) < (ans[1] - ans[0]):
                ans = [s, e]
            s += 1
            cur -= sequence[s - 1]
    return ans