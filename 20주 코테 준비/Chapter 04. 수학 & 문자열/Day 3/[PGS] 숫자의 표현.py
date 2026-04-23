def solution(n):
    ans, s, e, tot = 1, 1, 1, 1
    while e < n:
        if tot == n:
            ans += 1
            e += 1
            tot += e
        elif tot < n:
            e += 1
            tot += e
        else:
            tot -= s
            s += 1
    return ans
