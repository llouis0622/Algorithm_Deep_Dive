def solution(absolutes, signs):
    res = 0
    for absolute, sign in zip(absolutes, signs):
        if sign:
            res += absolute
        else:
            res -= absolute
    return res