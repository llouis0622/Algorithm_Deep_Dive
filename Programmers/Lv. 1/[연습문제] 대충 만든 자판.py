def solution(keymap, targets):
    dict = {}
    for i, k in enumerate(keymap):
        for j, c in enumerate(k):
            if c in dict:
                dict[c] = min(dict[c], j + 1)
            else:
                dict[c] = j + 1
    result = []
    for i in targets:
        cnt = 0
        for c in i:
            if c in dict:
                cnt += dict[c]
            else:
                cnt = -1
                break
        result.append(cnt)
    return result