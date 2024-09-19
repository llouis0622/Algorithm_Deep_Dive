def solution(k, m, score):
    ans = 0
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        num = score[i:i + m]
        if len(num) == m:
            ans += min(num) * m
    return ans