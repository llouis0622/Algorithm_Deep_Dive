def solution(s):
    ans = []
    for i in s.split(' '):
        word = ''
        for i, j in enumerate(i):
            if i % 2 == 0:
                word += j.upper()
            else:
                word += j.lower()
        ans.append(word)
    return ' '.join(ans)