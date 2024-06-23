def solution(code):
    mode = 0
    res = ''
    for i in range(len(code)):
        if code[i] == '1':
            mode = 1 - mode
        else:
            if mode == 0:
                if code[i] != 1:
                    if i % 2 == 0:
                        res += code[i]
                elif code[i] == 1:
                    mode = 1
            elif mode == 1:
                if code[i] != 1:
                    if i % 2 == 1:
                        res += code[i]
                elif code[i] == 1:
                    mode = 0
    if res == '':
        return 'EMPTY'
    else:
        return res