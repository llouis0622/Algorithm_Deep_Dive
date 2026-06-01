def solution(dartResult):
    stack = []
    i = 0
    while i < len(dartResult):
        if dartResult[i:i + 2] == '10':
            num = 10
            i += 2
        else:
            num = int(dartResult[i])
            i += 1
        temp = dartResult[i]
        i += 1
        if temp == 'D':
            num **= 2
        elif temp == 'T':
            num **= 3
        if i < len(dartResult):
            if dartResult[i] == '*':
                if stack:
                    stack[-1] *= 2
                num *= 2
                i += 1
            elif dartResult[i] == '#':
                num *= -1
                i += 1
        stack.append(num)
    return sum(stack)
