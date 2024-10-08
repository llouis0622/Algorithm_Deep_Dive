def solution(survey, choices):
    score = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }
    num = {1: 3, 2: 2, 3: 1, 5: 1, 6: 2, 7: 3}
    for i in range(len(survey)):
        disagree, agree = survey[i]
        choice = choices[i]
        if choice < 4:
            score[disagree] += num[choice]
        elif choice > 4:
            score[agree] += num[choice]
    res = []
    res.append('R' if score['R'] >= score['T'] else 'T')
    res.append('C' if score['C'] >= score['F'] else 'F')
    res.append('J' if score['J'] >= score['M'] else 'M')
    res.append('A' if score['A'] >= score['N'] else 'N')
    return ''.join(res)