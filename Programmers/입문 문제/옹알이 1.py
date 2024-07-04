def solution(babbling):
    arr = ["aya", "ye", "woo", "ma"]
    ans = 0
    for i in babbling:
        for j in arr:
            if j in i:
                i = i.replace(j, ' ')
        if i.strip() == '':
            ans += 1
    return ans