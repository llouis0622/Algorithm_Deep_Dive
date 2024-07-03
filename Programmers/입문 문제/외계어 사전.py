def solution(spell, dic):
    arr = set(spell)
    for i in dic:
        if arr == set(i):
            return 1
    return 2