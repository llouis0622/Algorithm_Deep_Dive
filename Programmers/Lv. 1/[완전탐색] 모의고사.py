def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score1 = 0
    score2 = 0
    score3 = 0
    for i in range(len(answers)):
        if answers[i] == pattern1[i % len(pattern1)]:
            score1 += 1
        if answers[i] == pattern2[i % len(pattern2)]:
            score2 += 1
        if answers[i] == pattern3[i % len(pattern3)]:
            score3 += 1
    scores = [score1, score2, score3]
    arr = max(scores)
    res = []
    for i in range(3):
        if scores[i] == arr:
            res.append(i + 1)
    return res