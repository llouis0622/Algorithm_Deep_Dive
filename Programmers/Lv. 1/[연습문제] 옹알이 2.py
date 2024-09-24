def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for i in babbling:
        for pw in word:
            if pw * 2 not in i:
                i = i.replace(pw, ' ')
        if i.strip() == '':
            cnt += 1
    return cnt