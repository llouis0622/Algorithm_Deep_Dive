import re


def solution(dartResult):
    arr = []
    rgx = r'(\d+)([SDT])([*#]?)'
    res = re.findall(rgx, dartResult)
    for i, (score, bonus, option) in enumerate(res):
        score = int(score)
        if bonus == 'S':
            score = score ** 1
        elif bonus == 'D':
            score = score ** 2
        elif bonus == 'T':
            score = score ** 3
        if option == '*':
            score *= 2
            if i > 0:
                arr[i - 1] *= 2
        elif option == '#':
            score *= -1
        arr.append(score)
    return sum(arr)